# v0.4 Wave 3 — Coverage Saturation Audit

**Date:** 2026-05-24

## Wave 3 Results

| # | Paper | B2b | Stack | Category | New Route? |
|---|-------|-----|-------|----------|------------|
| 1 | Galileo HAS SSR product quality + PPP performance | 40 | B2b+HAS | P1 | No |
| 2 | Temporal outlier detection for PPP-B2b orbit/clock | 112 | B2b | ANOMALY_CLOCK | **Yes** |
| 3 | BDS-3 PPP-B2b + MEMS IMU + LiDAR tight integration | 50 | B2b+INS | INS | **Yes** |
| 4 | Real-time uncombined PPP with BDS-3 PPP-B2b multi-freq | 110 | B2b | MULTI_FREQ | **Yes** |
| 5 | Orbit/clock combination of B2b+HAS+MADOCA | 109 | B2b+HAS | B2B_HAS_FUSION | **Yes** |
| 6 | Real-time ocean PPP with BDS-3 PPP-B2b | 91 | B2b | CORE | No |
| 7 | Real-time single-freq PPP using BDS-3 PPP-B2b | 117 | B2b | CORE | No |
| 8 | Real-time BDS-3 satellite clock estimation + PPP (SHAO) | 68 | B2b | INS | No |
| 9 | Jianfei Zang — earthquake (v0.3 DUP) | 223 | B2b | SEISMOGEO | No |

**9 papers. 0 WRONG_SUPPORT. 0 PS errors. v0.3 regression: 17/17 PASS.**

## Singleton Route Status (Waves 1-3)

| Route | Wave 1 | Wave 2 | Wave 3 | Status |
|-------|--------|--------|--------|--------|
| PPP-B2b-RTK | 1 | 0 | 0 | **UNCONFIRMED SINGLETON** |
| BDSet / public dataset | 1 | 0 | 0 | **UNCONFIRMED SINGLETON** |
| Short-message B2b | 2 | 0 | 0 | **NICHE (2 papers, same author group?)** |
| LEO PPP-B2b | 0 | 2 | 0 | Confirmed (2 papers) |
| Smartphone B2b | 0 | 1 | 0 | **UNCONFIRMED SINGLETON** |
| B2b Seismogeodesy | 0 | 1 | 0 | **UNCONFIRMED SINGLETON** |

## New Routes in Wave 3

| Route | Papers | Previously in v0.3? |
|-------|--------|---------------------|
| B2b orbit/clock outlier detection | 1 (remotesensing-16-02337) | No |
| B2b + INS + LiDAR tight integration | 1 (1-s2.0-S0263224124019006) | Partial (v0.3 had Factor Graph INS) |
| Uncombined multi-freq B2b PPP | 1 (1-s2.0-S0273117724008755) | Partial (v0.3 had multi-freq) |
| B2b+HAS+MADOCA triple combination | 1 (1-s2.0-S026322412601448X) | No |

## Saturation Assessment

| Metric | Wave 1 | Wave 2 | Wave 3 | Trend |
|--------|--------|--------|--------|-------|
| Papers processed | 10 | 10 | 9 | — |
| Genuinely new routes | 3 | 3 | 2 | **DECLINING** |
| Singleton confirmations | — | 2 | 0 | **DECLINING** |
| Duplicate/v0.3 papers hit | 1 | 0 | 1 | — |
| Papers reinforcing existing routes | 6 | 5 | 6 | **INCREASING** |

## Decision

```
SATURATION_TREND = APPROACHING
NEW_ROUTES_PER_WAVE = 3 → 3 → 2 (declining)
SINGLETON_CONFIRMATIONS = 2 → 0 (declining)
REINFORCEMENT_RATIO = 60% → 50% → 67% (increasing)

RECOMMENDATION = STOP_AFTER_WAVE_4_OR_FREEZE_NOW
```

**Rationale:**
- Wave 3 found 2 genuinely new routes (anomaly detection, HAS+B2b+MADOCA triple), but rate is declining
- 3 critical singletons remain unconfirmed (PPP-B2b-RTK, BDSet, smartphone)
- 67% of Wave 3 papers reinforce existing routes
- ~50 papers remain in queue, but most are P2/P3 application papers

**Options:**
1. **FREEZE_NOW** — accept 29-paper v0.4 as sufficient; mark 3 singletons as "emerging, needs future monitoring"
2. **WAVE_4_TARGETED** — process only the singleton confirmation targets (5-6 papers max), skip P2/P3
