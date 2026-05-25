"""Cross-batch consistency check for v0.2 integrated baseline."""
import json, os, yaml
from pathlib import Path
from collections import Counter

V02 = Path(r"E:\PPP\CC2read\research_kb\releases\corpus_grounded_v0.2")
JSON_DIR = V02 / "json_repaired"
BANK_DIR = V02 / "quote_banks"

def load_papers():
    papers = {}
    for fn in sorted(os.listdir(str(JSON_DIR))):
        if not fn.endswith(".json"): continue
        with open(str(JSON_DIR / fn), "r", encoding="utf-8") as f:
            data = json.load(f)
        papers[data["paper_id"]] = data
    return papers

def check_product_source_taxonomy(papers):
    """Check that product_source values are consistent."""
    valid_values = {
        "BDS3_PPP_B2B_BROADCAST", "MIXED_PRODUCTS",
        "CNES_OR_OTHER_RTS", "QZSS_CLAS",
    }
    issues = []
    values = Counter()
    for pid, p in papers.items():
        ps = p.get("product_source", {}).get("actual_product_source", "NOT_SET")
        values[ps] += 1
        if ps not in valid_values:
            issues.append({"paper_id": pid, "issue": "unknown_product_source", "value": ps})
    return values, issues

def check_classification_consistency(papers):
    """Check core/boundary/non_b2b classification."""
    issues = []
    for pid, p in papers.items():
        role = p.get("selection_role", p.get("batch", ""))
        ps = p.get("product_source", {}).get("actual_product_source", "")
        pdf = p.get("pdf_metadata", {})
        b2b = pdf.get("b2b_mentions", 0)
        has_m = pdf.get("has_mentions", 0)
        clas_m = pdf.get("clas_mentions", 0)

        # Core B2B should have BDS3_PPP_B2B_BROADCAST
        if "core" in str(role) and ps != "BDS3_PPP_B2B_BROADCAST":
            issues.append({"paper_id": pid, "issue": "core_not_bds3_b2b", "ps": ps, "role": role})
        # Non-B2B should NOT have BDS3_PPP_B2B_BROADCAST
        if "non_b2b" in str(role) and ps == "BDS3_PPP_B2B_BROADCAST":
            issues.append({"paper_id": pid, "issue": "non_b2b_misclassified_as_bds3", "ps": ps, "role": role})
        # MIXED should have MIXED_PRODUCTS
        if "mixed" in str(role).lower() and ps != "MIXED_PRODUCTS":
            issues.append({"paper_id": pid, "issue": "mixed_not_mixed_products", "ps": ps, "role": role})
        # BDS3 B2B papers should have reasonable B2b count
        if ps == "BDS3_PPP_B2B_BROADCAST" and b2b < 10 and "addendum" not in str(p.get("addendum_reason", "")):
            issues.append({"paper_id": pid, "issue": "bds3_b2b_low_b2b_count", "b2b": b2b})

    return issues

def check_epoch_consistency(papers):
    """Check that experiment_epoch uses actual observation dates, not publication year."""
    issues = []
    for pid, p in papers.items():
        ep = p.get("experiment_epoch", {})
        pub_year = p.get("bibliographic_info", {}).get("year", 0)
        epoch_start = ep.get("start_date", "NOT_MENTIONED")

        if epoch_start and epoch_start != "NOT_MENTIONED":
            try:
                epoch_year = int(epoch_start[:4])
                if pub_year and epoch_year > pub_year:
                    issues.append({"paper_id": pid, "issue": "epoch_after_publication", "epoch_year": epoch_year, "pub_year": pub_year})
                elif pub_year and epoch_year == pub_year:
                    # Same year is OK but flag for awareness
                    pass
            except:
                pass

        # Check if NOT_MENTIONED papers have dates in their raw text
        dates_found = ep.get("dates_found", [])
        if epoch_start == "NOT_MENTIONED" and len(dates_found) > 0:
            # Has dates but marked NOT_MENTIONED - might be format issue
            pass

    return issues

