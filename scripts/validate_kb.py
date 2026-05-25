"""
知识库校验脚本 —— 反幻觉防线 v2。

新增硬规则：
- grounding_quotes: invalid rate > 5% → failed_validation; > 20% → block from corpus
- product_source: expanded enum (QZSS_CLAS, QZSS_MADOCA, SBAS etc.)
- domain_relevance: consistency check with product_source
- non-B2B guard: verify non-B2B papers aren't mislabeled as core_ppp_b2b
"""

import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPER_DIR = PROJECT_ROOT / "paper"
MARKDOWN_DIR = PROJECT_ROOT / "research_kb" / "markdown"
JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json"
METADATA_DIR = PROJECT_ROOT / "research_kb" / "metadata"
PARSE_REPORT_PATH = METADATA_DIR / "pdf_parse_report.json"
UNRESOLVED_PATH = PROJECT_ROOT / "unresolved_items.yaml"
LOG_PATH = PROJECT_ROOT / "extraction_log.json"

logger = logging.getLogger("validate")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)

# ---- 常量 ----

GQ_FIELDS = [
    "product_source", "mathematical_model", "ionospheric_handling",
    "correction_types", "technical_route", "experiment_epoch",
    "datasets", "metrics", "main_results", "novelty_audit",
    "reproducibility_audit",
]

INVALID_QUOTE_RATE_WARN = 0.05   # 5%
INVALID_QUOTE_RATE_FAIL = 0.10  # 10%
INVALID_QUOTE_RATE_BLOCK = 0.20  # 20%

# 非 B2B 关键词检测（正文层面）
NON_B2B_MARKERS = {
    "QZSS_CLAS": [
        r"QZSS\s*CLAS", r"Centimeter\s*Level\s*Augmentation\s*Service",
        r"CLAS\s*augmentation", r"L6D\s*signal", r"L6\s*augmentation\s*signal",
        r"L6D\s*augmentation", r"CLAS\s*service",
    ],
    "QZSS_MADOCA": [
        r"MADOCA", r"L6E\s*(?:signal|product)",
    ],
    "SBAS": [
        r"\bSBAS\b", r"\bWAAS\b", r"\bEGNOS\b", r"\bMSAS\b", r"\bGAGAN\b",
    ],
}

# ---- 工具函数 ----


def _normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _normalize_unicode(text: str) -> str:
    replacements = {
        "​": "", "‌": "", "‍": "", "﻿": "",
        "‎": "", "‏": "",
        "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "--",
        "‘": "'", "’": "'", "“": '"', "”": '"',
        " ": " ", "　": " ",
    }
    result = text
    for k, v in replacements.items():
        result = result.replace(k, v)
    return result


def _normalize_blend(text: str) -> str:
    """尝试修复 PDF 提取导致的单词粘连"""
    result = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    result = re.sub(r"(\d)([a-zA-Z])", r"\1 \2", result)
    result = re.sub(r"([a-zA-Z])(\d)", r"\1 \2", result)
    return _normalize_ws(result)


def _fuzzy_match(text_a: str, text_b: str, threshold: float = 0.90) -> bool:
    """使用 difflib 做 fuzzy 匹配"""
    import difflib
    ratio = difflib.SequenceMatcher(None, text_a, text_b).ratio()
    return ratio >= threshold


def _find_quote_with_level(md_text: str, quote: str) -> tuple[bool, str]:
    """
    多级匹配 quote，返回 (matched, level)。
    level: "exact" | "normalized" | "unicode" | "blend" | "fuzzy" | "none"
    """
    q = quote.strip()
    if not q:
        return False, "none"

    # Level 1: exact substring
    if q in md_text:
        return True, "exact"

    # Level 2: whitespace normalized
    q_ws = _normalize_ws(q)
    md_ws = _normalize_ws(md_text)
    if q_ws in md_ws:
        return True, "normalized"

    # Level 3: unicode normalized
    q_u = _normalize_unicode(q_ws)
    md_u = _normalize_unicode(md_ws)
    if q_u in md_u:
        return True, "unicode"

    # Level 4: blend expansion (fix PDF word merging)
    q_b = _normalize_blend(q_u)
    md_b = _normalize_blend(md_u)
    if q_b in md_b:
        return True, "blend"

    # Level 5: difflib fuzzy (threshold 0.90)
    if _fuzzy_match(q_b, md_b, threshold=0.90):
        return True, "fuzzy"

    return False, "none"


