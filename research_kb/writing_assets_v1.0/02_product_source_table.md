# 02 — Product Source Distribution Table (for thesis)

## Table X: Product source classification of the 107 admitted papers

| Product Source | Count | % | Description |
|----------------|-------|---|-------------|
| BDS3_PPP_B2B_BROADCAST | 93 | 89.6 | PPP-B2b broadcast corrections from BDS-3 GEO satellites |
| MIXED_PRODUCTS | 10 | 9.3 | B2b compared/combined with Galileo HAS, MADOCA, CNES RTS |
| CNES_OR_OTHER_RTS | 2 | 1.9 | Galileo HAS or general PPP not specific to BDS-3 |
| QZSS_CLAS | 2 | 1.9 | QZSS CLAS centimeter-level augmentation |

**Note:** CNES_OR_OTHER_RTS is a known granularity limitation. The 2 papers are: Borio 2023 (GHASP Galileo HAS parser) and Zhou Peiyuan 2024 (Galileo HAS initial assessment). A future taxonomy revision may split this into GALILEO_HAS.

## Pipeline provenance

| Stage | Ingested | Unique after dedup |
|-------|----------|-------------------|
| v0.3 seed baseline | 37 | 37 |
| v0.4 expansion waves | 29 | 29 |
| CI-001→004 incremental | 27 | 27 |
| Final drain | 79 | ~13 unique |
| **Total** | **172** | **106** |

> Do NOT cite 172 in the thesis body. The thesis corpus is 107 unique admitted papers.
