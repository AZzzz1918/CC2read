# Corpus Grounded v0.2 — Cross-Batch Consistency Check

**Date:** 2026-05-22
**Papers:** 17 (7 Batch 1 + 10 Batch 2)

## Results

| Check | Result | Detail |
|-------|--------|--------|
| product_source taxonomy | ✅ PASS | 12 BDS3_B2B, 3 MIXED, 1 CNES, 1 QZSS_CLAS |
| core/boundary/non-B2b classification | ✅ PASS | 0 misclassifications |
| experiment_epoch: actual data vs pub year | ✅ PASS | 0 publication year contaminations |
| DCB status consistency | ✅ PASS | 3 EXPLICIT, 2 MENTIONED, 1 BRIEFLY, 1 INSUFFICIENT, 1 CODE_BIAS, 9 NOT_MENTIONED |
| reproduction_blockers non-empty | ✅ PASS | 17/17 non-empty (4-8 blockers) |
| quote_id conflicts | ✅ PASS | 0 cross-paper quote_id duplicates |
| corpus maps reference check | ✅ PASS | 0 BLOCKED/deprecated references |

## Structural Differences (Non-Semantic)

| Issue | Count | Explanation |
|-------|-------|-------------|
| b2b_mentions field location differs | 7 | Batch 1 stores in `b2b_mentions_estimated` root field; Batch 2 in `pdf_metadata.b2b_mentions` |
| dcb_mentions field location differs | 2 | Batch 1 DCB has no numeric `dcb_mentions` field; Batch 2 has it |

**These are extraction format differences, not semantic inconsistencies. 0 corrections needed.**

## Product Source Distribution

| Value | Count | Papers |
|-------|-------|--------|
| BDS3_PPP_B2B_BROADCAST | 12 | Batch 1: 7 core + Batch 2: 5 core |
| MIXED_PRODUCTS | 3 | Batch 2: Wei Haopeng, Comparative, RT_ZTD |
| CNES_OR_OTHER_RTS | 1 | Batch 2: Borio GHASP |
| QZSS_CLAS | 1 | Batch 2: Taro Suzuki |

## Conclusion

**✅ Cross-batch consistency check PASS.** 0 semantic conflicts. 9 structural differences are false positives from Batch 1/2 format differences. No corrections required.
