"""Regression test runner for corpus_grounded_v0.2."""
import json, os, sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
V02 = PROJECT_ROOT / "research_kb" / "releases" / "corpus_grounded_v0.2"
GOLDENS = PROJECT_ROOT / "research_kb" / "tests" / "regression_goldens"
JSON_DIR = V02 / "json_repaired"

def run_tests():
    results = {"passed": 0, "failed": 0, "errors": []}

    for gf in sorted(os.listdir(str(GOLDENS))):
        if not gf.endswith(".golden.json"): continue

        with open(str(GOLDENS / gf), "r", encoding="utf-8") as f:
            golden = json.load(f)

        pid = golden["paper_id"]
        paper_path = JSON_DIR / (pid + ".json")

        if not paper_path.exists():
            results["errors"].append({"paper_id": pid, "error": "paper_json_missing"})
            results["failed"] += 1
            continue

        with open(str(paper_path), "r", encoding="utf-8") as f:
            paper = json.load(f)

        ps = paper.get("product_source", {}).get("actual_product_source", "?")
        ep = paper.get("experiment_epoch", {})
        dcb = paper.get("dcb_handling", {}).get("status", "?")
        gs = paper.get("gate_status", {})
        rb = paper.get("reproducibility_audit", {}).get("reproduction_blockers", [])

        failures = []

        if ps != golden["expected_product_source"]:
            failures.append("product_source: expected=%s actual=%s" % (golden["expected_product_source"], ps))

        if gs.get("wrong_support", False) and golden["must_not_have_wrong_support"]:
            failures.append("wrong_support=True (must_not_have)")

        if len(rb) == 0 and golden["must_have_reproduction_blockers"]:
            failures.append("empty_reproduction_blockers")

        if failures:
            results["failed"] += 1
            results["errors"].append({"paper_id": pid, "failures": failures})
        else:
            results["passed"] += 1

    return results

def main():
    print("Running regression tests for corpus_grounded_v0.2...")
    results = run_tests()
    print("Passed: %d" % results["passed"])
    print("Failed: %d" % results["failed"])

    if results["failed"] > 0:
        print("\nFailures:")
        for e in results["errors"]:
            print("  %s: %s" % (e["paper_id"][:50], e.get("failures", e.get("error", "?"))))

    passed = results["failed"] == 0
    print("\nREGRESSION: %s" % ("PASS" if passed else "FAIL"))

    # Save results
    out = PROJECT_ROOT / "research_kb" / "reports" / "regression_test_results.json"
    with open(str(out), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(main())
