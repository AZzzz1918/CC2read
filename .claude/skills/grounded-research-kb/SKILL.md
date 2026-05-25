# Grounded Research KB — Formal Skill

**Version:** 2.0 (current baseline: corpus_grounded_v1.0)
**Papers:** 107 unique admitted (from 173 raw ingestion)
**WRONG_SUPPORT:** 0
**Status:** PRODUCTION (with documented known gaps)
**Last updated:** 2026-05-25

---

## 一、Purpose

构建 **quote_id-grounded、可回归、可审计** 的科研知识库，适用于 PPP-B2b / GNSS / real-time correction literature audit。

### 核心原则

1. **evidence first** — 所有关键字段必须有证据支持
2. **quote_bank first** — 证据来自 canonical markdown，不是 LLM 自由生成
3. **no free-form LLM quote** — 禁止 LLM 编造、改写、翻译 quote text
4. **no publication-year epoch contamination** — experiment_epoch 必须来自正文实验日期
5. **no silent correction** — 所有修正必须记录在 semantic_corrections.yaml
6. **phased expansion only** — 不允许一次性全量跑

---

## 二、Current Baseline

### corpus_grounded_v1.0

| Metric | Value |
|--------|-------|
| Total admitted (unique) | **107** |
| Raw ingested (before dedup) | 173 |
| Duplicate groups removed | 66 raw → 66 dup pairs deduped |
| NOT_MENTIONED title papers | **0** (9 fixed in v1.0-patch-1/2) |

### Product Source Distribution

| Value | Count | Description |
|-------|-------|-------------|
| BDS3_PPP_B2B_BROADCAST | 93 | BDS-3 PPP-B2b broadcast corrections |
| MIXED_PRODUCTS | 10 | PPP-B2b + Galileo HAS / MADOCA / CNES |
| CNES_OR_OTHER_RTS | 2 | Galileo HAS / general PPP (non-B2b) |
| QZSS_CLAS | 2 | QZSS CLAS augmentation |

### Release History

| Stage | Papers (raw) | Date |
|-------|-------------|------|
| corpus_grounded_v0.3 (archived baseline) | 37 | 2026-05-22 |
| v0.4 Targeted Wave 1 | +10 | 2026-05-23 |
| v0.4 Targeted Wave 2 | +10 | 2026-05-23 |
| v0.4 Targeted Wave 3 | +9 | 2026-05-23 |
| CI-001 → CI-004 | +27 | 2026-05-24 |
| Final Drain | +79 | 2026-05-24 |
| **v1.0 Consolidation** | **172→107 unique** | 2026-05-24 |
| v1.0-patch-1 (NOT_MENTIONED dedup fix) | +2 restored | 2026-05-25 |
| v1.0-patch-2 (remaining NOT_MENTIONED fix) | −1 dup removed | 2026-05-25 |

---

## 三、Input / Output Layout

### Input

```
paper/                          # 原始 PDF
research_kb/markdown/           # canonical markdown (with PAGE markers)
research_kb/chunks/             # markdown chunks
research_kb/evidence/           # quote_banks, support_audits
research_kb/inventory/          # all_papers_registry, duplicate_groups, exclusion_registry
```

### Output (v1.0 release)

```
research_kb/releases/corpus_grounded_v1.0/
├── manifest.json
├── corpus_index.json
├── corpus_index.yaml
├── json_admitted/              # 107 papers
├── maps/
│   └── taxonomy.json
├── writing_views/
│   └── by_product_source.yaml
├── query_views/
└── reports/
    └── final_status.md

research_kb/writing_assets_v1.0/  # 13 thesis writing assets
├── 01_corpus_summary_for_thesis.md
├── 02_product_source_table.md
├── 03_evidence_claim_table.md
├── 04_application_route_distribution.md
├── 05_evolution_timeline.md
├── 06_reproducibility_blockers_summary.md
├── 07_limitations_to_acknowledge.md
├── 08_recommended_figures_tables.md
├── 09_thesis_backbone_outline.md
├── 10_mixed_vs_core_separation.md
├── 11_thesis_writing_checklist.md
├── 12_cross_reference_map.md
└── 13_ready_to_write_status.md
```

---

## 四、HARD RULES (9 条)