def _find_quote_any_level(md_text: str, quote: str) -> bool:
    """Legacy boolean alias"""
    ok, _ = _find_quote_with_level(md_text, quote)
    return ok


def _find_quote_verbatim(md_text: str, quote: str) -> bool:
    """Legacy alias — 多级匹配"""
    return _find_quote_any_level(md_text, quote)


def _load_paper_id_mapping() -> dict[str, str]:
    mapping = {}
    if PARSE_REPORT_PATH.exists():
        try:
            reports = json.loads(PARSE_REPORT_PATH.read_text(encoding="utf-8"))
            for paper_id in reports:
                mapping[paper_id] = paper_id
        except Exception:
            pass
    for md_path in sorted(MARKDOWN_DIR.glob("*.md")):
        mapping[md_path.stem] = md_path.stem
    return mapping


def _extract_year_from_date(date_str: str) -> int | None:
    if not date_str or date_str in ("NOT_MENTIONED", "INSUFFICIENT_EVIDENCE", ""):
        return None
    m = re.search(r"(\d{4})", str(date_str))
    return int(m.group(1)) if m else None


# ---- grounding_quotes 审计 ----

def check_grounding_quotes(data: dict, md_text: str | None, pid: str) -> tuple[list[str], dict]:
    """
    返回 (issues, stats) where stats = {total, invalid, invalid_rate, ...}
    """
    issues = []
    total_quotes = 0
    invalid = 0
    field_invalid_counts: dict[str, int] = {}

    if md_text is None:
        # 无 Markdown → 所有 quotes 无法验证
        for field in GQ_FIELDS:
            val = data.get(field, {})
            if isinstance(val, dict):
                quotes = val.get("grounding_quotes", [])
                if quotes:
                    total_quotes += len(quotes)
                    invalid += len(quotes)
                    field_invalid_counts[field] = len(quotes)
        issues.append(f"markdown_not_found:all_{total_quotes}_quotes_unverified")
        stats = {"total": total_quotes, "invalid": invalid,
                 "invalid_rate": 1.0, "field_invalid": field_invalid_counts}
        return issues, stats

    # --- 检查是否使用 post-repair 格式 (grounding_quote_ids) ---
    has_quote_ids = False
    for field in GQ_FIELDS:
        val = data.get(field, {})
        if isinstance(val, dict) and val.get("grounding_quote_ids"):
            has_quote_ids = True
            break

    if has_quote_ids:
        # Post-repair 路径：基于 quote_id 有效性
        return _check_grounding_quote_ids(data, md_text, pid, issues, total_quotes, invalid, field_invalid_counts)

    # 原始路径：基于字符串匹配
    return _check_grounding_quotes_legacy(data, md_text, pid, issues, total_quotes, invalid, field_invalid_counts)


