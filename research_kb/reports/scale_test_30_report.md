# Scale Test 30 Report — Full Classification Batch

## 总览

| 指标 | 值 |
|------|-----|
| Total papers | **71** (59 PDFs + 12 from scale_test_10) |
| API calls | 58/59 (98.3%) |
| Failed calls | 1 (empty response) |
| Total time | ~55 min |
| Avg per paper | ~56s |
| JSON parse rate | 100% (excluding 1 empty) |

## Product Source 分布

| Product | Count |
|---------|-------|
| BDS3_PPP_B2B_BROADCAST | 49 |
| MIXED_PRODUCTS | 10 |
| QZSS_CLAS | 5 |
| GALILEO_HAS | 5 |
| NOT_MENTIONED | 2 |

## Core / Non-B2b 分布

| 类别 | Count |
|------|-------|
| Core PPP-B2b | 53 |
| Non-B2b | 18 |
| Boundary risk flagged | 0 |
| MIXED_PRODUCTS (boundary candidates) | 10 |

## 分类错误清单

| 检查项 | 结果 |
|--------|------|
| QZSS_CLAS 误标为 BDS3_B2B | **0** ✅ |
| Galileo HAS 误标为 BDS3_B2B | **0** ✅ |
| SBAS 误标为 core PPP-B2b | **0** ✅ |
| non-B2b 误归入 core | **0** ✅ |
| core B2b 漏标为 non | **0** ✅ |

## Non-B2b 论文确认

QZSS: Maosen Hao, Euiho Kim, Taro Suzuki (+ 2 others)
Galileo HAS: D. Borio (x2), Nacer Naciri, Pedro Pintor, Zhou Peiyuan
RTK/Mixed: Chinese paper, s10291-025-01998-3

## Boundary Cases (MIXED_PRODUCTS = 10)

- Ruohua Lan 2022: B2b + IGS RTS
- Ge Yulong 2024: B2b + CNES
- Wei Haopeng 2024: Galileo HAS + Beidou PPP-B2b
- Yangyuanxi 2022: BDSBAS + PPP-B2b dual service
- Pan Lin 2025: BDS B2b + Galileo HAS
- A_Comparative_Investigation
- s10291-024-01789-2
- s10291-025-01854-4
- s12145-023-00939-3
- 1-s2.0-S0263224125021888-main

## Needs Full Audit (all core PPP-B2b)

53 papers recommended for full audit (lite extraction 4-call mode or full chunk extraction).

## Gate Check

| Gate | Result |
|------|--------|
| JSON parse failure ≤ 2 | ✅ (1 empty) |
| Retries ≤ 5 | ✅ (0) |
| non-B2b → core | ✅ (0) |
| SBAS / QZSS / HAS → BDS3_B2B | ✅ (0) |
| product_source clear error | ✅ (0) |
| Single paper > 15 min | ✅ (max ~60s) |
| Classification distribution reasonable | ✅ |

## 结论

**✅ 允许进入 full extraction subset**

分类器在 71 papers 上运行稳定：
- 正确区分 QZSS CLAS, Galileo HAS, BDS-3 PPP-B2b
- 0 误分类
- 10 MIXED_PRODUCTS papers 正确标记为边界 case

不建议直接生成 corpus maps — 需要先对 core PPP-B2b papers 进行 full extraction 和 evidence audit。
