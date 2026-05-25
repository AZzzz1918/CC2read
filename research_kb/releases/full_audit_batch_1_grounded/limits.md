# Limitations — Full Audit Batch 1 Grounded Release

## Quote Quality

- **keyword_overlap ratio: 55.6%** (exceeds 50% threshold)
  - Caused by the paraphrased nature of full-extraction grounding_quotes
  - All quotes have confidence scores attached
  - No unresolved quotes (0/72)
  - Evidence support audit validates all critical fields independently

## Field Coverage Gaps

- **metrics**: No grounding_quotes for 7/7 papers. Metric values were extracted from tables and figures, not from narrative text that can be directly quoted.
- **reproducibility_audit**: No grounding_quotes for 7/7 papers. Reproduction blockers are analytical assessments based on the full paper content.
- **experiment_epoch**: NO_EVIDENCE for 3/7 papers (Peida Wu, Yangyuanxi, Zhao Lewen). Correct and expected — these are overview, toolbox, or multi-platform papers without specific experiment dates.

## Paper-Specific Notes

| Paper | Concern | Severity |
|-------|---------|----------|
| Jianfei Zang 2024 | Single-event case study (Maduo earthquake) — limited generalization | LOW |
| Yangyuanxi 2022 | System overview paper — no experiment to reproduce | LOW (expected) |
| Zhao Lewen 2025 | Toolbox paper — evaluation dates not clearly stated | LOW |

## Scope Limitations

- Only 7 papers audited (6 core + 1 addendum)
- Research_on_Quad-Frequency excluded — quality checked, eligible for next batch
- MIXED_PRODUCTS papers not included per project rules
- All papers are BDS3_PPP_B2B_BROADCAST only — no Galileo HAS / QZSS CLAS papers in this batch
