"""
Quote Repair v2 — 对 unresolved quotes 增强匹配。
策略：提取 DeepSeek quote 的关键词，找 quote_bank 中包含最多关键词的 span。
不调用 API，不修改语义字段。
"""

import difflib
import json
import re
import sys
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json"
BANK_DIR = PROJECT_ROOT / "research_kb" / "quote_banks"
REPAIRED_DIR = PROJECT_ROOT / "research_kb" / "papers"

GQ_FIELDS = [
    "product_source", "mathematical_model", "ionospheric_handling",
    "correction_types", "technical_route", "experiment_epoch",
    "datasets", "metrics", "main_results", "novelty_audit",
    "reproducibility_audit",
]

STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "can", "shall", "to", "of", "in", "for",
    "on", "with", "at", "by", "from", "as", "into", "through", "during",
    "before", "after", "above", "below", "between", "and", "but", "or",
    "nor", "not", "so", "yet", "both", "either", "neither", "each", "every",
    "this", "that", "these", "those", "it", "its", "we", "they", "them",
    "their", "our", "his", "her", "its", "about", "also", "than", "then",
    "which", "where", "when", "how", "all", "any", "no", "such", "only",
    "other", "new", "most", "some", "more", "very", "just", "been", "being",
}


def _normalize(text: str) -> str:
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    replacements = {"‑": "-", "–": "--", "—": "---", "‘": "'", "’": "'", "“": '"', "”": '"', " ": " ", "　": " "}
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t


def _extract_keywords(text: str, min_len: int = 3) -> set[str]:
    """提取有意义的非停用词关键词"""
    t = _normalize(text).lower()
    words = re.findall(r"[a-z0-9_]+", t)
    return {w for w in words if len(w) >= min_len and w not in STOP_WORDS}


def _keyword_overlap_score(quote_kw: set[str], span_text: str) -> float:
    """关键词覆盖评分"""
    span_kw = _extract_keywords(span_text)
    if not quote_kw:
        return 0.0
    overlap = quote_kw & span_kw
    return len(overlap) / len(quote_kw)


def _find_best_match_v2(invalid_quote: str, bank: list[dict], min_score: float = 0.30) -> dict | None:
    """
    v2 增强匹配：先精确匹配，再关键词 overlap。
    """
    q_norm = _normalize(invalid_quote)
    q_kw = _extract_keywords(invalid_quote)

    best = None
    best_score = 0.0

    for entry in bank:
        span_norm = _normalize(entry["text"])

        # Level 1: exact normalized match
        if q_norm == span_norm:
            return {
                "quote_id": entry["quote_id"],
                "quote_text": entry["text"],
                "match_type": "exact_repair_v2",
                "repair_confidence": "high",
                "score": 1.0,
            }

        # Level 2: substring match
        if q_norm in span_norm or span_norm in q_norm:
            score = min(len(q_norm), len(span_norm)) / max(len(q_norm), len(span_norm))
            if score > best_score:
                best_score = score
                best = {
                    "quote_id": entry["quote_id"],
                    "quote_text": entry["text"],
                    "match_type": "normalized_repair_v2",
                    "repair_confidence": "high" if score > 0.7 else "medium",
                    "score": round(score, 3),
                }

        # Level 3: keyword overlap
        if best_score < 0.70 and q_kw:
            kw_score = _keyword_overlap_score(q_kw, entry["text"])
            if kw_score > best_score:
                best_score = kw_score
                best = {
                    "quote_id": entry["quote_id"],
                    "quote_text": entry["text"],
                    "match_type": "keyword_overlap_repair",
                    "repair_confidence": "high" if kw_score > 0.7 else "medium" if kw_score > 0.5 else "low",
                    "score": round(kw_score, 3),
                }

        # Level 4: fuzzy fallback
        if best_score < 0.50:
            ratio = difflib.SequenceMatcher(None, q_norm, span_norm).ratio()
            if ratio > best_score and ratio > 0.80:
                best_score = ratio
                best = {
                    "quote_id": entry["quote_id"],
                    "quote_text": entry["text"],
                    "match_type": "fuzzy_repair_v2",
                    "repair_confidence": "medium" if ratio > 0.88 else "low",
                    "score": round(ratio, 3),
                }

    if best and best_score >= min_score:
        return best
    return None


