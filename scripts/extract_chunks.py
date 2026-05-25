"""
DeepSeek 逐 chunk 信息抽取模块。

读取 research_kb/chunks/ 中的分块文件，对每个 chunk 调用 DeepSeek API
进行严格信息抽取，保存原始抽取结果。
"""

import json
import logging
import sys
import time
from pathlib import Path

from call_deepseek import call_deepseek_json

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHUNKS_DIR = PROJECT_ROOT / "research_kb" / "chunks"
EXTRACT_DIR = PROJECT_ROOT / "research_kb" / "extractions"
PROMPT_PATH = PROJECT_ROOT / "prompts" / "deepseek_system_prompt.txt"
SCHEMA_PATH = PROJECT_ROOT / "schemas" / "paper_schema.json"

logger = logging.getLogger("extract")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)

SYSTEM_PROMPT: str = ""
SCHEMA: dict = {}


def load_prompt() -> str:
    global SYSTEM_PROMPT
    if not SYSTEM_PROMPT:
        SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8").strip()
    return SYSTEM_PROMPT


def load_schema() -> dict:
    global SCHEMA
    if not SCHEMA:
        SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return SCHEMA


def build_user_prompt(chunk: dict) -> str:
    """构造发给 DeepSeek 的用户提示词"""
    text = chunk.get("text", "")
    meta = {
        "paper_id": chunk.get("paper_id"),
        "chunk_id": chunk.get("chunk_id"),
        "chunk_type": chunk.get("chunk_type"),
        "section_guess": chunk.get("section_guess"),
        "page_start": chunk.get("page_start"),
        "page_end": chunk.get("page_end"),
    }
    return (
        f"--- CHUNK CONTEXT ---\n"
        f"{json.dumps(meta, ensure_ascii=False)}\n\n"
        f"--- PAPER MARKDOWN（由 PDF 经 danielmiessler-pdf skill 转换得到）---\n"
        f"{text}\n\n"
        f"你正在读取由 PDF 转换得到的 Markdown 论文文本。"
        f"请严格按照系统提示词的要求，从以上文本中抽取信息，"
        f"填充知识库 JSON。只输出 JSON，不要添加任何其他内容。"
    )


def extract_chunk(chunk: dict, schema: dict) -> dict | None:
    """对单个 chunk 执行 DeepSeek 抽取"""
    user_prompt = build_user_prompt(chunk)

    result = call_deepseek_json(
        system_prompt=load_prompt(),
        user_prompt=user_prompt,
        schema_hint=schema,
        max_retries=3,
        temperature=0.1,
        max_tokens=8192,
        chunk_context={
            "paper_id": chunk.get("paper_id"),
            "chunk_id": chunk.get("chunk_id"),
            "chunk_index": chunk.get("chunk_index"),
            "chunk_type": chunk.get("chunk_type"),
        },
    )
    return result


def extract_all(delay: float = 0.5) -> dict[str, list[dict]]:
    """
    遍历所有 chunk 文件，逐个调用 DeepSeek 抽取。

    Args:
        delay: API 调用间隔（秒），避免限流

    Returns:
        {paper_id: [extraction_results]}
    """
    load_prompt()
    schema = load_schema()
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

    chunk_files = sorted(CHUNKS_DIR.glob("*.json"))
    logger.info("Found %d chunk files to extract", len(chunk_files))

    all_results: dict[str, list[dict]] = {}

    for cf in chunk_files:
        paper_id = cf.stem
        chunks = json.loads(cf.read_text(encoding="utf-8"))
        logger.info("Extracting %s: %d chunks", paper_id, len(chunks))

        paper_results = []
        for chunk in chunks:
            result = extract_chunk(chunk, schema)
            if result is not None:
                result["_meta"] = {
                    "chunk_id": chunk["chunk_id"],
                    "chunk_index": chunk["chunk_index"],
                    "chunk_type": chunk["chunk_type"],
                }
                paper_results.append(result)
            else:
                # 记录失败
                paper_results.append({
                    "_meta": {
                        "chunk_id": chunk["chunk_id"],
                        "chunk_index": chunk["chunk_index"],
                        "chunk_type": chunk["chunk_type"],
                    },
                    "_error": "extraction_failed",
                })
            time.sleep(delay)

        all_results[paper_id] = paper_results

        # 保存中间结果
        out_path = EXTRACT_DIR / f"{paper_id}_raw.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(paper_results, f, ensure_ascii=False, indent=2)
        logger.info("  Saved %d extractions to %s", len(paper_results), out_path.name)

    return all_results


if __name__ == "__main__":
    extract_all()
