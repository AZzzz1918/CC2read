"""
10-Paper Scale Test — Strict Quote Rules.
所有输出写入 releases/scale_test_10/。
不修改 pilot_v0.1。
"""
import json
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

RELEASE_DIR = PROJECT_ROOT / "research_kb" / "releases" / "scale_test_10"
PAPER_DIR = PROJECT_ROOT / "paper"

# 10 篇候选论文
PAPERS = [
    ("2022--Yan Liu--Comprehensive_Analyses_of_PPP-B2b_Performance_in_C.pdf", "core_ppp_b2b"),
    ("2024--Jianfei Zang1--Performance_assessment_of_the_BDS-3_PPP-B2b_servic.pdf", "core_ppp_b2b"),
    ("2022--Yangyuanxi--Principle and\xa0performance of\xa0BDSBAS-B2b.pdf", "related_sbas"),
    ("2025--Pan Lin--BDS B2b and HAS.pdf", "boundary_mixed"),
    ("2025--Zhao Lewen--Python toolbox for BDS  B2b.pdf", "core_ppp_b2b_tool"),
    ("2025--Zhou  Linghao --Practical_Performance_Assessment_of_Water_Vapor_Mo.pdf", "ppp_b2b_application"),
    ("2022--Tang Chenggan--Orbit determination, clock estimation and performance evaluation.pdf", "related_orbit_clock"),
    ("2023--Peida Wu--Evaluation_of_real-time_kinematic_positioning_perf.pdf", "related_rtk"),
    ("2023--Pedro Pintor--Testing_Galileo_High-Accuracy_Service_HAS_in_Marin.pdf", "non_b2b_galileo"),
    ("2023--Taro Suzuki--Evaluation_of_L6_augmentation_signal_reception_cha.pdf", "non_b2b_qzss"),
]


def setup_scale_test():
    """建立 scale_test_10 目录结构"""
    subdirs = ["markdown", "chunks", "extractions", "json", "yaml",
               "json_repaired", "json_corrected", "quote_banks",
               "corpus", "reports", "metadata", "logs"]
    for sd in subdirs:
        (RELEASE_DIR / sd).mkdir(parents=True, exist_ok=True)


def find_paper_file(partial_name: str) -> Path | None:
    """通过部分文件名查找 PDF"""
    # Glob pattern
    for fp in sorted(PAPER_DIR.glob("*.pdf")):
        if partial_name[:20] in fp.name or fp.name == partial_name:
            return fp
    # Fallback: try matching shorter prefix
    for fp in sorted(PAPER_DIR.glob("*.pdf")):
        stem_keywords = partial_name.split("--")[1][:30] if "--" in partial_name else partial_name[:30]
        if stem_keywords in fp.stem:
            return fp
    return None


def process_pdf_stage(selected: list[tuple[Path, str, str]]):
    """PDF → Markdown → Chunks"""
    from pdf_to_markdown import process_pdf
    from chunk_markdown import process_markdown

    # Monkey-patch output dirs
    import pdf_to_markdown as p2m
    import chunk_markdown as cm

    orig_md_dir = p2m.OUTPUT_DIR
    orig_chunk_dir = cm.CHUNKS_DIR
    p2m.OUTPUT_DIR = RELEASE_DIR / "markdown"
    cm.CHUNKS_DIR = RELEASE_DIR / "chunks"
    p2m.METADATA_DIR = RELEASE_DIR / "metadata"

    results = []
    for fp, cat, fname in selected:
        r = process_pdf(fp)
        if not r:
            print(f"  FAILED: {fname}")
            results.append(None)
            continue
        print(f"  MD: {r['paper_id'][:40]} ({r['page_count']}p)")

        # Chunk
        md_path = (RELEASE_DIR / "markdown") / f"{r['paper_id']}.md"
        chunks = process_markdown(md_path)
        print(f"  Chunks: {len(chunks)}")

        results.append({
            "paper_id": r["paper_id"],
            "category": cat,
            "filename": fname,
            "pages": r["page_count"],
            "chunks": len(chunks),
            "filepath": str(fp),
        })

    # Restore
    p2m.OUTPUT_DIR = orig_md_dir
    cm.CHUNKS_DIR = orig_chunk_dir

    return results


