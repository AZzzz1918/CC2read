"""
Grounding quote repair 工具。

输入 paper JSON 和对应 Markdown，对所有 grounding_quotes 做 exact substring check，
尝试轻量修复后将 quote 替换为 Markdown 中真实存在的 exact substring。

修复策略：
1. exact match（含空白标准化）
2. 轻量修复：Unicode 标准化、连字符标准化、合并不规范断行
3. fuzzy match：找到 Markdown 中最接近的原文片段
4. 无法修复 → INVALID_QUOTE
"""

import json
import logging
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_DIR = PROJECT_ROOT / "research_kb" / "markdown"
JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json"

logger = logging.getLogger("repair_quotes")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)

# ---- Normalization utilities ----


def _normalize_ws(text: str) -> str:
    """标准化空白：压缩连续空白"""
    return re.sub(r"\s+", " ", text).strip()


def _normalize_unicode(text: str) -> str:
    """标准化 Unicode 标点和不可见字符"""
    replacements = {
        "​": "", "‌": "", "‍": "", "﻿": "", "‎": "", "‏": "",
        "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "--",
        "‘": "'", "’": "'", "“": '"', "”": '"',
        " ": " ", "　": " ",
    }
    result = text
    for k, v in replacements.items():
        result = result.replace(k, v)
    return result


def _normalize_blend(text: str) -> str:
    """
    尝试修复 PDF 提取导致的单词粘连。

    策略：在 camelCase 边界、数字-字母边界、已知高频粘连处插入空格。
    返回 (normalized_text, was_modified)。
    """
    modified = False

    # 小写字母后紧跟大写字母 → 插入空格
    result = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    if result != text:
        modified = True

    # 数字后紧跟字母
    result2 = re.sub(r"(\d)([a-zA-Z])", r"\1 \2", result)
    if result2 != result:
        modified = True

    # 字母后紧跟数字
    result3 = re.sub(r"([a-zA-Z])(\d)", r"\1 \2", result2)
    if result3 != result2:
        modified = True

    return result3, modified


def normalize_for_match(text: str, level: str = "full") -> str:
    """
    分级标准化。

    level:
      - "ws": 仅空白
      - "unicode": 空白 + Unicode
      - "blend": 空白 + Unicode + 粘连修复
      - "full": 全部 (默认)
    """
    if level == "none":
        return text

    result = _normalize_ws(text)
    if level in ("unicode", "blend", "full"):
        result = _normalize_unicode(result)
    if level in ("blend", "full"):
        result, _ = _normalize_blend(result)
        result = _normalize_ws(result)  # blend 后再次合并空白

    return result


# ---- Matching ----


def exact_substring_match(md_text: str, quote: str) -> bool:
    """检查 quote 是否是 md_text 的 exact substring（含空白标准化）"""
    q = quote.strip()
    if not q:
        return False
    # Level 0: raw match
    if q in md_text:
        return True
    # Level 1: whitespace normalize both sides
    if normalize_for_match(q, "ws") in normalize_for_match(md_text, "ws"):
        return True
    # Level 2: unicode normalize
    if normalize_for_match(q, "unicode") in normalize_for_match(md_text, "unicode"):
        return True
    # Level 3: blend repair
    if normalize_for_match(q, "blend") in normalize_for_match(md_text, "blend"):
        return True
    return False


