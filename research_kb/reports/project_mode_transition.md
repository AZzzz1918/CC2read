# Project Mode Transition

**Date:** 2026-05-24
**From:** Analysis and Writing Stage
**To:** Continuously Extensible Research Knowledge Base

---

## New Project State

```
PROJECT_MODE = CONTINUOUS_KB_BUILDING
WRITING = OUT_OF_SCOPE (manuscript drafting indefinitely postponed)
V0_3_ROLE = VALIDATED_SEED_BASELINE (37 papers, 0 errors, immutable)
V0_4_ROLE = INCREMENTAL_EXPANSION_SERIES (Waves 1-3, 29 papers)
FREEZE_MEANING = IMMUTABLE_VERSION_SNAPSHOT_ONLY (does not stop ingestion)
NEXT_PRIORITY = CONTINUOUS_INGESTION_PIPELINE
```

## Release Re-labeling

| Release | Old Role | New Role |
|---------|----------|----------|
| corpus_grounded_v0.3 | "final complete corpus" | **validated_seed_baseline** |
| v0.4 Wave 1 | "decide if Phase C needed" | **incremental_expansion_validation_batch** |
| v0.4 Wave 2 | "coverage saturation probe" | **incremental_expansion_validation_batch** |
| v0.4 Wave 3 | "focused saturation probe" | **incremental_expansion_validation_batch** |

## Knowledge Base Architecture

```
research_kb/
├── inventory/          — paper tracking (registry, queue, duplicates, exclusions)
├── source/             — raw inputs (pdf/, markdown/, chunks/)
├── evidence/           — grounded evidence (quote_banks/, support_audits/)
├── papers/             — paper lifecycle (admitted/, processing/, quarantined/, superseded/)
├── entities/           — knowledge views (routes, innovations, methods, datasets, applications)
├── indexes/            — queryable indexes (paper_index, route_index, evidence_index)
├── tests/              — regression goldens
├── releases/           — immutable version snapshots
└── reports/            — human-readable status reports
```

## Entity Registries Created

| File | Content |
|------|---------|
| `entities/product_sources.yaml` | 5 taxonomy values + 8 component_stack values |
| `entities/technical_routes.yaml` | 14 routes with maturity levels |
| `entities/innovations.yaml` | 7 innovations with route_status |
| `entities/methods.yaml` | 10 methods |
| `entities/datasets.yaml` | 9 datasets (incl. BDSet) |
| `entities/applications.yaml` | 10 application domains |
| `entities/open_problems.yaml` | 8 open problems |

## Admission States

| State | Meaning | Count |
|-------|---------|-------|
| GROUNDED_ADMITTED | Passed full pipeline | 66 |
| SCREENED_CANDIDATE | Passed screening, queued | ~51 |
| INVENTORY_ONLY | Registered, not screened | ~10 |
| EXCLUDED_OUT_OF_SCOPE | Confirmed non-GNSS | ~4 |
| QUARANTINED_TEXT_QUALITY | PDF extraction failure | 0 |
| QUARANTINED_EVIDENCE_FAILURE | Failed audit | 0 |

## Pipeline (14 Steps)

1. inventory registration → 2. duplicate detection → 3. relevance screening → 4. PDF quality gate → 5. canonical markdown → 6. quote bank → 7. extraction → 8. quote repair → 9. evidence audit → 10. admission decision → 11. entity delta update → 12. index regeneration → 13. regression test → 14. release snapshot

## Next Execution

```
Priority 1: Import remaining ~51 screened candidates via incremental waves (5-10 papers each)
Priority 2: Generate entity deltas after each wave
Priority 3: Rebuild indexes and query views
Priority 4: Maintain regression test coverage
```