def _check_grounding_quote_ids(data, md_text, pid, issues, total_quotes, invalid, field_invalid_counts):
    """基于 quote_id 有效性的校验（post quote-repair）"""
    level_counts = {"valid_quote_id": 0, "unresolved": 0}

    for field in GQ_FIELDS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue
        ids = val.get("grounding_quote_ids", [])
        field_invalid = 0
        for ref in ids:
            total_quotes += 1
            qid = ref.get("quote_id") if isinstance(ref, dict) else None
            if qid:
                level_counts["valid_quote_id"] += 1
            else:
                invalid += 1
                field_invalid += 1
                level_counts["unresolved"] += 1
                oq = ref.get("original_deepseek_quote", "") if isinstance(ref, dict) else ""
                issues.append(f"unresolved_quote_id:{field}:{oq[:80]}")
        if field_invalid > 0:
            field_invalid_counts[field] = field_invalid

    invalid_rate = invalid / total_quotes if total_quotes > 0 else 0.0
    valid_rate = 1.0 - invalid_rate

    if total_quotes > 0:
        issues.insert(0, f"quote_id_valid_rate:{valid_rate:.1%},invalid_id_rate:{invalid_rate:.1%}")

    if invalid_rate > INVALID_QUOTE_RATE_BLOCK:
        issues.insert(0, f"BLOCKED:invalid_quote_id_rate_{invalid_rate:.1%}_exceeds_{INVALID_QUOTE_RATE_BLOCK:.0%}")
    elif invalid_rate > INVALID_QUOTE_RATE_FAIL:
        issues.insert(0, f"FAILED_VALIDATION:invalid_quote_id_rate_{invalid_rate:.1%}_exceeds_{INVALID_QUOTE_RATE_FAIL:.0%}")
    elif invalid_rate > INVALID_QUOTE_RATE_WARN:
        issues.insert(0, f"WARN:invalid_quote_id_rate_{invalid_rate:.1%}_exceeds_{INVALID_QUOTE_RATE_WARN:.0%}")

    # 检查字段是否有至少一个 valid quote_id
    for field in GQ_FIELDS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue
        ids = val.get("grounding_quote_ids", [])
        if not ids:
            continue
        has_valid = any(
            (isinstance(ref, dict) and ref.get("quote_id"))
            for ref in ids
        )
        if not has_valid:
            issues.append(f"field_all_invalid_quote_ids:{field}")
            meaningful_count = sum(
                1 for k, v in val.items()
                if k not in ("grounding_quote_ids", "grounding_quotes", "reproduction_blockers",
                             "conflicting_evidence", "evidence_status", "quote_valid", "other_metrics")
                and v and v not in ("NOT_MENTIONED", "INSUFFICIENT_EVIDENCE", "", None, [], {})
            )
            if meaningful_count > 0:
                issues.append(f"missing_quote_id_evidence:{field}({meaningful_count}_meaningful_fields)")

    stats = {
        "total": total_quotes,
        "invalid": invalid,
        "invalid_rate": round(invalid_rate, 4),
        "valid_quote_id_rate": round(valid_rate, 4),
        "match_levels": level_counts,
        "field_invalid": field_invalid_counts,
    }
    return issues, stats


def _check_grounding_quotes_legacy(data, md_text, pid, issues, total_quotes, invalid, field_invalid_counts):
    """原始字符串匹配校验"""
    level_counts = {"exact": 0, "normalized": 0, "unicode": 0, "blend": 0, "fuzzy": 0, "none": 0}

    for field in GQ_FIELDS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue
        quotes = val.get("grounding_quotes", [])
        field_invalid = 0
        for q in quotes:
            total_quotes += 1
            matched, level = _find_quote_with_level(md_text, q)
            level_counts[level] = level_counts.get(level, 0) + 1
            if not matched:
                invalid += 1
                field_invalid += 1
                issues.append(f"unmatched_quote:{field}:{q[:100]}")
        if field_invalid > 0:
            field_invalid_counts[field] = field_invalid

    invalid_rate = invalid / total_quotes if total_quotes > 0 else 0.0
    exact_rate = level_counts["exact"] / total_quotes if total_quotes > 0 else 0.0
    normalized_rate = (level_counts["exact"] + level_counts["normalized"] + level_counts["unicode"] + level_counts["blend"]) / total_quotes if total_quotes > 0 else 0.0
    fuzzy_rate = (normalized_rate * total_quotes + level_counts["fuzzy"]) / total_quotes if total_quotes > 0 else 0.0

    if total_quotes > 0:
        issues.insert(0, f"quote_match_rates:exact={exact_rate:.1%},normalized={normalized_rate:.1%},fuzzy={fuzzy_rate:.1%},invalid={invalid_rate:.1%}")

    if invalid_rate > INVALID_QUOTE_RATE_BLOCK:
        issues.insert(0, f"BLOCKED:invalid_quote_rate_{invalid_rate:.1%}_exceeds_{INVALID_QUOTE_RATE_BLOCK:.0%}")
    elif invalid_rate > INVALID_QUOTE_RATE_FAIL:
        issues.insert(0, f"FAILED_VALIDATION:invalid_quote_rate_{invalid_rate:.1%}_exceeds_{INVALID_QUOTE_RATE_FAIL:.0%}")
    elif invalid_rate > INVALID_QUOTE_RATE_WARN:
        issues.insert(0, f"WARN:invalid_quote_rate_{invalid_rate:.1%}_exceeds_{INVALID_QUOTE_RATE_WARN:.0%}")

    # 检查关键字段只有 invalid quotes
    for field in GQ_FIELDS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue
        quotes = val.get("grounding_quotes", [])
        if not quotes:
            continue
        valid_quotes = [q for q in quotes if _find_quote_any_level(md_text, q)]
        if len(valid_quotes) == 0 and len(quotes) > 0:
            issues.append(f"field_all_invalid_quotes:{field}")
            meaningful_count = sum(
                1 for k, v in val.items()
                if k not in ("grounding_quotes", "reproduction_blockers", "conflicting_evidence",
                             "evidence_status", "quote_valid", "other_metrics")
                and v and v not in ("NOT_MENTIONED", "INSUFFICIENT_EVIDENCE", "", None, [], {})
            )
            if meaningful_count > 0 and len(valid_quotes) == 0:
                issues.append(f"missing_grounding_quotes:{field}({meaningful_count}_meaningful_fields_no_valid_quotes)")

    stats = {
        "total": total_quotes,
        "invalid": invalid,
        "invalid_rate": round(invalid_rate, 4),
        "exact_match_rate": round(exact_rate, 4),
        "normalized_match_rate": round(normalized_rate, 4),
        "fuzzy_match_rate": round(fuzzy_rate, 4),
        "match_levels": level_counts,
        "field_invalid": field_invalid_counts,
    }
    return issues, stats


