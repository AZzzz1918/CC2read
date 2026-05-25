"""
KNOWLEDGE BASE UPDATE — 总入口脚本。

运行方式：
    python scripts/update_kb.py

执行顺序：
    1. 扫描 paper/ 中的 PDF
    2. PDF → danielmiessler-pdf skill → research_kb/markdown/[paper_id].md
       + research_kb/metadata/pdf_parse_report.json
       + research_kb/metadata/needs_ocr.yaml
    3. Markdown → Chunks
    4. DeepSeek-v4 API chunk 抽取
    5. 单篇论文合并
    6. 跨论文图谱构建
    7. 知识库校验（含 grounding quote validation）
    8. 输出日志
"""

import hashlib
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path

# 确保 scripts 目录在 sys.path 中
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from pdf_to_markdown import process_pdf, compute_file_hash
from chunk_markdown import process_markdown
from extract_chunks import extract_all
from merge_paper_chunks import merge_all
from build_corpus_maps import build_all as build_corpus_all
from validate_kb import validate

logger = logging.getLogger("update_kb")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)

PAPER_DIR = PROJECT_ROOT / "paper"
MARKDOWN_DIR = PROJECT_ROOT / "research_kb" / "markdown"
STATE_FILE = PROJECT_ROOT / "research_kb" / ".kb_state.json"


def load_state() -> dict:
    """加载上次处理状态（用于增量更新）"""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_state(state: dict):
    """保存处理状态"""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["last_update"] = datetime.now().isoformat()
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def step(title: str):
    """打印步骤标题"""
    logger.info("=" * 60)
    logger.info("STEP: %s", title)
    logger.info("=" * 60)


def main():
    start_time = time.time()
    logger.info("KNOWLEDGE BASE UPDATE STARTED: %s", datetime.now().isoformat())
    logger.info("Project root: %s", PROJECT_ROOT)

    state = load_state()

    # ========== Step 1: 扫描 paper/ ==========
    step("1/8 扫描 paper/ 目录")
    pdf_files = sorted(PAPER_DIR.glob("*.pdf"))
    logger.info("Found %d PDF files", len(pdf_files))

    if not pdf_files:
        logger.warning("No PDF files found in paper/ directory. 请放入 PDF 后重试。")
        return

    # 计算 hash，判断增量
    new_hashes = {}
    for fp in pdf_files:
        fh = compute_file_hash(fp)
        new_hashes[fp.stem] = {"path": str(fp), "hash": fh}
    previous_hashes = state.get("file_hashes", {})

    changed = set()
    for stem, info in new_hashes.items():
        prev = previous_hashes.get(stem, {}).get("hash", "")
        if info["hash"] != prev:
            changed.add(stem)

    logger.info("Changed/new files: %d / %d", len(changed), len(pdf_files))

    # ========== Step 2: PDF → danielmiessler-pdf skill → Markdown + metadata ==========
    step("2/8 PDF → Markdown (danielmiessler-pdf skill pipeline)")
    md_results = {}
    for fp in pdf_files:
        if fp.stem in changed or not (MARKDOWN_DIR / f"{fp.stem}.md").exists():
            result = process_pdf(fp)
            if result:
                md_results[fp.stem] = result
        else:
            logger.info("Skipping (unchanged): %s", fp.name)
            md_results[fp.stem] = {"paper_id": fp.stem, "status": "skipped"}

    # ========== Step 3: Markdown → Chunks ==========
    step("3/8 Markdown → Chunks")
    md_files = sorted(MARKDOWN_DIR.glob("*.md"))
    for mf in md_files:
        process_markdown(mf)

    # ========== Step 4: DeepSeek chunk 抽取 ==========
    step("4/8 DeepSeek chunk 抽取")
    chunk_results = extract_all(delay=0.5)

    # ========== Step 5: 单篇论文合并 ==========
    step("5/8 单篇论文合并")
    merge_all()

    # ========== Step 6: 跨论文图谱构建 ==========
    step("6/8 跨论文图谱构建")
    corpus = build_corpus_all()

    # ========== Step 7: 知识库校验 ==========
    step("7/8 知识库校验")
    validation_log = validate()

    # ========== Step 8: 保存状态和日志 ==========
    step("8/8 保存状态")
    state["file_hashes"] = new_hashes
    state["validation"] = validation_log.get("summary", {})
    save_state(state)

    elapsed = time.time() - start_time
    logger.info("KNOWLEDGE BASE UPDATE COMPLETE in %.1f seconds", elapsed)
    logger.info("Summary: %s", json.dumps(validation_log.get("summary", {}), ensure_ascii=False))
    logger.info("Check extraction_log.json for detailed validation results.")


if __name__ == "__main__":
    main()
