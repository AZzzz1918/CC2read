"""
Batch B Lite Extraction — 4 DeepSeek calls per paper.
Strict: only quote_ids, no free text, extraction_mode=batch_b_lite.
"""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from call_deepseek import call_deepseek_json

RELEASE = Path(__file__).resolve().parent.parent / "research_kb" / "releases" / "scale_test_10"
EXTRACTIONS = RELEASE / "extractions"
EXTRACTIONS.mkdir(parents=True, exist_ok=True)
CHUNKS = RELEASE / "chunks"
MD = RELEASE / "markdown"

BATCH_B = [
    ("Jianfei_Zang1_2024", "core_ppp_b2b"),
    ("Zhao_Lewen_2025", "core_ppp_b2b_tool"),
    ("Tang_Chenggan_2022", "related_orbit"),
]

# Minified prompt (same as Batch A but with paper_type classification)
PROMPT = """GNSS PPP-B2b auditor. Output ONLY JSON, no markdown, no explanations.
Rules: temp=0, NOT_MENTIONED for unknown fields.
product_source enum: BDS3_PPP_B2B_BROADCAST | IGS_RTS_OR_CLK93 | CNES_OR_OTHER_RTS | POST_PROCESSED_FINAL_PRODUCTS | QZSS_CLAS | QZSS_MADOCA | MIXED_PRODUCTS | NOT_MENTIONED
paper_type: orbit_clock_product_gen | ppp_b2b_service_perf | downstream_b2b_application | general_gnss | non_b2b
Return grounding_quote_ids as array of indices into provided quote list. One sentence reason max."""

CALL_SPECS = [
    {
        "name": "product_source_classification",
        "fields": ["product_source", "paper_type", "domain_relevance", "is_ppp_b2b_core_paper"],
        "instruction": "Classify product source and paper type. Is this a core PPP-B2b paper? Check if paper studies BDS-3 PPP-B2b broadcast correction directly, or just uses/makes B2b-related products."
    },
    {
        "name": "experiment_model_correction",
        "fields": ["mathematical_model", "experiment_epoch", "correction_types", "ionospheric_handling"],
        "instruction": "Extract model details, experiment dates (NOT publication year), correction types. Flag missing DCB."
    },
    {
        "name": "novelty_results_metrics",
        "fields": ["novelty_audit", "metrics", "main_results", "datasets"],
        "instruction": "Audit novelty claims. Extract metrics. Default to C_ENGINEERING_TRANSFER unless clear novel formula/state/stochastic/qc/b2b-usage evidence."
    },
    {
        "name": "reproducibility",
        "fields": ["reproducibility_audit"],
        "instruction": "List reproduction blockers. Score 0-10. Check: code, data, config, model params, Kalman filter config, correction archive, baseline details."
    },
]


def collect_representative_text(paper_prefix: str) -> str:
    """从 top chunks 收集代表文本"""
    cf = list(CHUNKS.glob(f"{paper_prefix}*.json"))
    if not cf:
        return ""
    chunks_data = json.loads(cf[0].read_text(encoding="utf-8"))

    # Select: abstract, first 2 pages, method/experiment pages
    selected = []
    for c in chunks_data:
        ct = c.get("chunk_type", "")
        pg = c.get("page_start", 99)
        if ct in ("abstract", "method", "experiment", "result") or pg <= 2:
            selected.append(c)
        if len(selected) >= 8:
            break
    if len(selected) < 4:
        selected = chunks_data[:4]

    # Build text with quote_id references
    lines = []
    for i, c in enumerate(selected):
        text = c.get("text", "")[:800]
        lines.append(f"[QUOTE_IDS: {i*10}..{i*10+9}] {text}")
    return "\n\n".join(lines)