# ---- product_source 审计 ----

def check_product_source(data: dict, md_text: str | None) -> list[str]:
    """
    检查 product_source v2：
    1. actual_product_source 使用新的扩展枚举
    2. 检查 QZSS/SBAS/MADOCA 误标为 B2B
    3. conflict_flag 正确性
    4. domain_relevance 一致性
    """
    issues = []
    ps = data.get("product_source", {})
    if not isinstance(ps, dict):
        return issues

    actual = ps.get("actual_product_source") or ps.get("actual", "")
    claimed = ps.get("claimed", "")
    conflict_flag = ps.get("conflict_flag", False)
    quotes = ps.get("grounding_quotes", [])

    # 1. 检查是否误标 BDS3_PPP_B2B_BROADCAST
    if actual == "BDS3_PPP_B2B_BROADCAST" and md_text:
        # 在正文中搜 QZSS/SBAS/MADOCA 关键词
        for service_name, patterns in NON_B2B_MARKERS.items():
            for pat in patterns:
                if re.search(pat, md_text, re.IGNORECASE):
                    issues.append(
                        f"product_source:b2b_claimed_but_{service_name}_found_in_text(pattern={pat})"
                    )
                    break

    # 2. 正文有 QZSS CLAS 但 claimed 和 actual 都不是 QZSS_CLAS
    # 仅当 claimed 包含 CLAS 关键字或 CLAS 出现 ≥5 次才报错
    if md_text and actual != "QZSS_CLAS":
        clas_count = sum(len(re.findall(pat, md_text, re.IGNORECASE))
                        for pat in NON_B2B_MARKERS["QZSS_CLAS"])
        claimed_has_clas = any(
            re.search(pat, str(claimed), re.IGNORECASE)
            for pat in NON_B2B_MARKERS["QZSS_CLAS"]
        )
        if (claimed_has_clas or clas_count >= 5) and actual not in ("NOT_MENTIONED", "MIXED_PRODUCTS"):
            issues.append(
                f"product_source:qzss_clas_misclassified_as_{actual}"
            )

    # 3. 正文或 claimed 有 MADOCA 但标记不是 QZSS_MADOCA
    # 仅当 claimed product 包含 MADOCA 关键字或正文中 MADOCA 出现 ≥5 次才报错
    if md_text and actual != "QZSS_MADOCA":
        madoca_count = sum(len(re.findall(pat, md_text, re.IGNORECASE))
                          for pat in NON_B2B_MARKERS["QZSS_MADOCA"])
        claimed_has_madoca = any(
            re.search(pat, str(claimed), re.IGNORECASE)
            for pat in NON_B2B_MARKERS["QZSS_MADOCA"]
        )
        if claimed_has_madoca or madoca_count >= 5:
            issues.append(
                f"product_source:madoca_misclassified_as_{actual}(claimed_has_madoca={claimed_has_madoca},mentions={madoca_count})"
            )

    # 4. conflict_flag 应该是 true 的情况：title/abstract 有 PPP-B2b 但 actual 不是
    bib = data.get("bibliographic_info", {})
    title = bib.get("title", "") if isinstance(bib, dict) else ""
    has_b2b_in_title = bool(
        re.search(r"PPP[- ]?B2b|BDS[- ]?3.*B2b|\bB2b\b", title, re.IGNORECASE)
    )
    is_b2b_actual = actual in ("BDS3_PPP_B2B_BROADCAST",)
    is_non_b2b_actual = actual in (
        "QZSS_CLAS", "QZSS_MADOCA", "SBAS", "RTK_NTRIP",
        "IGS_RTS_OR_CLK93", "CNES_OR_OTHER_RTS",
        "POST_PROCESSED_FINAL_PRODUCTS", "OTHER_NON_B2B_GNSS_SERVICE",
    )

    if has_b2b_in_title and is_non_b2b_actual and not conflict_flag:
        issues.append(
            f"product_source:title_b2b_but_actual_{actual}_conflict_flag_not_set"
        )

    # 5. 如果 claimed 和 actual 都是非 B2B 服务且一致 → 不是 conflict
    if (claimed and actual
            and claimed not in ("NOT_MENTIONED",)
            and actual not in ("NOT_MENTIONED",)):
        # 只有当 title/abstract 声称 B2B 且 actual 不是 B2B 时才是真 conflict
        if not has_b2b_in_title and conflict_flag:
            issues.append("product_source:conflict_flag_set_but_no_b2b_claim_in_title")

    return issues


