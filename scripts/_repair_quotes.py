"""
Post-hoc Quote Repair — 不重跑 chunk，不修改语义字段。

对每个 paper JSON 中的 grounding_quotes：
1. 尝试在 quote_bank 中找到 matching span
2. 替换为 grounding_quote_ids
3. 保留无法修复的标记为 needs_evidence_repick

绝对约束：
- 不修改 product_source, experiment_epoch, novelty_grade, reproduction_blockers 等语义字段
- 不生成新 quote 文本
- 不根据常识补 quote
- 不删除 unresolved evidence
"""

import difflib
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json"
BANK_DIR = PROJECT_ROOT / "research_kb" / "quote_banks"
REPAIRED_JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_repaired"
REPAIRED_YAML_DIR = PROJECT_ROOT / "research_kb" / "papers" / "yaml_repaired"

GQ_FIELDS = [
    "product_source", "mathematical_model", "ionospheric_handling",
    "correction_types", "technical_route", "experiment_epoch",
    "datasets", "metrics", "main_results", "novelty_audit",
    "reproducibility_audit",
]

# 语义字段 —— 绝不能修改
SEMANTIC_FIELDS = {
    "product_source", "mathematical_model", "ionospheric_handling",
    "correction_types", "experiment_epoch", "novelty_audit",
    "reproducibility_audit", "main_results", "metrics", "datasets",
    "method", "technical_route", "research_problem",
    "bibliographic_info", "paper_id", "source_file", "file_hash",
    "formulas", "experiments", "conflicting_evidence",
}


