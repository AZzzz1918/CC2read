# Batch B Report — Lite Extraction 4-Call Mode

## 性能

| 论文 | Calls | Time | Product | Paper Type | Core B2b |
|------|-------|------|---------|-----------|---------|
| Jianfei Zang 2024 | 4/4 | ~160s | BDS3_PPP_B2B_BROADCAST | downstream_b2b_application | True |
| Zhao Lewen 2025 | 4/4 | 135s | BDS3_PPP_B2B_BROADCAST | ppp_b2b_service_perf | True |
| Tang Chenggan 2022 | 4/4 | 219s | BDS3_PPP_B2B_BROADCAST | orbit_clock_product_gen | True |

Total: 12/12 calls, ~514s, 0 retries, 100% JSON parse.

## Batch A+B 汇总

| # | Paper | Batch | Product | Type | Core | Category |
|---|-------|-------|---------|------|------|----------|
| 1 | Yan Liu 2022 | A | BDS3_B2B | — | True | core_ppp_b2b |
| 2 | Pan Lin 2025 | A | MIXED | — | — | boundary_mixed |
| 3 | Pedro Pintor 2023 | A | CNES | — | — | non_b2b_galileo |
| 4 | Jianfei Zang 2024 | B | BDS3_B2B | downstream_app | True | core_ppp_b2b |
| 5 | Zhao Lewen 2025 | B | BDS3_B2B | ppp_b2b_service | True | core_ppp_b2b_tool |
| 6 | Tang Chenggan 2022 | B | BDS3_B2B | orbit_clock_gen | True | core_ppp_b2b_precise_correction_generation (resolved) |

## Gate 检查

| Gate | Result |
|------|--------|
| product_source 无错误分类 | ✅ 6/6 correct |
| non-B2b 不归入 core | ✅ Pedro Pintor → CNES |
| core B2b 正确识别 | ✅ Yan Liu, Jianfei Zang, Zhao Lewen → BDS3 |
| boundary 正确识别 | ✅ Pan Lin → MIXED |
| extraction failures | ✅ 0 (24/24 calls) |

## Tang Chenggan — Boundary Review Resolved

Tang Chenggan 的 `paper_type=orbit_clock_product_gen`, `is_ppp_b2b_core_paper=True`。经人工确认：

- 论文研究 BDS-3 PPP-B2b 精密轨道/钟差改正数生成
- 不是 generic downstream PPP-B2b application
- corpus 分类：`core_ppp_b2b_precise_correction_generation`
- 已纳入 maps，不再标记为 boundary case

## 结论

**✅ Batch B PASS — 允许进入 Batch C**

6/6 papers extracted, 0 failures, product_source 100% correct, no non-B2b mislabeling, 1 boundary resolved (Tang Chenggan).