# ---- domain_relevance 审计 ----

def check_domain_relevance(data: dict) -> list[str]:
    """验证 domain_relevance 与 product_source 的一致性"""
    issues = []
    dr = data.get("domain_relevance", {})
    ps = data.get("product_source", {})
    is_core = data.get("is_ppp_b2b_core_paper", False)

    if not isinstance(dr, dict):
        issues.append("domain_relevance:missing")
        return issues

    actual = ps.get("actual_product_source") or ps.get("actual", "")
    dr_value = dr.get("value", "unknown")

    is_b2b_actual = actual == "BDS3_PPP_B2B_BROADCAST"
    is_non_b2b_actual = actual in (
        "QZSS_CLAS", "QZSS_MADOCA", "SBAS", "RTK_NTRIP",
        "IGS_RTS_OR_CLK93", "CNES_OR_OTHER_RTS",
        "POST_PROCESSED_FINAL_PRODUCTS", "OTHER_NON_B2B_GNSS_SERVICE",
    )

    # 规则：非 B2B 产品不能是 core_ppp_b2b
    if is_non_b2b_actual and dr_value == "core_ppp_b2b":
        issues.append(
            f"domain_relevance:non_b2b_marked_core_ppp_b2b(actual={actual})"
        )

    # 规则：非 B2B 产品不能 is_ppp_b2b_core_paper=true
    if is_non_b2b_actual and is_core:
        issues.append(
            f"domain_relevance:non_b2b_paper_is_ppp_b2b_core_paper=true(actual={actual})"
        )

    # 规则：is_ppp_b2b_core_paper 和 domain_relevance 一致
    if is_core and dr_value != "core_ppp_b2b":
        issues.append(
            f"domain_relevance:is_core_paper=true_but_domain={dr_value}"
        )

    # 规则：非 B2B 论文必须有 domain_relevance
    if is_non_b2b_actual and dr_value not in (
        "related_rt_ppp", "related_ssr", "negative_control", "out_of_scope"
    ):
        issues.append(
            f"domain_relevance:missing_for_non_b2b_paper(actual={actual},domain={dr_value})"
        )

    return issues


# ---- experiment_epoch ----