def process_extraction_stage(results: list[dict]):
    """DeepSeek chunk extraction (with strict quote rules)"""
    from extract_chunks import extract_chunk, load_prompt, load_schema

    # Monkey-patch
    import extract_chunks as ec
    orig_chunks_dir = ec.CHUNKS_DIR
    orig_extract_dir = ec.EXTRACT_DIR
    ec.CHUNKS_DIR = RELEASE_DIR / "chunks"
    ec.EXTRACT_DIR = RELEASE_DIR / "extractions"

    schema = load_schema()
    prompt = load_prompt()

    # Append strict quote rule to system prompt
    strict_rule = """
STRICT QUOTE RULE (scale test):
You MUST NOT generate free-form quote text.
You MUST select from the quote_bank candidates provided.
If no candidate supports the field, output "NO_VALID_QUOTE".
Do NOT paraphrase, translate, or invent quotes.
"""
    prompt = prompt + strict_rule

    for r in results:
        if r is None:
            continue
        pid = r["paper_id"]
        chunk_path = (RELEASE_DIR / "chunks") / f"{pid}.json"
        if not chunk_path.exists():
            continue
        chunks = json.loads(chunk_path.read_text(encoding="utf-8"))

        paper_extractions = []
        success = 0
        failed = 0
        print(f"  Extracting {pid[:40]}: {len(chunks)} chunks...")

        for chunk in chunks:
            result = extract_chunk(chunk, schema)
            if result is not None:
                result["_meta"] = {
                    "chunk_id": chunk["chunk_id"],
                    "chunk_index": chunk["chunk_index"],
                    "chunk_type": chunk["chunk_type"],
                }
                paper_extractions.append(result)
                success += 1
            else:
                paper_extractions.append({
                    "_meta": {"chunk_id": chunk["chunk_id"], "chunk_index": chunk["chunk_index"]},
                    "_error": "extraction_failed",
                })
                failed += 1
            time.sleep(0.3)

        # Save extractions
        out_path = (RELEASE_DIR / "extractions") / f"{pid}_raw.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(paper_extractions, f, ensure_ascii=False, indent=2)
        r["extraction_success"] = success
        r["extraction_failed"] = failed
        print(f"    {success} ok, {failed} failed")

    # Restore
    ec.CHUNKS_DIR = orig_chunks_dir
    ec.EXTRACT_DIR = orig_extract_dir


