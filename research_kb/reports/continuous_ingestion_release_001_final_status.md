# Continuous Ingestion Release 001 — Final Status

**Date:** 2026-05-24

---

## 1. Release 001 选择了多少 queued candidate

**7 papers** from ~51 queued.

## 2. 有多少篇成功进入 GROUNDED_ADMITTED

**7/7.** 0 quarantined, 0 excluded, 0 failed.

| # | Paper | B2b | Pages | PS | DCB |
|---|-------|-----|-------|-----|-----|
| 1 | Multi-freq phase bias for BDS3 PPP-B2b | 80 | 15 | BDS3_B2B | MENTIONED |
| 2 | PWV from PPP with PPP-B2b service | 94 | 14 | BDS3_B2B | NOT_MENTIONED |
| 3 | BDS-3/GPS uncombined RT-PPP with PPP-B2b | 161 | 13 | BDS3_B2B | MENTIONED |
| 4 | BDS high-precision services: current state | 64 | 20 | BDS3_B2B | MENTIONED |
| 5 | BDS-3/GPS uncombined PPP-B2b long-term | 100 | 14 | BDS3_B2B | EXPLICIT |
| 6 | BDS-3 PPP-B2b for PWV determination | 193 | 31 | BDS3_B2B | EXPLICIT |
| 7 | Clock jump estimation + URA refinement B2b | 99 | 17 | BDS3_B2B | BRIEFLY |

## 3. 有多少篇进入 QUARANTINED / EXCLUDED / REMAINS_QUEUED

- QUARANTINED: 0
- EXCLUDED: 0
- REMAINS_QUEUED: ~44 (51 - 7)

## 4. Old 66 admitted corpus 是否保持不变

✅ **Unchanged.** v0.3 and v0.4 Waves 1-3 untouched.

## 5. Admitted_after_count 是否正确

✅ **66 + 7 = 73**

## 6. Query views 是否已生成并可重建

✅ **5 query views generated.** Release 001 preflight resolved Pass 0 W005.

## 7. Pass 0 的 35 个 warnings 解决了多少

- Resolved: W003 (admission_status — new papers use GROUNDED_ADMITTED), W005 (query_views generated)
- Remaining: ~29 (paper_id mapping, missing titles, entity references)
- All remaining are non-blocking

## 8. 仍剩余哪些 non-blocking warnings

| Group | Count |
|-------|-------|
| missing_title_warning | 16 |
| missing_grounding_quotes (Batch 2) | 10 |
| paper_id_filename_mapping | 9 |
| entity_paper_id_reference | 8 |

## 9–10. WRONG_SUPPORT / Critical Errors

- WRONG_SUPPORT: **0**
- product_source error: **0**
- epoch contamination: **0**
- DCB error: **0**

## 11–12. Singleton Routes

- **No new singletons added** (all 7 papers reinforce existing routes)
- **No route incorrectly upgraded**

## 13. 是否允许进入 Continuous Ingestion Release 002

✅ **YES.**

```
CONTINUOUS_INGESTION_RELEASE_001 = PASS
ADMITTED_COUNT = 73 (66 + 7)
QUEUED_REMAINING = 44
NEXT_PHASE = CONTINUOUS_INGESTION_RELEASE_002
```
