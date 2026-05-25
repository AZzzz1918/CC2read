# Scale Test 9/10 Interim Summary

Pending: Peida Wu 2023 (related_rtk)

## Batch A/B/C 汇总

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
| 10 | **Peida Wu 2023** | D | ⏳ | ⏳ | ⏳ | related_rtk | ⏳ |

## 性能

- Total API calls: 36/36 (100%)
- Total time: ~2386s (~40 min)
- Avg per paper: ~265s
- Retries: 0
- JSON parse rate: 100%

## 分类准确性

| 类别 | 数量 | 正确 |
|------|------|------|
| core B2b 正确识别 | 6/6 | ✅ |
| non-B2b 正确排除 | 3/3 | ✅ |
| boundary 正确标记 | 1/1 | ✅ |
| non-B2b 误归入 core | 0 | ✅ |

## Resolved Notes

- **Tang Chenggan**: boundary resolved → core_ppp_b2b_precise_correction_generation
- **Yangyuanxi**: dual-service note — covers BDSBAS (SBAS, 83 mentions) AND PPP-B2b (55 mentions); core=True justified, not misclassified as "pure SBAS"

## Gate Status

| Gate | Result |
|------|--------|
| product_source 无错误 | ✅ |
| non-B2b 不归入 core | ✅ |
| lite mode 稳定性 | ✅ |
| JSON parse rate | ✅ 100% |

## Peida Wu

**Status**: 未补跑。预设类别 related_rtk。

**是否允许补跑**: ✅ YES
