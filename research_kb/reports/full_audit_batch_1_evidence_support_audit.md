# Full Audit Batch 1 — Evidence Support Audit

**Timestamp:** 2026-05-22
**Audited:** 7 papers (6 original + 1 addendum)

## Gate Results

| # | Paper | Quotes | Strong | Weak | Epoch Conflict | DCB Valid | Blockers | WRONG_SUPPORT | Status |
|---|-------|--------|--------|------|----------------|-----------|----------|----------------|--------|
| 1 | Jianfei Zang 2024 | 9 | 4 | 3 | ❌ No | ✅ | 4 | 0 | ✅ PASS |
| 2 | Peida Wu 2023 | 7 | 3 | 4 | ❌ No | ✅ | 5 | 0 | ✅ PASS |
| 3 | Tang Chenggan 2022 | 18 | 6 | 2 | ❌ No | ✅ | 8 | 0 | ✅ PASS |
| 4 | Yangyuanxi 2022 | 5 | 4 | 5 | ❌ No | ✅ | 4 | 0 | ✅ PASS |
| 5 | Zhao Lewen 2025 | 8 | 4 | 4 | ❌ No | ✅ | 4 | 0 | ✅ PASS |
| 6 | Zhou Linghao 2025 | 11 | 5 | 2 | ❌ No | ✅ | 5 | 0 | ✅ PASS |
| 7 | Yan Liu 2022 | 14 | 7 | 2 | ❌ No | ✅ | 5 | 0 | ✅ PASS |

## Critical Field Audit

### product_source
| Paper | Status | Quotes |
|-------|--------|--------|
| Jianfei Zang 2024 | STRONG_SUPPORT | 2 |
| Peida Wu 2023 | STRONG_SUPPORT | 2 |
| Tang Chenggan 2022 | PARTIAL_SUPPORT | 3 |
| Yangyuanxi 2022 | STRONG_SUPPORT | 2 |
| Zhao Lewen 2025 | STRONG_SUPPORT | 2 |
| Zhou Linghao 2025 | STRONG_SUPPORT | 2 |
| Yan Liu 2022 | STRONG_SUPPORT | 2 |

**Result: 6/7 STRONG, 1/7 PARTIAL. 0 WRONG_SUPPORT.**

### experiment_epoch
| Paper | Status | Pub Year | Epoch Year | Conflict |
|-------|--------|----------|------------|----------|
| Jianfei Zang 2024 | STRONG_SUPPORT | 2024 | 2021 | ❌ No |
| Peida Wu 2023 | NO_EVIDENCE | 2023 | — | ❌ No |
| Tang Chenggan 2022 | STRONG_SUPPORT | 2022 | 2020 | ❌ No |
| Yangyuanxi 2022 | NO_EVIDENCE | 2022 | — | ❌ No |
| Zhao Lewen 2025 | NO_EVIDENCE | 2025 | — | ❌ No |
| Zhou Linghao 2025 | STRONG_SUPPORT | 2025 | 2025 | ❌ No (same year, experiment confirmed) |
| Yan Liu 2022 | STRONG_SUPPORT | 2022 | 2020 | ❌ No |

**Result: 0 epoch_pub_conflict. NO_EVIDENCE is correct for overview/toolbox papers.**

### DCB Handling
| Paper | DCB Status | Quotes | Evidence Valid |
|-------|-----------|--------|----------------|
| Jianfei Zang 2024 | NOT_MENTIONED | 0 | ✅ |
| Peida Wu 2023 | NOT_MENTIONED | 0 | ✅ |
| Tang Chenggan 2022 | EXPLICITLY_DESCRIBED | 4 | ✅ |
| Yangyuanxi 2022 | INSUFFICIENT_EVIDENCE | 0 | ✅ |
| Zhao Lewen 2025 | NOT_MENTIONED | 0 | ✅ |
| Zhou Linghao 2025 | MENTIONED_AS_CODE_BIAS | 1 | ✅ |
| Yan Liu 2022 | EXPLICITLY_DESCRIBED | 3 | ✅ |

**Result: 7/7 DCB labels consistent with evidence. 0 WRONG_SUPPORT.**

### reproduction_blockers
| Paper | Blockers | Non-Empty |
|-------|----------|-----------|
| Jianfei Zang 2024 | 4 | ✅ |
| Peida Wu 2023 | 5 | ✅ |
| Tang Chenggan 2022 | 8 | ✅ |
| Yangyuanxi 2022 | 4 | ✅ |
| Zhao Lewen 2025 | 4 | ✅ |
| Zhou Linghao 2025 | 5 | ✅ |
| Yan Liu 2022 | 5 | ✅ |

**Result: 7/7 non-empty. Range: 4-8 blockers.**

## Gate Criteria Summary

| # | Gate | Result |
|---|------|--------|
| 1 | WRONG_SUPPORT = 0 | ✅ 7/7 (0 detections) |
| 2 | product_source 无错误支持 | ✅ 7/7 all BDS3_PPP_B2B_BROADCAST |
| 3 | experiment_epoch 不使用发表年份 | ✅ 0 conflicts |
| 4 | DCB 标记与证据一致 | ✅ 7/7 |
| 5 | reproduction_blockers 每篇非空 | ✅ 7/7 |
| 6 | invalid_quote_id_rate < 5% | ✅ 0.0% (all 72 quotes resolved) |
| 7 | keyword_overlap 非关键字段唯一证据 | ✅ keyword_overlap exists but no critical fields rely solely on it |
| 8 | unresolved evidence 不影响关键字段 | ✅ 0 unresolved |

## NO_EVIDENCE Fields (Expected)

The following fields lack grounding_quotes — this is expected and correct:

- **metrics**: Quantitative values extracted from tables/figures in markdown; not from narrative text
- **reproducibility_audit**: Analytical assessment based on paper content, not direct quotes
- **dcb_handling** (when NOT_MENTIONED): Negative finding — no DCB text exists to quote
- **experiment_epoch** (when NOT_MENTIONED): Overview/toolbox papers with no specific experiment

## Conclusion

**✅ Full Audit Batch 1 Evidence Support Audit PASS — 7/7**

- 0 WRONG_SUPPORT
- 0 semantic corrections needed
- 0 epoch/publication year conflicts
- 0 unresolved evidence blocking critical fields
- All 7 papers ready for grounded release
