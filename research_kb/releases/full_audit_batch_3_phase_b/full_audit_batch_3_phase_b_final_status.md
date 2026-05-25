# Full Audit Batch 3 Phase B — Final Status

**Release:** `research_kb/releases/full_audit_batch_3_phase_b/`
**Date:** 2026-05-22

## Results

| # | Paper | Role | PS | B2b | DCB | Status |
|---|-------|------|-----|-----|-----|--------|
| 1 | applsci_15_08033_v2 | core | BDS3_B2B | 77 | NOT_MENTIONED | ✅ |
| 2 | remotesensing_14_02769 | core | BDS3_B2B | 199 | EXPLICIT | ✅ |
| 3 | remotesensing_15_00199 | core | BDS3_B2B | 55 | BRIEFLY | ✅ |
| 4 | remotesensing_16_00833_v2 | core | BDS3_B2B | 275 | EXPLICIT | ✅ |
| 5 | s10291_023_01455_z | core | BDS3_B2B | 183 | MENTIONED | ✅ |
| 6 | s10291_025_01845_5 | core (reclassified) | BDS3_B2B | 76 | NOT_MENTIONED | ✅ |
| 7 | s10291_025_01882_0 | core (reclassified) | BDS3_B2B | 105 | MENTIONED | ✅ |
| 8 | s10291_024_01730_7 | boundary | MIXED | 125 | MENTIONED | ✅ |
| 9 | s43020_024_00146_5 | boundary | MIXED | 52 | MENTIONED | ✅ |
| 10 | Liu_Wei (Chinese thesis) | general PPP | CNES | 0 | MENTIONED | ✅ |

## Gate Results

| Gate | Status |
|------|--------|
| 10/10 PASS | ✅ |
| WRONG_SUPPORT | 0 ✅ |
| product_source error | 0 ✅ |
| experiment_epoch contamination | 0 ✅ |
| DCB error | 0 ✅ |
| invalid_quote_id_rate | 0.0% ✅ |
| keyword_overlap ratio | 0.0% ✅ |
| v0.2 regression | 17/17 ✅ |
| BLOCKED | 0 ✅ |
| Circuit breaker triggers | 0 ✅ |

## Semantic Corrections (3 targeted)

| Paper | Change | Reason |
|-------|--------|--------|
| s10291_025_01845 | CNES → BDS3_B2B | 76 B2b, 0 HAS |
| s10291_025_01882 | CNES → BDS3_B2B | 105 B2b |
| Liu_Wei | BDS3_B2B → CNES | 0 B2b, general PPP thesis |

All corrections are role reclassifications based on keyword evidence. No field values were wrong — only pre-assigned roles.

## Phase C Readiness

| Check | Status |
|-------|--------|
| Phase A 10/10 | ✅ |
| Phase B 10/10 | ✅ |
| Cumulative 37 papers | 0 errors |
| Circuit breaker | Clean |

## Recommendation

**Phase B validated. 37-paper baseline established. Recommended: merge to corpus_grounded_v0.3 before considering Phase C.**
