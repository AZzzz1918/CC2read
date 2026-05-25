"""
Markdown 分块模块。

优先按章节切分；章节无法识别时按页码和长度切分。
每个 chunk 保留页码、章节信息，方便 quote grounding。
"""

import hashlib
import json
import logging
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_DIR = PROJECT_ROOT / "research_kb" / "markdown"
CHUNKS_DIR = PROJECT_ROOT / "research_kb" / "chunks"

logger = logging.getLogger("chunk")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)

MAX_CHUNK_CHARS = 3000  # 每个 chunk 最大字符数，降低截断率


def _detect_sections(markdown_text: str) -> list[dict]:
    """
    检测章节边界。返回 [{section_title, start_line, end_line, level}, ...]
    """
    lines = markdown_text.split("\n")
    sections = []
    page_markers = []  # (line_idx, page_num)

    for i, line in enumerate(lines):
        # 记录页码标记 (支持 OCR_DERIVED)
        m = re.match(r"^<!-- PAGE: (\d+)(?:\s+OCR_DERIVED)?\s+-->", line)
        if m:
            page_markers.append((i, int(m.group(1))))
        # 检测 Markdown 标题
        m = re.match(r"^(#{1,3})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            sections.append({
                "title": title,
                "start_line": i,
                "level": level,
            })

    # 设置结束行
    for i, sec in enumerate(sections):
        if i + 1 < len(sections):
            sec["end_line"] = sections[i + 1]["start_line"] - 1
        else:
            sec["end_line"] = len(lines) - 1

    # 给每个 section 分配页码
    for sec in sections:
        sec["page_start"] = _line_to_page(sec["start_line"], page_markers)
        sec["page_end"] = _line_to_page(sec["end_line"], page_markers)

    return sections


def _line_to_page(line_idx: int, page_markers: list[tuple[int, int]]) -> int | None:
    """根据行号推断页码"""
    page = None
    for lm_idx, pn in page_markers:
        if lm_idx <= line_idx:
            page = pn
        else:
            break
    return page


def _classify_chunk_type(section_title: str) -> str:
    """根据章节标题推断 chunk_type"""
    t = section_title.lower()
    if any(kw in t for kw in ["abstract", "摘要"]):
        return "abstract"
    if any(kw in t for kw in ["introduction", "intro", "引言", "介绍", "背景"]):
        return "introduction"
    if any(kw in t for kw in ["method", "approach", "model", "algorithm", "方法", "模型", "算法", "原理"]):
        return "method"
    if any(kw in t for kw in ["experiment", "experimental", "test", "validation", "实验", "测试", "验证", "结果与分析", "performance", "analysis"]):
        return "experiment"
    if any(kw in t for kw in ["result", "结果", "performance assessment", "evaluation"]):
        return "result"
    if any(kw in t for kw in ["conclusion", "discussion", "结论", "讨论", "总结"]):
        return "conclusion"
    if any(kw in t for kw in ["reference", "参考文献", "bibliography"]):
        return "references"
    return "unknown"


def chunk_markdown(text: str, paper_id: str, source_file: str) -> list[dict]:
    """
    将 Markdown 文本切分为 chunks。
    """
    lines = text.split("\n")
    sections = _detect_sections(text)

    # 提取页面标记
    page_markers = []
    for i, line in enumerate(lines):
        m = re.match(r"^<!-- PAGE: (\d+)(?:\s+OCR_DERIVED)?\s+-->", line)
        if m:
            page_markers.append((i, int(m.group(1))))

    chunks = []

    if not sections:
        # 无章节：按页面 + 长度切分
        chunks = _chunk_by_pages(lines, page_markers, paper_id, source_file)
    else:
        for sec in sections:
            sec_lines = lines[sec["start_line"]:sec["end_line"] + 1]
            sec_text = "\n".join(sec_lines).strip()
            if not sec_text:
                continue
            chunk_type = _classify_chunk_type(sec["title"])

            if chunk_type == "references":
                # references 单独成 chunk，不切分
                chunk_id = _make_chunk_id(paper_id, sec["title"])
                chunks.append({
                    "paper_id": paper_id,
                    "source_file": source_file,
                    "chunk_id": chunk_id,
                    "chunk_index": len(chunks),
                    "page_start": sec.get("page_start"),
                    "page_end": sec.get("page_end"),
                    "section_guess": sec["title"],
                    "chunk_type": chunk_type,
                    "text": sec_text,
                })
            elif len(sec_text) > MAX_CHUNK_CHARS:
                # 长章节按段落切分
                sub_chunks = _split_long_text(
                    sec_text, sec["title"], chunk_type,
                    paper_id, source_file,
                    sec.get("page_start"), sec.get("page_end"),
                    start_index=len(chunks),
                )
                chunks.extend(sub_chunks)
            else:
                chunk_id = _make_chunk_id(paper_id, sec["title"])
                chunks.append({
                    "paper_id": paper_id,
                    "source_file": source_file,
                    "chunk_id": chunk_id,
                    "chunk_index": len(chunks),
                    "page_start": sec.get("page_start"),
                    "page_end": sec.get("page_end"),
                    "section_guess": sec["title"],
                    "chunk_type": chunk_type,
                    "text": sec_text,
                })

    # 重新编号
    for i, c in enumerate(chunks):
        c["chunk_index"] = i

    return chunks