def find_closest_substring(md_text: str, quote: str, min_similarity: float = 0.6) -> tuple[str, float] | None:
    """
    用滑动窗口 + SequenceMatcher 在 Markdown 中找到与 quote 最接近的 substring。
    返回 (closest_substring, similarity) 或 None。
    """
    q = quote.strip()
    if len(q) < 10:
        return None

    q_norm = normalize_for_match(q, "blend")
    md_norm = normalize_for_match(md_text, "blend")

    # 快速路径：子串匹配
    if q_norm in md_norm:
        # 在原文中找到对应位置
        idx = md_norm.find(q_norm)
        # 返回原始 md 中的对应片段
        return md_text[idx:idx + len(q_norm)], 1.0

    # 滑动窗口 fuzzy match
    best_score = 0.0
    best_match = None
    q_len = len(q)
    window_sizes = [q_len, int(q_len * 0.8), int(q_len * 1.2), int(q_len * 1.5)]
    window_sizes = [w for w in window_sizes if 10 < w < len(md_text)]

    step = max(1, q_len // 4)
    for win_size in window_sizes:
        for i in range(0, len(md_text) - win_size, step):
            candidate = md_text[i:i + win_size]
            score = SequenceMatcher(None, q.lower(), candidate.lower()).ratio()
            if score > best_score:
                best_score = score
                best_match = candidate.strip()

    if best_score >= min_similarity and best_match:
        return best_match, round(best_score, 4)

    return None


# ---- Quote-level repair ----


def repair_single_quote(md_text: str, quote: str) -> dict:
    """
    对单条 quote 执行修复。

    Returns:
        {
            "quote": str,           # 最终 quote（可能已被替换为 exact substring）
            "valid": bool,          # 是否可在 Markdown 中验证
            "repaired": bool,       # 是否经过修复
            "repair_method": str,   # "none" | "exact_ws" | "exact_unicode" | "blend_repair" | "fuzzy_match" | "irreparable"
            "similarity_score": float | None,
            "original_quote": str,  # 原始 quote
        }
    """
    result = {
        "quote": quote,
        "valid": True,
        "repaired": False,
        "repair_method": "none",
        "similarity_score": None,
        "original_quote": quote,
    }

    q = quote.strip()
    if not q:
        result["valid"] = False
        result["repair_method"] = "empty_quote"
        return result

    # Step 1: Raw exact match
    if q in md_text:
        return result

    # Step 2: Whitespace normalization
    q_ws = normalize_for_match(q, "ws")
    md_ws = normalize_for_match(md_text, "ws")
    if q_ws in md_ws:
        result["repaired"] = True
        result["repair_method"] = "exact_ws"
        return result

    # Step 3: Unicode normalization
    q_uni = normalize_for_match(q, "unicode")
    md_uni = normalize_for_match(md_text, "unicode")
    if q_uni in md_uni:
        result["repaired"] = True
        result["repair_method"] = "exact_unicode"
        return result

    # Step 4: Blend repair (fix run-together words)
    q_blend = normalize_for_match(q, "blend")
    md_blend = normalize_for_match(md_text, "blend")
    if q_blend in md_blend:
        # Find the exact position in the blended md_text
        idx = md_blend.find(q_blend)
        result["quote"] = md_text[idx:idx + len(q)]
        result["repaired"] = True
        result["repair_method"] = "blend_repair"
        return result

    # Step 5: Fuzzy match
    closest = find_closest_substring(md_text, q, min_similarity=0.65)
    if closest:
        match_str, sim = closest
        result["quote"] = match_str
        result["repaired"] = True
        result["repair_method"] = "fuzzy_match"
        result["similarity_score"] = sim
        # Verify the matched string is actually in md_text
        assert match_str in md_text, f"Fuzzy match result not in md_text: {match_str[:80]}..."
        return result

    # Step 6: Irreparable
    result["valid"] = False
    result["repaired"] = False
    result["repair_method"] = "irreparable"
    return result


# ---- Paper-level repair ----


GQ_FIELDS = [
    "product_source", "mathematical_model", "ionospheric_handling",
    "correction_types", "technical_route", "experiment_epoch",
    "datasets", "metrics", "main_results", "novelty_audit",
    "reproducibility_audit",
]


def repair_paper_quotes(paper_json: dict, md_text: str) -> dict:
    """
    对单篇论文的所有 grounding_quotes 执行检查和修复。

    Returns 更新后的 paper_json，附带 _quote_audit 元数据。
    """
    stats = {
        "total": 0,
        "valid_raw": 0,
        "repaired_ws": 0,
        "repaired_unicode": 0,
        "repaired_blend": 0,
        "repaired_fuzzy": 0,
        "invalid": 0,
        "invalid_quotes": [],
    }

    for field in GQ_FIELDS:
        val = paper_json.get(field, {})
        if not isinstance(val, dict):
            continue

        quotes = val.get("grounding_quotes", [])
        if not quotes:
            continue

        repaired_quotes = []
        for q in quotes:
            stats["total"] += 1
            r = repair_single_quote(md_text, q)

            if r["valid"]:
                repaired_quotes.append(r["quote"])
                if r["repair_method"] == "none":
                    stats["valid_raw"] += 1
                elif r["repair_method"] == "exact_ws":
                    stats["repaired_ws"] += 1
                elif r["repair_method"] == "exact_unicode":
                    stats["repaired_unicode"] += 1
                elif r["repair_method"] == "blend_repair":
                    stats["repaired_blend"] += 1
                elif r["repair_method"] == "fuzzy_match":
                    stats["repaired_fuzzy"] += 1
            else:
                stats["invalid"] += 1
                stats["invalid_quotes"].append({
                    "field": field,
                    "quote": q,
                    "repair_method": r["repair_method"],
                })

        val["grounding_quotes"] = repaired_quotes

        # 标记 evidence_status
        if stats["invalid"] > 0:
            # 检查该字段的 valid quotes 数量
            valid_count = len(repaired_quotes)
            if valid_count == 0:
                val["evidence_status"] = "INVALID_QUOTE"
                val["quote_valid"] = False
            elif stats["invalid"] > 0:
                val["evidence_status"] = "PARTIAL_INVALID"

    # 计算 invalid rate
    invalid_rate = stats["invalid"] / stats["total"] if stats["total"] > 0 else 0.0
    stats["invalid_rate"] = round(invalid_rate, 4)

    paper_json["_quote_audit"] = stats

    return paper_json


def repair_all():
    """对所有已有 paper JSON 执行 quote repair"""
    for jp in sorted(JSON_DIR.glob("*.json")):
        paper_id = jp.stem
        logger.info("Repairing quotes for: %s", paper_id)

        paper_json = json.loads(jp.read_text(encoding="utf-8"))

        # 找到对应 Markdown
        md_path = MARKDOWN_DIR / f"{paper_id}.md"
        if not md_path.exists():
            logger.warning("  Markdown not found: %s", md_path)
            continue

        md_text = md_path.read_text(encoding="utf-8")

        # 执行修复
        repaired = repair_paper_quotes(paper_json, md_text)

        # 覆盖写入
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(repaired, f, ensure_ascii=False, indent=2)

        audit = repaired.get("_quote_audit", {})
        logger.info(
            "  total=%d valid=%d repaired=%d(ws:%d uni:%d blend:%d fuzzy:%d) invalid=%d rate=%.1f%%",
            audit.get("total", 0),
            audit.get("valid_raw", 0),
            audit.get("repaired_ws", 0) + audit.get("repaired_unicode", 0) +
            audit.get("repaired_blend", 0) + audit.get("repaired_fuzzy", 0),
            audit.get("repaired_ws", 0),
            audit.get("repaired_unicode", 0),
            audit.get("repaired_blend", 0),
            audit.get("repaired_fuzzy", 0),
            audit.get("invalid", 0),
            audit.get("invalid_rate", 0) * 100,
        )


if __name__ == "__main__":
    repair_all()
