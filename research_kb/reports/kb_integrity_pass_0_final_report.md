# KB Integrity Pass 0 — Final Report

**Date:** 2026-05-24

## Summary

| Layer | Status | Blocking | Warnings |
|-------|--------|----------|----------|
| Inventory | ✅ PASS | 0 | 0 |
| Admitted Papers | ✅ PASS | 0 | 26 |
| Evidence | ✅ PASS | 0 | 0 |
| Entities | ✅ PASS | 0 | 8 |
| Indexes | ✅ PASS | 0 | 1 |
| **TOTAL** | **PASS** | **0** | **35** |

## Key Metrics

| Metric | Value |
|--------|-------|
| Admitted papers | 66 |
| Registry entries (batch-level) | 7 |
| Queued candidates | 51 |
| Excluded out-of-scope | 4 |
| Duplicate groups | 5 |
| Quote banks | 66 papers, 6,237 spans |
| WRONG_SUPPORT | 0 |
| Unresolved quotes | 0 |
| Epoch publication year issues | 0 |
| Product source errors | 0 |
| Singleton routes (correctly marked) | 5 |
| Confirmed/established routes | 12 |
| Entity files | 7 |
| Query views generated | 0 (not yet built) |

## Non-Blocking Warnings

| # | Type | Count | Detail |
|---|------|-------|--------|
| 1 | Missing titles | 16 | Batch 2 programmatic papers + DOI-only filenames |
| 2 | Missing grounding quotes | 10 | Batch 2 programmatic extraction mode |
| 3 | admission_status NOT_SET | 66 | Legacy papers not yet migrated to new admission states |
| 4 | Paper_id/bank filename mismatch | 9 | Naming convention differences between releases |
| 5 | Entity paper_id references | 8 | Short paper_ids not matching full paper_ids in admitted corpus |
| 6 | Empty query_views/ | 1 | Views not yet generated from entities |

## Singleton Route Verification

| Route | Paper Count | Status | Correct? |
|-------|-------------|--------|----------|
| PPP-B2b-RTK | 1 | emerging_singleton | ✅ |
| BDSet Public Dataset | 1 | emerging_singleton | ✅ |
| Smartphone PPP-B2b | 1 | emerging_singleton | ✅ |
| B2b+HAS+MADOCA Triple | 1 | emerging_singleton | ✅ |
| B2b Orbit/Clock Outlier | 1 | emerging_singleton | ✅ |

## Decision

```
KB_INTEGRITY_PASS_0 = PASS
BLOCKING_ERRORS = 0
NON_BLOCKING_WARNINGS = 35
NEXT_ACTION = START_INCREMENTAL_INGESTION_RELEASE_001
```

## Recommended Next Actions (Non-Urgent)

1. Migrate 66 admitted papers to new `admission_status: GROUNDED_ADMITTED` field
2. Backfill missing titles for 16 DOI-only papers
3. Normalize paper_id ↔ bank filename mapping for 9 mismatched papers
4. Generate query views from entity registries
5. Add paper-level entries to all_papers_registry.jsonl (currently batch-level)