def repair_all_v2():
    """对已有 repaired JSON 中的 unresolved quotes 做 v2 增强匹配"""
    repaired_json_dir = PROJECT_ROOT / "research_kb" / "papers" / "json_repaired"
    repaired_yaml_dir = PROJECT_ROOT / "research_kb" / "papers" / "yaml_repaired"

    # 从 v1 修复结果继续
    v1_dir = PROJECT_ROOT / "research_kb" / "papers" / "json_repaired"
    json_files = sorted(v1_dir.glob("*.json"))
    all_stats = {}

    for jf in json_files:
        paper_id = jf.stem
        data = json.loads(jf.read_text(encoding="utf-8"))

        bank_path = BANK_DIR / f"{paper_id}_bank.json"
        if not bank_path.exists():
            print(f"SKIP {paper_id}: no quote_bank")
            continue

        bank = json.loads(bank_path.read_text(encoding="utf-8"))

        stats = {
            "total_quotes": 0,
            "exact_repair_v2": 0,
            "normalized_repair_v2": 0,
            "keyword_overlap_repair": 0,
            "fuzzy_repair_v2": 0,
            "still_unresolved": 0,
            "previously_repaired": 0,
            "newly_repaired": 0,
        }

        for field in GQ_FIELDS:
            val = data.get(field, {})
            if not isinstance(val, dict):
                continue

            ids = val.get("grounding_quote_ids", [])
            if not ids:
                continue

            for ref in ids:
                stats["total_quotes"] += 1

                # 跳过已修复的
                if ref.get("quote_id") and ref.get("match_type") != "unresolved":
                    stats["previously_repaired"] += 1
                    continue

                # 尝试 v2 匹配
                old_quote = ref.get("original_deepseek_quote", "")
                if not old_quote:
                    stats["still_unresolved"] += 1
                    continue

                best = _find_best_match_v2(old_quote, bank)
                if best:
                    ref["quote_id"] = best["quote_id"]
                    ref["quote_text"] = best["quote_text"]
                    ref["match_type"] = best["match_type"]
                    ref["repair_confidence"] = best["repair_confidence"]
                    ref["score"] = best["score"]
                    ref.pop("repair_status", None)
                    stats["newly_repaired"] += 1

                    if best["match_type"] == "exact_repair_v2":
                        stats["exact_repair_v2"] += 1
                    elif best["match_type"] == "normalized_repair_v2":
                        stats["normalized_repair_v2"] += 1
                    elif best["match_type"] == "keyword_overlap_repair":
                        stats["keyword_overlap_repair"] += 1
                    elif best["match_type"] == "fuzzy_repair_v2":
                        stats["fuzzy_repair_v2"] += 1
                else:
                    stats["still_unresolved"] += 1

        # 保存
        json_out = repaired_json_dir / f"{paper_id}.json"
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        import yaml
        yaml_out = repaired_yaml_dir / f"{paper_id}.yaml"
        with open(yaml_out, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

        all_stats[paper_id] = stats

        total = stats["total_quotes"]
        resolved = total - stats["still_unresolved"]
        print(f"{paper_id[:45]}:")
        print(f"  {resolved}/{total} resolved "
              f"(prev_repaired={stats['previously_repaired']}, "
              f"new_exact={stats['exact_repair_v2']}, "
              f"new_norm={stats['normalized_repair_v2']}, "
              f"new_kw={stats['keyword_overlap_repair']}, "
              f"new_fuzzy={stats['fuzzy_repair_v2']}, "
              f"unresolved={stats['still_unresolved']})")

    return all_stats


if __name__ == "__main__":
    repair_all_v2()