def check_experiment_epoch(data: dict, md_text: str | None) -> list[str]:
    issues = []
    bib = data.get("bibliographic_info", {})
    pub_year = bib.get("year") if isinstance(bib, dict) else None

    epoch = data.get("experiment_epoch", {})
    if not isinstance(epoch, dict):
        return issues

    start_date = epoch.get("start_date", "")
    end_date = epoch.get("end_date", "")
    epoch_quotes = epoch.get("grounding_quotes", [])

    if epoch.get("is_publication_year_mistake"):
        issues.append("experiment_epoch:self_reported_as_publication_year_mistake")

    if pub_year and isinstance(pub_year, int) and pub_year > 1900:
        start_year = _extract_year_from_date(start_date)
        end_year = _extract_year_from_date(end_date)

        if start_year == pub_year or end_year == pub_year:
            if not epoch_quotes:
                issues.append(
                    f"experiment_epoch:year_match_publication_no_quotes("
                    f"pub={pub_year}, exp={start_date}~{end_date})"
                )
            elif md_text:
                quotes_verified = any(
                    _find_quote_any_level(md_text, q) for q in epoch_quotes
                )
                if not quotes_verified:
                    issues.append(
                        f"experiment_epoch:year_match_pub_quotes_not_in_md(pub={pub_year})"
                    )

    if epoch.get("duration_days") in (0, None):
        if start_date and start_date not in ("NOT_MENTIONED",):
            issues.append("experiment_epoch:duration_missing")

    return issues


# ---- DCB ----

def check_dcb(data: dict) -> list[str]:
    issues = []
    iono = data.get("ionospheric_handling", {})
    if not isinstance(iono, dict):
        return issues

    dcb_source = iono.get("dcb_source", "")
    dcb_missing_flag = iono.get("dcb_missing_flag", False)

    if not dcb_source and not dcb_missing_flag:
        mm = data.get("mathematical_model", {})
        mode = mm.get("processing_mode", "") if isinstance(mm, dict) else ""
        if mode in ("SINGLE_FREQUENCY_PPP", "UNCOMBINED_PPP", "PPP_AR", "NOT_MENTIONED"):
            issues.append(f"dcb_missing:mode={mode}:no_dcb_source_and_no_missing_flag")
        else:
            issues.append(f"possible_missing_dcb_handling:mode={mode}")

    return issues


# ---- reproduction_blockers ----

def check_reproduction_blockers(data: dict) -> list[str]:
    issues = []
    repro = data.get("reproducibility_audit", {})
    if not isinstance(repro, dict):
        return ["reproducibility_audit:not_a_dict"]

    blockers = repro.get("reproduction_blockers", [])
    score = repro.get("reproducibility_score")

    checks = [
        ("public_observation_data", "公开观测数据"),
        ("b2b_replay_capability", "PPP-B2b/SSR 实时流回放方法"),
        ("correction_archive", "SSR/B2b correction archive"),
        ("stochastic_model_params", "完整随机模型参数"),
        ("kalman_filter_config", "Kalman filter 初始方差/过程噪声/观测噪声"),
        ("code_repository", "代码仓库"),
        ("run_entry_point", "运行入口"),
        ("config_files", "配置文件"),
        ("metric_definitions", "收敛时间/RMS/STD/95%/3D/ENU 指标定义"),
        ("baseline_details", "基线方法和外部产品版本"),
    ]

    missing_info_fields = []

    for field_key, desc in checks:
        val = repro.get(field_key)
        is_missing = val in (None, "", "NOT_MENTIONED", "INSUFFICIENT_EVIDENCE")
        if is_missing:
            missing_info_fields.append(field_key)
            # NOT_MENTIONED 本身就是阻断依据，不需要 positive quote
            # 检查 blocker 列表中是否覆盖该字段
            blocker_mentions = [
                b for b in blockers
                if isinstance(b, str) and (
                    field_key in b.lower()
                    or desc[:4] in b
                    or any(kw in b.lower() for kw in field_key.split("_"))
                )
            ]
            if not blocker_mentions:
                issues.append(f"repro:missing_not_blocked:{field_key}({desc})")

    # 去重 + 结构化检查
    deduped_blockers = list(set(str(b) for b in blockers))
    duplicates = len(blockers) - len(deduped_blockers)
    if duplicates > 5:
        issues.append(f"repro:blockers_duplicated(dup={duplicates},total={len(blockers)})")

    # blockers 为空但大量缺失
    if len(blockers) == 0 and len(missing_info_fields) >= 5:
        issues.append(f"repro:blockers_empty_but_{len(missing_info_fields)}_items_missing")

    # score 一致（允许 ±3 余量，因为各项权重不同）
    if isinstance(score, (int, float)):
        expected_score = max(0, 10 - len(missing_info_fields))
        if abs(score - expected_score) > 3:
            issues.append(f"repro:score_inconsistent(reported={score},expected≈{expected_score})")

    return issues


