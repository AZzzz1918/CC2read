# Pilot 审计报告

生成时间：2026-05-20  
处理论文：3 篇（选文策略见附录）

---

## 1. 处理状态总览

| 论文 | Paper ID | 状态 | 页数 | Chunks | DeepSeek 成功 | DeepSeek 失败 |
|------|----------|------|------|--------|-------------|-------------|
| QZSS CLAS (对照) | Maosen_Hao_2020 | ✅ **完成** | 13 | 13 | 13/13 | 0 |
| BDS-3 PPP-B2b (明确) | Ruohua_Lan_2022 | ⏳ 部分 | 25 | 25 | ~18/25 | 1 (chunk_idx=3) |
| Galileo HAS+PPP-B2b (边界) | Wei_Haopeng_2024 | ⬜ 未开始 | 14 | 14 | — | — |

**处理中止原因**：Extraction 速度过慢（~3 小时仅 1/3 完成），API 调用频繁产生空响应和 JSON 截断，需先修复性能瓶颈。

---

## 2. PDF 解析质量

| 论文 | 页数 | 可提取页 | 不可提取页 | 页码标记完整性 |
|------|------|---------|-----------|-------------|
| Maosen_Hao_2020 | 13 | 13 | 0 | 13/13 ✓ |
| Ruohua_Lan_2022 | 25 | 25 | 0 | 25/25 ✓ |
| Wei_Haopeng_2024 | 14 | 14 | 0 | 14/14 ✓ |

**结论**：PDF 解析覆盖率 100%，无 OCR 需求。  
**已知问题**：pdfplumber 在部分 PDF 中合并单词（丢失词间空格），导致 quote 逐字匹配率下降。

---

## 3. Maosen Hao (QZSS CLAS) — 详细审计

### 3.1 product_source 判定

| 字段 | 值 | 证据 |
|------|-----|------|
| `claimed` | QZSS CLAS L6 augmentation signal | 论文正文明确描述 QZSS L6D CLAS 服务 |
| `actual` | **NON_B2B_EXTERNAL_PRODUCTS** ✓ | QZSS CLAS ≠ BDS-3 PPP-B2b，属于日本 QZSS 的 L6 增强服务 |
| `conflict_flag` | False | claimed 和 actual 无冲突——论文未声称使用 BDS-3 B2b |
| `grounding_quotes` | 23 条 | 从 markdown 中提取了 QZSS CLAS 相关原文 |

**审计结论**：✅ 正确。QZSS CLAS 未被误标为 BDS-3 PPP-B2b。product_source 分类准确。

### 3.2 experiment_epoch 判定

| 字段 | 值 |
|------|-----|
| `start_date` | 2019-09-15 |
| `end_date` | 2019-09-17 |
| `duration_days` | 3 |
| `is_publication_year_mistake` | False |
| `publication_year` | 2020 |

**审计结论**：✅ 实验时间（2019-09）≠ 出版年份（2020），epoch anchoring 正确。有 3 条 grounding_quotes 支撑。

### 3.3 DCB Handling 判定

| 字段 | 值 |
|------|-----|
| `dcb_source` | CLAS correction (code bias) and Code DCB correction |
| `dcb_missing_flag` | True |

**审计结论**：⚠️ DCB 处理被标记为缺失。论文描述使用 CLAS 改正信息中的 code bias 校正，但未明确 DCB 产品来源。

### 3.4 novelty_grade 判定

| 创新证据 | 值 |
|---------|-----|
| `audit_grade` | **U_INSUFFICIENT_EVIDENCE** |
| `novel_formula` | False |
| `novel_state_design` | False |
| `novel_stochastic_model` | False |
| `novel_qc_mechanism` | False |
| `novel_b2b_usage` | False |
| `is_mere_migration` | False |

**审计结论**：✅ 正确评估为“证据不足”。论文是标准的 QZSS CLAS PPP 性能评估，未声称重大创新。

### 3.5 reproduction_blockers

| 指标 | 值 |
|------|-----|
| `reproducibility_score` | 0/10 |
| `reproduction_blockers` 数量 | 50 条 |
| 关键阻断项 | 无公开数据、无代码、无模型参数、无滤波器配置、无 DCB 处理详情 |

**审计结论**：✅ 复现难度极高。50 条阻断项全面覆盖了论文的信息缺口。

---

## 4. JSON 校验结果

| 类别 | 数量 | 说明 |
|------|------|------|
| grounding_quotes unmatched | 44 | pdfplumber 空格丢失导致（非 DeepSeek 错误） |
| grounding_quotes missing | 0 | ✅ 所有有值字段都有 quote |
| product_source issues | 1 | 轻度 warning |
| experiment_epoch issues | 1 | 无关紧要的标记 |
| reproduction issues | 6 | ✅ 正确识别了信息缺失 |
| conflicting_evidence | 1 | 已标记 |
| **validate 状态** | **CRITICAL** | 仅因 unmatched quotes 触发 |

