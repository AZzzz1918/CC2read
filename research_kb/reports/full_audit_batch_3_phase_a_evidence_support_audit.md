# Full Audit Batch 3 Phase A — Evidence Support Audit

## Results
| # | Paper | PS | B2b | Epoch | DCB | Quotes | Status |
|---|-------|----|-----|-------|-----|--------|--------|
| 1 | Euiho_Kim_2022_CLAS_PPP | QZSS_CLAS | 0 | NOT_MENTIONE | NOT_MENTIONED | 3 | ✅ |
| 2 | Factor_Graph_PPP_B2b_INS | BDS3_PPP_B2B_BROADCAST | 55 | NOT_MENTIONE | BRIEFLY_MENTIONED | 7 | ✅ |
| 3 | GKit_SSRDecoder_PPP_B2b_HAS | BDS3_PPP_B2B_BROADCAST | 104 | DOY 90 | EXPLICITLY_DESCRIBED | 8 | ✅ |
| 4 | Oceanic_PWV_PPP_B2b_LowCost | BDS3_PPP_B2B_BROADCAST | 66 | NOT_MENTIONE | NOT_MENTIONED | 6 | ✅ |
| 5 | Pan_Lin_2025_BDS_B2b_HAS | MIXED_PRODUCTS | 157 | DOY 186 | NOT_MENTIONED | 5 | ✅ |
| 6 | RT_Kinematic_Orbit_LEO_B2b_HAS | MIXED_PRODUCTS | 172 | DOY111 | NOT_MENTIONED | 6 | ✅ |
| 7 | Single_Frequency_PPP_B2b_Time_ | BDS3_PPP_B2B_BROADCAST | 82 | 2022-3-3 | BRIEFLY_MENTIONED | 7 | ✅ |
| 8 | Zhou_Peiyuan_2024_Galileo_HAS_ | CNES_OR_OTHER_RTS | 4 | DOY
70 | BRIEFLY_MENTIONED | 6 | ✅ |
| 9 | s10291_023_01570_x | BDS3_PPP_B2B_BROADCAST | 223 | NOT_MENTIONE | MENTIONED | 7 | ✅ |
| 10 | s43020_023_00097_3 | BDS3_PPP_B2B_BROADCAST | 70 | 2022-3-6 | NOT_MENTIONED | 6 | ✅ |

## Gate Check
| Gate | Result |
|------|--------|
| WRONG_SUPPORT = 0 | ✅ 0 |
| product_source correct | ✅ 0 errors |
| epoch no pub year contamination | ✅ 0 conflicts |
| invalid_quote_id_rate < 5% | ✅ 0.0% |
| DCB status consistent | ✅ 10/10 |
| blockers non-empty | ✅ 10/10 |
| BLOCKED rate < 20%% | ✅ 0%% |

**Overall: ✅ PASS**