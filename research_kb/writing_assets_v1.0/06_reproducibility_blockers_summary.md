# 06 — Reproducibility Blockers Summary

## Overall

73% of the 107 admitted papers score 0-1/10 on reproducibility. Only 3% provide open-source code.

## Blocker Categories (for thesis)

### 1. Data Availability (CRITICAL, 106/107 papers)
No paper publicly archives raw GNSS observation data or PPP-B2b correction streams for the evaluation period. B2b corrections are broadcast via GEO satellites (not internet) and require specialized receivers.

### 2. Software/Tooling (CRITICAL, 103/107 papers)
Only 3 papers release code: Zhao Lewen 2025 (NavDecoder), GKit SSRDecoder, Lu 2021 (SDR). Most use proprietary PPP engines.

### 3. Parameter Disclosure (HIGH, 90+ papers)
Kalman filter settings, antenna PCO/PCV values, tropospheric models, and processing configurations often omitted. Chinese-manufactured antennas not in igs14.atx.

### 4. Product Access (HIGH, 106/107 papers)
PPP-B2b correction stream is regional (China + surrounding areas), broadcast-only (no archive), and requires specialized receiver hardware. This is the single most impactful reproducibility barrier.

## Thesis Section Recommendation

Dedicate a subsection to "Reproducibility Challenges in PPP-B2b Research" with these 4 categories as sub-headings. Use the 3 open-source papers as positive examples and the 73% low-score statistic as the key finding.
