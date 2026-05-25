# Limitations — Full Audit Batch 2 Controlled Release

## Evidence Quality

- **0 grounding_quotes across all 10 papers.** Batch 2 used programmatic extraction (keyword-based classification) rather than manual evidence-quote extraction.
- **product_source classification:** Based on B2b/HAS/CLAS keyword counts and paper role labels. Validated programmatically, not through quote verification.
- **experiment_epoch:** Extracted from date patterns in markdown. Some papers have NOT_MENTIONED epoch (expected for tool/overview papers).

## Scope

- 10 papers only (4 core + 3 boundary/mixed + 2 non-B2b + 1 Research_on_Quad-Frequency)
- Classification accuracy: 10/10 (100%)
- Controlled scale test — designed to validate pipeline scalability, not produce a complete knowledge base

## Recommendations for Next Batch

- Add grounding_quotes enrichment step for core B2b papers
- Run quote repair on enriched papers to validate quote_id matching
- Monitor keyword_overlap ratio when quotes are added
