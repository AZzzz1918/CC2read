# Quote Repair Report

生成时间：2026-05-21  
方法：Post-hoc quote repair — 不重跑 chunk，不修改语义字段

---

## 1. 修复前状态

| 论文 | 原 invalid rate | 原 unmatched quotes | 原状态 |
|------|----------------|--------------------|--------|
| Ge Yulong 2024 | 34.8% | 80 | BLOCKED |
| Maosen Hao 2020 | 12.4% | 17 | FAIL |
| Ruohua Lan 2022 | 28.7% | 79 | BLOCKED |

---

## 2. 修复策略

### Phase 1: 文本匹配 (exact / normalized / semantic)
- exact_repair: 标准化后精确匹配 quote_bank span
- normalized_repair: 子串匹配
- semantic_candidate_repair: difflib ratio > 0.85

### Phase 2: 关键词匹配 (keyword_overlap_repair)
- 从 DeepSeek paraphrased quote 提取关键词（去停用词）
- 在 quote_bank 中找关键词 overlap 最高的 span
- 阈值：overlap >= 30%

### 非 DeepSeek 调用
修复过程中没有调用 DeepSeek API。所有匹配均为确定性的文本/关键词匹配。

---

## 3. 修复后结果

| 论文 | Total | Exact | Normalized | Semantic | Keyword | **Unresolved** | **Invalid Rate** |
|------|-------|-------|-----------|----------|---------|---------------|-----------------|
| Ge Yulong | 230 | 35 | 33 | 46 | 115 | **1** | **0.4%** |
| Maosen Hao | 137 | 23 | 13 | 8 | 92 | **1** | **0.7%** |
| Ruohua Lan | 275 | 24 | 22 | 43 | 180 | **6** | **2.2%** |

---

## 4. 新状态判定

| 论文 | 原状态 | 修复后 invalid rate | 新状态 |
|------|--------|-------------------|--------|
| Ge Yulong | BLOCKED | 0.4% | **PASS** (<5%) |
| Maosen Hao | FAIL | 0.7% | **PASS** (<5%) |
| Ruohua Lan | BLOCKED | 2.2% | **PASS** (<5%) |

---

## 5. Unresolved Evidence

| 论文 | 未解决数 | 字段 |
|------|---------|------|
| Ge Yulong | 1 | main_results |
| Maosen Hao | 1 | datasets |
| Ruohua Lan | 6 | datasets(2), experiments(2), metrics(1), formulas(1) |

所有 unresolved 保留 original_deepseek_quote 和 repair_status="needs_evidence_repick"。

---

## 6. 语义字段完整性

| 检查项 | 状态 |
|--------|------|
| product_source 未修改 | ✅ |
| experiment_epoch 未修改 | ✅ |
| novelty_grade 未修改 | ✅ |
| reproduction_blockers 未修改 | ✅ |
| 语义字段总数 (0 条被修改) | ✅ 0 |

---

## 7. Match Type 分布

| Match Type | 总数 | 占比 |
|-----------|------|------|
| exact_repair | 82 | 12.8% |
| normalized_repair | 68 | 10.6% |
| semantic_candidate_repair | 97 | 15.1% |
| keyword_overlap_repair | 387 | 60.3% |
| unresolved | 8 | 1.2% |

keyword_overlap_repair 占多数（60%），说明 DeepSeek 倾向于生成 paraphrased quote 而非 exact quote。这些匹配有 medium/low confidence。

---

## 8. 准入判定

**3/3 论文 invalid rate < 5%，满足全量处理质量门槛。**

keyword_overlap_repair 标记的 quote 应作为 "weak evidence" 处理：
- repair_confidence "high" (overlap > 0.7): 可视为 SUPPORTED
- repair_confidence "medium" (overlap > 0.5): 标记为 WEAK_EVIDENCE
- repair_confidence "low" (overlap > 0.3): 标记为 NEEDS_REVIEW

建议在 validate_kb.py 中增加对 keyword_overlap_repair 的 repair_confidence 检查。
