# Problem Evolution Timeline

**Within the grounded v0.3 corpus (37 papers, 2020–2025).**

---

## Phase 1: System Validation (2020–2021, 3 papers)

### Context
BDS-3 completed constellation deployment (June 2020), announced PPP-B2b service (July 2020). Research community begins initial assessment.

### Key Papers
- **Maosen Hao 2020** (pilot, QZSS CLAS context): pre-B2b reference point — centimeter-level augmentation service evaluation for QZSS
- **Nie 2021** (Remote Sensing): first comprehensive BDS PPP-B2b orbit/clock correction precision assessment
- **Lu 2021** (IEEE Sensors): software-defined receiver approach to decode B2b signals

### Key Questions
- What is the accuracy of PPP-B2b orbit and clock corrections?
- Can B2b signals be decoded with commodity SDR hardware?
- How does B2b compare with post-processed precise products?

### Evidence
- Tang Chenggan 2022 (published later, data from Aug 2020): orbit URE 0.05m, clock STD 0.2ns
- Nie 2021: first independent B2b correction quality assessment

---

## Phase 2: Comprehensive Evaluation (2022–2023, 10 papers)

### Context
PPP-B2b service matures. Research shifts from "does it work" to "how well, where, and under what conditions."

### Key Papers
- **Yan Liu 2022** (Remote Sensing, 28pp): most comprehensive PPP-B2b evaluation — 8 IGS MGEX stations in China + surrounding countries, static/kinematic, orbit/clock/DCB/SISRE
- **Tang Chenggan 2022** (Journal of Geodesy): orbit determination and clock estimation strategy behind PPP-B2b correction generation
- **Yangyuanxi 2022** (Satellite Navigation): BDSBAS + PPP-B2b system principle by BDS chief designer Yuanxi Yang
- **Peida Wu 2023** (GPS Solutions): first multi-platform kinematic evaluation (car, vessel, aircraft)
- **Zhou 2023** (IEEE Sensors): multi-frequency B2b evaluation
- **Euiho Kim 2022**: CLAS PPP fault-free protection level (QZSS, non-B2b baseline)
- **Borio 2023** (GPS Solutions): GHASP Galileo HAS parser (non-B2b baseline)
- **Taro Suzuki 2023** (GPS Solutions): QZSS CLAS L6 compact antenna evaluation

### Key Questions
- How does PPP-B2b perform outside China territory?
- Can kinematic platforms achieve operational accuracy?
- How do competing services (Galileo HAS, QZSS CLAS) compare?
- What is the correction generation pipeline?

---

## Phase 3: Application Diversification (2024–2025, 18 papers)

### Context
PPP-B2b proven. Research diversifies into downstream applications, cross-system comparison, and operational tooling.

### Key Papers — Applications
- **Jianfei Zang 2024** (GPS Solutions): earthquake source description using PPP-B2b (2021 Maduo Mw 7.4)
- **Zhou Linghao 2025** (Applied Sciences): operational water vapor monitoring (25-day experiment, Wuhan)
- **Wang 2024** (Survey Review): PPP-B2b coverage and ZTD performance in multi-region
- **Oceanic PWV**: low-cost GNSS devices for oceanic PWV sensing
- **Quad-Frequency Time Transfer** (2024 IEEE I&M): QF PPP-B2b time transfer (<0.1ns CCD)
- **Single-Frequency Time Transfer**: complementary SF approach

### Key Papers — Cross-System Comparison
- **Pan Lin 2025**: BDS B2b and HAS comparison
- **Wei Haopeng 2024**: Galileo HAS + BDS B2b Helmert combination
- **Comparative Broadcast Frameworks**: B2b/HAS/MADOCA three-system comparison
- **RT ZTD**: three-system ZTD estimation
- **RT Kinematic Orbit LEO**: HAS + B2b for LEO orbit determination

### Key Papers — Tooling
- **Zhao Lewen 2025** (GPS Solutions): NavDecoder — open-source Python toolbox
- **GKit SSRDecoder**: open-source C/C++ decoder for B2b and HAS
- **Factor Graph PPP-B2b/INS**: tightly-coupled optimization-based integration

---

## Evolution Summary

| Phase | Years | Papers | Focus |
|-------|-------|--------|-------|
| System Validation | 2020–2021 | 3 | Does B2b work? |
| Comprehensive Evaluation | 2022–2023 | 10 | How well, where, vs what? |
| Application Diversification | 2024–2025 | 18 | What can we do with it? |

## Observed Trends (within v0.3 corpus)

1. **Increasing application diversity**: from pure positioning (2021) → time transfer + ZTD + earthquake + LEO (2024–2025)
2. **Cross-system comparison emerges**: MIXED_PRODUCTS category grows from 0 (2021) to 7 papers
3. **Tooling maturity**: open-source decoders appear in 2024–2025
4. **Convergence of findings**: orbit/clock accuracy estimates converge across independent assessments
