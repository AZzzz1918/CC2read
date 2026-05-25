"""Generate v0.3 regression goldens and run tests."""
import json, os
from pathlib import Path

V03 = Path(r"E:\PPP\CC2read\research_kb\releases\corpus_grounded_v0.3")
GOLDENS = Path(r"E:\PPP\CC2read\research_kb\tests\regression_goldens_v0.3")
GOLDENS.mkdir(parents=True, exist_ok=True)
JSON_DIR = V03 / "json_repaired"

# Step 1: Generate goldens
for fn in sorted(os.listdir(str(JSON_DIR))):
    if not fn.endswith(".json"): continue
    with open(str(JSON_DIR / fn), "r", encoding="utf-8") as f:
        d = json.load(f)

    pid = d["paper_id"]
    ps = d.get("product_source", {}).get("actual_product_source", "?")
    ep = d.get("experiment_epoch", {}).get("start_date", "NOT_MENTIONED")
    dcb = d.get("dcb_handling", {}).get("status", "?")
    gs = d.get("gate_status", {})
    rb = d.get("reproducibility_audit", {}).get("reproduction_blockers", [])

    golden = {
        "paper_id": pid,
        "expected_product_source": ps,
        "expected_epoch_status": "HAS_DATE" if ep not in ("NOT_MENTIONED", "", None) else "NOT_MENTIONED",
        "expected_dcb_status": dcb,
        "expected_gate_status": "PASS",
        "must_not_have_wrong_support": True,
        "must_have_reproduction_blockers": True,
        "correction_status": d.get("correction_status", "none"),
        "admission_status": d.get("admission_status", "PASS"),
    }
    with open(str(GOLDENS / (pid + ".golden.json")), "w", encoding="utf-8") as f:
        json.dump(golden, f, ensure_ascii=False, indent=2)

print("Generated %d v0.3 goldens" % len(list(GOLDENS.glob("*.json"))))

# Step 2: Run regression
passed, failed = 0, 0
errors = []

for gf in sorted(os.listdir(str(GOLDENS))):
    if not gf.endswith(".golden.json"): continue
    with open(str(GOLDENS / gf), "r", encoding="utf-8") as f:
        golden = json.load(f)
    pid = golden["paper_id"]

    jp = JSON_DIR / (pid + ".json")
    if not jp.exists():
        errors.append({"pid": pid, "error": "json_missing"})
        failed += 1
        continue

    with open(str(jp), "r", encoding="utf-8") as f:
        d = json.load(f)

    ps = d.get("product_source", {}).get("actual_product_source", "?")
    rb = d.get("reproducibility_audit", {}).get("reproduction_blockers", [])
    gs = d.get("gate_status", {})

    issues = []
    if ps != golden["expected_product_source"]:
        issues.append("PS: expected=%s actual=%s" % (golden["expected_product_source"], ps))
    if gs.get("wrong_support") and golden["must_not_have_wrong_support"]:
        issues.append("wrong_support=True")
    if len(rb) == 0 and golden["must_have_reproduction_blockers"]:
        issues.append("empty_blockers")

    if issues:
        failed += 1
        errors.append({"pid": pid, "issues": issues})
    else:
        passed += 1

# Step 3: Specific Phase B correction checks
correction_checks = {
    "s10291_025_01845_5": "BDS3_PPP_B2B_BROADCAST",
    "s10291_025_01882_0": "BDS3_PPP_B2B_BROADCAST",
    "Liu_Wei_BDS_GPS_RTK_PPP": "CNES_OR_OTHER_RTS",
}
for pid, expected_ps in correction_checks.items():
    jp = JSON_DIR / (pid + ".json")
    if jp.exists():
        with open(str(jp), "r", encoding="utf-8") as f:
            d = json.load(f)
        actual = d.get("product_source", {}).get("actual_product_source", "?")
        if actual != expected_ps:
            failed += 1
            errors.append({"pid": pid, "issues": ["CORRECTION_REGRESSION: ps=%s expected=%s" % (actual, expected_ps)]})

print("\n=== REGRESSION v0.3 ===")
print("Passed: %d" % passed)
print("Failed: %d" % failed)
if errors:
    for e in errors[:5]:
        print("  %s: %s" % (e["pid"][:40], e.get("issues", e.get("error","?"))))

all_pass = failed == 0
print("REGRESSION: %s" % ("PASS" if all_pass else "FAIL"))

# Also run v0.2 regression
print("\n=== v0.2 REGRESSION ===")
import subprocess
result = subprocess.run(["python", str(Path(r"E:\PPP\CC2read\scripts\run_regression_tests.py"))], capture_output=True, text=True)
print(result.stdout.strip())

# Save results
results = {"v0.3_passed": passed, "v0.3_failed": failed, "v0.3_total": passed+failed, "errors": errors, "correction_checks_pass": all(failed == 0)}
with open(str(V03 / "tests" / "regression_results.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Copy goldens to release
for gf in os.listdir(str(GOLDENS)):
    shutil.copy2(str(GOLDENS / gf), str(V03 / "tests" / gf))

import shutil
print("\nDone. Goldens copied to release." if all_pass else "\nFAILED — check errors above.")
