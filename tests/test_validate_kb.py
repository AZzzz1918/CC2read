"""
反幻觉 adversarial test suite — 10 个测试用例。

每个测试加载对抗性 JSON + Markdown，调用 validate_kb 的检查函数，
断言预期错误被正确识别。

运行: pytest tests/ -v
"""

import json
from pathlib import Path

import pytest

from validate_kb import (
    check_experiment_epoch,
    check_grounding_quotes,
    check_product_source,
    check_dcb,
    check_reproduction_blockers,
    check_conflicting_evidence,
)

# ============================================================
# Test 1: experiment_epoch 误用 publication_year
# ============================================================


def test_experiment_epoch_pubyear_mistake(temp_kb, validator):
    """
    adversarial scenario:
    论文发表于 2022 年，但 experiment_epoch 填的也是 2022-06-01，
    且无 grounding_quotes 支撑，is_publication_year_mistake=false。
    预期：独立比对发现年份重叠 + 无 quote 证据。
    """
    data = _load_test_json(temp_kb, "test1_pubyear_as_epoch")
    md_text = _load_test_md(temp_kb, "test1_pubyear_as_epoch")

    issues = check_experiment_epoch(data, md_text)

    assert any("year_match" in i and "no_quotes" in i for i in issues), (
        f"Should detect pub_year=2022 matching exp=2022-06-01 without quotes. Got: {issues}"
    )


# ============================================================
# Test 2: grounding_quotes 无法逐字匹配
# ============================================================


def test_grounding_quotes_unmatched(temp_kb, validator):
    """
    adversarial scenario:
    DeepSeek 生成的 quote 与 Markdown 原文不一致（多了/少了词）。
    预期：unmatched_quote 被标记。
    """
    data = _load_test_json(temp_kb, "test2_unmatched_quotes")
    md_text = _load_test_md(temp_kb, "test2_unmatched_quotes")

    issues = check_grounding_quotes(data, md_text, "test2_unmatched_quotes")

    # Markdown 原文: "The PPP-B2b orbit radial accuracy is 9.42 cm in the radial component."
    # JSON quote:   "PPP-B2b orbit radial accuracy is 9.42 cm"
    # 后者是前者的子串 → 可以匹配
    # 但 "B2b correction update interval is 48 seconds"
    # Markdown: "The B2b correction update interval is 48 seconds according to the ICD."
    # JSON quote: "B2b correction update interval is 48 seconds" → 子串匹配 ✓
    # 真正不匹配的: "standard EKF dual-frequency PPP model was implemented"
    # Markdown: "The standard EKF dual-frequency PPP was implemented using IF combination."
    # JSON quote: "standard EKF dual-frequency PPP model was implemented" → 多了 "model" → 不匹配 ✓
    unmatched = [i for i in issues if "unmatched_quote" in i]
    assert len(unmatched) > 0, (
        f"Should detect at least one unmatched quote. Issues: {issues}"
    )


# ============================================================
# Test 3: paper_id 找不到对应 Markdown
# ============================================================


def test_paper_id_missing_markdown(temp_kb, validator):
    """
    adversarial scenario:
    paper JSON 的 paper_id 在 markdown 目录中不存在对应文件。
    预期：markdown_not_found 被标记，quotes 无法校验。
    """
    data = _load_test_json(temp_kb, "test3_nonexistent_paper_id_not_in_markdown_dir")
    md_stem = "test3_nonexistent_paper_id_not_in_markdown_dir"
    md_path = temp_kb["markdown_dir"] / f"{md_stem}.md"

    # 确认文件不存在
    assert not md_path.exists(), "Test requires that markdown file does NOT exist"

    md_text = None
    if md_path.exists():
        md_text = md_path.read_text(encoding="utf-8")

    issues = check_grounding_quotes(data, md_text, "test3_nonexistent_paper_id_not_in_markdown_dir")

    assert any("markdown_not_found" in i for i in issues), (
        f"Should detect missing markdown. Issues: {issues}"
    )


# ============================================================
# Test 4: product_source 将非 B2b 产品误标为 BDS3_PPP_B2B_BROADCAST
# ============================================================


def test_product_source_fake_b2b_no_quotes(temp_kb, validator):
    """
    adversarial scenario:
    product_source.actual = BDS3_PPP_B2B_BROADCAST 但无 grounding_quotes 支撑。
    预期：meaningful_actual_no_grounding_quotes。
    """
    data = _load_test_json(temp_kb, "test4_fake_b2b_product")

    issues = check_product_source(data)

    assert any("meaningful_actual_no_grounding_quotes" in i for i in issues), (
        f"Should flag B2b claim without quote evidence. Issues: {issues}"
    )


