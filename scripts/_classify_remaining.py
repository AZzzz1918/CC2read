"""
Batch classification: 1 API call per paper, first 2 pages only.
"""
import fitz, json, sys, time, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from call_deepseek import call_deepseek_json

PAPER_DIR = Path("E:/PPP/CC2read/paper")
OUT_DIR = Path("E:/PPP/CC2read/research_kb/releases/scale_test_30/per_paper")
OUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPT = """GNSS PPP-B2b classifier. Output ONLY JSON.
Classify this paper:
- product_source: BDS3_PPP_B2B_BROADCAST | IGS_RTS_OR_CLK93 | CNES_OR_OTHER_RTS | POST_PROCESSED_FINAL_PRODUCTS | QZSS_CLAS | QZSS_MADOCA | SBAS | GALILEO_HAS | RTK_NTRIP | MIXED_PRODUCTS | NOT_MENTIONED
- paper_type: orbit_clock_product_gen | ppp_b2b_service_perf | downstream_b2b_application | rtk_positioning | has_service | clas_service | sbas_service | general_gnss | non_b2b
- is_ppp_b2b_core_paper: true/false
- domain_relevance: core_ppp_b2b | related_ppp_ssr | related_gnss_augmentation | general_gnss | out_of_scope
- classification_reason: one sentence
- boundary_risk: true/false (true if title mentions PPP-B2b but actual products are non-B2b)
- needs_full_audit: true/false (true for core_ppp_b2b papers)
"""

# Already processed via scale test (skip these)
SKIP_PREFIXES = [
    "Yan_Liu_2022", "Pan_Lin_2025", "Pedro_Pintor_2023",
    "Jianfei", "Zhao_Lewen_2025", "Tang_Chenggan_2022",
    "Zhou__Linghao_2025", "Taro_Suzuki_2023", "Yangyuanxi_2022",
    "Ruohua_Lan_2022", "Ge_yulong_2024", "Maosen_Hao_2020",
    "Wei_Haopeng_2024", "Peida",
]

results = []
total = 0
ok = 0

for fp in sorted(PAPER_DIR.glob("*.pdf")):
    # Skip already processed
    stem = fp.stem
    if any(s in stem for s in SKIP_PREFIXES):
        continue

    total += 1
    paper_id = stem[:60]

    try:
        # Quick text extraction (first 2 pages)
        doc = fitz.open(str(fp))
        text = ""
        for i in range(min(2, doc.page_count)):
            text += doc[i].get_text("text") + "\n"
        doc.close()

        if len(text.strip()) < 50:
            results.append({"paper_id": paper_id, "error": "no_text", "source_file": fp.name})
            continue

        # 1 API call for classification
        result = call_deepseek_json(
            system_prompt=PROMPT,
            user_prompt=f"TEXT:\n{text[:2000]}",
            max_retries=1, temperature=0, max_tokens=2048,
            chunk_context={"paper_id": paper_id},
        )

        if result:
            ok += 1
            result["source_file"] = fp.name
            result["paper_id"] = paper_id
            result["extraction_mode"] = "batch_classify_1call"

            # Save per-paper
            out_path = OUT_DIR / f"{paper_id.replace(chr(0xa0),'_')[:80]}.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            ps = result.get("product_source", "?")
            actual = ps.get("actual_product_source", "?") if isinstance(ps, dict) else str(ps)
            core = result.get("is_ppp_b2b_core_paper", "?")
            boundary = result.get("boundary_risk", "?")
            reason = result.get("classification_reason", "")[:80]

            results.append(result)
            print(f"[{total:2d}] {paper_id[:40]}: product={actual}, core={core}, boundary={boundary}")

        else:
            results.append({"paper_id": paper_id, "error": "api_failed", "source_file": fp.name})
            print(f"[{total:2d}] {paper_id[:40]}: API FAILED")

    except Exception as e:
        print(f"[{total:2d}] {paper_id[:40]}: ERROR {str(e)[:50]}")
        results.append({"paper_id": paper_id, "error": str(e)[:100], "source_file": fp.name})

# Count results
core_count = sum(1 for r in results if r.get("is_ppp_b2b_core_paper") is True)
non_core = sum(1 for r in results if r.get("is_ppp_b2b_core_paper") is False)
boundary = sum(1 for r in results if r.get("boundary_risk") is True)
errors = sum(1 for r in results if "error" in r)

print(f"\nTotal: {total} | OK: {ok} | Errors: {errors}")
print(f"Core B2b: {core_count} | Non-B2b: {non_core} | Boundary risk: {boundary}")

# Save summary
summary = {
    "total_processed": total,
    "ok": ok,
    "errors": errors,
    "core_ppp_b2b": core_count,
    "non_b2b": non_core,
    "boundary_risk": boundary,
    "papers": [],
}
for r in results:
    ps = r.get("product_source", {})
    actual = ps.get("actual_product_source", "?") if isinstance(ps, dict) else r.get("product_source", "?")
    summary["papers"].append({
        "paper_id": r.get("paper_id", "?"),
        "product_source": str(actual),
        "is_core": r.get("is_ppp_b2b_core_paper"),
        "boundary_risk": r.get("boundary_risk"),
        "domain": r.get("domain_relevance"),
        "reason": r.get("classification_reason", "")[:120],
    })

with open(OUT_DIR / "_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