违反任一条 → **STOP，不冻结 release。**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | PDF 必须先经过 pdfplumber/PyMuPDF → canonical markdown pipeline，不允许直接 Read PDF 后抽取 | 防止乱码、缺页、OCR 失败被静默忽略 |
| 2 | Markdown 必须保留 `<!-- PAGE: N -->` 页码标记 | quote 锚点不可丢失，支持证据溯源 |
| 3 | product_source 分类必须用 keyword evidence / quote evidence 验证，防止 pre-assignment 误判 | Phase B 3 次 pre-assignment 错误已证明此风险 |
| 4 | experiment_epoch 不得使用 publication year；无实验日期必须标记 NOT_MENTIONED | 防止 epoch 污染 |
| 5 | DCB / ionospheric handling 未提及时必须标记 NOT_MENTIONED，不得幻觉补充 | 防止 LLM 编造 |
| 6 | reproduction_blockers 每篇必须非空 | 防止空评估 |
| 7 | MIXED_PRODUCTS 不得并入 core BDS3_PPP_B2B_BROADCAST | 防止分类污染 |
| 8 | Controlled expansion 必须按 phase 推进；Phase A 完成前不得启动 Phase B | 防止批量错误传播 |
| 9 | Circuit breaker: WRONG_SUPPORT > 0 → STOP | 第 0 级安全熔断 |

---

## 五、SHOULD RULES (5 条)

违反应记录为 `limitations.md` 内容，严重情况下可阻止 release。

| # | Rule | Threshold |
|---|------|-----------|
| 10 | Quote text 必须来自 canonical markdown，不允许 LLM 自由生成 quote | 0 tolerance |
| 11 | keyword_overlap ratio 不得 >60%，且不得作为关键字段唯一证据 | >60% → flagged |
| 12 | invalid_quote_id_rate 必须 <5% | >=5% → STOP |
| 13 | Targeted correction 优先于 full re-extraction | 默认选择 |
| 14 | Semantic corrections 必须记录 old_value, new_value, reason, evidence_summary, source_report | 每条必填 |

---

## 六、Formal Pipeline (7 Phases)

### Phase 0: PDF Quality Check

- 检查 page count、text extraction rate、references section
- 检查 garbled_text_ratio、quote_bank eligibility
- 不合格 → `needs_pdf_reprocessing` 或 `needs_manual_review`
- 不进入 Phase 1

### Phase 1: Canonical Markdown

- 生成 markdown，保留 `<!-- PAGE: N -->` 标记
- 保留 section heading、tables、figure captions
- 不允许破坏 quote anchoring
- 工具: `pdfplumber` / `PyMuPDF(fitz)` / `danielmiessler-pdf` skill

### Phase 2: Full Extraction

- 抽取字段: product_source, b2b_mentions, experiment_epoch, DCB, ionospheric_handling, novelty, datasets, metrics, main_results, mathematical_formulation, reproduction_blockers
- `extraction_mode` 必须显式记录 (`full` / `full_strict_quotes` / `programmatic_full`)
- 不得使用 lite audit 替代 full extraction
- **注：v1.0 中并非所有 107 篇都经过 full extraction。部分论文仅通过了 classification pass（product_source + gate check），其 mathematical_model、metrics、main_results 等字段仍为 NOT_MENTIONED。此缺口已在第十六节中记录。**

### Phase 3: Quote Bank + Quote Repair

- 从 canonical markdown 生成 `quote_bank` (quote_id, text, span_index, char_length)
- `quote_id` 必须稳定 (hash-based, per-paper scope)
- quote text 只能来自 markdown
- repair 只修 grounding evidence mapping，**不修改语义字段**
- 输出: `json_repaired/` + `yaml_repaired/`

### Phase 4: Evidence Support Audit

审计每个 quote_id 是否真的支持其字段值。

**support_status 五级:**

| Status | Meaning |
|--------|---------|
| STRONG_SUPPORT | >=2 high-confidence quotes |
| PARTIAL_SUPPORT | >=1 quote, or mixed confidence |
| WEAK_SUPPORT | only low-confidence keyword_overlap |
| WRONG_SUPPORT | quote contradicts field value |
| NEEDS_MANUAL_REVIEW | unresolvable conflict |

