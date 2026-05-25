"""
pytest conftest — 为反幻觉测试构建隔离的临时知识库环境。

将 tests/fixtures/ 中的对抗性 JSON 和 Markdown 复制到临时
research_kb 目录，然后运行 validate_kb 进行检查。
"""

import json
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
ADV_JSON_DIR = FIXTURES_DIR / "adversarial_json"
ADV_MD_DIR = FIXTURES_DIR / "adversarial_markdown"


@pytest.fixture
def temp_kb(tmp_path: Path):
    """
    构建临时知识库环境。
    对抗性 Markdown 通过 MD_NAME_MAP 映射到正确的 paper_id。
    """
    # Markdown fixture stem → paper_id (JSON 中的 paper_id)
    MD_NAME_MAP = {
        "pubyear_as_epoch": "test1_pubyear_as_epoch",
        "fake_b2b_claim": "test5_title_b2b_but_igs",
        "missing_dcb_uc": "test6_missing_dcb_uc",
        "overclaimed_novelty": "test8_overclaimed_novelty",
        "no_repro_info": "test7_empty_blockers",
    }

    # 创建目录
    md_dir = tmp_path / "research_kb" / "markdown"
    json_dir = tmp_path / "research_kb" / "papers" / "json"
    metadata_dir = tmp_path / "research_kb" / "metadata"
    for d in [md_dir, json_dir, metadata_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # 复制对抗性 JSON
    paper_ids = []
    for jf in sorted(ADV_JSON_DIR.glob("*.json")):
        data = json.loads(jf.read_text(encoding="utf-8"))
        pid = data.get("paper_id", jf.stem)
        paper_ids.append(pid)
        dest = json_dir / f"{pid}.json"
        shutil.copy2(jf, dest)

    # 复制对抗性 Markdown（应用名称映射）
    md_files_present = []
    for mf in sorted(ADV_MD_DIR.glob("*.md")):
        stem = mf.stem
        target_stem = MD_NAME_MAP.get(stem, stem)
        dest = md_dir / f"{target_stem}.md"
        shutil.copy2(mf, dest)
        md_files_present.append(target_stem)

    # 为没有 fixture 的测试创建最小 markdown
    SKIP_AUTO_MD = {
        "test3_nonexistent_paper_id_not_in_markdown_dir",  # 故意缺失，测试 markdown_not_found
    }
    for pid in paper_ids:
        if pid in SKIP_AUTO_MD:
            continue
        expected_path = md_dir / f"{pid}.md"
        if not expected_path.exists():
            _create_minimal_markdown(expected_path, pid)

    # 生成 pdf_parse_report.json
    parse_report = {}
    for pid in paper_ids:
        parse_report[pid] = {
            "paper_id": pid,
            "source_file": f"paper/{pid}.pdf",
            "file_hash": "test_hash",
            "page_count": 3,
            "extraction_method": "test",
        }
    with open(metadata_dir / "pdf_parse_report.json", "w", encoding="utf-8") as f:
        json.dump(parse_report, f, ensure_ascii=False, indent=2)

    return {
        "tmp_path": tmp_path,
        "markdown_dir": md_dir,
        "json_dir": json_dir,
        "metadata_dir": metadata_dir,
        "paper_ids": paper_ids,
        "md_files_present": md_files_present,
    }


def _create_minimal_markdown(path: Path, paper_id: str):
    """为缺少 fixture 的测试创建最小 markdown"""
    templates = {
        "test2_unmatched_quotes": [
            "<!-- PAGE: 1 -->",
            "",
            "# Performance Assessment",
            "",
            "The PPP-B2b orbit radial accuracy is 9.42 cm in the radial component.",
            "The standard EKF dual-frequency PPP was implemented using IF combination.",
            "The B2b correction update interval is 48 seconds according to the ICD.",
            "",
            "<!-- PAGE: 2 -->",
            "",
            "## Results",
            "",
            "The positioning accuracy reached 5 cm in static tests using B2b corrections.",
        ],
        "test4_fake_b2b_product": [
            "<!-- PAGE: 1 -->",
            "",
            "# Evaluation of BDS-3 Real-Time Positioning Performance",
            "",
            "We evaluate the real-time positioning performance of BDS-3 using real-time",
            "products accessed via NTRIP from the IGS Real-Time Service.",
            "",
            "<!-- PAGE: 2 -->",
            "",
            "The stations JFNG and WUH2 were used for testing.",
            "Note: orbit and clock corrections were obtained from CLK93 stream.",
        ],
        "test9_citation_bad_ref": [
            "<!-- PAGE: 1 -->",
            "",
            "# Comprehensive Review of GNSS Augmentation Services",
            "",
            "This paper reviews various GNSS augmentation services including SBAS, CLAS,",
            "PPP-B2b, and Galileo HAS. No original experiments are conducted.",
        ],
        "test10_conflict_passed": [
            "<!-- PAGE: 1 -->",
            "",
            "# Dual-Frequency PPP Performance with Mixed Products",
            "",
            "We propose a novel strategy for combining B2b and RTS corrections.",
            "BDS satellites used PPP-B2b while GPS used IGS RTS via NTRIP.",
            "",
            "<!-- PAGE: 2 -->",
            "",
            "DCB corrections were applied using CAS products.",
            "Data collected from March 1 to March 15, 2022 at stations JFNG, WUH2, CUSV.",
        ],
    }

    lines = templates.get(paper_id)
    if lines is None:
        lines = [
            f"<!-- PAGE: 1 -->",
            f"",
            f"# {paper_id}",
            f"",
            f"Minimal test markdown for {paper_id}.",
        ]

    path.write_text("\n".join(lines), encoding="utf-8")


@pytest.fixture
def validator(temp_kb):
    """
    返回一个配置好临时路径的 validate 函数。
    """
    import validate_kb

    # Monkey-patch 路径
    original_root = validate_kb.PROJECT_ROOT
    original_md = validate_kb.MARKDOWN_DIR
    original_json = validate_kb.JSON_DIR
    original_parse = validate_kb.PARSE_REPORT_PATH
    original_log = validate_kb.LOG_PATH
    original_unresolved = validate_kb.UNRESOLVED_PATH

    tp = temp_kb["tmp_path"]
    validate_kb.PROJECT_ROOT = tp
    validate_kb.MARKDOWN_DIR = tp / "research_kb" / "markdown"
    validate_kb.JSON_DIR = tp / "research_kb" / "papers" / "json"
    validate_kb.PARSE_REPORT_PATH = tp / "research_kb" / "metadata" / "pdf_parse_report.json"
    validate_kb.LOG_PATH = tp / "extraction_log.json"
    validate_kb.UNRESOLVED_PATH = tp / "unresolved_items.yaml"

    yield validate_kb

    # 恢复
    validate_kb.PROJECT_ROOT = original_root
    validate_kb.MARKDOWN_DIR = original_md
    validate_kb.JSON_DIR = original_json
    validate_kb.PARSE_REPORT_PATH = original_parse
    validate_kb.LOG_PATH = original_log
    validate_kb.UNRESOLVED_PATH = original_unresolved
