# Corpus Grounded v0.4 — Wave 1 Coverage Impact

**Date:** 2026-05-24
**Wave:** 1 (10 papers: 5 P0 + 5 P1)

---

## 1. 是否新增技术路线

✅ **YES — 3 new technical routes discovered:**

| Route | Papers | v0.3 Coverage |
|-------|--------|---------------|
| **PPP-B2b-RTK** | s10291-025-01854-4 (155 B2b) | **0 papers in v0.3** |
| **B2b Public Dataset** | s41597-026-07032-6 BDSet (204 B2b) | **0 papers in v0.3** |
| **B2b Short-Message Enhancement** | s00190-025-01965-3 (77 B2b), 1-s2.0-S0263224124014428 (34 B2b) | **0 papers in v0.3** |

## 2. 是否出现 PPP-B2b-RTK / PPP-B2b-AR 路线

✅ **PPP-B2b-RTK confirmed.** s10291-025-01854-4: "PPP-B2b-RTK: a PPP-B2b augmentation method by using the SSR corrections from a single reference station" — 155 B2b mentions, 16 pages. This fills the largest gap identified in v0.3 analysis.

## 3. 是否新增公开数据集路线

✅ **BDSet confirmed.** s41597-026-07032-6: 204 B2b mentions, 15 pages, 35 DCB mentions. First-ever BDS PPP augmentation dataset since 2023. Published in Scientific Data (Nature).

## 4. 是否改变 product_source taxonomy

⚠️ **No taxonomy change needed, but boundary expanded.** All Wave 1 papers are BDS3_PPP_B2B_BROADCAST. The taxonomy labels remain valid. However, the v0.3 claim that "CNES_OR_OTHER_RTS needs refinement" is now secondary to the finding that core B2b routes were undersampled.

## 5. 是否改变 method_lineage

✅ **Yes — 4 new method nodes:**

| Method | Status in v0.3 | Wave 1 Evidence |
|--------|---------------|-----------------|
| PPP-B2b-RTK | **Absent** | Confirmed (s10291-025-01854-4) |
| B2b + short-message communication | **Absent** | Confirmed (2 papers) |
| B2b anomaly/SIS detection | **Absent** | Confirmed (s10291-025-01850-8, 260 B2b) |
| B2b dual→five frequency | **Partial** (only DF+SF in v0.3) | Strengthened (s40623-024-02031-6) |

## 6. 是否改变 future work

✅ **Yes.** v0.3 analysis stated "PPP-AR / PPP-RTK with B2b: 0 papers in corpus" and "no HIGH severity gaps." Both claims are invalidated. Wave 1 alone found PPP-B2b-RTK and 3 additional routes absent from v0.3.

## 7. 是否需要继续 Wave 2

✅ **YES. Strongly recommended.** Rationale:
- 80 genuinely new papers in queue
- 50 P2_APPLICATION papers remaining (core B2b positioning/timing/PWV/INS)
- 20 P1_CORE remaining
- 5 P3_BOUNDARY remaining
- Wave 1 proved the pipeline can handle them efficiently

## 8. 是否应暂停 writing package 的哪些结论

**These v0.3 conclusions are PAUSED/INVALIDATED:**

| Conclusion | New Status |
|-----------|------------|
| "37 papers sufficient for comprehensive review" | ❌ INVALIDATED — at least 50 more B2b papers exist |
| "0 HIGH severity coverage gaps" | ❌ INVALIDATED — PPP-B2b-RTK was a HIGH gap |
| "Phase C DO_NOT_RUN" | ❌ INVALIDATED — replace with TARGETED_WAVES |
| "No new technical routes needed" | ❌ INVALIDATED — 3 new routes confirmed |
| "v0.3 coverage gap: only MEDIUM taxonomy" | ❌ INVALIDATED — core B2b routes were undersampled |

**These v0.3 conclusions remain VALID:**

| Conclusion | Status |
|-----------|--------|
| v0.3 pipeline is robust (0 errors) | ✅ |
| BDS3_PPP_B2B_BROADCAST is the dominant category | ✅ |
| Reproducibility is critically low | ✅ |
| DCB under-reporting is systemic | ✅ |

## Recommendation

```
CONTINUE_WAVE_2 = YES
TARGET = Process P1+P2 papers in 5 more waves (10 papers each)
V0.3_STATUS = VALIDATED_SEED (not invalidated, just incomplete)
WRITING = REMAIN_PAUSED until v0.4 corpus reaches coverage saturation
```
