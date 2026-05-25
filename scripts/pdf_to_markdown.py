"""
PDF → Markdown 转换模块 v2。

使用 PyMuPDF/fitz 提取正文（优先，空格保留更好），pdfplumber 辅助表格提取。
保留页码标记、表格、图注。严格只做内容提取，不做科研理解。
"""

import hashlib
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF
import yaml
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "research_kb" / "markdown"
METADATA_DIR = PROJECT_ROOT / "research_kb" / "metadata"

logger = logging.getLogger("pdf2md")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)


def _sanitize(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9_\- ]", "", s)
    s = re.sub(r"\s+", "_", s)
    return s[:60]


def generate_paper_id(filepath: Path, pypdf_meta: dict | None = None) -> str:
    stem = filepath.stem
    m = re.match(r"^(\d{4})--(.+?)$", stem)
    if m:
        year = m.group(1)
        rest = m.group(2)
        parts = rest.split("--", 1)
        if len(parts) == 2:
            author = parts[0].strip().replace(" ", "_")
            title = _sanitize(parts[1])
            return f"{author}_{year}_{title}"[:120]
        else:
            return _sanitize(f"{parts[0]}_{year}")[:120]
    if pypdf_meta:
        author = pypdf_meta.get("author", "") or ""
        title = pypdf_meta.get("title", "") or ""
        if author and title:
            first = author.split(",")[0].split(";")[0].strip()
            return _sanitize(f"{first}_{title}")[:120]
    h = hashlib.sha256(stem.encode()).hexdigest()[:12]
    return f"unknown_{h}"


def compute_file_hash(filepath: Path) -> str:
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha.update(chunk)
    return sha.hexdigest()


def _font_size_of_line(line: dict) -> float:
    """从 fitz dict line 中提取最大字号"""
    sizes = [s.get("size", 10) for s in line.get("spans", [])]
    return max(sizes) if sizes else 10


def _is_bold_line(line: dict) -> bool:
    """检查是否粗体"""
    for s in line.get("spans", []):
        f = s.get("font", "").lower()
        if "bold" in f or "heavy" in f or "black" in f:
            return True
        flags = s.get("flags", 0)
        if flags & 2 ** 3:  # bold flag in fitz
            return True
    return False


def _guess_heading_level(line: dict, avg_size: float) -> int | None:
    """基于字号+粗体检测标题层级"""
    size = _font_size_of_line(line)
    bold = _is_bold_line(line)
    if size >= avg_size * 1.5:
        return 1
    if size >= avg_size * 1.25 and bold:
        return 2
    if size >= avg_size * 1.1 and bold:
        return 3
    return None


def _extract_page_with_fitz(page: fitz.Page, avg_font_size: float) -> tuple[str, bool]:
    """
    使用 PyMuPDF/fitz 提取单页文本（纯文本，不添加标题标记以保持按页分块）。
    保留图片占位符。

    Returns: (page_text, not_extractable)
    """
    text = page.get_text("text")
    text = text.strip()

    # 补充图片标记
    blocks = page.get_text("dict")["blocks"]
    img_count = sum(1 for b in blocks if b["type"] == 1)
    if img_count > 0:
        text += f"\n\n> [{img_count} Figure(s)]"

    not_extractable = len(text) < 50
    return text, not_extractable


