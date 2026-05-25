# Full Audit Batch 3 — Ramped Expansion Plan

**Date:** 2026-05-22
**Target:** 20-30 papers in 3 phases

## Phase Allocation

| Phase | Papers | Trigger for next phase |
|-------|--------|----------------------|
| Phase A | 10 papers | All 10 PASS, 0 WRONG_SUPPORT |
| Phase B | 10 papers | Phase A complete, cumulative 20 PASS |
| Phase C | 0-10 papers | Only if 20/20 PASS, 0 circuit breaker triggers |

## Candidate Selection by Category

### Category 1: core_ppp_b2b (target: 8+ papers)

| # | Candidate | Year | Risk | Phase |
|---|-----------|------|------|-------|
| 1 | Nie 2021 — Initial Assessment (remotesensing-13-02050) | 2021 | LOW | Already in Batch 2 |
| 2 | Lu 2021 — SDR Decoding B2b | 2021 | LOW | Already in Batch 2 |
| 3 | Multi-Frequency RT B2b (Zhou 2023) | 2023 | LOW | Already in Batch 2 |
| 4 | PPP-B2b Coverage ZTD (Wang 2024) | 2024 | LOW | Already in Batch 2 |
| 5 | Quad-Frequency Time Transfer | 2024 | LOW | Already in Batch 2 |
| 6 | Factor Graph PPP-B2b/INS | ? | LOW | Phase A |
| 7 | Real-Time Kinematic Orbit LEO + B2b | ? | MEDIUM | Phase A |
| 8 | GKit-SSRDecoder open-source | ? | LOW | Phase A |
| 9 | BDS-3 PPP-B2b + low-cost devices PWV | ? | LOW | Phase B |
| 10 | Mathematical Problems — BDS-3 Real-time PPP | 2022 | LOW | Phase B |
| 11 | Mathematical Problems — Signal-in-Space BDS Augmentation | 2022 | MEDIUM | Phase B |
| 12 | Single-Frequency PPP-B2b Time Transfer | ? | LOW | Phase C |

### Category 2: boundary_mixed/comparison (target: 5+ papers)

| # | Candidate | Year | Risk | Phase |
|---|-----------|------|------|-------|
| 13 | Wei Haopeng 2024 — HAS + B2b | 2024 | MEDIUM | Already in Batch 2 |
| 14 | Comparative Broadcast Frameworks | 2024 | MEDIUM | Already in Batch 2 |
| 15 | RT ZTD B2b HAS MADOCA | 2024 | MEDIUM | Already in Batch 2 |
| 16 | Pan Lin 2025 — BDS B2b and HAS | 2025 | MEDIUM | Phase A |
| 17 | Zhou Peiyuan 2024 — Galileo HAS Initial | 2024 | MEDIUM | Phase B |

### Category 3: non_b2b_augmentation (target: 4+ papers)

| # | Candidate | Year | Risk | Phase |
|---|-----------|------|------|-------|
| 18 | Borio GHASP (Galileo HAS) | 2023 | LOW | Already in Batch 2 |
| 19 | Taro Suzuki QZSS CLAS | 2023 | LOW | Already in Batch 2 |
| 20 | Nacer Naciri — Galileo HAS Assessment | 2023 | LOW | Phase A |
| 21 | Daniele Borio — HASCoordSept2023 | 2023 | LOW | Phase B |
| 22 | Euiho Kim 2022 — CLAS PPP Fault-Free | 2022 | LOW | Phase B |

### Category 4: toolbox/implementation (target: 2+ papers)

| # | Candidate | Year | Risk | Phase |
|---|-----------|------|------|-------|
| 23 | Zhao Lewen 2025 — NavDecoder | 2025 | LOW | Already in Batch 1 |
| 24 | GKit-SSRDecoder | ? | LOW | Phase A |

### Category 5: difficult/risk PDFs (target: 1-2 papers)

| # | Candidate | Year | Risk | Phase |
|---|-----------|------|------|-------|
| 25 | 基于北斗_GPS的RTK和实时PPP (刘威) | ? | HIGH | Phase B/C |
| 26 | Qin 2024 Phys. Scr. | 2024 | HIGH | Phase C |

## Research_on_Quad-Frequency Status
- ✅ Already processed in Batch 2
- PDF quality: PASS (6 pages, digital native)
- Eligible for any batch — **already included**

## Coverage Gap Analysis vs Batch 1+2

| Dimension | Batch 1+2 (17 papers) | Batch 3 Target |
|-----------|----------------------|----------------|
| core_ppp_b2b | 12 | +8 = 20 |
| boundary_mixed | 3 | +2 to 3 = 5-6 |
| non_b2b | 2 | +2 to 3 = 4-5 |
| toolbox | 1 | +1 to 2 = 2-3 |
| difficult PDF | 0 | +1 to 2 = 1-2 |
| Chinese-language | 0 | +1 = 1 |

## Circuit Breaker Rules (inherited)

1. WRONG_SUPPORT > 0 → STOP
2. product_source misclassification → STOP
3. experiment_epoch contamination → STOP
4. invalid_quote_id_rate >= 5% → STOP
5. BLOCKED rate > 20% → STOP
6. keyword_overlap as sole critical field evidence → STOP
7. quote_bank generation failure → STOP
8. corpus maps contaminated with BLOCKED papers → STOP

## Recommended Scale

**Target: 20 papers for Batch 3.** Phase A (10) + Phase B (10). Phase C only if cumulative metrics are clean.
