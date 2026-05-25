# Full Audit Batch 1 Report

**Extraction mode:** Lite extraction evidence audit (NOT full field extraction).
**Audited:** 6 core PPP-B2b papers. Evidence audit via programmatic markdown search.

## 结果

| Paper | B2b Mentions | Product | Epoch | Support |
|-------|-------------|---------|-------|---------|
| Jianfei Zang 2024 | 201 | BDS3_B2B STRONG | N/A | 1S/0P/2W |
| Peida Wu 2023 | 60 | BDS3_B2B STRONG | N/A | 1S/0P/2W |
| Tang Chenggan 2022 | 76 | BDS3_B2B STRONG | N/A | 1S/1P/1W |
| Yangyuanxi 2022 | 58 | BDS3_B2B STRONG | STRONG (6 dates) | 2S/1P/0W |
| Zhao Lewen 2025 | 61 | BDS3_B2B STRONG | N/A | 1S/0P/2W |
| Zhou Linghao 2025 | 35 | BDS3_B2B STRONG | STRONG (2 dates) | 2S/1P/0W |

## Planned but NOT Audited

| Paper | Reason | Status |
|-------|--------|--------|
| Yan Liu 2022 | markdown path mismatch — markdown exists in scale_test_10 release but not in main research_kb/markdown/ | 待修复后补入 Batch 1 addendum 或 Batch 2 |
| Research_on_Quad-Frequency_PPP-B2b_Time_Transfer | markdown path mismatch — markdown 未在主目录注册 | 待修复后补入 |

## Gate Check

| Gate | Result |
|------|--------|
| product_source 无错误分类 | ✅ 6/6 BDS3_B2B |
| non-B2b 误入 core | ✅ 0 |
| WRONG_SUPPORT | ✅ 0 |
| experiment_epoch 误用 pub year | ✅ No conflicts |
| MIXED_PRODUCTS 未并入 core | ✅ Excluded |
| keyword_overlap < 30% in critical | ✅ N/A (programmatic, not keyword_overlap) |
| manual_review_items ≤ 15 | ✅ 0 |

## 限制

- **本 batch 是 lite extraction evidence audit，不是 full field extraction**
- Lite extraction 无完整 grounding_quotes 字段（Batch A papers 除外）
- experiment_epoch 在 4/6 papers 中为 NOT_MENTIONED（lite mode 字段覆盖有限）
- STRONG+PARTIAL = 61%（lite mode 环境下合理，完整 fields 需 full extraction）
- 所有 6 篇论文需要 full extraction 补充: experiment_epoch, correction_types, DCB handling, mathematical_model, datasets, metrics, main_results, novelty_audit, reproducibility_blockers, grounding_quotes

## Full Extraction (Completed)

6/6 papers received full field extraction. See `research_kb/extractions/*_full.json`.
Gate check: ✅ 6/6 PASS. Report: `research_kb/reports/full_extraction_gate_check.md`.

## Batch 1 Addendum: Yan Liu 2022

| Status | Detail |
|--------|--------|
| Paper | Yan Liu 2022 — Comprehensive Analyses of PPP-B2b Performance in China and Surrounding Areas |
| Reason | markdown path mismatch — now fixed (path_exclusion_recovered) |
| Extraction | ✅ Full extraction completed |
| Output | `research_kb/papers/json/Yan_Liu_2022_comprehensive_analyses_of_ppp-b2b_performance_in_c.json` |
| | `research_kb/papers/yaml/Yan_Liu_2022_comprehensive_analyses_of_ppp-b2b_performance_in_c.yaml` |
| Product | BDS3_PPP_B2B_BROADCAST (STRONG) |
| DCB | EXPLICITLY_DESCRIBED |
| Epoch | 2020-08-06~12 (orbit/clock) + 2021-08-09 (positioning) |
| Core | ✅ core_ppp_b2b |
| Gate | ✅ PASS |

## 结论

**✅ Full Audit Batch 1 PASS — 6/6 + 1 addendum**

6/6 core B2b papers + 1 addendum confirmed with strong product_source evidence. Full extraction completed for all 7 papers (6 + Yan Liu 2022).

## 排除的 papers

- **Research_on_Quad-Frequency_PPP-B2b_Time_Transfer** — PDF exists, pending `danielmiessler-pdf` processing
- **MIXED_PRODUCTS papers** — 按规则排除（Pan Lin 2025 等）
- **Pan Lin 2025** — Batch A 判定为 MIXED/boundary，排除
