# Technical Routes Synthesis

**Within the grounded v0.3 corpus (37 papers).**

---

## Route 1: PPP-B2b Positioning Performance (25 papers)

The largest route. Core findings within the corpus:

- **Static PPP:** cm-level accuracy consistently reported. Yan Liu 2022: 3D RMSE 3.9–8.3cm across 8 IGS MGEX stations in China and surrounding areas.
- **Kinematic PPP:** dm-level. Peida Wu 2023: 95% errors <20cm horizontal, <35cm vertical across static stations, car, vessel, and aircraft platforms.
- **Orbit/clock quality:** Tang Chenggan 2022: orbit URE 0.05m (BDS-3 MEO), clock STD 0.172ns. Nie 2021: first comprehensive B2b orbit/clock assessment.
- **Multi-frequency:** Zhou 2023: multi-frequency (B1I/B3I, B1C/B2a) evaluation. Improved convergence with additional frequencies.
- **Coverage analysis:** Wang 2024: ZTD estimation and positioning in different regions. Availability rate varies significantly with location (60–89%).

**Evidence quality:** STRONG. Multiple independent assessments converge on similar accuracy ranges.

## Route 2: PPP-B2b Time Transfer (3 papers)

- Quad-Frequency PPP-B2b Time Transfer (2024 IEEE I&M Magazine): QF model achieves smoother CCD results (<0.1ns fluctuation) compared to DF. Long-baseline residuals within 1ns.
- Single-Frequency PPP-B2b Time Transfer: complementary single-frequency approach.
- Comparative Broadcast Frameworks: compares B2b, HAS, and MADOCA-PPP for time transfer.

**Evidence quality:** PARTIAL. 3 papers from related author groups. Need more independent validation.

## Route 3: PPP-B2b ZTD/PWV Retrieval (4 papers)

- Zhou Linghao 2025: 25-day continuous experiment in Wuhan. PWV RMS 3.71–4.66mm vs radiosonde. First demonstration of operational meteorology readiness.
- Oceanic PWV (low-cost): extends to low-cost GNSS devices.
- Wang 2024: multi-region ZTD estimation.
- RT_ZTD: compares B2b, HAS, MADOCA-PPP for ZTD.

**Evidence quality:** STRONG for Zhou Linghao (clear experimental setup). PARTIAL for others (less detail in accessible text).

## Route 4: PPP-B2b + INS / Factor Graph (1 paper)

- Factor Graph PPP-B2b/INS: tightly coupled integration for real-time precise positioning. Novel optimization-based approach vs traditional Kalman filter.

**Evidence quality:** TENTATIVE. Single paper, novel approach, needs independent validation.

## Route 5: B2b vs HAS vs CLAS vs MADOCA Comparison (7 papers)

- Pan Lin 2025: BDS B2b and HAS comparison.
- Wei Haopeng 2024: Galileo HAS + BDS PPP-B2b with Helmert transformation.
- Comparative Broadcast Frameworks: three-system time transfer comparison.
- RT ZTD: three-system ZTD estimation comparison.

**Evidence quality:** STRONG for product classification boundary. MIXED_PRODUCTS category validated.

## Route 6: Toolbox / Decoder / SDR (3 papers)

- GKit SSRDecoder: open-source C/C++ decoder for both PPP-B2b and HAS.
- Zhao Lewen 2025 NavDecoder: Python toolbox for B2b and HAS decoding.
- Lu 2021: software-defined receiver for B2b signal decoding.

**Evidence quality:** STRONG for reproducibility (open-source code available).

## Route 7: Orbit/Clock Correction Generation (1 paper)

- Tang Chenggan 2022: ISL-enhanced orbit determination + real-time Kalman filter clock estimation for PPP-B2b. Describes the operational B2b correction generation pipeline.

**Evidence quality:** STRONG (authoritative, from B2b system developers at SHAO/BSNC).

## Route 8: Earthquake Monitoring (1 paper)

- Jianfei Zang 2024: 2021 Mw 7.4 Maduo earthquake case study. PPP-B2b coseismic displacement accuracy 0.3–0.4cm (combined GPS/BDS). Focal mechanism consistent with USGS/CENC.

**Evidence quality:** PARTIAL. Single-event case study. Generalization to other earthquake scenarios not demonstrated.

---

## Route Coverage Summary

| Route | Papers | Evidence Quality |
|-------|--------|------------------|
| Positioning Performance | 25 | STRONG |
| Time Transfer | 3 | PARTIAL |
| ZTD/PWV | 4 | STRONG (1) + PARTIAL (3) |
| INS/Factor Graph | 1 | TENTATIVE |
| Multi-system Comparison | 7 | STRONG |
| Toolbox/Decoder | 3 | STRONG |
| Orbit/Clock Generation | 1 | STRONG |
| Earthquake | 1 | PARTIAL |

**Gap: PPP-AR / PPP-RTK with B2b — 0 papers in the v0.3 corpus.**