**重点审计字段:**

product_source.actual_product_source, b2b_mentions, experiment_epoch, DCB, ionospheric_handling, novelty, datasets, metrics, main_results, mathematical_formulation, reproduction_blockers

**注：v1.0 的 evidence support audit 仅在 v0.3 baseline (37篇) 上完整执行。后续 70 篇的 audit 覆盖不完整。此缺口已在第十六节中记录。**

### Phase 5: Targeted Correction

- 只允许修正 **audit 明确证明错误** 的字段
- 禁止静默覆盖、批量重写、为通过而删除 evidence
- 每条记录: `old_value → new_value, reason, evidence, source_report`
- correction layer 写入 `semantic_corrections.yaml`
- corrected paper: `admission_status = PASS_WITH_CORRECTION`

### Phase 6: Freeze Release

- 生成 manifest, corpus_index, maps, reports, limitations, regression goldens
- `PASS_WITH_CORRECTION` 必须显式保留，不得伪装为 clean PASS
- `correction_status` 记录 `targeted_reclassification_applied`

### Phase 7: Regression Test

- 每次新 release 必须回归**所有**旧 golden verdicts
- 检查项: product_source, experiment_epoch, DCB status, quote_id validity, reproduction_blockers 非空
- 任一 fail → 不冻结 release
- **注：v1.0 regression goldens 仅在 v0.3 baseline (17 papers) 上生成和验证。107-paper regression suite 待建立。此缺口已在第十六节中记录。**

---

## 七、Product Source Taxonomy

### Current (v1.0)

| Value | Count | Description |
|-------|-------|-------------|
| BDS3_PPP_B2B_BROADCAST | 93 | BDS-3 PPP-B2b broadcast corrections as primary source |
| MIXED_PRODUCTS | 10 | PPP-B2b co-equally compared/combined with Galileo HAS, MADOCA, CNES RTS |
| CNES_OR_OTHER_RTS | 2 | Non-B2b GNSS augmentation (Galileo HAS parser, QZSS CLAS) |
| QZSS_CLAS | 2 | QZSS CLAS augmentation |

### Taxonomy Refinement (open item, not yet executed)

v0.3 已识别 `CNES_OR_OTHER_RTS` 粒度不足，混合了:
- Galileo HAS (Borio GHASP)
- General PPP (Liu Wei Chinese thesis)

**建议在 v1.1 或 v2.0 中细分为:**
- `GALILEO_HAS` — Galileo High Accuracy Service
- `NON_B2B_GENERAL_PPP` — general PPP/RTK not specific to any satellite-based augmentation
- `CNES_REAL_TIME` / `OTHER_RTS` — CNES RTS / IGS RTS (if evidence sufficient)

**当前数据不修改。** 此细化留待后续 release。

---

## 八、Circuit Breaker Rules

任一触发 → **立即停止当前 phase，不冻结 release。**

| # | Rule | Threshold |
|---|------|-----------|
| CB-1 | WRONG_SUPPORT | > 0 |
| CB-2 | product_source misclassification | > 0 |
| CB-3 | experiment_epoch publication-year contamination | > 0 |
| CB-4 | invalid_quote_id_rate | >= 5% |
| CB-5 | BLOCKED rate | > 20% |
| CB-6 | keyword_overlap as sole critical evidence | any |
| CB-7 | quote_bank generation failure | any |
| CB-8 | regression failure | any |
| CB-9 | corpus maps include BLOCKED papers | any |

---

## 九、Correction Layer Rules

Phase B 的经验教训已固化：

1. **pre-assignment 会错** — 3 次 targeted reclassification 证明（s10291_025_01845, s10291_025_01882, Liu_Wei）
2. **correction layer 必须保留** — 不静默覆盖，不删除审计轨迹
3. **admission_status** — corrected paper = `PASS_WITH_CORRECTION`
4. **correction_status** — `targeted_reclassification_applied`
5. **regression goldens 锁定 corrected value** — 防止回退

---

## 十、v1.0 Consolidation Policy

### Dedup method

v1.0 合并了 7 个 source releases 的 172 篇论文，通过**标题归一化去重**得到 107 篇 unique:

