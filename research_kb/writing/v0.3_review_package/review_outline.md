# Review Outline: BDS-3 PPP-B2b and Satellite-Based Real-Time PPP Correction Services

**Grounded on:** corpus_grounded_v0.3 (37 papers, 2020–2025)
**Evidence standard:** quote_id-grounded, audit-verified

---

## 1. Introduction

- Satellite-based real-time PPP: BDS-3 PPP-B2b, Galileo HAS, QZSS CLAS/MADOCA
- Problem: internet dependency, correction quality, service coverage
- Scope: within the grounded v0.3 corpus (37 papers), covering 2020–2025
- Contribution: first evidence-grounded, regression-tested systematic review of PPP-B2b literature

## 2. Background

- 2.1 BDS-3 constellation and PPP-B2b signal (Yangyuanxi 2022, Tang Chenggan 2022)
- 2.2 PPP-B2b correction message types: orbit, clock, DCB, URAI (Tang Chenggan 2022, Yan Liu 2022)
- 2.3 Galileo HAS and QZSS CLAS as comparison baselines (Borio 2023, Taro Suzuki 2023)
- 2.4 IGS RTS and CNES products as ground truth (Comparative Broadcast, RT_ZTD)

## 3. Product Source Taxonomy

- 3.1 BDS3_PPP_B2B_BROADCAST (25/37 papers): pure B2b correction users
- 3.2 MIXED_PRODUCTS (7/37): B2b + HAS + MADOCA comparison studies
- 3.3 CNES_OR_OTHER_RTS (3/37): Galileo HAS + general PPP
- 3.4 QZSS_CLAS (2/37): Japanese QZSS augmentation
- 3.5 Taxonomy refinement: CNES_OR_OTHER_RTS granularity limitation (v0.3 known issue)

## 4. Technical Routes

- 4.1 PPP-B2b positioning performance (Yan Liu 2022, Nie 2021, Peida Wu 2023, 15+ papers)
- 4.2 PPP-B2b time transfer (Quad-Frequency, Single-Frequency, Comparative Broadcast)
- 4.3 PPP-B2b ZTD/PWV retrieval (Zhou Linghao 2025, Wang 2024, Oceanic PWV, RT_ZTD)
- 4.4 PPP-B2b combined with INS/factor graph (Factor Graph PPP-B2b/INS)
- 4.5 PPP-B2b vs HAS vs CLAS vs MADOCA comparison (Pan Lin 2025, Wei Haopeng 2024, 7 papers)
- 4.6 Toolbox and open-source decoder (GKit SSRDecoder, Zhao Lewen NavDecoder, Lu 2021 SDR)
- 4.7 Earthquake monitoring with PPP-B2b (Jianfei Zang 2024)
- 4.8 Orbit/clock correction generation (Tang Chenggan 2022)

## 5. Application Scenarios

- Geodesy and surveying (static PPP, cm-level)
- Real-time kinematic positioning (car, vessel, aircraft — Peida Wu 2023)
- Time transfer and UTC calculation (Quad-Freq, Single-Freq)
- Water vapor monitoring / meteorology (Zhou Linghao 2025, Oceanic PWV)
- Earthquake early warning (Jianfei Zang 2024)
- LEO satellite orbit determination (RT Kinematic Orbit LEO)

## 6. Reproducibility Assessment

- 6.1 Data availability: PPP-B2b correction streams rarely archived
- 6.2 Product access: BDS-3 GEO broadcast requires specialized receivers
- 6.3 Parameter disclosure: Kalman filter settings often omitted
- 6.4 Software/tooling: only 3 papers provide open-source code
- 6.5 Reproducibility score distribution: majority score 0–1/10

## 7. Open Problems

- PPP-AR / PPP-RTK with B2b: 0 papers in corpus
- Multi-constellation beyond GPS+BDS: limited coverage
- DCB handling: 16/37 papers NOT_MENTIONED
- experiment_epoch extraction: 25/37 NOT_MENTIONED (need deeper extraction)
- Chinese-language literature: 1 paper only (Liu Wei thesis)

## 8. Future Work

- Taxonomy refinement: split CNES_OR_OTHER_RTS → GALILEO_HAS + NON_B2B_GENERAL_PPP
- PPP-AR / PPP-RTK with B2b literature expansion
- Low-cost receiver + PPP-B2b operational deployment
- BDS-3 PPP-B2b long-term stability monitoring