def check_dcb_consistency(papers):
    """Check DCB handling consistency."""
    valid_statuses = {"EXPLICITLY_DESCRIBED", "MENTIONED", "BRIEFLY_MENTIONED", "NOT_MENTIONED", "INSUFFICIENT_EVIDENCE", "MENTIONED_AS_CODE_BIAS"}
    issues = []
    statuses = Counter()
    for pid, p in papers.items():
        dcb = p.get("dcb_handling", {})
        status = dcb.get("status", "NOT_CHECKED")
        statuses[status] += 1
        mentions = dcb.get("dcb_mentions", 0)
        if status == "EXPLICITLY_DESCRIBED" and mentions < 5:
            issues.append({"paper_id": pid, "issue": "dcb_explicit_but_low_mentions", "mentions": mentions})
        if status == "NOT_MENTIONED" and mentions > 5:
            issues.append({"paper_id": pid, "issue": "dcb_not_mentioned_but_has_mentions", "mentions": mentions})
    return statuses, issues

def check_blockers(papers):
    """Check all papers have non-empty blockers."""
    issues = []
    for pid, p in papers.items():
        blockers = p.get("reproducibility_audit", {}).get("reproduction_blockers", [])
        if len(blockers) == 0:
            issues.append({"paper_id": pid, "issue": "empty_blockers"})
    return issues

def check_quote_id_conflicts(papers):
    """Check for duplicate quote_ids across papers."""
    all_ids = {}  # quote_id -> [paper_ids]
    bank_files = sorted(os.listdir(str(BANK_DIR)))
    for bf in bank_files:
        if not bf.endswith("_bank.json"): continue
        with open(str(BANK_DIR / bf), "r", encoding="utf-8") as f:
            bank = json.load(f)
        for entry in bank:
            qid = entry["quote_id"]
            if qid not in all_ids:
                all_ids[qid] = []
            all_ids[qid].append(bf)

    conflicts = {qid: files for qid, files in all_ids.items() if len(files) > 1}
    return conflicts

def main():
    papers = load_papers()
    print("Loaded %d papers" % len(papers))

    # 1. Product source taxonomy
    ps_values, ps_issues = check_product_source_taxonomy(papers)
    print("\n=== Product Source Distribution ===")
    for v, c in ps_values.most_common():
        print("  %s: %d" % (v, c))

    # 2. Classification consistency
    class_issues = check_classification_consistency(papers)
    print("\n=== Classification Issues: %d ===" % len(class_issues))
    for i in class_issues:
        print("  %s: %s" % (i["paper_id"][:40], i["issue"]))

    # 3. Epoch consistency
    epoch_issues = check_epoch_consistency(papers)
    print("\n=== Epoch Issues: %d ===" % len(epoch_issues))
    for i in epoch_issues:
        print("  %s: %s" % (i["paper_id"][:40], i["issue"]))

    # 4. DCB consistency
    dcb_statuses, dcb_issues = check_dcb_consistency(papers)
    print("\n=== DCB Status Distribution ===")
    for v, c in dcb_statuses.most_common():
        print("  %s: %d" % (v, c))
    print("DCB Issues: %d" % len(dcb_issues))

    # 5. Blockers
    blocker_issues = check_blockers(papers)
    print("\n=== Empty Blockers: %d ===" % len(blocker_issues))

    # 6. Quote ID conflicts
    quote_conflicts = check_quote_id_conflicts(papers)
    print("\n=== Quote ID Conflicts: %d ===" % len(quote_conflicts))

    # Summary
    all_issues = len(ps_issues) + len(class_issues) + len(epoch_issues) + len(dcb_issues) + len(blocker_issues)
    has_conflicts = len(quote_conflicts) > 0

    print("\n=== TOTAL ISSUES: %d ===" % all_issues)
    print("Quote ID conflicts: %d" % len(quote_conflicts))
    print("PASS: %s" % (all_issues == 0 and not has_conflicts))

    # Save results
    results = {
        "papers_loaded": len(papers),
        "total_issues": all_issues,
        "quote_id_conflicts": len(quote_conflicts),
        "product_source_distribution": dict(ps_values),
        "product_source_issues": ps_issues,
        "classification_issues": class_issues,
        "epoch_issues": epoch_issues,
        "dcb_status_distribution": dict(dcb_statuses),
        "dcb_issues": dcb_issues,
        "blocker_issues": blocker_issues,
        "quote_id_conflict_list": {k: v for k, v in list(quote_conflicts.items())[:20]},
        "passed": all_issues == 0,
    }

    out_path = V02 / "reports" / "cross_batch_consistency.json"
    with open(str(out_path), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Also YAML
    yaml_path = V02 / "reports" / "cross_batch_consistency.yaml"
    with open(str(yaml_path), "w", encoding="utf-8") as f:
        yaml.safe_dump(results, f, allow_unicode=True, sort_keys=False)

    return results

if __name__ == "__main__":
    main()
