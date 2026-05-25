"""
Evidence Support Audit — 检查每个 grounding_quote_id 是否真实支持字段值。
不调用 DeepSeek (先做程序化初筛)，不修改语义字段。
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPAIRED_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_repaired"
BANK_DIR = PROJECT_ROOT / "research_kb" / "quote_banks"
REPORT_PATH = PROJECT_ROOT / "research_kb" / "reports" / "evidence_support_audit.md"
UNRESOLVED_REPORT = PROJECT_ROOT / "research_kb" / "reports" / "unresolved_evidence_review.md"

GQ_FIELDS = [
    "product_source", "mathematical_model", "ionospheric_handling",
    "correction_types", "technical_route", "experiment_epoch",
    "datasets", "metrics", "main_results", "novelty_audit",
    "reproducibility_audit",
]

HIGH_RISK_FIELDS = [
    "product_source", "experiment_epoch", "novelty_audit",
    "reproducibility_audit", "ionospheric_handling",
    "datasets", "metrics", "main_results",
]

# ---- 关键词词典 ----

PRODUCT_KEYWORDS = {
    "BDS3_PPP_B2B_BROADCAST": ["PPP-B2b", "B2b", "PPP B2b", "BDS-3 PPP-B2b", "B2b signal", "B2b correction", "BDS B2b", "PPP-B2b service"],
    "IGS_RTS_OR_CLK93": ["IGS RTS", "CLK93", "IGS real-time", "IGS Real-Time Service", "IGS01", "IGS02", "IGS03"],
    "MIXED_PRODUCTS": ["both", "and", "comparison"],
    "QZSS_CLAS": ["QZSS", "CLAS", "L6", "L6D", "centimeter level augmentation"],
}

EPOCH_PATTERNS = [
    r"\d{4}[-/]\d{2}[-/]\d{2}",  # 2021-12-20
    r"DOY\s*\d{1,3}[,.]?\s*\d{4}",  # DOY 354, 2021
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}",
    r"\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}",
    r"\d{4}\s*~\s*\d{4}",
    r"\d+\s*(?:day|week|month|year)s?\s+(?:of|data|observation)",
    r"during\s+\d{4}",
]


def _contains_date(text: str) -> bool:
    for pat in EPOCH_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _contains_product_keywords(text: str) -> list[str]:
    found = []
    for cat, kws in PRODUCT_KEYWORDS.items():
        for kw in kws:
            if kw.lower() in text.lower():
                found.append(cat)
    return list(set(found))


def _is_references_section(quote_text: str) -> bool:
    t = quote_text.lower()
    ref_markers = ["references", "bibliography", "acknowledgment", "acknowledgement", "conflict of interest", "funding"]
    first_100 = t[:100]
    return any(m in first_100 for m in ref_markers)


# ---- 支持度判定 ----

def assess_support(field: str, field_value, quote_text: str, match_type: str, repair_confidence: str) -> dict:
    """
    程序化判定 evidence 对字段值的支持度。
    返回 {"status": "...", "reason": "...", "risk": "high|medium|low"}
    """
    qt = (quote_text or "").strip()
    if not qt:
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "empty quote text", "risk": "high"}

    # --- References section check ---
    if _is_references_section(qt):
        return {"status": "WEAK_SUPPORT", "reason": "quote from references/acknowledgment section", "risk": "high"}

    # --- Keyword overlap risk ---
    if match_type == "keyword_overlap_repair" and repair_confidence == "low":
        # Check if quote actually contains content relevant to the field
        pass  # proceed to field-specific checks

    # --- Field-specific checks ---
    if field == "product_source":
        return _assess_product_source(field_value, qt, match_type, repair_confidence)
    elif field == "experiment_epoch":
        return _assess_experiment_epoch(field_value, qt, match_type)
    elif field == "novelty_audit":
        return _assess_novelty(field_value, qt, match_type)
    elif field == "reproducibility_audit":
        return _assess_repro(field_value, qt, match_type)
    elif field == "ionospheric_handling":
        return _assess_dcb(field_value, qt, match_type)
    elif field == "datasets":
        return _assess_datasets(field_value, qt, match_type)
    elif field == "metrics":
        return _assess_metrics(field_value, qt, match_type)
    elif field == "main_results":
        return _assess_main_results(field_value, qt, match_type)
    else:
        return _assess_generic(field, field_value, qt, match_type, repair_confidence)


def _assess_product_source(fv, qt, mt, rc):
    if not isinstance(fv, dict):
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "non-dict product_source", "risk": "high"}

    actual = fv.get("actual_product_source") or fv.get("actual", "")
    cats_found = _contains_product_keywords(qt)

    if actual == "BDS3_PPP_B2B_BROADCAST":
        if "BDS3_PPP_B2B_BROADCAST" in cats_found:
            return {"status": "STRONG_SUPPORT", "reason": "quote mentions PPP-B2b explicitly", "risk": "low"}
        if cats_found and "BDS3_PPP_B2B_BROADCAST" not in cats_found:
            return {"status": "WRONG_SUPPORT", "reason": f"quote mentions {cats_found}, not PPP-B2b", "risk": "high"}
        return {"status": "WEAK_SUPPORT", "reason": "quote does not contain PPP-B2b keywords", "risk": "medium"}

    if actual == "MIXED_PRODUCTS":
        if len(cats_found) >= 2:
            return {"status": "STRONG_SUPPORT", "reason": "quote mentions multiple product sources", "risk": "low"}
        if len(cats_found) == 1:
            return {"status": "PARTIAL_SUPPORT", "reason": "quote mentions only one product source", "risk": "medium"}
        return {"status": "WEAK_SUPPORT", "reason": "no product keywords in quote", "risk": "high"}

    if actual == "QZSS_CLAS":
        if "QZSS_CLAS" in cats_found:
            return {"status": "STRONG_SUPPORT", "reason": "quote mentions QZSS CLAS", "risk": "low"}
        return {"status": "WEAK_SUPPORT", "reason": "quote lacks QZSS/CLAS keywords", "risk": "high"}

    if actual in ("NOT_MENTIONED", "", None):
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "actual is NOT_MENTIONED but has quotes", "risk": "high"}

    return {"status": "PARTIAL_SUPPORT", "reason": f"product keywords: {cats_found}", "risk": "medium"}


def _assess_experiment_epoch(fv, qt, mt):
    if not isinstance(fv, dict):
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "non-dict", "risk": "high"}
    has_date = _contains_date(qt)
    if has_date:
        return {"status": "STRONG_SUPPORT", "reason": "quote contains date/DOY/period", "risk": "low"}
    if mt == "keyword_overlap_repair":
        return {"status": "WEAK_SUPPORT", "reason": "no date in quote; may just mention experiment setup", "risk": "high"}
    return {"status": "PARTIAL_SUPPORT", "reason": "no explicit date, but may contain temporal context", "risk": "medium"}


def _assess_novelty(fv, qt, mt):
    if not isinstance(fv, dict):
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "non-dict", "risk": "high"}
    grade = fv.get("audit_grade", "")
    # Check for self-defeating quotes
    no_novel = ["no new", "standard", "conventional", "same as", "follows", "not introduce", "not propose", "not present"]
    if any(phrase in qt.lower() for phrase in no_novel):
        if grade in ("A_SUBSTANTIVE", "B_INCREMENTAL"):
            return {"status": "WRONG_SUPPORT", "reason": "quote contradicts novelty claim", "risk": "high"}
        return {"status": "STRONG_SUPPORT", "reason": "quote correctly supports low/no novelty", "risk": "low"}
    return {"status": "PARTIAL_SUPPORT", "reason": "generic supporting quote", "risk": "medium"}


def _assess_repro(fv, qt, mt):
    if not isinstance(fv, dict):
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "non-dict", "risk": "high"}
    blockers = fv.get("reproduction_blockers", [])
    # A reproduction quote should show MISSING info, not present info
    presence_words = ["we provide", "we release", "available at", "download", "open source", "github", "code is", "published"]
    if any(pw in qt.lower() for pw in presence_words):
        if len(blockers) > 0:
            return {"status": "WEAK_SUPPORT", "reason": "quote shows info IS provided, contradicting blocker", "risk": "high"}
    return {"status": "PARTIAL_SUPPORT", "reason": "generic repro evidence", "risk": "medium"}


def _assess_dcb(fv, qt, mt):
    if not isinstance(fv, dict):
        return {"status": "NEEDS_MANUAL_REVIEW", "reason": "non-dict", "risk": "high"}
    dcb_keywords = ["DCB", "code bias", "differential code bias", "CAS DCB", "CODE DCB", "MGEX DCB"]
    if any(kw.lower() in qt.lower() for kw in dcb_keywords):
        return {"status": "STRONG_SUPPORT", "reason": "quote discusses DCB/code bias", "risk": "low"}
    return {"status": "WEAK_SUPPORT", "reason": "quote lacks DCB terminology", "risk": "medium"}


def _assess_datasets(fv, qt, mt):
    stn_keywords = ["station", "MGEX", "IGS", "receiver", "antenna", "JFNG", "WUH2", "CUSV"]
    if any(kw.lower() in qt.lower() for kw in stn_keywords):
        return {"status": "STRONG_SUPPORT", "reason": "quote mentions stations/equipment", "risk": "low"}
    return {"status": "WEAK_SUPPORT", "reason": "no station/dataset keywords", "risk": "medium"}


def _assess_metrics(fv, qt, mt):
    metric_kw = ["RMS", "STD", "cm", "mm", "convergence", "percentile", "95%", "3D error", "accuracy", "precision", "ENU"]
    if any(kw.lower() in qt.lower() for kw in metric_kw):
        return {"status": "STRONG_SUPPORT", "reason": "quote contains metric values", "risk": "low"}
    return {"status": "WEAK_SUPPORT", "reason": "no metric keywords in quote", "risk": "medium"}


def _assess_main_results(fv, qt, mt):
    if len(qt) < 40:
        return {"status": "WEAK_SUPPORT", "reason": "quote too short for result statement", "risk": "high"}
    return {"status": "PARTIAL_SUPPORT", "reason": "generic result quote", "risk": "medium"}


def _assess_generic(field, fv, qt, mt, rc):
    if mt == "exact_repair" and rc == "high":
        return {"status": "STRONG_SUPPORT", "reason": "exact match with high confidence", "risk": "low"}
    if mt == "keyword_overlap_repair" and rc == "low":
        return {"status": "WEAK_SUPPORT", "reason": "keyword overlap with low confidence", "risk": "high"}
    if mt == "keyword_overlap_repair" and rc == "medium":
        return {"status": "PARTIAL_SUPPORT", "reason": "keyword overlap with medium confidence", "risk": "medium"}
    return {"status": "PARTIAL_SUPPORT", "reason": "generic", "risk": "medium"}


# ---- 主审计 ----

def audit_all():
    json_files = sorted(REPAIRED_DIR.glob("*.json"))
    all_results = {}
    unresolved_review = []
    global_match_types = Counter()
    global_support_status = Counter()
    global_field_issues = defaultdict(list)

    for jf in json_files:
        paper_id = jf.stem
        data = json.loads(jf.read_text(encoding="utf-8"))
        bank_path = BANK_DIR / f"{paper_id}_bank.json"
        bank = json.loads(bank_path.read_text(encoding="utf-8")) if bank_path.exists() else []

        paper_stats = {
            "match_types": Counter(),
            "support_status": Counter(),
            "field_audits": {},
            "high_risk_evidence": [],
            "wrong_support": [],
            "unresolved": [],
        }

        for field in GQ_FIELDS:
            val = data.get(field, {})
            if not isinstance(val, dict):
                continue

            ids = val.get("grounding_quote_ids", [])
            if not ids:
                continue

            field_audits = []
            for ref in ids:
                mt = ref.get("match_type", "unknown")
                rc = ref.get("repair_confidence", "unknown")
                qt = ref.get("quote_text", "")
                oq = ref.get("original_deepseek_quote", "")
                qid = ref.get("quote_id")

                paper_stats["match_types"][mt] += 1

                if qid is None:
                    # Unresolved
                    paper_stats["support_status"]["NEEDS_MANUAL_REVIEW"] += 1
                    paper_stats["unresolved"].append({
                        "field": field, "original_quote": oq[:120],
                        "match_type": mt,
                    })
                    unresolved_review.append({
                        "paper_id": paper_id,
                        "field": field,
                        "field_value_summary": str(val)[:200],
                        "original_quote": oq[:150],
                        "status": "unresolved",
                        "suggestion": "manual_replace",
                    })
                    field_audits.append({"status": "NEEDS_MANUAL_REVIEW", "risk": "high", "reason": "unresolved quote"})
                    continue

                # 评估支持度
                result = assess_support(field, val, qt, mt, rc)
                paper_stats["support_status"][result["status"]] += 1
                global_support_status[result["status"]] += 1

                if result["risk"] == "high":
                    paper_stats["high_risk_evidence"].append({
                        "field": field, "quote_id": qid,
                        "match_type": mt, "confidence": rc,
                        "support_status": result["status"],
                        "reason": result["reason"],
                        "quote_preview": qt[:120],
                    })

                if result["status"] == "WRONG_SUPPORT":
                    paper_stats["wrong_support"].append({
                        "field": field, "quote_id": qid,
                        "reason": result["reason"],
                        "quote_preview": qt[:120],
                    })
                    global_field_issues[paper_id].append(f"WRONG_SUPPORT:{field}:{result['reason']}")

                if result["status"] == "WEAK_SUPPORT" and field in HIGH_RISK_FIELDS:
                    global_field_issues[paper_id].append(f"WEAK_SUPPORT_ON_HIGH_RISK:{field}")

                field_audits.append(result)

            paper_stats["field_audits"][field] = {
                "total": len(field_audits),
                "strong": sum(1 for a in field_audits if a["status"] == "STRONG_SUPPORT"),
                "partial": sum(1 for a in field_audits if a["status"] == "PARTIAL_SUPPORT"),
                "weak": sum(1 for a in field_audits if a["status"] == "WEAK_SUPPORT"),
                "wrong": sum(1 for a in field_audits if a["status"] == "WRONG_SUPPORT"),
                "needs_review": sum(1 for a in field_audits if a["status"] == "NEEDS_MANUAL_REVIEW"),
            }

        global_match_types += paper_stats["match_types"]
        all_results[paper_id] = paper_stats

        # 打印摘要
        total_q = sum(paper_stats["match_types"].values())
        high_risk = len(paper_stats["high_risk_evidence"])
        wrong = len(paper_stats["wrong_support"])
        print(f"{paper_id[:45]}: {total_q} quotes, "
              f"high_risk={high_risk}, wrong_support={wrong}, "
              f"status_dist={dict(paper_stats['support_status'])}")

    # 输出 unresolved review
    _write_unresolved_report(unresolved_review)

    # 输出主报告
    _write_audit_report(all_results, global_match_types, global_support_status, global_field_issues)

    return all_results


def _write_unresolved_report(items):
    lines = [
        "# Unresolved Evidence Review",
        "",
        f"Total unresolved: {len(items)}",
        "",
        "| Paper | Field | Original Quote | Suggestion |",
        "|-------|-------|---------------|------------|",
    ]
    for item in items:
        lines.append(f"| {item['paper_id'][:30]} | {item['field']} | {item['original_quote'][:80]} | {item['suggestion']} |")

    lines.extend([
        "",
        "## 处理建议",
        "",
        "1. 每条 unresolved 需人工确认是否可找到替代 quote",
        "2. 如果字段值已经是 NOT_MENTIONED，可以移除该 evidence",
        "3. 如果需要补充，使用 quote_bank 中的 span 替换",
        "4. 如果完全无法找到支撑证据，将该字段标记为 INSUFFICIENT_EVIDENCE",
    ])
    UNRESOLVED_REPORT.write_text("\n".join(lines), encoding="utf-8")


def _write_audit_report(all_results, match_types, support_status, field_issues):
    lines = [
        "# Evidence Support Audit Report",
        "",
        f"生成时间：2026-05-21",
        "",
        "## 1. 总体 Match Type 分布",
        "",
        "| Match Type | Count | Pct |",
        "|-----------|-------|-----|",
    ]
    total = sum(match_types.values())
    for mt, count in match_types.most_common():
        lines.append(f"| {mt} | {count} | {count/total*100:.1f}% |")

    lines.extend([
        "",
        "## 2. 总体 Support Status 分布",
        "",
        "| Status | Count | Pct |",
        "|--------|-------|-----|",
    ])
    for st in ["STRONG_SUPPORT", "PARTIAL_SUPPORT", "WEAK_SUPPORT", "WRONG_SUPPORT", "NEEDS_MANUAL_REVIEW"]:
        count = support_status.get(st, 0)
        lines.append(f"| {st} | {count} | {count/total*100:.1f}% |")

    lines.extend([
        "",
        "## 3. 每篇论文审计",
        "",
    ])

    for pid, stats in all_results.items():
        total_q = sum(stats["match_types"].values())
        wrong = len(stats["wrong_support"])
        high_risk = len(stats["high_risk_evidence"])
        ss = stats["support_status"]

        # Determine pass status
        if wrong > 0:
            pass_status = "BLOCKED"
        elif ss.get("WEAK_SUPPORT", 0) > total_q * 0.10:
            pass_status = "PASS_WITH_WEAK_EVIDENCE"
        elif ss.get("NEEDS_MANUAL_REVIEW", 0) > 0:
            pass_status = "PASS_WITH_WEAK_EVIDENCE"
        else:
            pass_status = "PASS"

        lines.extend([
            f"### {pid}",
            "",
            f"**Status: {pass_status}**",
            f"- Total quotes: {total_q}",
            f"- High risk evidence: {high_risk}",
            f"- Wrong support: {wrong}",
            f"- Support: STRONG={ss.get('STRONG_SUPPORT',0)}, PARTIAL={ss.get('PARTIAL_SUPPORT',0)}, WEAK={ss.get('WEAK_SUPPORT',0)}, WRONG={ss.get('WRONG_SUPPORT',0)}, REVIEW={ss.get('NEEDS_MANUAL_REVIEW',0)}",
            "",
            "#### 字段审计",
            "",
            "| Field | Total | Strong | Partial | Weak | Wrong | Review |",
            "|-------|-------|--------|---------|------|-------|--------|",
        ])
        for field, fa in stats["field_audits"].items():
            lines.append(f"| {field} | {fa['total']} | {fa['strong']} | {fa['partial']} | {fa['weak']} | {fa['wrong']} | {fa['needs_review']} |")

        if high_risk > 0:
            lines.extend([
                "",
                "#### 高风险 Evidence",
                "",
            ])
            for hr in stats["high_risk_evidence"][:10]:
                lines.append(f"- **{hr['field']}**: [{hr['support_status']}] {hr['reason']} (match={hr['match_type']}, conf={hr['confidence']})")

        if wrong > 0:
            lines.extend([
                "",
                "#### ❌ WRONG_SUPPORT",
                "",
            ])
            for w in stats["wrong_support"]:
                lines.append(f"- **{w['field']}**: {w['reason']}")
                lines.append(f"  Quote: {w['quote_preview'][:100]}")

        lines.append("")

    # Field issues summary
    lines.extend([
        "## 4. 高风险字段汇总",
        "",
        "| Paper | Issues |",
        "|-------|--------|",
    ])
    for pid, issues in field_issues.items():
        for issue in issues[:5]:
            lines.append(f"| {pid[:35]} | {issue} |")
        if len(issues) > 5:
            lines.append(f"| {pid[:35]} | ... ({len(issues)} total) |")

    # Final pass rules
    lines.extend([
        "",
        "## 5. 准入判定",
        "",
        "### 判定规则",
        "- invalid_quote_id_rate < 5%: ✅ (quote repair 阶段已验证)",
        "- WRONG_SUPPORT = 0: see per-paper status",
        "- 高风险字段 STRONG+PARTIAL >= 95%: see field audit table",
        "- 语义字段修改数 = 0: ✅",
        "- unresolved evidence 不影响关键字段: see unresolved report",
        "",
        "### 结果",
    ])

    for pid, stats in all_results.items():
        wrong = len(stats["wrong_support"])
        if wrong > 0:
            lines.append(f"- **{pid}**: ❌ BLOCKED ({wrong} WRONG_SUPPORT)")
        else:
            weak = stats["support_status"].get("WEAK_SUPPORT", 0)
            review = stats["support_status"].get("NEEDS_MANUAL_REVIEW", 0)
            total_q = sum(stats["match_types"].values())
            if weak + review > total_q * 0.10:
                lines.append(f"- **{pid}**: ⚠️ PASS_WITH_WEAK_EVIDENCE ({weak} weak, {review} needs review)")
            else:
                lines.append(f"- **{pid}**: ✅ PASS")

    lines.extend([
        "",
        "## 6. 语义字段修改数",
        "",
        "**0** — 本次审计未修改任何语义字段。",
    ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    audit_all()