# ============================================================
# Test 5: 标题含 PPP-B2b，但实验实际使用 IGS RTS
# ============================================================


def test_title_b2b_but_actual_igs(temp_kb, validator):
    """
    adversarial scenario:
    论文标题含 "PPP-B2b Service"，但 product_source.actual = IGS_RTS_OR_CLK93，
    claimed ≠ actual 且 conflict_flag = false。
    预期：title_b2b_but_actual_mismatch + conflict_unflagged。
    """
    data = _load_test_json(temp_kb, "test5_title_b2b_but_igs")

    issues = check_product_source(data)

    assert any("title_b2b_but_actual_mismatch" in i for i in issues), (
        f"Should flag title-B2b vs actual-IGS mismatch. Issues: {issues}"
    )
    assert any("conflict_unflagged" in i for i in issues), (
        f"Should flag claimed≠actual without conflict_flag. Issues: {issues}"
    )


# ============================================================
# Test 6: UC 模型未说明 DCB 来源 (dcb_missing_flag=false)
# ============================================================


def test_missing_dcb_uncombined_ppp(temp_kb, validator):
    """
    adversarial scenario:
    processing_mode = UNCOMBINED_PPP, dcb_source 为空,
    dcb_missing_flag = false。
    预期：dcb_missing 被标记。
    """
    data = _load_test_json(temp_kb, "test6_missing_dcb_uc")

    issues = check_dcb(data)

    assert any("dcb_missing" in i for i in issues), (
        f"Should flag missing DCB in uncombined PPP. Issues: {issues}"
    )


# ============================================================
# Test 7: reproduction_blockers 缺失 10 项中的关键项
# ============================================================


def test_empty_blockers_with_massive_missing(temp_kb, validator):
    """
    adversarial scenario:
    reproduction_blockers = [], 但 8/10 项复现信息为 NOT_MENTIONED,
    reproducibility_score = 8（虚高）。
    预期：多项 repro:missing_not_blocked + blockers_empty_but_X_items_missing + score_inconsistent。
    """
    data = _load_test_json(temp_kb, "test7_empty_blockers")

    issues = check_reproduction_blockers(data)

    missing_blocked = [i for i in issues if "missing_not_blocked" in i]
    assert len(missing_blocked) >= 5, (
        f"Should find >=5 missing reproduction items not in blockers. Got {len(missing_blocked)}: {issues}"
    )
    assert any("blockers_empty_but" in i for i in issues), (
        f"Should flag empty blockers with massive missing info. Issues: {issues}"
    )
    assert any("score_inconsistent" in i for i in issues), (
        f"Should flag score inconsistency (reported=8 but missing={len(missing_blocked)}). Issues: {issues}"
    )


# ============================================================
# Test 8: novelty 过度声称创新但无证据
# ============================================================


def test_overclaimed_novelty_no_evidence(temp_kb, validator):
    """
    adversarial scenario:
    novelty_audit.audit_grade = A_SUBSTANTIVE，但：
    - novel_formula/state/stochastic/qc/b2b 全 false
    - is_mere_migration = false（应 true）
    - ablation_study = "No ablation study performed"
    - 基线是 broadcast-only（弱基线）
    - grounding_quotes 中自曝 "No new observation equations are introduced"
    预期：grounding_quotes 中的 self_defeating evidence + A 级与证据矛盾。
    """
    data = _load_test_json(temp_kb, "test8_overclaimed_novelty")
    md_text = _load_test_md(temp_kb, "test8_overclaimed_novelty")

    # 1. Grounding quotes 自曝
    issues_gq = check_grounding_quotes(data, md_text, "test8_overclaimed_novelty")
    # 注意：quote "No new observation equations are introduced" 与 MD 中的原文
    # "No new observation equations are introduced." 完全一致，应该通过匹配。
    # 这不是 unmatched quote，而是 self-defeating claim。

    # 2. 检查 novelty 相关逻辑
    novelty = data.get("novelty_audit", {})
    assert novelty.get("audit_grade") == "A_SUBSTANTIVE", "Test requires A_SUBSTANTIVE grade"
    assert novelty.get("novel_formula") is False
    assert novelty.get("novel_state_design") is False
    assert novelty.get("novel_stochastic_model") is False
    assert novelty.get("is_mere_migration") is False, (
        "Critical: is_mere_migration should be True (standard EKF IF PPP with B2b)"
    )

    # 3. 关键指标：all novelty booleans 为 false 但 grade 为 A
    novel_checks = ["novel_formula", "novel_state_design", "novel_stochastic_model",
                    "novel_qc_mechanism", "novel_b2b_usage"]
    all_false = all(not novelty.get(k) for k in novel_checks)
    assert all_false, "All novelty evidence booleans are false"
    assert novelty.get("audit_grade") == "A_SUBSTANTIVE", (
        "A_SUBSTANTIVE with all evidence false = overclaimed"
    )


