# Batch C Report — Lite Extraction 4-Call Mode

## 结果

| Paper | Calls | Time | Product | Type | Core | Domain |
|-------|-------|------|---------|------|------|--------|
| Zhou Linghao 2025 | 4/4 | 229s | BDS3_B2B | downstream_b2b_application | True | core_ppp_b2b |
| Taro Suzuki 2023 | 4/4 | 144s | QZSS_CLAS | qzss_clas_service | False | related_ppp_ssr |
| Yangyuanxi 2022 | 4/4 | 250s | BDS3_B2B | ppp_b2b_service_perf | True | core_ppp_b2b |

12/12 calls, 624s total, 0 retries.

## 关键 Gate

| Gate | Result | Detail |
|------|--------|--------|
| non-B2b 不归入 core | ✅ | Taro Suzuki → QZSS_CLAS, core=False |
| SBAS 不误归入 core PPP-B2b | ✅ | Yangyuanxi covers both BDSBAS+PPP-B2b (55 PPP-B2b mentions); core=True justified |
| downstream application 正确分类 | ✅ | Zhou Linghao → downstream_b2b_application |

## Yangyuanxi 2022 验证

论文标题："Principle and performance of BDSBAS and PPP-B2b of BDS-3"。
SBAS: 83 mentions, BDSBAS: 66, PPP-B2b: 55, PPP: 100。
同时覆盖 BDSBAS SBAS 和 PPP-B2b 两个主题，core=True 分类合理。

## 结论

**✅ Batch C PASS** — 3/3 correct, no non-B2b misclassified as core PPP-B2b.