```python
title_norm = re.sub(r'[^a-z0-9]', '', title.lower())[:60]
# 前 40 字符匹配 → 视为重复
```

### NOT_MENTIONED dedup bug (已修复)

**问题**: 标题未提取（标记为 "NOT_MENTIONED"）的论文，其 `title_norm` 全部为 `"notmentioned"`，导致去重算法将它们误判为重复。

**影响范围**: 9 篇论文标题为 NOT_MENTIONED，其中:
- 2 篇被错误排除（s10291_024_01730_7, s43020_024_00146_5）
- 1 组真实重复被确认并移除（Zhou_Linghao_2025 / applsci_15_08033_v2）

**修复**（`_consolidate_v1.0.py`）:
```python
if title and title != 'NOT_MENTIONED' and len(title) > 10:
    # 执行去重
else:
    print("WARNING: skipping dedup for %s" % pid)
```

### Rule

- 标题为 NOT_MENTIONED 或空字符串的论文 **不参与去重**
- 每次 consolidation 后必须扫描 NOT_MENTIONED 标题并手工修复
- 所有 paper 的 bibliographic_info.title 必须在 freeze 前非空

---

## 十一、Phase Expansion Policy

**默认：不允许 full corpus 一次性全量跑。**

### 标准 expansion 路径

```
pilot (3) → Batch 1 (7) → Batch 2 (10) → Phase A (10) → Phase B (10)
                                                              ↓
                                                     corpus_grounded_vN
```

### Post-v1.0 expansion 触发条件（全部必须满足）

1. 外部 reviewer 明确指出文献缺口
2. 发现新的关键技术路线（如 PPP-AR / PPP-RTK with B2b）
3. 2026+ 新论文发表
4. `coverage_gap_report` 出现 **HIGH severity gap**

### 全量跑禁令

- **不允许** 跳过 phased approach 直接全量处理
- 任何跳过 attempt 必须提供 **一强证据** 证明为何分批不可行
- 默认：拒绝全量跑

---

## 十二、Map Generation Rules

### 必须生成的 7 个 maps

1. `technical_routes.yaml`
2. `problem_evolution.yaml`
3. `product_source_taxonomy.yaml`
4. `method_lineage.yaml`
5. `dataset_metric_index.yaml`
6. `reproduction_index.yaml`
7. `citation_graph.json`

### 规则

- 只使用 PASS / PASS_WITH_CORRECTION 论文
- 每个 node 必须带 `admission_status` 和 `correction_status`
- MIXED_PRODUCTS 不得污染 BDS3_PPP_B2B_BROADCAST core route
- Liu_Wei 类 general PPP 论文不得进入 BDS3_B2B route
- PASS_WITH_CORRECTION 不得伪装成 clean PASS
- 不得包含 BLOCKED paper

**注：v1.0 的 7 maps 仅在 v0.3 baseline (37篇) 上生成。全量 107 篇 maps 尚未重新生成。此缺口已在第十六节中记录。**

---

## 十三、Writing Assets

v1.0 配套生成 **13 个 thesis writing assets**，位于 `research_kb/writing_assets_v1.0/`:

| # | Asset | Purpose |
|---|-------|---------|
| 01 | corpus_summary_for_thesis.md | Key numbers, writing rules |
| 02 | product_source_table.md | 4-category taxonomy for thesis |
| 03 | evidence_claim_table.md | STRONG/PARTIAL/TENTATIVE claims |
| 04 | application_route_distribution.md | 10 application routes |
| 05 | evolution_timeline.md | 2020-2025 three-phase evolution |
| 06 | reproducibility_blockers_summary.md | 4 blocker categories |
| 07 | limitations_to_acknowledge.md | 8 must-acknowledge limitations |
| 08 | recommended_figures_tables.md | 6 figures + 5 tables |
| 09 | thesis_backbone_outline.md | 8-chapter outline |
| 10 | mixed_vs_core_separation.md | MIXED vs core B2b separation rules |
| 11 | thesis_writing_checklist.md | Per-claim verification rules |
| 12 | cross_reference_map.md | Asset→section→evidence links |
| 13 | ready_to_write_status.md | Final status confirmation |

