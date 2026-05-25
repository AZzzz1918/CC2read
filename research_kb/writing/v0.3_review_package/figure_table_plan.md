# Figure & Table Plan

**For manuscript: BDS-3 PPP-B2b and Satellite-Based Real-Time PPP — An Evidence-Grounded Review**

---

## Required Figures

### Fig 1: Evidence-Grounded Corpus Construction Workflow
**Type:** Flow diagram
**Content:** 7-phase pipeline from PDF Quality Check → Markdown → Extraction → Quote Bank → Repair → Audit → Freeze
**Data source:** SKILL.md Section 五

### Fig 2: Product Source Taxonomy Distribution
**Type:** Pie chart or horizontal bar chart
**Content:** BDS3_B2B (25), MIXED (7), CNES/RTS (3), QZSS_CLAS (2)
**Data source:** corpus_grounded_v0.3 product_source_taxonomy.yaml

### Fig 3: Paper Publication Year Distribution
**Type:** Histogram
**Content:** 2020:1, 2021:2, 2022:3, 2023:7, 2024:15, 2025:3, year=0:6
**Caveat:** 6 papers with year=0 are DOI-only papers where year was not extracted

### Fig 4: Technical Route Map
**Type:** Network/tree diagram
**Content:** 8 technical routes with paper counts and evidence quality (STRONG/PARTIAL/TENTATIVE)
**Data source:** technical_routes_synthesis.md

### Fig 5: Problem Evolution Timeline (2020–2025)
**Type:** Timeline with annotated phases
**Content:** Phase 1 (System Validation), Phase 2 (Comprehensive Evaluation), Phase 3 (Application Diversification)
**Data source:** problem_evolution_timeline.md

### Fig 6: Method Lineage Tree
**Type:** Hierarchical tree
**Content:** Ionosphere-Free PPP → Kalman Filter / SISRE → Time Transfer / ZTD / INS Integration → HAS / CLAS / CNES comparison
**Data source:** method_lineage_summary.md

### Fig 7: Reproducibility Blocker Matrix
**Type:** Grouped bar chart or heatmap
**Content:** 4 blocker categories × paper types. Data (37/37), Product Access (37/37), Parameters (30+), Software (34/37)
**Data source:** reproducibility_discussion.md

### Fig 8: Taxonomy Refinement Map (v0.3 → v0.4)
**Type:** Before/after comparison
**Content:** CNES_OR_OTHER_RTS (3 papers) → GALILEO_HAS (2) + NON_B2B_GENERAL_PPP (1)
**Caveat:** v0.4 is proposed, not implemented

---

## Required Tables

### Table 1: Corpus Summary Statistics
| Metric | Value |
|--------|-------|
| Total papers | 37 |
| Date range | 2020–2025 |
| Product categories | 4 |
| Technical routes | 8 |
| PASS / PASS_WITH_CORRECTION | 34 / 3 |
| WRONG_SUPPORT | 0 |
| Reproducibility score 0–1 | 27 (73%) |
| Open-source code | 3 (8%) |

### Table 2: Product Source Taxonomy
| Value | Count | % | Representative Papers |
|-------|-------|---|----------------------|
| BDS3_PPP_B2B_BROADCAST | 25 | 67.6 | Yan Liu 2022, Tang Chenggan 2022, Nie 2021 |
| MIXED_PRODUCTS | 7 | 18.9 | Pan Lin 2025, Wei Haopeng 2024 |
| CNES_OR_OTHER_RTS | 3 | 8.1 | Borio 2023, Zhou Peiyuan 2024 |
| QZSS_CLAS | 2 | 5.4 | Taro Suzuki 2023, Euiho Kim 2022 |

### Table 3: PPP-B2b Performance Summary
| Metric | Value | Source |
|--------|-------|--------|
| Orbit URE (BDS-3 MEO) | 0.05m | Tang Chenggan 2022 |
| Clock STD | 0.12–0.17ns | Yan Liu 2022, Tang Chenggan 2022 |
| Static 3D RMSE | 3.9–8.3cm | Yan Liu 2022 |
| Kinematic 3D RMSE | ~21cm mean | Yan Liu 2022 |
| Convergence (static BDS+GPS) | 7–12 min | Tang Chenggan 2022 |
| PWV RMS vs radiosonde | 3.7–4.7mm | Zhou Linghao 2025 |
| Availability (center) | ~89% | Yan Liu 2022 |
| Availability (boundary) | ~61% | Yan Liu 2022 |

### Table 4: Reproducibility Blocker Categories
| Category | Papers Affected | Severity |
|----------|----------------|----------|
| Data not publicly archived | 37/37 | CRITICAL |
| B2b correction stream inaccessible | 37/37 | CRITICAL |
| Processing parameters not disclosed | 30+ | HIGH |
| No source code release | 34/37 | HIGH |
| Specialized receiver required | 37/37 | MEDIUM |

### Table 5: Taxonomy Refinement Proposal (v0.3 → v0.4)
| v0.3 Label | v0.4 Label | Papers |
|-----------|-----------|--------|
| CNES_OR_OTHER_RTS | GALILEO_HAS | 2 |
| CNES_OR_OTHER_RTS | NON_B2B_GENERAL_PPP | 1 |

### Table 6: Evidence Quality by Technical Route
| Route | Papers | Quality |
|-------|--------|---------|
| Positioning Performance | 25 | STRONG |
| Time Transfer | 3 | PARTIAL |
| ZTD/PWV | 4 | STRONG (1) + PARTIAL (3) |
| INS/Factor Graph | 1 | TENTATIVE |
| Multi-system Comparison | 7 | STRONG |
| Toolbox/Decoder | 3 | STRONG |
| Orbit/Clock Generation | 1 | STRONG |
| Earthquake | 1 | PARTIAL |

---

## Notes

- All figures and tables should include footnote: "Within the grounded v0.3 corpus (37 papers)."
- PASS_WITH_CORRECTION papers should be marked in tables with a dagger symbol.
- Evidence quality ratings (STRONG/PARTIAL/TENTATIVE) should be visually distinguished.
