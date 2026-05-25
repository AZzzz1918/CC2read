"""Evidence Support Audit for Batch 1 papers."""
import json, os

repaired_dir = r"E:\PPP\CC2read\research_kb\papers\json_repaired"
bank_dir = r"E:\PPP\CC2read\research_kb\quote_banks"

BATCH1_IDS = {
    "Jianfei Zang1_2024_performance_assessment_of_the_bds-3_ppp-b2b_servic",
    "Peida Wu_2023_evaluation_of_real-time_kinematic_positioning_perf",
    "Tang_Chenggan_2022_orbit_determination_clock_estimation_and_performance_evaluat",
    "Yangyuanxi_2022_principle_andperformance_ofbdsbas-b2b",
    "Zhao_Lewen_2025_python_toolbox_for_bds_b2b",
    "Zhou__Linghao_2025_practical_performance_assessment_of_water_vapor_mo",
    "Yan_Liu_2022_comprehensive_analyses_of_ppp-b2b_performance_in_c",
}

papers = sorted(os.listdir(repaired_dir))

CRITICAL_FIELDS = [
    "product_source", "experiment_epoch", "dcb_handling",
    "mathematical_model", "datasets", "metrics",
    "main_results", "novelty_audit", "reproducibility_audit",
]

results = {}

for pf in papers:
    if not pf.endswith(".json"):
        continue

    with open(os.path.join(repaired_dir, pf), "r", encoding="utf-8") as f:
        data = json.load(f)

    pid = data["paper_id"]

    # Only audit Batch 1 papers
    if pid not in BATCH1_IDS:
        continue
    ps = data.get("product_source", {})
    ep = data.get("experiment_epoch", {})
    dcb = data.get("dcb_handling", {})
    rb = data.get("reproducibility_audit", {})
    gs = data.get("gate_status", {})

    # Count per-field evidence
    field_support = {}
    total_quotes = 0
    total_unresolved = 0
    total_strong = 0
    total_weak = 0

    for field_name in CRITICAL_FIELDS:
        val = data.get(field_name, {})
        if not isinstance(val, dict):
            continue
        quotes = val.get("grounding_quotes", [])
        q_count = len(quotes)
        total_quotes += q_count

        unresolved_count = 0
        high_conf_count = 0
        for q in quotes:
            if isinstance(q, dict):
                if q.get("match_type") == "unresolved":
                    unresolved_count += 1
                elif q.get("confidence") == "high":
                    high_conf_count += 1

        total_unresolved += unresolved_count

        if q_count == 0:
            support = "NO_EVIDENCE"
            total_weak += 1
        elif unresolved_count > 0:
            support = "WEAK_SUPPORT"
            total_weak += 1
        elif high_conf_count >= q_count * 0.5:
            support = "STRONG_SUPPORT"
            total_strong += 1
        else:
            support = "PARTIAL_SUPPORT"

        field_support[field_name] = {
            "quote_count": q_count,
            "unresolved": unresolved_count,
            "high_confidence": high_conf_count,
            "support_status": support,
        }

    # Check experiment_epoch vs publication year
    pub_year = data.get("bibliographic_info", {}).get("year", 0)
    epoch_start = ep.get("start_date", "")
    epoch_event = ep.get("event_date", "")
    epoch_orbit = ep.get("orbit_clock_evaluation", {})
    if isinstance(epoch_orbit, dict):
        epoch_start = epoch_orbit.get("start_date", epoch_start)

    epoch_year = None
    try:
        if epoch_start and epoch_start != "NOT_MENTIONED":
            epoch_year = int(epoch_start[:4])
        elif epoch_event and epoch_event != "NOT_MENTIONED" and epoch_event[:4].isdigit():
            epoch_year = int(epoch_event[:4])
    except (ValueError, TypeError):
        epoch_year = None

    epoch_pub_conflict = False
    if epoch_year and pub_year and epoch_year > pub_year:
        epoch_pub_conflict = True  # epoch after publication = suspicious

    # Check DCB consistency
    dcb_status = dcb.get("status", "NOT_CHECKED")
    dcb_valid = dcb_status in [
        "EXPLICITLY_DESCRIBED", "NOT_MENTIONED",
        "INSUFFICIENT_EVIDENCE", "MENTIONED_AS_CODE_BIAS",
    ]

    # Check reproduction_blockers
    blockers = rb.get("reproduction_blockers", [])
    blockers_ok = len(blockers) > 0

    # Overall gate
    wrong_support = (
        (not dcb_valid)
        or epoch_pub_conflict
        or (field_support.get("product_source", {}).get("support_status") == "WEAK_SUPPORT")
    )

    results[pid] = {
        "field_support": field_support,
        "total_quotes": total_quotes,
        "unresolved": total_unresolved,
        "strong_fields": total_strong,
        "weak_fields": total_weak,
        "epoch_pub_conflict": epoch_pub_conflict,
        "dcb_valid": dcb_valid,
        "blockers_ok": blockers_ok,
        "blockers_count": len(blockers),
        "wrong_support": wrong_support,
    }

    print(f"{pid[:55]}:")
    print(f"  quotes={total_quotes} unresolved={total_unresolved} strong={total_strong} weak={total_weak}")
    for fn, fs in field_support.items():
        print(f"  {fn}: {fs['support_status']} ({fs['quote_count']}q)")
    print(f"  epoch_pub_conflict={epoch_pub_conflict} dcb_valid={dcb_valid} blockers={len(blockers)} wrong_support={wrong_support}")
    print()

# Summary
total_wrong = sum(1 for r in results.values() if r["wrong_support"])
print(f"=== SUMMARY ===")
print(f"Papers audited: {len(results)}")
print(f"WRONG_SUPPORT: {total_wrong}")
print(f"All pass: {total_wrong == 0}")

# Save results
out_path = r"E:\PPP\CC2read\research_kb\metadata\evidence_support_audit_results.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"Saved: {out_path}")