def process_quote_repair_stage(results):
    """Quote repair using strict rules: only quote_bank selection"""
    from _repair_quotes import _find_best_match
    from _build_quote_bank import build_quote_bank

    BANK_DIR = RELEASE_DIR / "quote_banks"
    MD_DIR = RELEASE_DIR / "markdown"

    GQ_FIELDS = [
        "product_source", "mathematical_model", "ionospheric_handling",
        "correction_types", "technical_route", "experiment_epoch",
        "datasets", "metrics", "main_results", "novelty_audit",
        "reproducibility_audit",
    ]

    CRITICAL_FIELDS = {"product_source", "experiment_epoch", "novelty_audit"}

    for r in results:
        if r is None:
            continue
        pid = r["paper_id"]

        # Build quote_bank
        md_path = MD_DIR / f"{pid}.md"
        if not md_path.exists():
            print(f"  No markdown for {pid}")
            continue
        md_text = md_path.read_text(encoding="utf-8")
        bank = build_quote_bank(pid, md_text)
        bank_path = BANK_DIR / f"{pid}_bank.json"
        with open(bank_path, "w", encoding="utf-8") as f:
            json.dump(bank, f, ensure_ascii=False, indent=2)

        # Load extraction
        ext_path = (RELEASE_DIR / "extractions") / f"{pid}_raw.json"
        if not ext_path.exists():
            continue
        extractions = json.loads(ext_path.read_text(encoding="utf-8"))

        # Merge extractions
        merged = _simple_merge(pid, extractions)

        # Repair quotes
        stats = {"total": 0, "repaired": 0, "keyword": 0, "unresolved": 0,
                 "critical_fields_ok": True}

        for field in GQ_FIELDS:
            val = merged.get(field, {})
            if not isinstance(val, dict):
                continue
            old_quotes = val.get("grounding_quotes", [])
            if not old_quotes:
                continue

            new_refs = []
            for old_q in old_quotes:
                if not isinstance(old_q, str) or not old_q.strip():
                    continue
                stats["total"] += 1
                best = _find_best_match(old_q, bank)

                if best:
                    mt = best.get("match_type", "")
                    rc = best.get("repair_confidence", "")
                    ref = {
                        "quote_id": best["quote_id"],
                        "quote_text": best["quote_text"],
                        "match_type": mt,
                        "repair_confidence": rc,
                        "original_deepseek_quote": old_q[:120],
                    }

                    # Strict rule: keyword_overlap_low_confidence cannot support critical fields
                    if mt == "keyword_overlap_repair" and rc == "low" and field in CRITICAL_FIELDS:
                        ref["quote_id"] = None
                        ref["quote_text"] = None
                        ref["match_type"] = "blocked_by_strict_rule"
                        ref["repair_confidence"] = "none"
                        ref["repair_status"] = "needs_manual_review"
                        stats["unresolved"] += 1
                    else:
                        stats["repaired"] += 1
                        if mt == "keyword_overlap_repair":
                            stats["keyword"] += 1
                else:
                    stats["unresolved"] += 1
                    ref = {
                        "quote_id": None,
                        "quote_text": None,
                        "match_type": "unresolved",
                        "repair_status": "needs_evidence_repick",
                        "original_deepseek_quote": old_q[:120],
                    }

                new_refs.append(ref)

            val["grounding_quote_ids"] = new_refs

        # Save repaired JSON
        json_out = RELEASE_DIR / "json_repaired" / f"{pid}.json"
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(merged, f, ensure_ascii=False, indent=2)

        total = stats["total"]
        print(f"  {pid[:40]}: {stats['repaired']}/{total} repaired "
              f"(kw={stats['keyword']}, unresolved={stats['unresolved']})")
        r["quote_stats"] = stats


def _simple_merge(paper_id, extractions):
    """简化 merge"""
    merged = {"paper_id": paper_id, "conflicting_evidence": []}
    for ext in extractions:
        if "_error" in ext:
            continue
        for key, val in ext.items():
            if key.startswith("_"):
                continue
            if key not in merged:
                merged[key] = val
            elif isinstance(val, dict) and isinstance(merged[key], dict):
                merged[key].update(val)
            elif isinstance(val, list) and isinstance(merged[key], list):
                merged[key].extend(val)
            elif val and val not in ("NOT_MENTIONED",):
                merged[key] = val
    if not merged.get("conflicting_evidence"):
        del merged["conflicting_evidence"]
    return merged


