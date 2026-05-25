# Full Audit Batch 2 — Evidence Support Audit

**Timestamp:** 2026-05-22
**Audited:** 10 papers

## Classification Results

| # | Paper ID | Role | Product Source | B2b | HAS | CLAS | DCB | Status |
|---|----------|------|----------------|-----|-----|------|-----|--------|
| 1 | Nie 2021 | core | BDS3_B2B | 100 | 0 | 0 | MENTIONED | ✅ |
| 2 | Lu 2021 | core | BDS3_B2B | 101 | 0 | 0 | MENTIONED | ✅ |
| 3 | Zhou 2023 | core | BDS3_B2B | 78 | 0 | 0 | EXPLICIT | ✅ |
| 4 | Wang 2024 | core | BDS3_B2B | 131 | 0 | 0 | NOT_MENTIONED | ✅ |
| 5 | Wei Haopeng 2024 | boundary | MIXED | 133 | 0 | 0 | NOT_MENTIONED | ✅ |
| 6 | Comparative Broadcast | boundary | MIXED | 42 | 11 | 1 | NOT_MENTIONED | ✅ |
| 7 | RT ZTD | boundary | MIXED | 71 | 0 | 0 | NOT_MENTIONED | ✅ |
| 8 | Borio 2023 | non_b2b | CNES | 0 | 13 | 5 | NOT_MENTIONED | ✅ |
| 9 | Taro Suzuki 2023 | non_b2b | QZSS_CLAS | 3 | 0 | 0 | NOT_MENTIONED | ✅ |
| 10 | Quad-Frequency | core | BDS3_B2B | 85 | 0 | 0 | BRIEFLY | ✅ |

## Gate Check

| Gate | Result |
|------|--------|
| WRONG_SUPPORT | ✅ 0 |
| product_source 误判 | ✅ 0 |
| experiment_epoch 误用 pub year | ✅ 0 |
| DCB 标记一致 | ✅ 10/10 |
| reproduction_blockers 非空 | ✅ 10/10 |
| BLOCKED rate | ✅ 0% |
| B2b suspicious (low B2b on core) | ✅ 0 |

## Circuit Breaker Status

| # | Rule | Threshold | Actual | Status |
|---|------|-----------|--------|--------|
| 1 | BLOCKED rate | < 20% | 0% | ✅ |
| 2 | product_source WRONG_SUPPORT | 0 | 0 | ✅ |
| 3 | epoch publication year contamination | 0 | 0 | ✅ |
| 4 | invalid_quote_id_rate | < 5% | 0% | ✅ |
| 5 | keyword_overlap ratio | < 60% | N/A | ✅ |
| 6 | DCB/iono systematic misjudgment | 0 | 0 | ✅ |

**Conclusion: ✅ Full Audit Batch 2 PASS — 10/10**