**使用规则:**
- Thesis 正文中引用总数必须是 **107**（不是 173）
- MIXED_PRODUCTS 论文不得用于纯 B2b statistics
- 每个 claim 必须标注 STRONG / PARTIAL / TENTATIVE
- 所有统计数据必须 traceable to `corpus_index.json`

---

## 十四、Regression Golden Format

每篇论文必须保存 golden verdict:

```json
{
  "paper_id": "",
  "expected_product_source": "",
  "expected_epoch_status": "HAS_DATE | NOT_MENTIONED",
  "expected_dcb_status": "",
  "expected_gate_status": "PASS",
  "expected_admission_status": "PASS | PASS_WITH_CORRECTION",
  "must_not_have_wrong_support": true,
  "must_have_reproduction_blockers": true,
  "must_have_valid_quote_ids": true
}
```

每次新 release → 运行全部 goldens → 全 PASS 才冻结。

**当前状态:**
- v0.3 baseline: 17 golden verdicts, 54/54 regression checks (archived)
- v1.0 full: **goldens 不存在** — 107-paper regression suite 待建立

---

## 十五、Do / Do Not

### DO

- build quote_bank first
- audit support, not just quote existence
- preserve corrections in correction layer
- preserve manual review queue
- stop on circuit breaker
- use phased expansion
- cite evidence by quote_id
- record old_value, new_value, reason for every correction
- regression test before every release freeze
- fix NOT_MENTIONED titles before consolidation freeze
- keep writing assets in sync with corpus counts

### DO NOT

- let LLM invent quote text
- use publication year as experiment epoch
- merge MIXED_PRODUCTS into BDS3_B2B core
- silently overwrite corrected fields
- delete unresolved evidence to pass validation
- run full expansion without phase gates
- modify frozen releases
- skip quote_bank or evidence support audit
- mark PASS_WITH_CORRECTION as clean PASS
- claim 107-paper regression coverage when only 17 golden verdicts exist
- merge NOT_MENTIONED-title papers during dedup

---

## 十六、Known Gaps (v1.0 → v2.0 roadmap)

以下缺口**不阻止 v2.0 SKILL freeze**，但必须在 thesis 或后续 release 中 acknowledge:

| # | Gap | Severity | Plan |
|---|-----|----------|------|
| G1 | CNES_OR_OTHER_RTS taxonomy 未细化 | MEDIUM | v1.1 或 thesis limitation |
| G2 | 107-paper regression goldens 不存在 | HIGH | 需生成 golden verdicts for all 107 |
| G3 | Full evidence audit 仅在 v0.3 (37篇) 完成 | HIGH | 剩余 70 篇需补充 audit |
| G4 | 部分论文仅有 classification pass，非 full extraction | MEDIUM | mathematical_model 等字段待补全 |
| G5 | v1.0 7 maps 仅在 37 篇 baseline 上生成 | MEDIUM | 需在 107 篇上重新生成 |
| G6 | 无自动化 CI pipeline — consolidation 为手工脚本 | LOW | 可接受，107 篇规模可控 |

---

## 十七、Acceptance Criteria

SKILL.md v2.0 生效条件：

- [x] v1.0 baseline (107 papers) 已写入
- [x] 9 HARD RULES 已保留
- [x] 5 SHOULD RULES 已保留
- [x] 7-phase pipeline 已保留并标注 v1.0 覆盖缺口
- [x] v1.0 product source distribution 已写入
- [x] NOT_MENTIONED dedup bug + fix 已写入
- [x] 172→107 consolidation history 已写入
- [x] Writing assets (13/13) 已索引
- [x] v0.3 archived baseline 已降级为历史记录
- [x] Known gaps (G1–G6) 已显式列出
- [x] "37 papers 是当前 corpus" **已删除**
- [x] "54/54 goldens 覆盖 107 篇" **未声称**
- [x] classification pass ≠ full extraction pass **已区分**
- [x] Taxonomy refinement 标记为 open item，非 completed

---

## Version History

| Version | Date | Baseline | Papers | Status |
|---------|------|----------|--------|--------|
| 1.0 | 2026-05-24 | corpus_grounded_v0.3 | 37 | ARCHIVED |
| **2.0** | **2026-05-25** | **corpus_grounded_v1.0** | **107** | **PRODUCTION** |
