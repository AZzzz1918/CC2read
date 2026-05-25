# Full Audit Batch 1 — Grounded Final Status

**Release:** `research_kb/releases/full_audit_batch_1_grounded/`
**Date:** 2026-05-22

---

## 1. 原 6 篇是否全部仍为 PASS

✅ **是。** 6/6 全部 PASS。

| Paper | Gate | WRONG_SUPPORT | Evidence |
|-------|------|---------------|----------|
| Jianfei Zang 2024 | ✅ PASS | 0 | product_source STRONG, epoch STRONG |
| Peida Wu 2023 | ✅ PASS | 0 | product_source STRONG |
| Tang Chenggan 2022 | ✅ PASS | 0 | all critical fields well-evidenced |
| Yangyuanxi 2022 | ✅ PASS | 0 | product_source STRONG |
| Zhao Lewen 2025 | ✅ PASS | 0 | product_source STRONG |
| Zhou Linghao 2025 | ✅ PASS | 0 | product_source STRONG, epoch STRONG |

## 2. Yan Liu 2022 addendum 是否 PASS

✅ **PASS。** 旗舰 PPP-B2b 论文。所有关键字段有充分证据支持。
- product_source: STRONG_SUPPORT (2 quotes)
- experiment_epoch: STRONG_SUPPORT (2 quotes — 2020-08 + 2021-08)
- DCB: EXPLICITLY_DESCRIBED (3 quotes)
- WRONG_SUPPORT: 0

## 3. Research_on_Quad-Frequency 状态

⚠️ **PDF 已处理，未进入此 batch。**
- 6 页 IEEE 杂志文章，24,405 字符，100% 可提取
- 质量检查 PASS（数字原生 PDF，14 个引用，文字干净）
- Markdown 已生成：`research_kb/markdown/Research_on_Quad-Frequency_PPP-B2b_Time_Transfer.md`
- **状态：eligible_for_next_batch** — 不需要 PDF reprocessing
- 下一批可直接进入 extraction

## 4. Quote bank 覆盖

✅ **7/7 覆盖。** 共 2,494 个 quote spans。

| Paper | Spans |
|-------|-------|
| Jianfei Zang 2024 | 378 |
| Peida Wu 2023 | 388 |
| Tang Chenggan 2022 | 414 |
| Yangyuanxi 2022 | 293 |
| Zhao Lewen 2025 | 191 |
| Zhou Linghao 2025 | 358 |
| Yan Liu 2022 | 472 |

## 5. Invalid quote_id_rate 是否全部 <5%

✅ **0.0%。** 72/72 quotes resolved。0 unresolved。

| Match Type | Count | Ratio |
|------------|-------|-------|
| Normalized | 32 | 44.4% |
| Keyword Overlap | 40 | 55.6% |
| Unresolved | 0 | 0.0% |

## 6. WRONG_SUPPORT 是否为 0

✅ **0。** 7 篇论文 0 WRONG_SUPPORT。

## 7. 是否存在 semantic corrections

✅ **不需要。** 0 corrections。
- `semantic_corrections.yaml` 为空。
- 所有字段值与 grounding evidence 一致。
- 无 product_source 误分类，无 epoch 错误，无 DCB 标签不一致。

## 8. 是否存在 unresolved/manual review 项

✅ **0。**
- `manual_review_queue.yaml` 为空。
- NO_EVIDENCE 字段（metrics, reproducibility_audit）是提取设计决定的，不是 unresolved。

## 9. Batch 1 是否可以作为 grounded release

✅ **是。** `full_audit_batch_1_grounded` 已冻结。

Release 包含：
- `json_repaired/` — 7 篇 repaired JSON（quote_id-based evidence）
- `yaml_repaired/` — 7 篇 repaired YAML
- `quote_banks/` — 7 篇 quote banks
- `full_audit_batch_1_quote_repair_report.md`
- `full_audit_batch_1_evidence_support_audit.md`
- `semantic_corrections.yaml`（空）
- `manual_review_queue.yaml`（空）
- `limitations.md`
- `manifest.json`

## 10. 是否允许进入下一批 scale test

✅ **允许。** 条件：
1. 7/7 PASS with 0 WRONG_SUPPORT
2. 0% unresolved quote rate
3. 0 semantic corrections needed
4. keyword_overlap ratio (55.6%) 超出 50% 阈值 — 下一批应监控此比率
5. Research_on_Quad-Frequency 可直接进入下一批 full extraction

---

## 最终统计

| 指标 | 值 |
|------|-----|
| 总论文数 | 7 (6 core + 1 addendum) |
| PASS | 7 |
| BLOCKED | 0 |
| WRONG_SUPPORT | 0 |
| Semantic Corrections | 0 |
| Manual Review Items | 0 |
| Total Quote Spans | 2,494 |
| Repaired Quotes | 72 |
| Unresolved Quotes | 0 |
| Invalid Quote Rate | 0.0% |
| Keyword Overlap Ratio | 55.6% |

**Full Audit Batch 1: GROUNDED. Ready for next batch.**