def _chunk_by_pages(lines, page_markers, paper_id, source_file) -> list[dict]:
    """按页码切分（fallback）"""
    chunks = []
    current_page = None
    current_lines = []

    for i, line in enumerate(lines):
        m = re.match(r"^<!-- PAGE: (\d+)(?:\s+OCR_DERIVED)?\s+-->", line)
        if m:
            if current_page is not None and current_lines:
                text = "\n".join(current_lines).strip()
                if text:
                    chunks.append(_make_page_chunk(current_page, text, paper_id, source_file, len(chunks)))
            current_page = int(m.group(1))
            current_lines = []
        else:
            current_lines.append(line)

    # 最后一页
    if current_page is not None and current_lines:
        text = "\n".join(current_lines).strip()
        if text:
            chunks.append(_make_page_chunk(current_page, text, paper_id, source_file, len(chunks)))

    return chunks


def _make_page_chunk(page: int, text: str, paper_id: str, source_file: str, idx: int) -> dict:
    return {
        "paper_id": paper_id,
        "source_file": source_file,
        "chunk_id": _make_chunk_id(paper_id, f"page_{page}"),
        "chunk_index": idx,
        "page_start": page,
        "page_end": page,
        "section_guess": "",
        "chunk_type": "mixed",
        "text": text,
    }


def _split_long_text(text: str, section_title: str, chunk_type: str,
                     paper_id: str, source_file: str,
                     page_start: int | None, page_end: int | None,
                     start_index: int = 0) -> list[dict]:
    """将长文本按段落边界切分为多个 chunk"""
    paragraphs = text.split("\n\n")
    chunks = []
    buf = []
    buf_len = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        para_len = len(para)
        if buf_len + para_len > MAX_CHUNK_CHARS and buf:
            chunk_text = "\n\n".join(buf)
            chunk_id = _make_chunk_id(paper_id, f"{section_title}_p{len(chunks)}")
            chunks.append({
                "paper_id": paper_id,
                "source_file": source_file,
                "chunk_id": chunk_id,
                "chunk_index": start_index + len(chunks),
                "page_start": page_start,
                "page_end": page_end,
                "section_guess": section_title,
                "chunk_type": chunk_type,
                "text": chunk_text,
            })
            buf = [para]
            buf_len = para_len
        else:
            buf.append(para)
            buf_len += para_len

    if buf:
        chunk_text = "\n\n".join(buf)
        chunk_id = _make_chunk_id(paper_id, f"{section_title}_p{len(chunks)}")
        chunks.append({
            "paper_id": paper_id,
            "source_file": source_file,
            "chunk_id": chunk_id,
            "chunk_index": start_index + len(chunks),
            "page_start": page_start,
            "page_end": page_end,
            "section_guess": section_title,
            "chunk_type": chunk_type,
            "text": chunk_text,
        })
    return chunks


def _make_chunk_id(paper_id: str, suffix: str) -> str:
    raw = f"{paper_id}_{suffix}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def process_markdown(md_path: Path) -> list[dict]:
    """处理单个 Markdown 文件，返回 chunks 列表"""
    paper_id = md_path.stem
    source_file = str(md_path.relative_to(PROJECT_ROOT))
    text = md_path.read_text(encoding="utf-8")

    chunks = chunk_markdown(text, paper_id, source_file)

    # 保存 chunk JSON
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CHUNKS_DIR / f"{paper_id}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    logger.info("Chunked %s: %d chunks -> %s", paper_id, len(chunks), out_path.name)
    return chunks


if __name__ == "__main__":
    md_files = sorted(MARKDOWN_DIR.glob("*.md"))
    logger.info("Found %d markdown files", len(md_files))
    for fp in md_files:
        process_markdown(fp)
