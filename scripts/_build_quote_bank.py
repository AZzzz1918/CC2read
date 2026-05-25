"""
为每篇论文基于 fitz markdown 生成 quote_bank。
每个条目有唯一 quote_id，可从 paper JSON 中引用。
"""
import hashlib
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MD_DIR = PROJECT_ROOT / "research_kb" / "markdown"
BANK_DIR = PROJECT_ROOT / "research_kb" / "quote_banks"

QUOTE_ID_PREFIX = "qb"


def _make_quote_id(paper_id: str, idx: int) -> str:
    raw = f"{paper_id}_{idx}"
    h = hashlib.md5(raw.encode()).hexdigest()[:10]
    return f"{QUOTE_ID_PREFIX}_{h}"


def _split_into_spans(text: str) -> list[str]:
    """将文本拆分为有意义的可引用片段"""
    spans = []
    # 按段落拆分
    paragraphs = text.split("\n\n")
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # 跳过页码标记和占位符
        if re.match(r"^<!-- PAGE:", para):
            continue
        if para.startswith("[PAGE_TEXT_NOT_EXTRACTABLE"):
            continue
        if para.startswith("> [Figure"):
            continue
        # 跳过 markdown 表格（以 | 开头的行）
        if para.startswith("|"):
            continue

        # 按句子拆分长段落
        sentences = re.split(r"(?<=[.!?])\s+", para)
        for sent in sentences:
            sent = sent.strip()
            if len(sent) >= 15:  # 最少 15 字符
                spans.append(sent)

    return spans


def build_quote_bank(paper_id: str, md_text: str) -> list[dict]:
    """为单篇论文构建 quote_bank"""
    spans = _split_into_spans(md_text)
    bank = []
    for idx, span in enumerate(spans):
        bank.append({
            "quote_id": _make_quote_id(paper_id, idx),
            "span_index": idx,
            "text": span,
            "char_length": len(span),
        })
    return bank


def build_all():
    BANK_DIR.mkdir(parents=True, exist_ok=True)
    md_files = sorted(MD_DIR.glob("*.md"))
    for mf in md_files:
        paper_id = mf.stem
        md_text = mf.read_text(encoding="utf-8")
        bank = build_quote_bank(paper_id, md_text)
        out_path = BANK_DIR / f"{paper_id}_bank.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(bank, f, ensure_ascii=False, indent=2)
        print(f"{paper_id[:50]}: {len(bank)} spans in quote_bank")


if __name__ == "__main__":
    build_all()
