"""
跨论文知识图谱构建模块。

基于所有 paper JSON 生成：
- technical_routes.yaml
- problem_evolution.yaml
- citation_graph.json
- method_lineage.yaml
- dataset_metric_index.yaml
- reproduction_index.yaml
- reports/*.md
"""

import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json"
CORPUS_DIR = PROJECT_ROOT / "research_kb" / "corpus"
REPORTS_DIR = PROJECT_ROOT / "research_kb" / "reports"

logger = logging.getLogger("corpus")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)


def load_all_papers() -> list[dict]:
    """加载所有 paper JSON"""
    papers = []
    for jp in sorted(JSON_DIR.glob("*.json")):
        try:
            data = json.loads(jp.read_text(encoding="utf-8"))
            papers.append(data)
        except Exception as e:
            logger.warning("Failed to load %s: %s", jp.name, e)
    logger.info("Loaded %d papers", len(papers))
    return papers


def build_technical_routes(papers: list[dict]) -> dict:
    """构建技术路线图"""
    routes = defaultdict(list)
    for p in papers:
        tr = p.get("technical_route", {})
        key_steps = tr.get("key_steps", []) if isinstance(tr, dict) else []
        pid = p.get("paper_id", "unknown")
        routes[pid] = {
            "title": p.get("bibliographic_info", {}).get("title", ""),
            "flow": tr.get("overall_flow", "") if isinstance(tr, dict) else "",
            "steps": key_steps,
            "tools": tr.get("tools_software", []) if isinstance(tr, dict) else [],
        }
    return dict(routes)


def build_problem_evolution(papers: list[dict]) -> dict:
    """构建问题演化图（按年份排列）"""
    evolution = defaultdict(list)
    for p in papers:
        bib = p.get("bibliographic_info", {})
        year = bib.get("year", 0) if isinstance(bib, dict) else 0
        rp = p.get("research_problem", {})
        evolution[str(year)].append({
            "paper_id": p.get("paper_id", ""),
            "problem": rp.get("problem_statement", "") if isinstance(rp, dict) else "",
            "questions": rp.get("research_questions", []) if isinstance(rp, dict) else [],
        })

    sorted_evolution = dict(sorted(evolution.items(), key=lambda x: x[0]))
    return sorted_evolution


def build_citation_graph(papers: list[dict]) -> dict:
    """构建引用关系图（基于 paper_id，后续可扩展）"""
    nodes = []
    for p in papers:
        pid = p.get("paper_id", "")
        bib = p.get("bibliographic_info", {})
        nodes.append({
            "id": pid,
            "title": bib.get("title", "") if isinstance(bib, dict) else "",
            "year": bib.get("year", 0) if isinstance(bib, dict) else 0,
            "authors": [a.get("name", "") if isinstance(a, dict) else str(a) for a in bib.get("authors", [])] if isinstance(bib, dict) else [],
        })

    return {
        "nodes": nodes,
        "edges": [],  # 引用关系需要单独提取（从参考文献中），暂留空
    }


def build_method_lineage(papers: list[dict]) -> dict:
    """构建方法谱系"""
    lineage = {}
    for p in papers:
        pid = p.get("paper_id", "")
        mm = p.get("mathematical_model", {})
        method = p.get("method", {})
        novelty = p.get("novelty_audit", {})

        lineage[pid] = {
            "processing_mode": mm.get("processing_mode", "NOT_MENTIONED") if isinstance(mm, dict) else "NOT_MENTIONED",
            "method_name": method.get("method_name", "") if isinstance(method, dict) else "",
            "novelty_grade": novelty.get("audit_grade", "U_INSUFFICIENT_EVIDENCE") if isinstance(novelty, dict) else "U_INSUFFICIENT_EVIDENCE",
            "is_mere_migration": novelty.get("is_mere_migration", False) if isinstance(novelty, dict) else False,
            "is_ppp_b2b_core_paper": p.get("is_ppp_b2b_core_paper", False),
            "domain_relevance": p.get("domain_relevance", {}).get("value", "unknown") if isinstance(p.get("domain_relevance"), dict) else "unknown",
        }
    return lineage


def build_dataset_metric_index(papers: list[dict]) -> dict:
    """构建数据集和指标索引"""
    idx = {}
    for p in papers:
        pid = p.get("paper_id", "")
        ds = p.get("datasets", {})
        met = p.get("metrics", {})
        epoch = p.get("experiment_epoch", {})

        idx[pid] = {
            "stations": ds.get("stations", []) if isinstance(ds, dict) else [],
            "satellite_systems": ds.get("satellite_systems", []) if isinstance(ds, dict) else [],
            "experiment_epoch": {
                "start": epoch.get("start_date", "NOT_MENTIONED") if isinstance(epoch, dict) else "NOT_MENTIONED",
                "end": epoch.get("end_date", "NOT_MENTIONED") if isinstance(epoch, dict) else "NOT_MENTIONED",
            },
            "convergence_time": met.get("convergence_time", "NOT_MENTIONED") if isinstance(met, dict) else "NOT_MENTIONED",
            "rms_3d": met.get("rms_3d", "NOT_MENTIONED") if isinstance(met, dict) else "NOT_MENTIONED",
            "percentile_95": met.get("percentile_95", "NOT_MENTIONED") if isinstance(met, dict) else "NOT_MENTIONED",
        }
    return idx