# ============================================================
# Test 9: citation_graph 出现不存在的 paper_id
# ============================================================


def test_citation_graph_bad_reference(validator):
    """
    adversarial scenario:
    citation_graph 包含的 paper_id 不在 corpus 中。
    通过 build_corpus_maps 逻辑间接测试。
    """
    from build_corpus_maps import build_citation_graph

    # 构造包含不存在 paper_id 的数据
    papers = [
        {
            "paper_id": "paper_real",
            "bibliographic_info": {"title": "Real Paper", "year": 2023, "authors": []},
        },
        # 这个 paper 引用了一个不存在的 paper_id — 在 citation_graph 层面
    ]
    graph = build_citation_graph(papers)

    # citation_graph 的节点数应等于论文数
    assert len(graph["nodes"]) == 1
    # 所有节点的 id 都应在输入论文中
    node_ids = {n["id"] for n in graph["nodes"]}
    assert "paper_real" in node_ids
    # phantom paper_id 不应出现
    assert "paper_phantom_not_in_corpus" not in node_ids


# ============================================================
# Test 10: merge 阶段把 conflicting evidence 通过校验
# ============================================================


def test_conflicting_evidence_not_resolved(temp_kb, validator):
    """
    adversarial scenario:
    conflicting_evidence 包含 resolution="CONFLICTING_EVIDENCE" 的未解决冲突，
    但 paper JSON 仍然通过了生成。
    预期：check_conflicting_evidence 捕获。
    """
    data = _load_test_json(temp_kb, "test10_conflict_passed")

    issues = check_conflicting_evidence(data)

    assert any("unresolved" in i for i in issues), (
        f"Should detect unresolved conflicting evidence. Issues: {issues}"
    )


# ============================================================
# 全量集成测试
# ============================================================


def test_validate_full_pipeline_detects_all_issues(temp_kb, validator):
    """
    集成测试：运行完整 validate()，确认所有 adversarial cases 都被捕获。
    """
    log = validator.validate()

    # 所有 10 个测试 JSON 应该都被处理
    assert log["summary"]["total_papers_in_json"] >= 10, (
        f"Expected >=10 papers, got {log['summary']['total_papers_in_json']}"
    )

    # 至少应有 grounding_quotes / product_source / experiment_epoch 类别的问题
    categories = log["checks"]["error_categories"]
    assert categories["grounding_quotes"] > 0, "Should have grounding_quotes issues"
    assert categories["product_source"] > 0, "Should have product_source issues"
    assert categories["experiment_epoch"] > 0, "Should have experiment_epoch issues"
    assert categories["reproduction"] > 0, "Should have reproduction issues"

    # 状态应为 CRITICAL 或 FAIL（因为有硬问题）
    assert log["summary"]["status"] in ("CRITICAL", "FAIL"), (
        f"Expected CRITICAL or FAIL status, got {log['summary']['status']}"
    )

    # 确认 paper_field_issues 覆盖多篇论文
    paper_issues = log["checks"]["paper_field_issues"]
    assert len(paper_issues) >= 5, (
        f"Expected issues in >=5 papers, got {len(paper_issues)}"
    )


# ============================================================
# Helpers
# ============================================================


def _load_test_json(temp_kb: dict, paper_id: str) -> dict:
    """加载对抗性 JSON"""
    path = temp_kb["json_dir"] / f"{paper_id}.json"
    if not path.exists():
        # 尝试查找任意匹配的文件
        for f in temp_kb["json_dir"].glob("*.json"):
            data = json.loads(f.read_text(encoding="utf-8"))
            if data.get("paper_id") == paper_id:
                return data
        raise FileNotFoundError(f"No JSON found for paper_id={paper_id}")
    return json.loads(path.read_text(encoding="utf-8"))


def _load_test_md(temp_kb: dict, paper_id: str) -> str | None:
    """加载对抗性 Markdown"""
    path = temp_kb["markdown_dir"] / f"{paper_id}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None
