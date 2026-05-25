# Method Lineage Summary

**Within the grounded v0.3 corpus (37 papers).**

---

## Core Methods

### Ionosphere-Free PPP (25+ papers)
The foundational processing mode across the corpus. Dual-frequency (B1I/B3I for BDS, L1/L2 for GPS) ionosphere-free linear combination eliminates first-order ionospheric delay.

**Evidence:** Yan Liu 2022 Eq.14–16; Tang Chenggan 2022 Table 5.

### Kalman Filter Estimation (10+ papers)
Dominant estimation approach for both real-time clock estimation (Tang Chenggan 2022) and user-side PPP (Peida Wu 2023, Zhao Lewen 2025). Forward Kalman filter for static PPP; combined forward-backward for kinematic.

### SISRE Computation (15+ papers)
Signal-in-Space Range Error as the standard metric for orbit/clock correction quality. BDS-3 constellation-specific weight factors (w_R=0.98, w_A,C=1/54).

**Evidence:** Yan Liu 2022 Eq.11–12; Tang Chenggan 2022 Eq.4–5.

---

## Specialized Methods

### ISL-Enhanced Orbit Determination (1 paper)
Tang Chenggan 2022: inter-satellite link measurements combined with regional L-band observations for BDS-3 orbit determination. Enables cm-level orbit accuracy without global tracking network.

### Software-Defined Receiver Decoding (1 paper)
Lu 2021: SDR-based PPP-B2b signal decoding. Alternative to dedicated receiver hardware.

### Factor Graph Optimization (1 paper)
Factor Graph PPP-B2b/INS: replacing Kalman filter with factor graph-based optimization for tightly-coupled integration. **Tentative:** single paper, not independently validated.

### PPP Time Transfer (3 papers)
Quad-frequency and single-frequency models. Key metric: common clock difference (CCD) stability.

### PWV/ZTD Retrieval (4 papers)
Standard PPP → ZTD estimation → PWV conversion using weighted mean temperature. Validated against radiosonde and ERA5.

---

## Method Relationships

```
Ionosphere-Free PPP (foundation)
├── Kalman Filter (estimation)
│   ├── Forward (static)
│   └── Forward-Backward (kinematic)
├── SISRE (quality metric)
├── Time Transfer (application)
│   ├── Dual-Frequency
│   ├── Single-Frequency
│   └── Quad-Frequency
├── ZTD/PWV Retrieval (application)
└── INS Integration (application)
    └── Factor Graph (alternative to KF)

External Products:
├── Galileo HAS → CNES_OR_OTHER_RTS
├── QZSS CLAS → QZSS_CLAS
└── IGS RTS / CNES → MIXED_PRODUCTS (comparison)

Correction Generation (infrastructure):
├── ISL-Enhanced Orbit Determination
└── Real-Time Kalman Filter Clock Estimation
```

---

## Method Gaps (within v0.3 corpus)

| Missing Method | Importance | Why Absent |
|----------------|------------|------------|
| PPP-AR (ambiguity resolution) with B2b | HIGH | No paper in corpus addresses B2b-specific AR |
| PPP-RTK with B2b | HIGH | Regional augmentation not explored |
| Machine learning for B2b correction prediction | MEDIUM | Emerging area, no papers yet |
| Multi-agent/network PPP with B2b | LOW | Niche application |

**These gaps represent genuine literature coverage gaps, not extraction failures.**