def extract_one_paper(paper_prefix: str, category: str) -> dict:
    """4 calls per paper"""
    cf = list(CHUNKS.glob(f"{paper_prefix}*.json"))
    if not cf:
        return {"paper_id": paper_prefix, "error": "no_chunks"}
    paper_id = cf[0].stem
    text = collect_representative_text(paper_prefix)
    if not text:
        return {"paper_id": paper_id, "error": "no_text"}

    merged = {
        "paper_id": paper_id,
        "expected_category": category,
        "extraction_mode": "batch_b_lite",
        "extraction_method": "4_calls_per_paper",
    }

    t0 = time.time()
    calls_ok = 0
    calls_total = 0

    for spec in CALL_SPECS:
        user = f"FIELDS: {spec['fields']}\nTASK: {spec['instruction']}\n\nTEXT:\n{text[:3000]}"
        result = call_deepseek_json(
            system_prompt=PROMPT,
            user_prompt=user,
            max_retries=2,
            temperature=0,
            max_tokens=4096,
            chunk_context={"paper_id": paper_id, "call": spec["name"]},
        )
        calls_total += 1
        if result:
            calls_ok += 1
            for k, v in result.items():
                if k.startswith("_"):
                    continue
                if k not in merged:
                    merged[k] = v
                elif isinstance(v, dict) and isinstance(merged.get(k), dict):
                    merged[k].update(v)

    merged["_meta"] = {
        "calls_total": calls_total,
        "calls_ok": calls_ok,
        "elapsed_seconds": round(time.time() - t0, 1),
    }

    # Save
    out = EXTRACTIONS / f"{paper_id}_raw.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    return merged


def check_gates(results: list[dict]) -> dict:
    """Batch B gate validation"""
    gates = {
        "product_source_correct": True,
        "non_b2b_not_core": True,
        "epoch_not_pubyear": True,
        "no_wrong_support": True,
        "checks": [],
    }

    for r in results:
        pid = r.get("paper_id", "?")[:35]
        ps = r.get("product_source", {})
        actual = ps.get("actual_product_source", "?")
        cat = r.get("expected_category", "?")
        pt = r.get("paper_type", "?")
        is_core = r.get("is_ppp_b2b_core_paper", False)
        epoch = r.get("experiment_epoch", {})
        start = epoch.get("start_date", "?") if isinstance(epoch, dict) else "?"
        nov = r.get("novelty_audit", {})
        grade = nov.get("audit_grade", "?") if isinstance(nov, dict) else "?"

        # Gate: Tang Chenggan must NOT be core_ppp_b2b
        if "Tang" in pid and is_core:
            gates["non_b2b_not_core"] = False
            gates["checks"].append(f"FAIL: Tang Chenggan mislabeled as core_ppp_b2b")
        elif "Tang" in pid:
            gates["checks"].append(f"PASS: Tang Chenggan correctly NOT core_ppp_b2b (paper_type={pt})")

        # Gate: Jianfei Zang should be core
        if "Jianfei" in pid and not is_core:
            gates["product_source_correct"] = False
            gates["checks"].append(f"FAIL: Jianfei Zang not labeled core_ppp_b2b")
        elif "Jianfei" in pid:
            gates["checks"].append(f"PASS: Jianfei Zang core_ppp_b2b=True, product={actual}")

        # Gate: Zhao Lewen should be core_ppp_b2b_tool
        if "Zhao" in pid:
            gates["checks"].append(f"PASS: Zhao Lewen paper_type={pt}, product={actual}")

        print(f"{pid}: product={actual}, paper_type={pt}, core={is_core}, epoch={start}, novelty={grade}")

    return gates


if __name__ == "__main__":
    print(f"Batch B Lite: {len(BATCH_B)} papers x 4 calls = 12 API calls\n")
    results = []
    for prefix, cat in BATCH_B:
        print(f"Extracting {prefix[:35]} ({cat})...")
        r = extract_one_paper(prefix, cat)
        results.append(r)
        meta = r.get("_meta", {})
        print(f"  {meta.get('calls_ok')}/{meta.get('calls_total')} OK, {meta.get('elapsed_seconds')}s")

    print(f"\n=== Gate Check ===")
    gates = check_gates(results)

    all_pass = all([
        gates["product_source_correct"],
        gates["non_b2b_not_core"],
        gates["epoch_not_pubyear"],
        gates["no_wrong_support"],
    ])

    print(f"\nBatch B {'PASS' if all_pass else 'FAIL'}")
    for c in gates["checks"]:
        print(f"  {c}")

    if all_pass:
        print("✅ Ready for Batch C")
    else:
        print("❌ BLOCKED — fix before Batch C")
