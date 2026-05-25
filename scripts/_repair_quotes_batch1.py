"""
Quote Repair for Batch 1 — maps grounding_quotes strings to quote_bank spans.
Works with papers/json/ format (string quotes, not v1 quote_id objects).
"""
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXTRACT_DIR = PROJECT_ROOT / "research_kb" / "extractions"
PAPERS_JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json"
BANK_DIR = PROJECT_ROOT / "research_kb" / "quote_banks"
REPAIRED_JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_repaired"
REPAIRED_YAML_DIR = PROJECT_ROOT / "research_kb" / "papers" / "yaml_repaired"

STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "can", "shall", "to", "of", "in", "for",
    "on", "with", "at", "by", "from", "as", "into", "through", "during",
    "before", "after", "above", "below", "between", "and", "but", "or",
    "nor", "not", "so", "yet", "both", "either", "neither", "each", "every",
    "this", "that", "these", "those", "it", "its", "we", "they", "them",
    "their", "our", "his", "her", "about", "also", "than", "then",
    "which", "where", "when", "how", "all", "any", "no", "such", "only",
    "other", "new", "most", "some", "more", "very", "just",
}

# Fields that contain grounding_quotes
GQ_FIELD_PATHS = [
    "product_source",
    "mathematical_model",
    "experiment_epoch",
    "dcb_handling",
    "datasets",
    "metrics",
    "main_results",
    "novelty_audit",
    "reproducibility_audit",
]

BATCH1_PAPERS = [
    "Jianfei Zang1_2024_performance_assessment_of_the_bds-3_ppp-b2b_servic",
    "Peida Wu_2023_evaluation_of_real-time_kinematic_positioning_perf",
    "Tang_Chenggan_2022_orbit_determination_clock_estimation_and_performance_evaluat",
    "Yangyuanxi_2022_principle_andperformance_ofbdsbas-b2b",
    "Zhao_Lewen_2025_python_toolbox_for_bds_b2b",
    "Zhou__Linghao_2025_practical_performance_assessment_of_water_vapor_mo",
    "Yan_Liu_2022_comprehensive_analyses_of_ppp-b2b_performance_in_c",
]


def _normalize(text: str) -> str:
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    replacements = {"‑": "-", "–": "--", "—": "---", "‘": "'", "’": "'", '"': '"', '"': '"', "\xa0": " ", "　": " "}
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t


def _extract_keywords(text: str, min_len: int = 3) -> set:
    t = _normalize(text).lower()
    words = re.findall(r"[a-z0-9_]+", t)
    return {w for w in words if len(w) >= min_len and w not in STOP_WORDS}


def _make_quote_id(paper_id: str, idx: int) -> str:
    raw = f"{paper_id}_{idx}"
    h = hashlib.md5(raw.encode()).hexdigest()[:10]
    return f"qb_{h}"


def find_best_match(quote_text: str, bank: list[dict]) -> dict | None:
    """Multi-level matching against quote_bank"""
    q_norm = _normalize(quote_text)
    q_kw = _extract_keywords(quote_text)

    best = None
    best_score = 0.0

    for entry in bank:
        span_norm = _normalize(entry["text"])

        # Level 1: exact normalized match
        if q_norm == span_norm:
            return {"quote_id": entry["quote_id"], "quote_text": entry["text"],
                    "match_type": "exact", "confidence": "high", "score": 1.0}

        # Level 2: contains check
        if len(q_norm) >= 30:
            if q_norm in span_norm:
                score = len(q_norm) / len(span_norm)
                if score > best_score:
                    best_score = score
                    best = {"quote_id": entry["quote_id"], "quote_text": entry["text"],
                            "match_type": "normalized", "confidence": "high" if score > 0.6 else "medium",
                            "score": round(score, 3)}
            elif span_norm in q_norm and len(span_norm) >= 30:
                score = len(span_norm) / len(q_norm)
                if score > best_score:
                    best_score = score
                    best = {"quote_id": entry["quote_id"], "quote_text": entry["text"],
                            "match_type": "normalized", "confidence": "high" if score > 0.6 else "medium",
                            "score": round(score, 3)}

        # Level 3: keyword overlap
        if best_score < 0.5 and q_kw:
            span_kw = _extract_keywords(entry["text"])
            if span_kw:
                overlap = q_kw & span_kw
                kw_score = len(overlap) / len(q_kw)
                if kw_score > best_score:
                    best_score = kw_score
                    confidence = "high" if kw_score > 0.7 else "medium" if kw_score > 0.5 else "low"
                    best = {"quote_id": entry["quote_id"], "quote_text": entry["text"],
                            "match_type": "keyword_overlap", "confidence": confidence,
                            "score": round(kw_score, 3)}

        # Level 4: fuzzy
        if best_score < 0.5 and len(q_norm) > 20:
            ratio = difflib.SequenceMatcher(None, q_norm, span_norm).ratio()
            if ratio > 0.75 and ratio > best_score:
                best_score = ratio
                best = {"quote_id": entry["quote_id"], "quote_text": entry["text"],
                        "match_type": "fuzzy", "confidence": "medium" if ratio > 0.85 else "low",
                        "score": round(ratio, 3)}

    if best and best_score >= 0.30:
        return best
    return None


