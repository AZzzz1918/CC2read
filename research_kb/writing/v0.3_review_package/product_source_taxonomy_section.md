# Product Source Taxonomy

**Within the grounded v0.3 corpus (37 papers).**

---

## Taxonomy Table

| Value | Count | % | Definition |
|-------|-------|---|------------|
| BDS3_PPP_B2B_BROADCAST | 25 | 67.6 | Papers that use or evaluate BDS-3 PPP-B2b broadcast corrections as primary data source |
| MIXED_PRODUCTS | 7 | 18.9 | Papers that combine or compare PPP-B2b with HAS / MADOCA / CNES / IGS RTS |
| CNES_OR_OTHER_RTS | 3 | 8.1 | Papers about Galileo HAS or general PPP not specific to BDS-3 B2b |
| QZSS_CLAS | 2 | 5.4 | Papers about QZSS CLAS augmentation |

## BDS3_PPP_B2B_BROADCAST (25 papers)

The dominant category. Papers evaluate:
- Orbit/clock correction accuracy (Tang Chenggan 2022: URE 0.05m BDS-3 MEO)
- Static/kinematic positioning performance (Yan Liu 2022: cm-level static, dm-level kinematic)
- Time transfer (Quad-Frequency: sub-ns accuracy)
- ZTD/PWV retrieval (Zhou Linghao 2025: 3.7–4.7mm RMS vs radiosonde)
- Earthquake displacement (Jianfei Zang 2024: 0.3–0.4cm combined GPS/BDS)

## MIXED_PRODUCTS (7 papers)

Critical for classification boundary validation. These papers compare PPP-B2b with:
- Galileo HAS (Pan Lin 2025, Wei Haopeng 2024)
- MADOCA-PPP (Comparative Broadcast Frameworks)
- CNES/IGS RTS (RT_ZTD)
- Multi-source LEO orbit determination (RT Kinematic Orbit LEO)

**Rule:** MIXED_PRODUCTS must NOT be merged into BDS3_PPP_B2B_BROADCAST core corpus — this would inflate B2b performance claims with multi-source results.

## CNES_OR_OTHER_RTS (3 papers)

Covers heterogeneous papers:
- Borio 2023 — GHASP Galileo HAS parser (pure Galileo HAS tool)
- Zhou Peiyuan 2024 — Galileo HAS initial performance assessment
- Liu Wei — 72-page Chinese thesis on general BDS/GPS RTK+PPP (0 B2b mentions)

## QZSS_CLAS (2 papers)

- Taro Suzuki 2023 — compact antenna evaluation for QZSS L6 CLAS reception
- Euiho Kim 2022 — fault-free protection level equation for CLAS PPP

## Taxonomy Refinement Note (v0.3 → v0.4)

**CNES_OR_OTHER_RTS granularity is insufficient.** Within the v0.3 corpus, this label mixes:
- Galileo HAS (2 papers)
- General PPP (1 paper)

**Recommended v0.4 refinement:**
- `GALILEO_HAS` for Galileo High Accuracy Service papers
- `NON_B2B_GENERAL_PPP` for general PPP/RTK not specific to any satellite-based augmentation
- `QZSS_MADOCA` if MADOCA-specific papers are added

**This is a taxonomy design note — v0.3 corpus data is not modified.**