def pdf_to_markdown(filepath: Path) -> tuple[str, str, dict, dict]:
    """将 PDF 转换为 Markdown（fitz 主提取 + 表格辅助）"""
    # --- pypdf 元数据 ---
    pypdf_reader = PdfReader(str(filepath))
    pypdf_meta = pypdf_reader.metadata
    meta_clean = {}
    if pypdf_meta:
        meta_clean = {
            "title": str(pypdf_meta.title) if pypdf_meta.title else None,
            "author": str(pypdf_meta.author) if pypdf_meta.author else None,
            "subject": str(pypdf_meta.subject) if pypdf_meta.subject else None,
            "creator": str(pypdf_meta.creator) if pypdf_meta.creator else None,
            "producer": str(pypdf_meta.producer) if pypdf_meta.producer else None,
        }
    pypdf_reader.close()

    paper_id = generate_paper_id(filepath, meta_clean)
    file_hash = compute_file_hash(filepath)

    # --- fitz 逐页提取 ---
    doc = fitz.open(str(filepath))
    page_count = doc.page_count

    # 计算全局平均字号
    all_sizes = []
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        all_sizes.append(span.get("size", 10))
    avg_font_size = sum(all_sizes) / len(all_sizes) if all_sizes else 10

    md_lines: list[str] = []
    not_extractable_pages: list[int] = []
    page_stats: list[dict] = []

    for page_idx in range(page_count):
        page = doc[page_idx]
        page_num = page_idx + 1

        page_text, not_extractable = _extract_page_with_fitz(page, avg_font_size)

        # 页码标记
        md_lines.append(f"<!-- PAGE: {page_num} -->")
        md_lines.append("")
        if not_extractable:
            md_lines.append("[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]")
            not_extractable_pages.append(page_num)
        else:
            md_lines.append(page_text)
        md_lines.append("")

        # 表格提取（用 fitz 的 find_tables）
        tables = page.find_tables()
        if tables and tables.tables:
            for tab in tables.tables:
                md = tab.to_markdown()
                if md and md.strip():
                    md_lines.append("")
                    md_lines.append(md)
                    md_lines.append("")

        page_stats.append({
            "page": page_num,
            "chars": len(page_text),
            "not_extractable": not_extractable,
        })

    doc.close()
    markdown_text = "\n".join(md_lines)

    # --- meta_dict ---
    meta_dict = {
        "paper_id": paper_id,
        "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        "file_hash": file_hash,
        "page_count": page_count,
        "not_extractable_pages": not_extractable_pages,
        "ocr_pages": [],
        "needs_ocr": len(not_extractable_pages) > page_count * 0.3,
        "extraction_timestamp": datetime.now().isoformat(),
    }

    # --- parse_report ---
    parse_report = {
        "paper_id": paper_id,
        "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        "file_hash": file_hash,
        "pdf_metadata": meta_clean,
        "page_count": page_count,
        "pages_extractable": page_count - len(not_extractable_pages),
        "pages_not_extractable": len(not_extractable_pages),
        "not_extractable_page_list": not_extractable_pages,
        "ocr_derived_pages": [],
        "needs_ocr": meta_dict["needs_ocr"],
        "extraction_method": "PyMuPDF/fitz + pypdf",
        "extraction_timestamp": meta_dict["extraction_timestamp"],
        "page_details": page_stats,
        "warnings": [],
    }
    if not_extractable_pages:
        parse_report["warnings"].append(
            f"{len(not_extractable_pages)} pages not extractable: {not_extractable_pages}"
        )

    return paper_id, markdown_text, meta_dict, parse_report


def process_pdf(filepath: Path) -> dict | None:
    """处理单个 PDF，输出 Markdown + parse_report + needs_ocr.yaml"""
    filepath = filepath.resolve()
    try:
        logger.info("Processing: %s", filepath.name)
        paper_id, markdown, meta_dict, parse_report = pdf_to_markdown(filepath)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        md_path = OUTPUT_DIR / f"{paper_id}.md"
        md_path.write_text(markdown, encoding="utf-8")

        METADATA_DIR.mkdir(parents=True, exist_ok=True)
        report_path = METADATA_DIR / "pdf_parse_report.json"
        _update_report_list(report_path, parse_report)

        ocr_path = METADATA_DIR / "needs_ocr.yaml"
        _update_ocr_list(ocr_path, meta_dict)

        logger.info(
            "  -> %s (pages=%d, extractable=%d, not_extractable=%d)",
            md_path.name,
            meta_dict["page_count"],
            meta_dict["page_count"] - len(meta_dict["not_extractable_pages"]),
            len(meta_dict["not_extractable_pages"]),
        )
        meta_dict["output_file"] = str(md_path.relative_to(PROJECT_ROOT))
        return meta_dict
    except Exception as e:
        logger.error("Failed to process %s: %s", filepath.name, e)
        return None


def _update_report_list(report_path: Path, new_report: dict):
    reports = {}
    if report_path.exists():
        try:
            reports = json.loads(report_path.read_text(encoding="utf-8"))
        except Exception:
            reports = {}
    if not isinstance(reports, dict):
        reports = {}
    reports[new_report["paper_id"]] = new_report
    report_path.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")


def _update_ocr_list(ocr_path: Path, meta_dict: dict):
    entries = {}
    if ocr_path.exists():
        try:
            data = yaml.safe_load(ocr_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                entries = data
        except Exception:
            pass
    pid = meta_dict["paper_id"]
    entries[pid] = {
        "paper_id": pid,
        "source_file": meta_dict["source_file"],
        "needs_ocr": meta_dict["needs_ocr"],
        "not_extractable_pages": meta_dict["not_extractable_pages"],
        "ocr_pages": meta_dict["ocr_pages"],
        "page_count": meta_dict["page_count"],
    }
    ocr_path.write_text(yaml.safe_dump(entries, allow_unicode=True, sort_keys=False), encoding="utf-8")


if __name__ == "__main__":
    paper_dir = PROJECT_ROOT / "paper"
    pdf_files = sorted(paper_dir.glob("*.pdf"))
    logger.info("Found %d PDF files", len(pdf_files))
    for fp in pdf_files:
        process_pdf(fp)