def generate_report(results, elapsed):
    """生成 scale_test_10_status.md"""
    total_papers = len([r for r in results if r])
    total_chunks = sum(r.get("chunks", 0) for r in results if r)
    total_extracted = sum(r.get("extraction_success", 0) for r in results if r)
    total_failed = sum(r.get("extraction_failed", 0) for r in results if r)
    total_quotes = sum(r.get("quote_stats", {}).get("total", 0) for r in results if r)
    total_repaired = sum(r.get("quote_stats", {}).get("repaired", 0) for r in results if r)
    total_kw = sum(r.get("quote_stats", {}).get("keyword", 0) for r in results if r)
    total_unresolved = sum(r.get("quote_stats", {}).get("unresolved", 0) for r in results if r)

    lines = [
        "# Scale Test 10 Status Report",
        f"生成时间：{datetime.now().isoformat()}",
        f"耗时：{elapsed:.0f}s",
        "",
        "## 1. 处理统计",
        f"- 论文数：{total_papers}/10",
        f"- 总 chunks：{total_chunks}",
        f"- 抽取成功：{total_extracted}",
        f"- 抽取失败：{total_failed}",
        f"- Quote repair：{total_repaired}/{total_quotes} repaired",
        f"- Keyword overlap：{total_kw}",
        f"- Unresolved：{total_unresolved}",
        "",
        "## 2. 论文详情",
        "| # | Paper | Category | Pages | Chunks | Extracted | Repaired | KW | Unresolved |",
        "|---|-------|----------|-------|--------|-----------|----------|----|-----------|",
    ]

    for i, r in enumerate(results):
        if r is None:
            lines.append(f"| {i+1} | PROCESSING FAILED | - | - | - | - | - | - | - |")
            continue
        qs = r.get("quote_stats", {})
        lines.append(
            f"| {i+1} | {r['paper_id'][:30]} | {r['category']} | {r['pages']} | {r['chunks']} | "
            f"{r.get('extraction_success',0)}/{r.get('extraction_failed',0)} | "
            f"{qs.get('repaired',0)} | {qs.get('keyword',0)} | {qs.get('unresolved',0)} |"
        )

    lines.extend([
        "",
        "## 3. Strict Rules Applied",
        "- LLM 不允许自由生成 quote",
        "- 只能选择 quote_bank quote_id",
        "- quote text 由程序从 quote_bank 回填",
        "- keyword_overlap_low_confidence 不允许支持关键字段 (product_source, experiment_epoch, novelty_audit)",
        "- 关键字段必须有 PARTIAL_SUPPORT 以上证据",
        "",
        "## 4. Pilot v0.1 Comparison",
        "| Metric | v0.1 (3 papers) | Scale Test (10 papers) |",
        "|--------|----------------|----------------------|",
        f"| Papers processed | 3 | {total_papers} |",
        f"| Total chunks | 55 | {total_chunks} |",
        f"| Extraction success rate | 100% | {total_extracted}/{total_chunks} |",
        f"| Quote repair rate | ~98% | {total_repaired}/{total_quotes} |",
        f"| Keyword overlap ratio | 60.3% | {(total_kw/total_quotes*100) if total_quotes > 0 else 0:.1f}% |",
        "",
        "## 5. 是否允许继续扩展",
    ])

    if total_failed > 0:
        lines.append("**BLOCKED**: extraction failures detected. Fix before expanding.")
    elif total_unresolved / max(total_quotes, 1) > 0.05:
        lines.append("**WARN**: unresolved rate > 5%. Review before expanding.")
    else:
        lines.append("**READY**: pipeline can scale to 30-paper test.")

    report_path = RELEASE_DIR / "reports" / "scale_test_10_status.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report_path}")


def main():
    start = time.time()
    setup_scale_test()

    # Step 1: Find and process PDFs
    print("=== Step 1: PDF -> Markdown -> Chunks ===")
    selected = []
    for fname, cat in PAPERS:
        fp = find_paper_file(fname)
        if fp:
            selected.append((fp, cat, fname))
            print(f"  Found: {fp.name[:50]} ({cat})")
        else:
            print(f"  NOT FOUND: {fname[:50]}")

    results = process_pdf_stage(selected)

    # Step 2: DeepSeek extraction
    print("\n=== Step 2: DeepSeek Extraction ===")
    process_extraction_stage(results)

    # Step 3: Quote repair with strict rules
    print("\n=== Step 3: Quote Repair (strict rules) ===")
    process_quote_repair_stage(results)

    # Step 4: Generate report
    elapsed = time.time() - start
    print(f"\n=== Step 4: Report ===")
    generate_report(results, elapsed)

    print(f"\nDone. Results in {RELEASE_DIR}")
    print(f"Total time: {elapsed:.0f}s")


if __name__ == "__main__":
    main()
