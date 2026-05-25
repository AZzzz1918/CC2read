# 03 — Evidence Claim Table (Thesis Backbone Claims)

Claims marked STRONG have >=2 independent supporting papers within the 107-paper corpus.
Claims marked PARTIAL have 1 paper or converging but not fully independent evidence.
Claims marked TENTATIVE need qualification in thesis text.

## STRONG Claims (suitable as thesis backbone)

| ID | Claim | Support | Use in thesis |
|----|-------|---------|---------------|
| C1 | BDS-3 PPP-B2b achieves cm-level static and dm-level kinematic positioning | 25+ papers | Section: PPP-B2b performance |
| C2 | PPP-B2b orbit URE ~0.05m (BDS-3 MEO), clock STD ~0.12-0.2ns | Yan Liu 2022, Tang Chenggan 2022, Nie 2021 | Section: correction quality |
| C3 | BDS/GPS dual-system PPP-B2b converges faster than single-system | Tang Chenggan 2022, Peida Wu 2023, multiple others | Section: convergence |
| C4 | PPP-B2b availability degrades from ~89% (center) to ~61% (boundary) | Yan Liu 2022, Wang 2024 | Section: coverage |
| C5 | PPP-B2b PWV accuracy meets operational meteorology requirements (3.7-4.7mm RMS) | Zhou Linghao 2025, Wang 2024, multiple PWV papers | Section: applications |
| C6 | PPP-B2b literature has critically low reproducibility (73% score 0-1, only 3% open-source) | All 107 papers | Section: reproducibility |
| C7 | PPP-B2b DCB corrections are broadcast but DCB handling is under-reported (29/107 NOT_MENTIONED) | 29 papers | Section: DCB |
| C8 | PPP-B2b SISRE is dominated by clock systematic bias, not orbit error | Yan Liu 2022 | Section: SISRE |

## PARTIAL Claims (use as supporting observation, not conclusion)

| ID | Claim | Support | Caveat |
|----|-------|---------|--------|
| C9 | PPP-B2b enables real-time earthquake source description | Jianfei Zang 2024 (1 paper) | Single-event case study |
| C10 | PPP-B2b time transfer achieves sub-nanosecond accuracy | 3 papers | Related author groups, limited independent validation |
| C11 | PPP-B2b-RTK is feasible using single-station SSR corrections | s10291-025-01854-4 (1 paper) | Emerging singleton, needs confirmation |

## TENTATIVE Claims (must qualify in thesis)

| ID | Claim | Support | Thesis handling |
|----|-------|---------|-----------------|
| C12 | BDSet is the first public BDS PPP-B2b dataset | 1 paper | Cite as "recently proposed", not "established" |
| C13 | Smartphone-grade PPP-B2b positioning is feasible | 1 paper | Cite with "preliminary evidence suggests" |