# ---- conflicting_evidence ----

def check_conflicting_evidence(data: dict) -> list[str]:
    issues = []
    conflicts = data.get("conflicting_evidence", [])
    if isinstance(conflicts, list):
        unresolved = [c for c in conflicts if isinstance(c, dict)
                      and c.get("resolution") == "CONFLICTING_EVIDENCE"]
        if len(unresolved) > 50:
            issues.append(f"conflicting_evidence:{len(unresolved)}_unresolved_EXCESSIVE_NOISE")
        elif unresolved:
            issues.append(f"conflicting_evidence:{len(unresolved)}_unresolved")
    return issues


# ---- 主校验 ----

def validate() -> dict:
    log = {
        "timestamp": datetime.now().isoformat(),
        "checks": {},
        "errors": [],
        "warnings": [],
        "summary": {},
    }

    pdf_files = sorted(PAPER_DIR.glob("*.pdf"))
    json_files = {f.stem: f for f in sorted(JSON_DIR.glob("*.json"))}

    paper_id_map = _load_paper_id_mapping()

    papers_data: dict[str, dict] = {}
    for stem, jp in json_files.items():
        try:
            data = json.loads(jp.read_text(encoding="utf-8"))
            pid = data.get("paper_id", stem)
            papers_data[pid] = data
        except json.JSONDecodeError as e:
            log["errors"].append(f"Invalid JSON: {jp.name} - {e}")

    log["checks"]["paper_count"] = len(papers_data)

    # ---- 逐篇审计 ----
    paper_issues: dict[str, list] = {}
    paper_quote_stats: dict[str, dict] = {}
    paper_status: dict[str, str] = {}  # paper_id → "PASS" | "WARN" | "FAIL" | "BLOCKED"

    for pid, data in papers_data.items():
        issues = []

        md_stem = paper_id_map.get(pid, pid)
        md_path = MARKDOWN_DIR / f"{md_stem}.md"
        md_text = None
        if md_path.exists():
            md_text = md_path.read_text(encoding="utf-8")
        else:
            issues.append(f"markdown_not_found:expected={md_stem}.md")
            log["warnings"].append(f"Markdown not found for paper_id={pid}")

        if not data.get("file_hash"):
            issues.append("missing_file_hash")

        # a. grounding_quotes
        gq_issues, gq_stats = check_grounding_quotes(data, md_text, pid)
        issues.extend(gq_issues)
        paper_quote_stats[pid] = gq_stats

        # b. product_source
        issues.extend(check_product_source(data, md_text))

        # c. domain_relevance
        issues.extend(check_domain_relevance(data))

        # d. experiment_epoch
        issues.extend(check_experiment_epoch(data, md_text))

        # e. DCB
        issues.extend(check_dcb(data))

        # f. reproduction_blockers
        issues.extend(check_reproduction_blockers(data))

        # g. conflicting_evidence
        issues.extend(check_conflicting_evidence(data))

        if issues:
            paper_issues[pid] = issues

        # 判定 paper 状态
        inv_rate = gq_stats.get("invalid_rate", 0)
        has_blocked = any("BLOCKED:" in i for i in issues)
        has_failed = any("FAILED_VALIDATION:" in i for i in issues)
        has_field_all_invalid = any("field_all_invalid_quotes:" in i for i in issues)
        has_product_misclass = any(
            "misclassified" in i or "non_b2b_marked_core" in i
            for i in issues
        )

        if has_blocked or inv_rate > INVALID_QUOTE_RATE_BLOCK:
            paper_status[pid] = "BLOCKED"
        elif has_failed or has_field_all_invalid or has_product_misclass or inv_rate > INVALID_QUOTE_RATE_FAIL:
            paper_status[pid] = "FAIL"
        elif inv_rate > INVALID_QUOTE_RATE_WARN:
            paper_status[pid] = "WARN"
        else:
            paper_status[pid] = "PASS"

    log["checks"]["paper_field_issues"] = paper_issues
    log["checks"]["paper_quote_stats"] = paper_quote_stats
    log["checks"]["paper_status"] = paper_status

    # ---- unresolved_items ----
    if UNRESOLVED_PATH.exists():
        try:
            unresolved = yaml.safe_load(UNRESOLVED_PATH.read_text(encoding="utf-8"))
            log["checks"]["unresolved_items_count"] = (
                len(unresolved) if isinstance(unresolved, list) else 0
            )
        except Exception:
            log["checks"]["unresolved_items_count"] = "parse_error"

    # ---- 分类统计 ----
    error_categories = {
        "grounding_quotes": 0,
        "product_source": 0,
        "domain_relevance": 0,
        "experiment_epoch": 0,
        "dcb": 0,
        "reproduction": 0,
        "conflicting_evidence": 0,
        "other": 0,
    }
    for pid, issues in paper_issues.items():
        for issue in issues:
            cat = "other"
            if "unmatched_quote" in issue or "quote_unmatch_rate" in issue or "missing_grounding_quotes" in issue or "invalid_quote_rate" in issue or "BLOCKED" in issue or "FAILED_VALIDATION" in issue or "field_all_invalid" in issue or "markdown_not_found" in issue:
                cat = "grounding_quotes"
            elif "product_source" in issue or "qzss_clas" in issue or "madoca" in issue or "b2b_claimed" in issue:
                cat = "product_source"
            elif "domain_relevance" in issue:
                cat = "domain_relevance"
            elif "experiment_epoch" in issue:
                cat = "experiment_epoch"
            elif "dcb" in issue:
                cat = "dcb"
            elif "repro" in issue:
                cat = "reproduction"
            elif "conflicting" in issue:
                cat = "conflicting_evidence"
            error_categories[cat] += 1

    log["checks"]["error_categories"] = error_categories

    # ---- 汇总 ----
    total_issues = sum(len(v) for v in paper_issues.values())
    error_count = len(log["errors"])
    warn_count = len(log["warnings"])

    blocked_count = sum(1 for s in paper_status.values() if s == "BLOCKED")
    failed_count = sum(1 for s in paper_status.values() if s == "FAIL")
    warn_count_p = sum(1 for s in paper_status.values() if s == "WARN")
    passed_count = sum(1 for s in paper_status.values() if s == "PASS")

    if blocked_count > 0:
        status = "BLOCKED"
    elif failed_count > 0:
        status = "FAIL"
    elif error_count > 0:
        status = "FAIL"
    elif total_issues > 20:
        status = "WARN"
    else:
        status = "PASS"

    log["summary"] = {
        "total_pdf": len(pdf_files),
        "total_papers_in_json": len(papers_data),
        "total_issues": total_issues,
        "papers_with_issues": len(paper_issues),
        "papers_passed": passed_count,
        "papers_warn": warn_count_p,
        "papers_failed": failed_count,
        "papers_blocked": blocked_count,
        "errors": error_count,
        "warnings": warn_count,
        "error_categories": error_categories,
        "status": status,
        "blocked_from_corpus": [pid for pid, s in paper_status.items() if s == "BLOCKED"],
        "failed_validation": [pid for pid, s in paper_status.items() if s in ("BLOCKED", "FAIL")],
        "blocked_from_search_index": [pid for pid, s in paper_status.items()
                                      if s in ("BLOCKED", "FAIL")],
    }

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

    logger.info("=" * 60)
    logger.info("VALIDATION: %s", status)
    logger.info("Papers: %d total | %d PASS | %d WARN | %d FAIL | %d BLOCKED",
                len(papers_data), passed_count, warn_count_p, failed_count, blocked_count)
    logger.info("Issue categories: %s", json.dumps(error_categories, ensure_ascii=False))
    logger.info("Full log: %s", LOG_PATH)

    if blocked_count > 0:
        logger.warning("BLOCKED papers (excluded from corpus): %s", log["summary"]["blocked_from_corpus"])

    return log


if __name__ == "__main__":
    validate()