def _normalize(text: str) -> str:
    """标准化文本以便匹配"""
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    # Unicode 标准化
    replacements = {
        "‑": "-", "–": "--", "—": "---",
        "‘": "'", "’": "'", "“": '"', "”": '"',
        " ": " ", "　": " ",
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t


def _find_best_match(invalid_quote: str, bank: list[dict]) -> dict | None:
    """
    在 quote_bank 中寻找最佳匹配。

    策略：
    1. 标准化后 exact match → exact_repair, high confidence
    2. 标准化后 substring match → normalized_repair, high confidence
    3. difflib ratio > 0.85 → semantic_candidate_repair, medium confidence
    4. 都不行 → None
    """
    q_norm = _normalize(invalid_quote)

    best = None
    best_score = 0.0
    best_type = ""

    for entry in bank:
        span_norm = _normalize(entry["text"])

        # Level 1: exact match after normalization
        if q_norm == span_norm:
            return {
                "quote_id": entry["quote_id"],
                "quote_text": entry["text"],
                "match_type": "exact_repair",
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
                    "match_type": "normalized_repair",
                    "repair_confidence": "high" if score > 0.8 else "medium",
                    "score": round(score, 3),
                }
                best_type = "normalized"

        # Level 3: difflib fuzzy match
        if best_score < 0.85:
            ratio = difflib.SequenceMatcher(None, q_norm, span_norm).ratio()
            if ratio > best_score and ratio > 0.85:
                best_score = ratio
                best = {
                    "quote_id": entry["quote_id"],
                    "quote_text": entry["text"],
                    "match_type": "semantic_candidate_repair",
                    "repair_confidence": "medium" if ratio > 0.90 else "low",
                    "score": round(ratio, 3),
                }
                best_type = "semantic"

    # Only return if we have a reasonable match
    if best and best_score >= 0.85:
        return best

    return None


def repair_paper_quotes(paper_id: str, data: dict, bank: list[dict]) -> tuple[dict, dict]:
    """
    修复单篇论文的 grounding_quotes。

    Returns: (repaired_data, repair_stats)
    """
    import copy
    repaired = copy.deepcopy(data)

    stats = {
        "total_quotes_processed": 0,
        "exact_repair": 0,
        "normalized_repair": 0,
        "semantic_candidate_repair": 0,
        "unresolved": 0,
        "skipped_already_valid": 0,
        "fields_modified": [],
    }

    for field in GQ_FIELDS:
        val = repaired.get(field, {})
        if not isinstance(val, dict):
            continue

        old_quotes = val.get("grounding_quotes", [])
        if not old_quotes:
            continue

        new_quote_refs = []
        field_modified = False

        for old_q in old_quotes:
            if not isinstance(old_q, str) or not old_q.strip():
                continue
            stats["total_quotes_processed"] += 1

            # 先尝试在 bank 中匹配
            best = _find_best_match(old_q, bank)

            if best and best["match_type"] == "exact_repair":
                stats["exact_repair"] += 1
                new_quote_refs.append({
                    "quote_id": best["quote_id"],
                    "quote_text": best["quote_text"],
                    "match_type": "exact_repair",
                    "repair_confidence": "high",
                    "original_deepseek_quote": old_q[:120],
                })
                field_modified = True
            elif best and best["match_type"] == "normalized_repair":
                stats["normalized_repair"] += 1
                new_quote_refs.append({
                    "quote_id": best["quote_id"],
                    "quote_text": best["quote_text"],
                    "match_type": "normalized_repair",
                    "repair_confidence": best["repair_confidence"],
                    "original_deepseek_quote": old_q[:120],
                })
                field_modified = True
            elif best and best["match_type"] == "semantic_candidate_repair":
                stats["semantic_candidate_repair"] += 1
                new_quote_refs.append({
                    "quote_id": best["quote_id"],
                    "quote_text": best["quote_text"],
                    "match_type": "semantic_candidate_repair",
                    "repair_confidence": best["repair_confidence"],
                    "original_deepseek_quote": old_q[:120],
                })
                field_modified = True
            else:
                stats["unresolved"] += 1
                new_quote_refs.append({
                    "quote_id": None,
                    "quote_text": None,
                    "match_type": "unresolved",
                    "repair_status": "needs_evidence_repick",
                    "original_deepseek_quote": old_q[:120],
                })
                field_modified = True

        if field_modified:
            val["grounding_quote_ids"] = new_quote_refs
            stats["fields_modified"].append(field)

    return repaired, stats


def repair_all():
    REPAIRED_JSON_DIR.mkdir(parents=True, exist_ok=True)
    REPAIRED_YAML_DIR.mkdir(parents=True, exist_ok=True)

    json_files = sorted(JSON_DIR.glob("*.json"))
    all_stats = {}

    for jf in json_files:
        paper_id = jf.stem
        data = json.loads(jf.read_text(encoding="utf-8"))

        bank_path = BANK_DIR / f"{paper_id}_bank.json"
        if not bank_path.exists():
            print(f"SKIP {paper_id}: no quote_bank found")
            continue

        bank = json.loads(bank_path.read_text(encoding="utf-8"))
        print(f"Repairing {paper_id[:50]}... ({len(bank)} bank entries)")

        repaired, stats = repair_paper_quotes(paper_id, data, bank)

        # 保存
        json_out = REPAIRED_JSON_DIR / f"{paper_id}.json"
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(repaired, f, ensure_ascii=False, indent=2)

        import yaml
        yaml_out = REPAIRED_YAML_DIR / f"{paper_id}.yaml"
        with open(yaml_out, "w", encoding="utf-8") as f:
            yaml.safe_dump(repaired, f, allow_unicode=True, sort_keys=False)

        all_stats[paper_id] = stats

        unresolved = stats["unresolved"]
        total = stats["total_quotes_processed"]
        resolved = total - unresolved
        print(f"  {resolved}/{total} repaired "
              f"(exact={stats['exact_repair']}, "
              f"normalized={stats['normalized_repair']}, "
              f"semantic={stats['semantic_candidate_repair']}, "
              f"unresolved={unresolved})")

    # 保存汇总统计
    stats_path = PROJECT_ROOT / "research_kb" / "metadata" / "quote_repair_stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(all_stats, f, ensure_ascii=False, indent=2)

    return all_stats


if __name__ == "__main__":
    repair_all()
