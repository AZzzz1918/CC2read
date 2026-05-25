"""
单篇论文 chunk 合并模块。

将同一篇论文的所有 chunk 抽取结果合并为最终的 paper JSON / YAML。
合并规则：优先使用非空、非 NOT_MENTIONED 的值；冲突时标记 CONFLICTING_EVIDENCE。
"""

import copy
import json
import logging
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXTRACT_DIR = PROJECT_ROOT / "research_kb" / "extractions"
JSON_OUT = PROJECT_ROOT / "research_kb" / "papers" / "json"
YAML_OUT = PROJECT_ROOT / "research_kb" / "papers" / "yaml"

logger = logging.getLogger("merge")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)

NOT_MENTIONED_VALUES = {"NOT_MENTIONED", "INSUFFICIENT_EVIDENCE", ""}


def _is_meaningful(value) -> bool:
    """判断值是否有实质信息"""
    if value is None:
        return False
    if isinstance(value, str) and value.strip() in NOT_MENTIONED_VALUES:
        return False
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False
    return True


def _deep_merge(base: dict, incoming: dict, path: str = "") -> dict:
    """
    深度合并两个抽取结果。
    - 优先保留有意义的值
    - 冲突时标记到 conflicting_evidence
    """
    merged = copy.deepcopy(base)
    conflicts = merged.setdefault("conflicting_evidence", [])

    for key, new_val in incoming.items():
        if key.startswith("_"):
            continue
        old_val = merged.get(key)

        if isinstance(new_val, dict) and isinstance(old_val, dict):
            merged[key] = _deep_merge(old_val, new_val, f"{path}/{key}")
        elif isinstance(new_val, list) and isinstance(old_val, list):
            # 列表合并：去重拼接
            existing_set = {json.dumps(v, ensure_ascii=False, sort_keys=True) if isinstance(v, dict) else str(v)
                            for v in old_val}
            for item in new_val:
                item_key = json.dumps(item, ensure_ascii=False, sort_keys=True) if isinstance(item, dict) else str(item)
                if item_key not in existing_set:
                    old_val.append(item)
                    existing_set.add(item_key)
            merged[key] = old_val
        elif not _is_meaningful(old_val) and _is_meaningful(new_val):
            merged[key] = new_val
        elif _is_meaningful(old_val) and not _is_meaningful(new_val):
            pass  # 保留旧值
        elif _is_meaningful(old_val) and _is_meaningful(new_val):
            old_str = json.dumps(old_val, ensure_ascii=False, sort_keys=True)
            new_str = json.dumps(new_val, ensure_ascii=False, sort_keys=True)
            if old_str != new_str:
                conflicts.append({
                    "field": f"{path}/{key}".lstrip("/"),
                    "claim_1": str(old_val)[:200],
                    "claim_2": str(new_val)[:200],
                    "resolution": "CONFLICTING_EVIDENCE",
                })

    return merged


def merge_paper(paper_id: str, extractions: list[dict]) -> dict:
    """合并单篇论文的所有 chunk 抽取结果"""
    if not extractions:
        return {
            "paper_id": paper_id,
            "_error": "no_extractions",
        }

    # 从第一个有意义的 extraction 开始
    merged = {"paper_id": paper_id, "conflicting_evidence": []}

    for ext in extractions:
        if "_error" in ext:
            continue
        merged = _deep_merge(merged, ext)

    # 清理空的 conflicting_evidence
    if not merged.get("conflicting_evidence"):
        del merged["conflicting_evidence"]

    return merged


def merge_all():
    """处理所有论文的合并"""
    JSON_OUT.mkdir(parents=True, exist_ok=True)
    YAML_OUT.mkdir(parents=True, exist_ok=True)

    extract_files = sorted(EXTRACT_DIR.glob("*_raw.json"))
    logger.info("Found %d extraction files", len(extract_files))

    for ef in extract_files:
        paper_id = ef.stem.replace("_raw", "")
        try:
            extractions = json.loads(ef.read_text(encoding="utf-8"))
            paper_json = merge_paper(paper_id, extractions)

            # 保存 JSON
            json_path = JSON_OUT / f"{paper_id}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(paper_json, f, ensure_ascii=False, indent=2)

            # 保存 YAML
            yaml_path = YAML_OUT / f"{paper_id}.yaml"
            with open(yaml_path, "w", encoding="utf-8") as f:
                yaml.safe_dump(paper_json, f, allow_unicode=True, sort_keys=False)

            logger.info("Merged %s: %d chunks -> %s", paper_id, len(extractions), json_path.name)
        except Exception as e:
            logger.error("Merge failed for %s: %s", paper_id, e)


if __name__ == "__main__":
    merge_all()
