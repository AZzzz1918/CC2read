"""
Lite Extraction — top-5 chunks per paper, speed-optimized prompt.
Concurrency support, no free-text quotes, quote_bank IDs only.
"""
import json
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from call_deepseek import call_deepseek_json
from _build_quote_bank import build_quote_bank, _make_quote_id

RELEASE = PROJECT_ROOT / "research_kb" / "releases" / "scale_test_10"

# ---- Speed-optimized prompt (minified) ----
LITE_PROMPT = """You are a GNSS PPP-B2b research auditor. Extract structured information from the markdown text.
Output ONLY valid JSON. No explanations, no markdown, no code fences.

Rules:
- If field not mentioned → "NOT_MENTIONED"
- product_source: BDS3_PPP_B2B_BROADCAST | IGS_RTS_OR_CLK93 | CNES_OR_OTHER_RTS | POST_PROCESSED_FINAL_PRODUCTS | QZSS_CLAS | QZSS_MADOCA | MIXED_PRODUCTS | NOT_MENTIONED
- experiment_epoch: extract actual observation dates from text, NOT publication year
- novelty_grade: A_SUBSTANTIVE | B_INCREMENTAL | C_ENGINEERING_TRANSFER | D_WEAK_OR_OVERCLAIMED | U_INSUFFICIENT_EVIDENCE
- For evidence, provide grounding_quote_ids (from context) not free text
- Keep reason to 1 sentence max
- temperature=0 means be deterministic"""

LITE_SCHEMA_HINT = {
    "paper_id": "", "bibliographic_info": {"title": "", "authors": [], "year": 0},
    "product_source": {"claimed": "", "actual_product_source": "", "grounding_quote_ids": []},
    "mathematical_model": {"processing_mode": "", "grounding_quote_ids": []},
    "experiment_epoch": {"start_date": "", "end_date": "", "grounding_quote_ids": []},
    "novelty_audit": {"audit_grade": "", "grounding_quote_ids": []},
    "reproducibility_audit": {"reproduction_blockers": [], "reproducibility_score": 0, "grounding_quote_ids": []},
}

CHUNK_TYPE_PRIORITY = {
    "abstract": 5, "introduction": 4, "method": 4,
    "experiment": 5, "result": 5, "conclusion": 3,
    "references": 1, "mixed": 2, "unknown": 1,
}


def select_top_chunks(chunks: list[dict], top_k: int = 5) -> list[dict]:
    """选择最重要的 top-k chunks"""
    scored = []
    for c in chunks:
        ct = c.get("chunk_type", "unknown")
        score = CHUNK_TYPE_PRIORITY.get(ct, 1)
        # Bonus for longer text
        text_len = len(c.get("text", ""))
        if text_len > 200:
            score += 1
        scored.append((score, c))
    scored.sort(key=lambda x: -x[0])
    return [c for _, c in scored[:top_k]]


def extract_one_chunk(chunk: dict, paper_id: str, bank: list[dict]) -> dict | None:
    """Extract one chunk with lite settings"""
    text = chunk.get("text", "")

    # Build context with quote_id hints
    context = {
        "paper_id": paper_id,
        "chunk_type": chunk.get("chunk_type"),
        "page": chunk.get("page_start"),
    }

    user_prompt = (
        f"CHUNK CONTEXT: {json.dumps(context)}\n\n"
        f"PAPER MARKDOWN:\n{text[:2500]}\n\n"
        f"Available quote_ids: {[b['quote_id'][:12] for b in bank[:20]]}\n"
        f"Extract structured fields. Output ONLY JSON."
    )

    return call_deepseek_json(
        system_prompt=LITE_PROMPT,
        user_prompt=user_prompt,
        schema_hint=LITE_SCHEMA_HINT,
        max_retries=2,
        temperature=0,
        max_tokens=4096,
        chunk_context={"paper_id": paper_id, "chunk_id": chunk.get("chunk_id")},
    )


