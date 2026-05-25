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
| Yan Liu 2022 | markdown path mismatch — markdown exists in scale_test_10 release but not in main research_kb/markdown/ | 待修复后补入 |
| Research_on_Quad-Frequency_PPP-B2b_Time_Transfer | markdown path mismatch | 待修复后补入 |

## Gate Check

| Gate | Result |
|------|--------|
| product_source 无错误分类 | ✅ 6/6 BDS3_B2B |
| non-B2b 误入 core | ✅ 0 |
| WRONG_SUPPORT | ✅ 0 |
| experiment_epoch 误用 pub year | ✅ No conflicts |
| MIXED_PRODUCTS 未并入 core | ✅ Excluded |
| manual_review_items ≤ 15 | ✅ 0 |

## 限制（Lite Extraction Mode）

- 无完整 grounding_quotes 字段（Batch A papers 除外）
- experiment_epoch 在 4/6 papers 中为 NOT_MENTIONED
- STRONG+PARTIAL = 61%
- 所有 6 篇需要 full extraction 补充完整字段

## 结论

**✅ Full Audit Batch 1 PASS — 6/6**
