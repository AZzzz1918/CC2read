# SKILL v2.0 Update Summary

**Date:** 2026-05-25
**From:** SKILL v1.0 (corpus_grounded_v0.3, 37 papers)
**To:** SKILL v2.0 (corpus_grounded_v1.0, 107 papers)

---

## 一、What Changed

### 1. Baseline 更新

| Item | v1.0 (old) | v2.0 (new) |
|------|-----------|-----------|
| Corpus | corpus_grounded_v0.3 | corpus_grounded_v1.0 |
| Papers | 37 | **107** |
| Raw ingestion | 37 | 173 |
| BDS3_PPP_B2B_BROADCAST | 25 | **93** |
| MIXED_PRODUCTS | 7 | **10** |
| CNES_OR_OTHER_RTS | 3 | 2 |
| QZSS_CLAS | 2 | 2 |
| NOT_MENTIONED titles | unknown | **0** |
| WRONG_SUPPORT | 0 | 0 |

### 2. 章节变化

v2.0 = 17 节（v1.0 为 14 节）。变化：

**新增 3 节：**

| Section | Title | Reason |
|---------|-------|--------|
| 二 | Current Baseline | 替换旧 v0.3 snapshot，如实反映 107 papers |
| 十 | v1.0 Consolidation Policy | 172→107 dedup 流程、NOT_MENTIONED bug 及修复 |
| 十六 | Known Gaps (v1.0 → v2.0 roadmap) | 6 个显式缺口，防止将未完成工作伪装为已完成 |

**升格为独立章节 1 项：**

| Section | Title | Reason |
|---------|-------|--------|
| 十三 | Writing Assets | 原仅散见于旧 SKILL 正文和 `writing_assets_v1.0/` 目录，现升格为独立章节，含 13 assets 完整索引 |

### 3. 修改的章节

| Section | Change |
|---------|--------|
| 六 (Pipeline) | Phase 2 注明 classification pass ≠ full extraction；Phase 4 注明 audit 仅在 37 篇完成；Phase 7 注明 107-paper goldens 不存在 |
| 七 (Taxonomy) | 更新为 v1.0 实际 counts；CNES refinement 标记为 open item |
| 十一 (Expansion Policy) | 重命名为 "Phase Expansion Policy"；Phase C → "Post-v1.0 expansion" |
| 十二 (Maps) | 注明 7 maps 仅在 37 篇生成 |
| 十四 (Regression) | 区分 "v0.3 archived: 17 goldens, 54/54 checks" vs "v1.0: goldens 不存在" |
| 十五 (Do/Do Not) | 新增 3 条: fix NOT_MENTIONED titles before freeze, keep writing assets in sync, don't claim false regression coverage |
| 十七 (Acceptance Criteria) | 完全重写，v2.0 标准替换 v1.0 标准 |

### 4. 删除/降级的内容

| Item | Disposition |
|------|-------------|
| "37 papers 足够支持 PPP-B2b 主线综述" | **删除** — 已不是当前状态 |
| "54/54 regression" | **改为 archived** — 仅覆盖 v0.3 baseline |
| Phase C DO_NOT_RUN policy | **改为** Post-v1.0 expansion trigger conditions |
| v0.3-specific coverage gap analysis | **删除** — 被 Known Gaps 章节替代 |

### 5. 保持不变的核心

- 9 HARD RULES — 全部保留
- 5 SHOULD RULES — 全部保留
- 7-phase pipeline framework — 保留，标注覆盖缺口
- Circuit breaker rules — 全部保留
- Correction layer rules — 全部保留
- Regression golden format — 保留

---

## 二、Known Gaps (显式记录)

6 个已知缺口不阻止 v2.0 freeze，但必须在 thesis limitation 或后续 release 中 address:

| # | Gap | Severity |
|---|-----|----------|
| G1 | CNES taxonomy 未细化 | MEDIUM |
| G2 | **107-paper regression goldens 不存在** | **HIGH** |
| G3 | **Full evidence audit 仅在 37 篇完成** | **HIGH** |
| G4 | 部分论文仅有 classification pass | MEDIUM |
| G5 | v1.0 7 maps 未在 107 篇上重新生成 | MEDIUM |
| G6 | 无自动化 CI pipeline | LOW |

---

## 三、Specific Prohibitions Enforced

以下 claims 已在 v2.0 中**全部移除**:

- ❌ "37 papers 是当前 corpus"
- ❌ "54/54 goldens 覆盖 107 篇"
- ❌ classification pass = full extraction pass
- ❌ v0.3 baseline 作为当前状态
- ❌ CNES taxonomy refinement 标记为 "建议 v0.4 执行"（已改为 open item）

---

## 四、Files Modified

| File | Action |
|------|--------|
| `.claude/skills/grounded-research-kb/SKILL.md` | **完全重写** → v2.0 |
| `research_kb/reports/skill_v2_update_summary.md` | **新建** (this file) |

## 五、Next Steps (不属于 SKILL update 范围)

1. 生成 107-paper regression goldens (G2)
2. 在剩余 70 篇上运行 full evidence audit (G3)
3. CNES taxonomy 细化 (G1)
4. 在 107 篇上重新生成 7 maps (G5)
5. 补全 classification-only papers 的 full extraction (G4)
