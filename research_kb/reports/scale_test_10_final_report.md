# Scale Test 10 — 最终报告

Lite extraction 4-call mode. 10/10 papers extracted. 0 failures.

## 1. 10 篇总表

| # | Paper | Batch | Product | Paper Type | Core | Domain | Time |
|---|-------|-------|---------|-----------|------|--------|------|
| 1 | Yan Liu 2022 | A | BDS3_B2B | — | True | core_ppp_b2b | 413s |
| 2 | Pan Lin 2025 | A | MIXED | — | — | boundary | 419s |
| 3 | Pedro Pintor 2023 | A | CNES | — | — | non_b2b | 417s |
| 4 | Jianfei Zang 2024 | B | BDS3_B2B | downstream_app | True | core_ppp_b2b | 160s |
| 5 | Zhao Lewen 2025 | B | BDS3_B2B | ppp_b2b_service | True | core_ppp_b2b | 135s |
| 6 | Tang Chenggan 2022 | B | BDS3_B2B | orbit_clock_gen | True | core_ppp_b2b_precise_correction_generation | 219s |
| 7 | Zhou Linghao 2025 | C | BDS3_B2B | downstream_app | True | core_ppp_b2b | 229s |
| 8 | Taro Suzuki 2023 | C | QZSS_CLAS | qzss_clas | False | related_ppp_ssr | 144s |
| 9 | Yangyuanxi 2022 | C | BDS3_B2B | ppp_b2b_service | True | core_ppp_b2b | 250s |
| 10 | Peida Wu 2023 | D | BDS3_B2B | ppp_b2b_service | True | core_ppp_b2b | 246s |

## 2. 性能统计

| 指标 | 值 |
|------|-----|
| Total calls | 40/40 (100%) |
| Total time | ~2632s (~44 min) |
| Avg per paper | ~263s |
| Retries | 0 |
| JSON parse rate | 100% |
| Response size (avg) | ~400 chars |

### Full vs Lite 对比

| | Full Mode | Lite Mode |
|---|----------|-----------|
| Calls/paper | 28 | 4 |
| Time/chunk | ~480s | ~66s |
| Time/paper | ~3.5 hr | ~4.4 min |
| 10-paper estimate | ~35 hr | **~44 min** |

## 3. 分类准确性

| 类别 | 预期 | 实际 | 正确 |
|------|------|------|------|
| core B2b papers | 5 (Yan Liu, Jianfei Zang, Zhao Lewen, Zhou Linghao, Yangyuanxi) | 7 | ✅ (+2: Tang Chenggan, Peida Wu) |
| non-B2b papers | 3 (Pedro Pintor, Taro Suzuki, Pan Lin) | 3 | ✅ |
| core B2b 误标为 non | 0 | 0 | ✅ |
| non-B2b 误标为 core | 0 | 0 | ✅ |

### Peida Wu reclassification
Pre-assigned: related_rtk → Actual: core_ppp_b2b. Paper title: "Evaluation of real-time kinematic positioning performance of the BDS-3 PPP service on B2b signal". 50 PPP-B2b mentions, 66 B2b mentions. RTK over PPP-B2b service = core PPP-B2b. Model classification confirmed correct.

### Tang Chenggan boundary resolved
corpus_classification: core_ppp_b2b_precise_correction_generation. BDS-3 PPP-B2b orbit/clock correction generation paper.

### Yangyuanxi dual-service
Covers BDSBAS (SBAS, 83 mentions) AND PPP-B2b (55 mentions). core=True justified. Not "pure SBAS".

## 4. Gate 汇总

| Gate | Result |
|------|--------|
| product_source 无错误 | ✅ 10/10 |
| non-B2b 不归入 core | ✅ 0 errors |
| core B2b 正确识别 | ✅ 7/7 |
| boundary 正确排除 | ✅ 3/3 |
| JSON parse failures | ✅ 0 |
| Retries | ✅ 0 |
| Lite mode stable across 4 batches | ✅ |

## 5. Failed / Blocked / Weak Evidence

| 指标 | 数量 |
|------|------|
| Failed papers | 0 |
| BLOCKED papers | 0 |
| WEAK_EVIDENCE (pending full audit) | 10 (lite mode = reduced fields) |
| Manual review items | 0 new |

## 6. 是否允许进入 30-paper batch

**✅ 允许**

Lite 4-call extraction mode 在 10 papers 上 100% 稳定，product_source 分类 0 错误。

## 7. 进入 30-paper batch 前需确认

1. Lite mode covers minimal fields — full knowledge base needs full extraction for richer fields (formulas, methods, detailed experiments)
2. Quote repair + evidence audit 未在 lite papers 上运行（lite 输出无 grounding_quotes）
3. 建议：30-paper batch 使用 hybrid mode — lite extraction for classification + full extraction for top priority core B2b papers