def repair_paper(paper_id: str, data: dict, bank: list[dict]) -> tuple[dict, dict]:
    """Repair one paper's grounding_quotes. Returns (repaired_data, stats)."""
    stats = {
        "total_quotes": 0,
        "exact": 0, "normalized": 0, "keyword_overlap": 0, "fuzzy": 0,
        "unresolved": 0, "no_quotes_field": 0,
    }

    for field in GQ_FIELD_PATHS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue

        quotes = val.get("grounding_quotes", [])
        if not quotes:
            stats["no_quotes_field"] += 1
            continue

        # Replace string quotes with structured quote_id refs
        resolved_quotes = []
        for q in quotes:
            stats["total_quotes"] += 1
            if isinstance(q, dict) and q.get("quote_id"):
                resolved_quotes.append(q)
                continue

            quote_str = q if isinstance(q, str) else str(q)
            match = find_best_match(quote_str, bank)

            if match:
                resolved_quotes.append({
                    "quote_id": match["quote_id"],
                    "quote_text": match["quote_text"],
                    "original_quote": quote_str,
                    "match_type": match["match_type"],
                    "confidence": match["confidence"],
                    "score": match["score"],
                })
                stats[match["match_type"]] += 1
            else:
                resolved_quotes.append({
                    "quote_id": None,
                    "original_quote": quote_str,
                    "match_type": "unresolved",
                    "confidence": "none",
                    "score": 0.0,
                })
                stats["unresolved"] += 1

        val["grounding_quotes"] = resolved_quotes

    return data, stats


def main():
    REPAIRED_JSON_DIR.mkdir(parents=True, exist_ok=True)
    REPAIRED_YAML_DIR.mkdir(parents=True, exist_ok=True)

    all_stats = {}
    total_exact = 0
    total_normalized = 0
    total_kw = 0
    total_fuzzy = 0
    total_unresolved = 0
    total_quotes = 0

    for paper_id in BATCH1_PAPERS:
        # Try extractions/ first, then papers/json/
        json_path = EXTRACT_DIR / f"{paper_id}_full.json"
        if not json_path.exists():
            json_path = PAPERS_JSON_DIR / f"{paper_id}.json"
        if not json_path.exists():
            print(f"SKIP {paper_id}: no JSON in extractions/ or papers/json/")
            continue

        bank_path = BANK_DIR / f"{paper_id}_bank.json"
        if not bank_path.exists():
            print(f"SKIP {paper_id}: no quote_bank")
            continue

        data = json.loads(json_path.read_text(encoding="utf-8"))
        bank = json.loads(bank_path.read_text(encoding="utf-8"))

        repaired, stats = repair_paper(paper_id, data, bank)

        # Save JSON
        out_json = REPAIRED_JSON_DIR / f"{paper_id}.json"
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(repaired, f, ensure_ascii=False, indent=2)

        # Save YAML
        import yaml
        out_yaml = REPAIRED_YAML_DIR / f"{paper_id}.yaml"
        with open(out_yaml, "w", encoding="utf-8") as f:
            yaml.safe_dump(repaired, f, allow_unicode=True, sort_keys=False)

        all_stats[paper_id] = stats

        resolved = stats["total_quotes"] - stats["unresolved"]
        total_quotes += stats["total_quotes"]
        total_exact += stats["exact"]
        total_normalized += stats["normalized"]
        total_kw += stats["keyword_overlap"]
        total_fuzzy += stats["fuzzy"]
        total_unresolved += stats["unresolved"]

        short_id = paper_id[:50]
        print(f"{short_id}:")
        print(f"  {resolved}/{stats['total_quotes']} resolved "
              f"(exact={stats['exact']}, norm={stats['normalized']}, "
              f"kw={stats['keyword_overlap']}, fuzzy={stats['fuzzy']}, "
              f"unresolved={stats['unresolved']})")

    # Summary
    total_resolved = total_quotes - total_unresolved
    invalid_rate = (total_unresolved / total_quotes * 100) if total_quotes > 0 else 0
    kw_ratio = ((total_kw + total_fuzzy) / total_quotes * 100) if total_quotes > 0 else 0

    print(f"\n=== TOTALS ===")
    print(f"Total quotes: {total_quotes}")
    print(f"Resolved: {total_resolved} ({total_resolved/total_quotes*100:.1f}%)" if total_quotes > 0 else "Resolved: 0")
    print(f"  exact: {total_exact}")
    print(f"  normalized: {total_normalized}")
    print(f"  keyword_overlap: {total_kw}")
    print(f"  fuzzy: {total_fuzzy}")
    print(f"Unresolved: {total_unresolved}")
    print(f"Invalid rate: {invalid_rate:.1f}%")
    print(f"Keyword overlap ratio: {kw_ratio:.1f}%")

    # Save stats
    stats_path = PROJECT_ROOT / "research_kb" / "metadata" / "quote_repair_stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({
            "totals": {
                "total_quotes": total_quotes,
                "resolved": total_resolved,
                "exact": total_exact,
                "normalized": total_normalized,
                "keyword_overlap": total_kw,
                "fuzzy": total_fuzzy,
                "unresolved": total_unresolved,
                "invalid_rate_pct": round(invalid_rate, 1),
                "keyword_overlap_ratio_pct": round(kw_ratio, 1),
            },
            "per_paper": all_stats,
        }, f, ensure_ascii=False, indent=2)

    return all_stats


if __name__ == "__main__":
    main()