---

## 5. 全量处理门槛评估

| 条件 | 要求 | 现状 | 通过？ |
|------|------|------|--------|
| 3 篇全部生成 paper JSON | 3/3 | 1/3 | ❌ |
| ≥90% grounding_quotes 逐字匹配 | ≥90% | ~63%（44/120 unmatched） | ❌ |
| product_source 无高危误判 | 无 | ✅ Maosen Hao 正确 | ✅ |
| experiment_epoch 无 publication_year 误用 | 无 | ✅ 2019-09 ≠ 2020 | ✅ |
| reproduction_blockers 不为空且一致 | 不为空 | ✅ 50 条阻断项 | ✅ |
| validate_kb.py 无 critical error | 无 | ❌ grounding_quotes → CRITICAL | ❌ |
| unresolved_items.yaml 无阻断级问题 | 无 | ❌ 1 chunk 完全失败 | ❌ |

**结论：❌ 不满足全量处理条件，不建议进入全量处理。**

---

## 6. 必须修复的问题（按优先级）

### 6.1 🔴 高优先：PDF 文本提取质量 → quote 匹配失败

**问题**：pdfplumber 提取的文本丢失词间空格（如 "CentimeterLevelAugmentationService" 应为 "Centimeter Level Augmentation Service"），导致 DeepSeek 生成的 quote 无法在 markdown 中逐字匹配。44/120 quotes 无法验证。

**修复方案**：
- 换用 PyMuPDF (fitz) 做文本提取（空间保留更好）
- 或在 pdfplumber 输出后增加后处理步骤修复合并的词
- add fuzzy matching fallback: `difflib.SequenceMatcher` > 0.95

### 6.2 🔴 高优先：API 性能瓶颈

**问题**：
- ~40% API 调用返回空响应（0 chars）
- ~50% 返回截断 JSON（`Unterminated string` at last char position → `max_tokens=4096` 不够）
- 每个 chunk 平均需 2-3 次重试
- 52 chunks 预估需 5-6 小时

**修复方案**：
- `max_tokens` 从 4096 提升到 8192
- 减小 chunk 大小：MAX_CHUNK_CHARS 从 6000 降到 3000
- 添加 `max_tokens` 截断后 JSON 修复逻辑
- 考虑并行调用（异步 + 线程池）

### 6.3 🟡 中优先：unresolved_items 处理

**问题**：1 chunk (Ruohua_Lan_2022 chunk_index=3) 三次重试全部失败，需人工介入。

**修复方案**：
- 对失败的 chunk 减小文本长度后重试（重试时截断到前 2000 chars）
- 添加 `unresolved_items.yaml` 的自动 re-processing 功能

### 6.4 🟡 中优先：merge 阶段去重

**问题**：reproduction_blockers 包含 50 条，但存在语义重复（如 "No stochastic model parameters provided" 出现多次）。

**修复方案**：
- merge 阶段对字符串列表做语义去重（用 `difflib` 或简单的 similarity threshold）

---

## 7. 附录：选文策略

| 角色 | 论文 | 选择依据 |
|------|------|---------|
| BDS-3 PPP-B2b 明确 | Ruohua Lan 2022 — *Evaluation of BDS-3 B1C/B2b PPP Using PPP-B2b and RTS SSR* | 直接研究 PPP-B2b broadcast correction，对比 IGS RTS |
| 边界论文 | Wei Haopeng 2024 — *Combining Galileo HAS and Beidou PPP-B2b with Helmert* | 标题含 PPP-B2b + Galileo HAS，混合产品源高风险 |
| 非 B2b 对照 | Maosen Hao 2020 — *QZSS CLAS PPP Performance Evaluation* | QZSS L6 CLAS，非 BDS-3，应被标为 NON_B2B_EXTERNAL_PRODUCTS |

### 已验证的反幻觉能力

| 能力 | Maosen Hao 结果 |
|------|---------------|
| product_source 区分 B2b vs 非 B2b | ✅ QZSS CLAS → NON_B2B_EXTERNAL_PRODUCTS |
| experiment_epoch ≠ publication_year | ✅ 2019-09 ≠ 2020 |
| novelty 不夸大 | ✅ U_INSUFFICIENT_EVIDENCE |
| reproduction_blockers 严格 | ✅ 50 条阻断项，score=0 |
| DCB 缺失检测 | ✅ dcb_missing_flag=True |
