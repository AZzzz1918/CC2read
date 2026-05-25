# Limitations of Full Audit Batch 1

## Extraction Mode

This batch used **lite extraction mode** (4 API calls per paper). This is an evidence audit, NOT a full field extraction.

## Fields NOT Covered (or partially covered)

| Field | Coverage | Notes |
|-------|----------|-------|
| experiment_epoch | 2/6 STRONG, 4/6 NOT_MENTIONED | Lite mode does not search for date ranges comprehensively |
| correction_types | 6/6 present but granularity varies | Some list only "orbit, clock" while others list full types |
| DCB handling | 2/6 mentioned, 4/6 NOT_MENTIONED | Differential code bias handling largely missing |
| mathematical_model | 4/6 present, 2/6 NOT_MENTIONED | Model descriptions are high-level |
| datasets | 4/6 present, 2/6 NOT_MENTIONED | Dataset descriptions are generic |
| metrics | 5/6 present, 1/6 NOT_MENTIONED | Metric names listed but values mostly absent |
| main_results | 3/6 with results, 3/6 generic | Quantitative results not captured |
| novelty_audit | 6/6 present | Lite mode provides high-level novelty grades |
| reproducibility_blockers | 6/6 present | Count varies (2-8), lite mode may miss detailed blockers |
| grounding_quotes | 3/10 papers (Batch A only) | Only Batch A papers have quote banks |

## Next Step

All 6 papers require **full field extraction** (28 API calls per paper) to populate:
- experiment_epoch with exact date ranges
- correction_types with full granularity
- DCB handling (NOT_MENTIONED / INSUFFICIENT_EVIDENCE / proper description)
- mathematical_model with equations and methods
- datasets with specific station names and time ranges
- metrics with quantitative values
- main_results with numerical outcomes
- grounding_quotes for all critical fields
