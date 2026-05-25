# Full Audit Batch 2 — Candidate Selection

**Date:** 2026-05-22
**Target:** 10 papers (4 core + 3 boundary/mixed + 2 non-B2b + 1 Research_on_Quad-Frequency)

---

## Selection Summary

| # | Paper ID | Year | Role | Expected Product | Risk |
|---|----------|------|------|-------------------|------|
| 1 | Nie_2021_initial_assessment_bds_ppp_b2b | 2021 | core_ppp_b2b | BDS3_PPP_B2B_BROADCAST | LOW |
| 2 | Lu_2021_decoding_ppp_corrections_bds_b2b_sdr | 2021 | core_ppp_b2b | BDS3_PPP_B2B_BROADCAST | LOW |
| 3 | Multi-Frequency_BDS-3_RT_PPP_B2b | 2023 | core_ppp_b2b | BDS3_PPP_B2B_BROADCAST | LOW |
| 4 | PPP-B2b_coverage_ZTD_positioning | 2024 | core_ppp_b2b | BDS3_PPP_B2B_BROADCAST | LOW |
| 5 | Wei_Haopeng_2024_combining_has_ppp_b2b | 2024 | boundary_mixed | MIXED_PRODUCTS | MEDIUM |
| 6 | Comparative_Broadcast_Frameworks_B2b_HAS_MADOCA | 2024 | boundary_mixed | MIXED_PRODUCTS | MEDIUM |
| 7 | RT_ZTD_PPP-B2b_HAS_MADOCA | 2024 | boundary_mixed | MIXED_PRODUCTS | MEDIUM |
| 8 | Borio_2023_ghasp_galileo_has_parser | 2023 | non_b2b_galileo | CNES_OR_OTHER_RTS | LOW |
| 9 | Taro_Suzuki_2023_qzss_clas_l6 | 2023 | non_b2b_qzss | QZSS_CLAS | LOW |
| 10 | Research_on_Quad-Frequency_PPP-B2b_Time_Transfer | 2024 | core_ppp_b2b | BDS3_PPP_B2B_BROADCAST | LOW |

---

## Detailed Candidate Cards

### 1. Nie 2021 — Initial Assessment BDS PPP-B2b Service
- **File:** `remotesensing-13-02050-v2.pdf`
- **Year:** 2021
- **Role:** core_ppp_b2b
- **Expected product_source:** BDS3_PPP_B2B_BROADCAST
- **Risk:** LOW — title explicitly states "BDS PPP-B2b Service"
- **Reason:** One of the earliest and most cited PPP-B2b assessment papers. Evaluates orbit/clock correction precision and PPP performance.
- **PDF ready:** ✅

### 2. Lu 2021 — Decoding PPP Corrections From BDS B2b Signals (SDR)
- **File:** `Decoding_PPP_Corrections_From_BDS_B2b_Signals_Using_a_Software-Defined_Receiver_An_Initial_Performance_Evaluation.pdf`
- **Year:** 2021
- **Role:** core_ppp_b2b
- **Expected product_source:** BDS3_PPP_B2B_BROADCAST
- **Risk:** LOW — title explicitly states "BDS B2b Signals"
- **Reason:** Software-defined receiver approach to decode B2b corrections. Unique technical perspective different from standard PPP evaluation.
- **PDF ready:** ✅

### 3. Multi-Frequency BDS-3 RT PPP-B2b
- **File:** `Multi-Frequency_BDS-3_Real-Time_Positioning_Performance_Assessment_Using_New_PPP-B2b_Augmentation_Service.pdf`
- **Year:** ~2023
- **Role:** core_ppp_b2b
- **Expected product_source:** BDS3_PPP_B2B_BROADCAST
- **Risk:** LOW — title states "PPP-B2b Augmentation Service"
- **Reason:** Multi-frequency evaluation of B2b service. Covers B1I/B3I, B1C/B2a combinations.
- **PDF ready:** ✅