def extract_paper_lite(paper_prefix: str, category: str, top_k: int = 5) -> dict | None:
    """Lite extraction for one paper"""
    # Find chunk file
    chunk_files = list((RELEASE / "chunks").glob(f"{paper_prefix}*.json"))
    if not chunk_files:
        return {"error": "no_chunks", "paper_prefix": paper_prefix}

    cf = chunk_files[0]
    paper_id = cf.stem
    chunks = json.loads(cf.read_text(encoding="utf-8"))

    # Build quote bank
    md_files = list((RELEASE / "markdown").glob(f"{paper_prefix}*.md"))
    bank = []
    if md_files:
        md_text = md_files[0].read_text(encoding="utf-8")
        bank = build_quote_bank(paper_id, md_text)

    # Select top chunks
    selected = select_top_chunks(chunks, top_k)
    print(f"  {paper_id[:40]}: {len(selected)}/{len(chunks)} chunks selected")

    # Extract
    results = []
    ok = 0
    t0 = time.time()
    for chunk in selected:
        result = extract_one_chunk(chunk, paper_id, bank)
        if result:
            result["_meta"] = {"chunk_id": chunk["chunk_id"], "chunk_type": chunk["chunk_type"]}
            results.append(result)
            ok += 1
        else:
            results.append({"_meta": {"chunk_id": chunk["chunk_id"]}, "_error": "failed"})

    elapsed = time.time() - t0

    # Merge
    merged = _quick_merge(paper_id, results)

    # Save
    out_path = RELEASE / "extractions" / f"{paper_id}_raw.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    return {
        "paper_id": paper_id,
        "category": category,
        "chunks_total": len(chunks),
        "chunks_selected": len(selected),
        "extraction_ok": ok,
        "extraction_failed": len(selected) - ok,
        "elapsed_seconds": round(elapsed, 1),
        "output": str(out_path),
    }


def _quick_merge(paper_id: str, extractions: list[dict]) -> dict:
    merged = {"paper_id": paper_id}
    for ext in extractions:
        if "_error" in ext:
            continue
        for k, v in ext.items():
            if k.startswith("_"):
                continue
            if k not in merged:
                merged[k] = v
            elif isinstance(v, dict) and isinstance(merged.get(k), dict):
                merged[k].update(v)
            elif isinstance(v, list) and isinstance(merged.get(k), list):
                merged[k].extend(v)
            elif v and v not in ("NOT_MENTIONED",):
                merged[k] = v
    return merged


def run_batch(paper_prefixes: list[tuple[str, str]], top_k: int = 5, concurrent: int = 1):
    """Run lite extraction for a batch"""
    print(f"Lite extraction: {len(paper_prefixes)} papers, top_k={top_k}, concurrent={concurrent}")

    if concurrent > 1:
        results = []
        with ThreadPoolExecutor(max_workers=concurrent) as executor:
            futures = {
                executor.submit(extract_paper_lite, prefix, cat, top_k): prefix
                for prefix, cat in paper_prefixes
            }
            for future in as_completed(futures):
                r = future.result()
                if r:
                    results.append(r)
                    if "error" not in r:
                        print(f"  DONE: {r['paper_id'][:40]} ({r['elapsed_seconds']}s, {r['extraction_ok']}/{r['chunks_selected']})")
        return results
    else:
        results = []
        for prefix, cat in paper_prefixes:
            r = extract_paper_lite(prefix, cat, top_k)
            if r:
                results.append(r)
                if "error" not in r:
                    print(f"  DONE: {r['paper_id'][:40]} ({r['elapsed_seconds']}s, {r['extraction_ok']}/{r['chunks_selected']})")
        return results


if __name__ == "__main__":
    batch_a = [
        ("Yan_Liu_2022", "core_ppp_b2b"),
        ("Pan_Lin_2025", "boundary_mixed"),
        ("Pedro_Pintor_2023", "non_b2b_galileo"),
    ]
    results = run_batch(batch_a, top_k=5, concurrent=1)

    total_time = sum(r.get("elapsed_seconds", 0) for r in results)
    total_ok = sum(r.get("extraction_ok", 0) for r in results)
    print(f"\nBatch A lite: {total_ok} extractions in {total_time:.0f}s")
