# Reproducibility Discussion

**Based on reproduction_blockers extracted from the grounded v0.3 corpus (37 papers).**

---

## Overall Reproducibility Score Distribution

| Score | Papers | % |
|-------|--------|---|
| 4–5 (best) | 2 | 5.4 |
| 2–3 | 8 | 21.6 |
| 0–1 (worst) | 27 | 73.0 |

**73% of papers score 0–1/10 on reproducibility.** The only 2 papers scoring ≥4 are software toolbox papers (Zhao Lewen NavDecoder, GKit SSRDecoder) where source code is openly available.

---

## Blocker Categories

### 1. Data Availability (37/37 papers)

**Primary blocker.** No paper in the v0.3 corpus publicly archives:
- Raw GNSS observation data used in experiments
- PPP-B2b correction streams for the evaluation period
- Reference station coordinates and metadata

Representative quote evidence:
- "GNSS observation data managed by university — available on request only" (Yan Liu 2022)
- "PPP-B2b correction data not publicly archived for the evaluation period" (multiple papers)

### 2. Product Access (37/37 papers)

**Critical blocker for independent reproduction.** PPP-B2b corrections are:
- Broadcast via BDS-3 GEO satellites (not internet)
- Require specialized receiver hardware to decode
- Not archived by any public data repository
- The B2b signal itself is regional (China + surrounding areas)

**Exception:** Some papers use the IGS MGEX / iGMAS station network, whose observation data is accessible. But the B2b correction stream remains inaccessible.

### 3. Parameter / Model Missing (30+ papers)

Common omissions:
- Kalman filter process noise parameters
- Satellite antenna PCO/PCV values (Chinese-manufactured antennas not in igs14.atx)
- Tropospheric mapping function configuration
- Ambiguity resolution strategy
- Elevation cutoff angle and observation weighting

### 4. Software / Tooling Missing (34/37 papers)

- Only 3 papers release code: Zhao Lewen 2025, GKit SSRDecoder, Lu 2021 (SDR)
- Most papers use proprietary PPP processing software
- Orbit determination software (SHAO/BSNC) is not publicly available

---

## Reproducibility by Paper Type

| Type | Avg Score | Main Blocker |
|------|-----------|--------------|
| Toolbox/Decoder | 4–5 | Minor (code available) |
| Positioning Performance | 0–1 | Data + correction stream |
| Time Transfer | 1–2 | Data + parameter |
| Comparison (MIXED) | 1–2 | Multi-source data access |
| Non-B2b (HAS/CLAS) | 0–1 | Proprietary hardware |

---

## Recommendations (based on corpus analysis)

1. **PPP-B2b correction archive:** The single most impactful reproducibility improvement would be a public archive of B2b corrections for evaluation periods.
2. **Reference implementation:** An open-source PPP engine with B2b support (beyond just decoding) would enable independent validation.
3. **Minimum reporting standards:** Kalman filter parameters, antenna models, and processing configurations should be mandatory in PPP-B2b papers.
4. **Data availability statements:** Most papers claim data is "available on request" — standardized data sharing would improve the field.

---

## Caveat

This assessment is within the v0.3 corpus (37 papers). The low reproducibility scores reflect systemic issues in the PPP-B2b literature, not extraction failures. Reproducibility blockers were extracted from each paper's reported limitations and verified against the paper content.
