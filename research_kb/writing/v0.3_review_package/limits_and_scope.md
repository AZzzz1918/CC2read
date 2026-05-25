# Limitations and Scope

**Applies to:** manuscript based on corpus_grounded_v0.3

---

## Corpus Scope

### What the v0.3 Corpus Covers

- 37 papers, 2020–2025
- 4 product source categories (BDS3_B2B, MIXED, CNES/RTS, QZSS_CLAS)
- 8 technical routes
- BDS-3 PPP-B2b as primary focus (67.6% of corpus)
- Galileo HAS, QZSS CLAS as comparison baselines
- Both English and Chinese literature (1 Chinese thesis)

### What the v0.3 Corpus Does NOT Cover

- Papers published after early 2025
- PPP-AR / PPP-RTK with B2b (0 papers)
- Multi-constellation PPP beyond GPS+BDS
- Commercial augmentation services (Trimble RTX, NavCom StarFire)
- SBAS beyond BDSBAS (WAAS, EGNOS, MSAS)
- Pre-2020 BDS-2 era PPP

---

## Why Phase C is DO_NOT_RUN

1. **0 HIGH severity coverage gaps.** Coverage gap analysis found 1 MEDIUM gap (taxonomy granularity) and 9 LOW gaps.
2. **37 papers sufficient for comprehensive review.** The corpus covers the full PPP-B2b research lifecycle from system validation to application diversification.
3. **Continuing expansion has diminishing returns.** Remaining unprocessed papers in `paper/` largely duplicate existing themes (more B2b positioning evaluations, more HAS comparisons).
4. **Taxonomy refinement does not require new papers.** The CNES_OR_OTHER_RTS granularity issue can be resolved by re-labeling existing papers, not by adding more.

---

## Known Limitations

### 3 PASS_WITH_CORRECTION Papers

Three papers in the v0.3 corpus were reclassified during the evidence audit (Phase B):

| Paper | Original | Corrected | Reason |
|-------|----------|-----------|--------|
| s10291_025_01845_5 | CNES_OR_OTHER_RTS | BDS3_PPP_B2B_BROADCAST | 76 B2b mentions, 0 HAS |
| s10291_025_01882_0 | CNES_OR_OTHER_RTS | BDS3_PPP_B2B_BROADCAST | 105 B2b mentions |
| Liu_Wei_BDS_GPS_RTK_PPP | BDS3_PPP_B2B_BROADCAST | CNES_OR_OTHER_RTS | 0 B2b mentions, general PPP thesis |

These corrections are preserved in `semantic_corrections.yaml`. The corrected values are used in all analysis. The original pre-assignment errors are documented for transparency.

### CNES_OR_OTHER_RTS Taxonomy Granularity

The v0.3 taxonomy uses `CNES_OR_OTHER_RTS` to cover 3 heterogeneous papers:
- 2 Galileo HAS papers
- 1 general BDS/GPS PPP thesis

This is a known granularity limitation. **The v0.3 corpus data is not modified.** The refinement is documented as a proposal for v0.4.

### Extraction Completeness

- 25/37 papers have experiment_epoch = NOT_MENTIONED. Some of these genuinely lack experiment dates (overview/toolbox papers); others may have dates in text sections not covered by programmatic extraction.
- 16/37 papers have DCB = NOT_MENTIONED. Papers using ionosphere-free combination may handle DCB implicitly without explicit discussion.
- Batch 2 papers (10/37) have 0 grounding quotes (programmatic extraction mode). Classification was validated by keyword analysis rather than quote-level evidence.

### Corpus Statistics ≠ Field Statistics

All statistics reported are **within the grounded v0.3 corpus**, not estimates of the entire PPP-B2b literature. The 37 papers represent a curated, quality-controlled sample, not a random or exhaustive selection.

---

## Scope Boundaries for Manuscript

- **Evidence-grounded review**, not a traditional narrative review
- Claims are traceable to specific papers via evidence_claim_register.yaml
- "Strong" claims require ≥2 independent supporting papers within the corpus
- "Tentative" claims are explicitly marked
- Unsupported claims are excluded