def build_reproduction_index(papers: list[dict]) -> dict:
    """构建复现难度索引"""
    idx = {}
    for p in papers:
        pid = p.get("paper_id", "")
        repro = p.get("reproducibility_audit", {})

        if isinstance(repro, dict):
            idx[pid] = {
                "score": repro.get("reproducibility_score", 0),
                "blockers": repro.get("reproduction_blockers", []),
                "code_available": bool(repro.get("code_repository") not in ("NOT_MENTIONED", None, "")),
                "data_available": bool(repro.get("public_observation_data") not in ("NOT_MENTIONED", None, "")),
            }
    # 按复现难度排序
    return dict(sorted(idx.items(), key=lambda x: x[1].get("score", 0), reverse=True))


def generate_report(papers: list[dict], corpus_data: dict):
    """生成综合报告"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # 概览报告
    overview_lines = [
        "# GNSS / PPP-B2b 科研论文知识库 — 概览报告",
        "",
        f"生成时间：自动",
        f"论文总数：{len(papers)}",
        "",
        "## 论文列表",
        "",
    ]
    for p in papers:
        bib = p.get("bibliographic_info", {})
        title = bib.get("title", "Unknown") if isinstance(bib, dict) else "Unknown"
        authors = bib.get("authors", []) if isinstance(bib, dict) else []
        author_names = ", ".join(a.get("name", "") if isinstance(a, dict) else str(a) for a in authors[:3])
        is_core = "⭐" if p.get("is_ppp_b2b_core_paper") else "🔬"
        domain = p.get("domain_relevance", {}).get("value", "unknown") if isinstance(p.get("domain_relevance"), dict) else "unknown"
        overview_lines.append(f"- {is_core} **{title}** — {author_names} ({bib.get('year', '?')}) [{domain}]")

    overview_path = REPORTS_DIR / "overview.md"
    overview_path.write_text("\n".join(overview_lines), encoding="utf-8")

    # 复现难度报告
    repro_idx = corpus_data.get("reproduction_index", {})
    repro_lines = [
        "# 复现难度索引",
        "",
        "| 论文 | 复现评分 | 代码 | 数据 | 主要阻断项 |",
        "|------|---------|------|------|-----------|",
    ]
    for pid, info in repro_idx.items():
        code = "✓" if info["code_available"] else "✗"
        data = "✓" if info["data_available"] else "✗"
        top_blocker = info["blockers"][0] if info["blockers"] else "-"
        repro_lines.append(f"| {pid} | {info['score']}/10 | {code} | {data} | {top_blocker} |")

    repro_path = REPORTS_DIR / "reproduction_index.md"
    repro_path.write_text("\n".join(repro_lines), encoding="utf-8")


def build_all():
    """执行全量知识图谱构建"""
    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    papers = load_all_papers()
    if not papers:
        logger.warning("No papers loaded, skipping corpus map generation")
        return

    # 构建各图谱
    corpus = {}

    corpus["technical_routes"] = build_technical_routes(papers)
    with open(CORPUS_DIR / "technical_routes.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(corpus["technical_routes"], f, allow_unicode=True, sort_keys=False)
    logger.info("Generated technical_routes.yaml")

    corpus["problem_evolution"] = build_problem_evolution(papers)
    with open(CORPUS_DIR / "problem_evolution.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(corpus["problem_evolution"], f, allow_unicode=True, sort_keys=False)
    logger.info("Generated problem_evolution.yaml")

    corpus["citation_graph"] = build_citation_graph(papers)
    with open(CORPUS_DIR / "citation_graph.json", "w", encoding="utf-8") as f:
        json.dump(corpus["citation_graph"], f, ensure_ascii=False, indent=2)
    logger.info("Generated citation_graph.json")

    corpus["method_lineage"] = build_method_lineage(papers)
    with open(CORPUS_DIR / "method_lineage.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(corpus["method_lineage"], f, allow_unicode=True, sort_keys=False)
    logger.info("Generated method_lineage.yaml")

    corpus["dataset_metric_index"] = build_dataset_metric_index(papers)
    with open(CORPUS_DIR / "dataset_metric_index.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(corpus["dataset_metric_index"], f, allow_unicode=True, sort_keys=False)
    logger.info("Generated dataset_metric_index.yaml")

    corpus["reproduction_index"] = build_reproduction_index(papers)
    with open(CORPUS_DIR / "reproduction_index.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(corpus["reproduction_index"], f, allow_unicode=True, sort_keys=False)
    logger.info("Generated reproduction_index.yaml")

    # 生成报告
    generate_report(papers, corpus)
    logger.info("Generated reports")

    return corpus


if __name__ == "__main__":
    build_all()
