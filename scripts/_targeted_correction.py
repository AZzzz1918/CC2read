"""
Targeted Semantic Correction — 只修改 Evidence Support Audit 已证明错误的字段。
"""
import json
import sys
from pathlib import Path
from datetime import datetime

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPAIRED_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_repaired"
REPAIRED_YAML_DIR = PROJECT_ROOT / "research_kb" / "papers" / "yaml_repaired"
CORRECTED_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_corrected"
CORRECTED_YAML_DIR = PROJECT_ROOT / "research_kb" / "papers" / "yaml_corrected"
CORPUS_OUTPUT_DIR = PROJECT_ROOT / "research_kb" / "corpus"
MANUAL_REVIEW_PATH = PROJECT_ROOT / "manual_review_queue.yaml"

CORRECTIONS_LOG = []
UNCHANGED_PAPERS = []


def apply_corrections():
    CORRECTED_DIR.mkdir(parents=True, exist_ok=True)
    CORRECTED_YAML_DIR.mkdir(parents=True, exist_ok=True)

    for jf in sorted(REPAIRED_DIR.glob("*.json")):
        paper_id = jf.stem
        data = json.loads(jf.read_text(encoding="utf-8"))
        corrections = []

        # ===== Ge Yulong: product_source.actual_product_source → MIXED_PRODUCTS =====
        if "Ge_yulong" in paper_id:
            ps = data.get("product_source", {})
            old_actual = ps.get("actual_product_source")
            new_actual = "MIXED_PRODUCTS"

            if old_actual != new_actual:
                ps["actual_product_source"] = new_actual
                ps["conflict_flag"] = True
                ps["conflict_detail"] = (
                    "Evidence audit: 4 quotes support MIXED_PRODUCTS (CNES, final products, "
                    "ultra-rapid) not pure BDS3_PPP_B2B_BROADCAST. "
                    f"Corrected from {old_actual} to {new_actual} via targeted semantic correction."
                )
                corrections.append({
                    "field": "product_source.actual_product_source",
                    "old_value": old_actual,
                    "new_value": new_actual,
                    "reason": "4 WRONG_SUPPORT in evidence audit: quotes mention CNES, final products, mixed sources — not pure B2b",
                    "evidence_audit_ref": "research_kb/reports/evidence_support_audit.md#Ge_yulong",
                })
                corrections.append({
                    "field": "product_source.conflict_flag",
                    "old_value": False,
                    "new_value": True,
                    "reason": "claimed (B2b service) vs actual (MIXED_PRODUCTS) now correctly flagged",
                })
                print(f"CORRECTED: {paper_id[:50]} -> {old_actual} => {new_actual}")
            else:
                UNCHANGED_PAPERS.append(paper_id)
                print(f"UNCHANGED: {paper_id[:50]} (already {old_actual})")
        else:
            UNCHANGED_PAPERS.append(paper_id)
            print(f"UNCHANGED: {paper_id[:50]} (no corrections needed)")

        # 保存 corrected JSON
        json_out = CORRECTED_DIR / f"{paper_id}.json"
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # 保存 corrected YAML
        yaml_out = CORRECTED_YAML_DIR / f"{paper_id}.yaml"
        with open(yaml_out, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

        if corrections:
            CORRECTIONS_LOG.append({"paper_id": paper_id, "corrections": corrections})

    # 生成 manual_review_queue.yaml
    _create_manual_review_queue()

    # 打印汇总
    print(f"\n=== Summary ===")
    print(f"Papers corrected: {len(CORRECTIONS_LOG)}")
    print(f"Papers unchanged: {len(UNCHANGED_PAPERS)}")
    for entry in CORRECTIONS_LOG:
        print(f"  {entry['paper_id']}: {len(entry['corrections'])} corrections")


def _create_manual_review_queue():
    """从 unresolved evidence + weak support 创建人工审核队列"""
    queue = {
        "created": datetime.now().isoformat(),
        "items": [],
    }

    for jf in sorted(REPAIRED_DIR.glob("*.json")):
        paper_id = jf.stem
        data = json.loads(jf.read_text(encoding="utf-8"))

        from collections import defaultdict
        GQ_FIELDS = [
            "product_source", "mathematical_model", "ionospheric_handling",
            "correction_types", "technical_route", "experiment_epoch",
            "datasets", "metrics", "main_results", "novelty_audit",
            "reproducibility_audit",
        ]

        for field in GQ_FIELDS:
            val = data.get(field, {})
            if not isinstance(val, dict):
                continue
            ids = val.get("grounding_quote_ids", [])
            for ref in ids:
                should_queue = False
                reason = ""

                if ref.get("match_type") == "unresolved" or ref.get("repair_status") == "needs_evidence_repick":
                    should_queue = True
                    reason = "unresolved_evidence"
                elif (ref.get("match_type") == "keyword_overlap_repair"
                      and ref.get("repair_confidence") == "low"):
                    should_queue = True
                    reason = "keyword_overlap_low_confidence"

                if should_queue:
                    queue["items"].append({
                        "paper_id": paper_id,
                        "field": field,
                        "quote_id": ref.get("quote_id"),
                        "quote_text": (ref.get("quote_text") or "")[:120],
                        "match_type": ref.get("match_type"),
                        "confidence": ref.get("repair_confidence"),
                        "reason": reason,
                        "suggestion": "manual_replace",
                    })

    with open(MANUAL_REVIEW_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(queue, f, allow_unicode=True, sort_keys=False)

    print(f"Manual review queue: {len(queue['items'])} items -> {MANUAL_REVIEW_PATH}")


if __name__ == "__main__":
    apply_corrections()