### 4. PPP-B2b Coverage and ZTD Performance
- **File:** `An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions.pdf`
- **Year:** ~2024
- **Role:** core_ppp_b2b
- **Expected product_source:** BDS3_PPP_B2B_BROADCAST
- **Risk:** LOW — title states "PPP-B2b coverage"
- **Reason:** Regional coverage analysis of PPP-B2b service. Extends prior single-region studies to multiple regions.
- **PDF ready:** ✅

### 5. Wei Haopeng 2024 — Combining Galileo HAS and BeiDou PPP-B2b
- **File:** `2024--Wei Haopeng--Combining Galileo HAS and Beidou PPP-B2b with Helmert coordinate .pdf`
- **Year:** 2024
- **Role:** boundary_mixed
- **Expected product_source:** MIXED_PRODUCTS
- **Risk:** MEDIUM — model might incorrectly classify as pure BDS3_B2B
- **Reason:** Explicitly combines Galileo HAS + BDS PPP-B2b. Tests MIXED_PRODUCTS separation.
- **PDF ready:** ✅

### 6. Comparative Broadcast Frameworks
- **File:** `A_Comparative_Investigation_of_Broadcast_Frameworks_Service_Availability_and_Time_Transfer_Performance_in_PPP-B2b_HAS_and_MADOCA-PPP.pdf`
- **Year:** ~2024
- **Role:** boundary_mixed
- **Expected product_source:** MIXED_PRODUCTS
- **Risk:** MEDIUM — three systems compared
- **Reason:** Compares B2b, HAS, MADOCA-PPP. Tests multi-system MIXED classification.
- **PDF ready:** ✅

### 7. RT ZTD with PPP-B2b, HAS, MADOCA-PPP
- **File:** `Real-Time_Precise_Zenith_Tropospheric_Delay_Estimation_With_BDS_PPP-B2b_Galileo_HAS_and_QZSS_MADOCA-PPP_Services.pdf`
- **Year:** ~2024
- **Role:** boundary_mixed
- **Expected product_source:** MIXED_PRODUCTS
- **Risk:** MEDIUM — three systems compared for ZTD
- **Reason:** Tests ZTD estimation across three satellite-based PPP services.
- **PDF ready:** ✅

### 8. Borio 2023 — GHASP Galileo HAS Parser
- **File:** `2023--D. Borio--GHASP_a_Galileo_HAS_parser.pdf`
- **Year:** 2023
- **Role:** non_b2b_galileo
- **Expected product_source:** CNES_OR_OTHER_RTS
- **Risk:** LOW — explicitly Galileo HAS
- **Reason:** Pure Galileo HAS parser. Tests non-B2b classification.
- **PDF ready:** ✅

### 9. Taro Suzuki 2023 — QZSS CLAS L6 Evaluation
- **File:** `2023--Taro Suzuki--Evaluation_of_L6_augmentation_signal_reception_cha.pdf`
- **Year:** 2023
- **Role:** non_b2b_qzss
- **Expected product_source:** QZSS_CLAS
- **Risk:** LOW — explicitly QZSS CLAS
- **Reason:** Pure QZSS CLAS. Tests non-B2b classification. Lite extraction already available from scale_test_10.
- **PDF ready:** ✅

### 10. Research on Quad-Frequency PPP-B2b Time Transfer
- **File:** `Research_on_Quad-Frequency_PPP-B2b_Time_Transfer.pdf`
- **Year:** 2024
- **Role:** core_ppp_b2b
- **Expected product_source:** BDS3_PPP_B2B_BROADCAST
- **Risk:** LOW — explicitly PPP-B2b
- **Reason:** Already passed PDF quality check. Markdown generated. Ready for full extraction.
- **Markdown ready:** ✅

---

## Expected Classification Accuracy Targets

| Category | Count | Expected Correct | Acceptable Errors |
|----------|-------|------------------|-------------------|
| core_ppp_b2b → BDS3_B2B | 5 | 5 | 0 |
| boundary_mixed → MIXED | 3 | 3 | 0 |
| non_b2b → correct external | 2 | 2 | 0 |
| **Total** | **10** | **10** | **0** |

## Risk Matrix

| Risk | Papers |
|------|--------|
| HIGH (product_source ambiguity) | 0 |
| MEDIUM (MIXED products) | 3 (#5, #6, #7) |
| LOW | 7 |
