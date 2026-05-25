"""Evidence Support Audit for Batch 2 — 10 papers."""
import json, os

REPAIRED_DIR = r"E:\PPP\CC2read\research_kb\papers\json_batch_2_repaired"

CRITICAL_FIELDS = ["product_source", "experiment_epoch", "dcb_handling", "ionospheric_handling", "mathematical_model", "datasets", "metrics", "main_results", "novelty_audit", "reproducibility_audit"]

def audit_paper(data):
    pid = data["paper_id"]
    ps = data.get("product_source", {})
    ep = data.get("experiment_epoch", {})
    dcb = data.get("dcb_handling", {})
    iono = data.get("ionospheric_handling", {})
    rb = data.get("reproducibility_audit", {})
    gs = data.get("gate_status", {})
    pdf = data.get("pdf_metadata", {})

    # Product source check
    actual_ps = ps.get("actual_product_source", "NOT_CHECKED")
    expected_ps = gs.get("expected_product_source", "NOT_CHECKED")
    ps_match = actual_ps == expected_ps
    b2b_mentions = pdf.get("b2b_mentions", 0)
    has_mentions = pdf.get("has_mentions", 0)
    clas_mentions = pdf.get("clas_mentions", 0)

    # Epoch check
    epoch_start = ep.get("start_date", "NOT_MENTIONED")
    pub_year = data.get("bibliographic_info", {}).get("year", 0)
    epoch_conflict = False
    if epoch_start != "NOT_MENTIONED" and pub_year:
        try:
            if int(epoch_start[:4]) > pub_year:
                epoch_conflict = True
        except:
            pass

    # DCB check
    dcb_status = dcb.get("status", "NOT_CHECKED")
    dcb_mentions = dcb.get("dcb_mentions", 0)
    dcb_valid = dcb_status in ["EXPLICITLY_DESCRIBED", "MENTIONED", "BRIEFLY_MENTIONED", "NOT_MENTIONED", "INSUFFICIENT_EVIDENCE"]

    # Iono check
    iono_status = iono.get("status", "NOT_CHECKED")
    iono_mentions = iono.get("iono_mentions", 0)

    # Blockers check
    blockers = rb.get("reproduction_blockers", [])
    blockers_ok = len(blockers) > 0

    # Field support levels
    field_support = {}
    total_quotes = 0
    for field in CRITICAL_FIELDS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue
        quotes = val.get("grounding_quotes", [])
        q_count = len(quotes)
        total_quotes += q_count
        if q_count == 0:
            field_support[field] = "NO_EVIDENCE"
        else:
            field_support[field] = "HAS_EVIDENCE"

    # Determine wrong_support
    wrong_support = (not ps_match) or epoch_conflict or (not dcb_valid)

    # Determine if this paper is misclassified
    # For non-B2b papers with high B2b mentions => wrong
    # For core B2b papers with low B2b mentions => suspicious
    role = data.get("selection_role", "unknown")
    b2b_suspicious = False
    if role == "core_ppp_b2b" and b2b_mentions < 10:
        b2b_suspicious = True
    if role.startswith("non_b2b") and b2b_mentions > 50:
        b2b_suspicious = True

    return {
        "paper_id": pid,
        "role": role,
        "actual_ps": actual_ps,
        "expected_ps": expected_ps,
        "ps_match": ps_match,
        "b2b_mentions": b2b_mentions,
        "has_mentions": has_mentions,
        "clas_mentions": clas_mentions,
        "epoch_start": epoch_start,
        "pub_year": pub_year,
        "epoch_conflict": epoch_conflict,
        "dcb_status": dcb_status,
        "dcb_mentions": dcb_mentions,
        "dcb_valid": dcb_valid,
        "iono_status": iono_status,
        "blockers_count": len(blockers),
        "blockers_ok": blockers_ok,
        "total_quotes": total_quotes,
        "field_support": field_support,
        "wrong_support": wrong_support,
        "b2b_suspicious": b2b_suspicious,
    }


def main():
    results = {}
    for fn in sorted(os.listdir(REPAIRED_DIR)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(REPAIRED_DIR, fn), "r", encoding="utf-8") as f:
            data = json.load(f)
        r = audit_paper(data)
        results[r["paper_id"]] = r

        ps_flag = "OK" if r["ps_match"] else "WRONG_PS"
        ep_flag = "CONFLICT" if r["epoch_conflict"] else "OK"
        b2b_flag = "SUSPICIOUS" if r["b2b_suspicious"] else "OK"
        wrong = "WRONG" if r["wrong_support"] else "OK"
        pid = r["paper_id"]
        print("%s: role=%s ps=%s[%s] b2b=%d epoch=%s[%s] dcb=%s blockers=%d q=%d [%s]" % (
            pid[:45], r["role"], r["actual_ps"], ps_flag, r["b2b_mentions"],
            r["epoch_start"][:20], ep_flag, r["dcb_status"], r["blockers_count"], r["total_quotes"], wrong
        ))

    # Summary
    total = len(results)
    wrong_ps = sum(1 for r in results.values() if not r["ps_match"])
    epoch_conflicts = sum(1 for r in results.values() if r["epoch_conflict"])
    b2b_suspicious = sum(1 for r in results.values() if r["b2b_suspicious"])
    wrong_support = sum(1 for r in results.values() if r["wrong_support"])
    blocked = sum(1 for r in results.values() if not r["blockers_ok"])
    zero_quotes = sum(1 for r in results.values() if r["total_quotes"] == 0)

    print("\n=== SUMMARY ===")
    print("Papers: %d" % total)
    print("WRONG product_source: %d" % wrong_ps)
    print("Epoch conflicts: %d" % epoch_conflicts)
    print("B2b suspicious: %d" % b2b_suspicious)
    print("WRONG_SUPPORT: %d" % wrong_support)
    print("BLOCKED: %d" % blocked)
    print("Zero quotes: %d" % zero_quotes)

    passed = (wrong_ps == 0 and epoch_conflicts == 0 and wrong_support == 0 and blocked == 0)
    print("PASS: %s" % ("YES" if passed else "NO"))

    # Save
    out_path = r"E:\PPP\CC2read\research_kb\metadata\evidence_support_batch2_results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"per_paper": {k: v for k, v in results.items()}, "summary": {
            "total": total, "wrong_ps": wrong_ps, "epoch_conflicts": epoch_conflicts,
            "wrong_support": wrong_support, "blocked": blocked, "zero_quotes": zero_quotes,
            "passed": passed,
        }}, f, ensure_ascii=False, indent=2)

    return passed

if __name__ == "__main__":
    main()
