# Semantic Correction Report

生成时间：2026-05-21  
方法：Targeted Semantic Correction — 仅修正 Evidence Support Audit 已证明错误的字段

---

## 1. 修改内容

### Ge Yulong 2024

| 字段 | Old Value | New Value | 原因 |
|------|----------|-----------|------|
| `product_source.actual_product_source` | `BDS3_PPP_B2B_BROADCAST` | `MIXED_PRODUCTS` | Evidence audit 发现 4 条 WRONG_SUPPORT：quote 指向 CNES、final products、ultra-rapid — 非纯 B2b |
| `product_source.conflict_flag` | `false` | `true` | claimed (B2b service) 与 actual (MIXED_PRODUCTS) 现存在冲突 |

**证据引用**：
- "We collected 29 days of experimental data and compared it with the Centre National d'Etudes Spatiales (CNES) real-time products" — 提及 CNES
- "The CNES real-time products were received and recovered by BNC software" — 使用 CNES via BNC
- "Final products and ultra-rapid products released from Wuhan university were downloaded from ftp://" — 使用 final products
- "Then, time transfer based on BDS-3, GPS, and BDS-3/GPS PPP was investigated" — 多系统（MIXED）

来源：`research_kb/reports/evidence_support_audit.md` §Ge_yulong

### Maosen Hao 2020

**无修改** — PASS_WITH_WEAK_EVIDENCE，语义字段保持不变。

### Ruohua Lan 2022

**无修改** — PASS_WITH_WEAK_EVIDENCE，语义字段保持不变。

---

## 2. 未修改字段确认

| 字段 | Ge Yulong | Maosen Hao | Ruohua Lan |
|------|----------|-----------|-----------|
| experiment_epoch | 未修改 | 未修改 | 未修改 |
| novelty_grade | 未修改 | 未修改 | 未修改 |
| reproduction_blockers | 未修改 | 未修改 | 未修改 |
| dcb_missing_flag | 未修改 | 未修改 | 未修改 |
| mathematical_model | 未修改 | 未修改 | 未修改 |
| datasets | 未修改 | 未修改 | 未修改 |
| metrics | 未修改 | 未修改 | 未修改 |
| main_results | 未修改 | 未修改 | 未修改 |

**语义字段修改总数：2**（仅 Ge Yulong product_source）

---

## 3. Corrected Validate 结果

| 论文 | Status | Issues | Grounding |
|------|--------|--------|-----------|
| Ge Yulong | **PASS** | 5 | 0 grounding issues |
| Maosen Hao | **PASS** | 7 | 0 grounding issues |
| Ruohua Lan | **PASS** | 10 | 0 grounding issues |

**Overall: WARN**（非 grounding issues：reproduction 4, conflicting_evidence 3, domain 1, experiment_epoch 1）

---

## 4. Corpus Maps

| 文件 | 状态 | 论文数 |
|------|------|--------|
| technical_routes.yaml | ✅ | 3 |
| problem_evolution.yaml | ✅ | 3 |
| citation_graph.json | ✅ | 3 |
| method_lineage.yaml | ✅ | 3 |
| dataset_metric_index.yaml | ✅ | 3 |
| reproduction_index.yaml | ✅ | 3 |

---

## 5. Manual Review Queue

13 items in `manual_review_queue.yaml`：

| Reason | Count |
|--------|-------|
| unresolved_evidence | 8 |
| keyword_overlap_low_confidence | 5 |

建议：在进入正式知识库前逐条确认或替换。

---

## 6. Corpus Index 状态

| 论文 | Status |
|------|--------|
| Ge Yulong 2024 | **PASS_WITH_CORRECTION** |
| Maosen Hao 2020 | **PASS_WITH_WEAK_EVIDENCE** |
| Ruohua Lan 2022 | **PASS_WITH_WEAK_EVIDENCE** |

---

## 7. 结论

- 3/3 论文通过 validate，可进入 corpus maps
- Ge Yulong product_source 已从 BDS3_PPP_B2B_BROADCAST 修正为 MIXED_PRODUCTS
- Maosen Hao 和 Ruohua Lan 保持原有语义字段不变
- 13 items 需人工审核（manual_review_queue.yaml）
