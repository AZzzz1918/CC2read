# v0.4 Wave 2 — Coverage Saturation Audit

**Date:** 2026-05-24

## Wave 2 Results

| # | Paper | B2b | Pages | Category | Product Source |
|---|-------|-----|-------|----------|----------------|
| 1 | Precise real-time navigation of LEO satellite by BDS-3 PPP-B2b | 184 | 17 | LEO Orbit | BDS3_B2B |
| 2 | BDS-PPP-B2b Smartphone Precise Positioning | 66 | 19 | Smartphone | BDS3_B2B |
| 3 | Time Comparison and Positioning of BDS-3 PPP-B2b Signal via GEO | 244 | 21 | Timing | BDS3_B2B |
| 4 | PWV retrieval by BeiDou PPP-B2b (ocean-based) | 111 | 13 | ZTD/PWV | BDS3_B2B |
| 5 | BDS-3 PPP-B2b RTS compared with CNES RTS | 137 | 16 | Boundary B2b+RTS | BDS3_B2B |
| 6 | Precise LEO orbit determination using PPP-B2b | 175 | 12 | LEO Orbit | BDS3_B2B |
| 7 | Real-time seismogeodesy using Galileo HAS + BDS PPP-B2b | 180 | 16 | Seismogeodesy | BDS3_B2B |
| 8 | PPP-B2b satellite clock and time transfer (Qin 2024) | 107 | 15 | Clock/Timing | BDS3_B2B |
| 9 | Real-time PPP with Galileo HAS + BDS-3 PPP-B2b fusion | 139 | 16 | HAS+B2b Fusion | BDS3_B2B |
| 10 | Integration of Galileo HAS + BDS-3 PPP-B2b + INS | 186 | 15 | HAS+B2b+INS | BDS3_B2B |

**10/10 PASS. 0 WRONG_SUPPORT. 0 product source errors. v0.3 regression: 17/17.**

---

## 1. 是否新增技术路线

✅ **YES — 3 new application routes confirmed:**

| Route | Wave 2 Papers | v0.3 Coverage |
|-------|--------------|---------------|
| **LEO satellite PPP-B2b navigation** | 184+175 B2b (2 papers) | 0 papers |
| **Smartphone PPP-B2b positioning** | 66 B2b (1 paper) | 0 papers |
| **B2b seismogeodesy (shake table)** | 180 B2b (1 paper) | 0 papers |

## 2. Wave 1 PPP-B2b-RTK 路线是否被更多证据支持

⚠️ **No second PPP-B2b-RTK paper in Wave 2.** The single paper from Wave 1 (s10291-025-01854-4) remains the only PPP-B2b-RTK paper found. This suggests it's an **emerging method, not a well-established route.**

## 3. Wave 1 BDSet 路线是否被更多证据支持

⚠️ **No second dataset paper in Wave 2.** BDSet (s41597-026-07032-6) from Wave 1 remains unique. Public B2b datasets are rare.

## 4. Wave 1 short-message 路线是否被更多证据支持

⚠️ **No second short-message paper in Wave 2.** This is a niche route.

## 5. 是否新增独立应用路线

✅ **LEO orbit (2 papers), smartphone (1 paper), seismogeodesy (1 paper).** These were absent from v0.3.

## 6. 是否改变 product_source taxonomy

**No.** All Wave 2 papers are BDS3_PPP_B2B_BROADCAST. Taxonomy labels unchanged.

## 7. 是否改变 method_lineage

✅ **3 new method nodes:**
- LEO PPP-B2b orbit determination
- Smartphone-grade PPP-B2b
- B2b + HAS seismogeodesy

## 8. 是否改变 future work

✅ **Yes.** v0.3 stated "LEO coverage limited" — now disproven. Smartphone B2b is a new application direction.

## 9. 是否改变 manuscript section structure

⚠️ **Yes — new application sections needed:** LEO navigation, smartphone positioning, seismogeodesy.

## 10. 是否出现大量重复论文，提示 coverage saturation

**No.** Waves 1+2 continue to find new application routes. Saturation not yet reached.

## 11. 是否继续 Wave 3

✅ **YES.** Rationale:
- Wave 2 found 3 new application routes
- Wave 1's RTK/dataset/short-message routes need more evidence
- 60+ P1/P2 papers remain in queue
- B2b+INS, B2b multi-frequency, anomaly detection routes not yet fully explored

## 12. Wave 3 应优先处理 P1、P2，还是 boundary / manual review

**P1 + P2.** Focus on:
- Remaining P1 anomaly/clock analysis papers
- P2 INS integration papers
- P2 multi-frequency papers
- P2 boundary B2b+HAS papers

---

## Recommendation

```
CONTINUE_WAVE_3 = YES
SATURATION_REACHED = NO
PRIORITY = P1_ANOMALY + P2_INS + P2_MULTIFREQ + P2_BOUNDARY
WAVE_3_SIZE = 10
```
