# 07 — Limitations to Acknowledge in Thesis

These must be explicitly acknowledged in the thesis, not hidden.

## Corpus Limitations

1. **Not exhaustive.** 173 papers were ingested; 107 unique after dedup. The remaining paper/ PDFs (~18) are either CAJ format, out-of-scope, or were not processed. The 107 papers represent a systematic but not complete sample of the PPP-B2b literature.

2. **Language bias.** Only 1 Chinese-language paper (Liu Wei thesis, 72 pages, general BDS/GPS PPP). Chinese-language BDS literature is undersampled.

3. **CNES_OR_OTHER_RTS granularity.** This category mixes Galileo HAS (2 papers) with general PPP. Taxonomy refinement is deferred to a future version.

4. **Programmatic extraction for Batch 2.** 10 papers have 0 grounding quotes (keyword-based classification only). These are correctly classified but have weaker evidence chains than manually extracted papers.

## Evidence Limitations

5. **7 false-positive consistency warnings.** These are Batch 1 papers where b2b_mentions field is stored in a different JSON path. They are well-known PPP-B2b papers with high B2b content; the warning is a format artifact.

6. **Emerging singleton routes.** PPP-B2b-RTK, BDSet, and Smartphone B2b are supported by only 1 paper each. They are admitted as emerging routes but should not be presented as established findings.

## Pipeline Limitations

7. **107 unique papers have not been manually verified uniformly.** Deduplication used title normalization; some near-duplicates (preprint vs published) may remain.

8. **Regression tests cover v0.2 baseline only (17 papers).** Full v1.0 regression goldens have not been generated for all 107 papers.
