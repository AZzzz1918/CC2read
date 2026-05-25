# Corpus Grounded v0.3 — Cross-Batch Consistency Check

**Date:** 2026-05-22
**Papers:** 37

## Product Source Taxonomy

| Value | Count |
|-------|-------|
| BDS3_PPP_B2B_BROADCAST | 25 |
| MIXED_PRODUCTS | 7 |
| CNES_OR_OTHER_RTS | 3 |
| QZSS_CLAS | 2 |

## Check Results

| Check | Status |
|-------|--------|
| Taxonomy consistency | ✅ 0 conflicts |
| Epoch publication year contamination | ✅ 0 |
| Paper ID duplicates | ✅ 0 |
| Cross-batch duplicate papers | ✅ 0 |
| Quote ID cross-paper conflicts | ⚠️ 17 (false positives — cross-paper hash collisions, per-paper scope) |
| Corpus maps contain BLOCKED papers | ✅ 0 |
| Phase B corrections preserved | ✅ 3/3 confirmed |

## Phase B Correction Verification

| Paper | Old PS | New PS | Preserved in v0.3 |
|-------|--------|--------|-------------------|
| s10291_025_01845 | CNES_OR_OTHER_RTS | BDS3_PPP_B2B_BROADCAST | ✅ |
| s10291_025_01882 | CNES_OR_OTHER_RTS | BDS3_PPP_B2B_BROADCAST | ✅ |
| Liu_Wei | BDS3_PPP_B2B_BROADCAST | CNES_OR_OTHER_RTS | ✅ |

## Conclusion

**✅ Cross-batch consistency PASS.** 0 semantic conflicts. 3 targeted corrections preserved. 37 papers clean.
