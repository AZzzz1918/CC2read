# Pilot Failure Analysis — Maosen Hao 2020 QZSS CLAS

Date: 2026-05-20
Paper: Maosen_Hao_2020_pppperformanceevaluationofqzsscentimeterlevelaugmentationser
Status: FAILED_VALIDATION (44/120 invalid grounding_quotes = 36.7%)

---

## 1. 为什么 44/120 grounding_quotes 无法匹配？

### Root Cause 1 (主因): PDF 文本提取产生粘合词 (run-together words)

`danielmiessler-pdf` skill 提取的 Markdown 中，PDF 行末断词处的空格会丢失，导致相邻单词粘连。

**证据：**

| DeepSeek 生成的 quote | Markdown 中真实文本 | 问题 |
|---|---|---|
| `Real-time precise orbit recovery:` | `Real-timepreciseorbitrecovery:` | 单词粘连，无空格 |
| `Real-time precise clock error recovery:` | `Real-timepreciseclockerrorrecovery:` | 单词粘连，无空格 |
| `the correction parameter C and C in QZSS are zero` | `the correction parameterC andC in QZSS are zero` | 部分粘连 |
| `the dual-frequency PPP performance of the augmented service is evaluated.` | `the dual-frequencyPPPperformanceoftheaugmentedserviceisevaluated.` | 全部粘连 |
| `the clock offset precision is about 0.46m, the radial average precision is about 0.26m` | `the clock offset precision is about 0.46m, the radial average precisionisabout 0.26m` | 部分粘连 |
| `SISURE precision is about 0.62m` | `SISURE precisionisabout 0.62m` | 部分粘连 |

**机制链：**
1. PDF 内部没有空格字符，视觉上的空格是排版位置偏移
2. `danielmiessler-pdf` 提取文本时，行末断词处的空格不保留
3. DeepSeek 收到粘连文本后，语义理解正确，但在"引用"时自动补回空格
4. 补回空格的 "quote" 不是 Markdown 原文的 exact substring
5. `_normalize_whitespace()` 只能合并多余空白，无法补回缺失空白 → 匹配失败

### Root Cause 2 (次因): DeepSeek 改写 quote

即使不考虑粘连词问题，DeepSeek 也会改写 quote：
- 缩短：`QZSS mainly releases augmented information in the form of RTCM-SSR, including correction information` → 原文是 `includingcorrectioninformationofsatelliteorbitandclockerror,phasebias,code bias, ionosphere, etc.`
- 标准化标点：ASCII/U+200B/U+FEFF 等不可见字符被模型"清理"
- 合并句子：多个不连续片段被拼接成一条 quote

**但最关键的是：DeepSeek 是语言模型，不是字符串拷贝工具。** 即使 temperature=0.1，它也会对文本做微小"修正"。系统 prompt 要求"exact substring"，但模型本质上做不到。

### Root Cause 3 (再次因): 粘连词的 quote 即使在 normalize 后也不匹配

当前 `_normalize_whitespace` 实现：
```python
re.sub(r"\s+", " ", text).strip()
```
只能压缩多余空白→单个空格。面对 `Real-timepreciseorbitrecovery:`（无空格），它不改动任何字符。而 DeepSeek quote `Real-time precise orbit recovery:` normalize 后是 `Real-time precise orbit recovery:`。两者不匹配。

### Root Cause 4: merge 阶段把 quote 差异变成 conflicting_evidence

`merge_paper_chunks.py` 的 `_deep_merge` 对不同 chunk 的同一字段，如果值不同就标记 CONFLICTING_EVIDENCE，但**不去重、不优选、不验证**。同一句话在不同 chunk 中被 DeepSeek 改写为略有不同的 quote，merge 后全部堆积在 conflicting_evidence 中（本论文共产生 200+ 条 conflicting_evidence，绝大多数是 quote 措辞差异而非实质矛盾）。

---

## 2. 为什么 QZSS CLAS 被错误关联到 PPP-B2b？

### 结论：本论文的 `actual` 字段实际上是正确的（NON_B2B_EXTERNAL_PRODUCTS）

重新审查 pilot paper JSON：
```json
"product_source": {
  "claimed": "QZSS CLAS L6 augmentation signal",
  "actual": "NON_B2B_EXTERNAL_PRODUCTS",
  "conflict_flag": false
}
```

**classification 方向正确，但存在以下问题：**

### 问题 2a: Schema 缺少 QZSS_CLAS 枚举值

当前 `product_source.actual` 枚举：
```
BDS3_PPP_B2B_BROADCAST | IGS_RTS_OR_CLK93 | CNES_OR_OTHER_RTS |
POST_PROCESSED_FINAL_PRODUCTS | NON_B2B_EXTERNAL_PRODUCTS |
MIXED_PRODUCTS | NOT_MENTIONED
```

QZSS CLAS 被归入模糊的 `NON_B2B_EXTERNAL_PRODUCTS`，无法区分 QZSS CLAS、QZSS MADOCA、SBAS、RTK/NTRIP 等不同服务。

### 问题 2b: 缺少 `domain_relevance` 字段

无法表达"这篇论文虽然不是 PPP-B2b 核心论文，但作为实时 SSR 服务的对照实验仍有参考价值"这一信息。

### 问题 2c: `conflict_flag=false` 的语义模糊

当前 validate_kb.py 认为 `claimed ≠ actual` 就应该设置 conflict_flag。但对于 QZSS CLAS 这种正确归类为非 B2B 的论文，claimed 和 actual 本来就不同，不应视为 conflict。正确的逻辑是：`conflict_flag` 应该标记 **标题/摘要声称 PPP-B2b 但实验使用非 B2B 产品** 的情况，而不是标记正常分类差异。

### 问题 2d: validate_kb.py 缺少非 B2B 产品检测

没有检测：
- 正文出现 "QZSS CLAS" / "CLAS" / "L6D" / "L6E" → 不得标为 BDS3_PPP_B2B_BROADCAST
- 正文出现 "MADOCA" → 不得标为 BDS3_PPP_B2B_BROADCAST
- 正文出现 "SBAS" / "WAAS" / "EGNOS" → 不得标为 BDS3_PPP_B2B_BROADCAST

---

## 3. 为什么 reproduction_blockers 漏报？

### 分析：DeepSeek 实际抽取了 reproduction_blockers，但存在三个问题

### 问题 3a: 重复/冗余

Merge 阶段把所有 chunk 的 blockers 全部拼接，产生 35+ 条冗余项：
```
"No stochastic model parameters provided"     ← 出现 3 次变体
"No Kalman filter configuration given"       ← 出现 3 次变体
"No code or processing software described"   ← 出现 5 次变体
```

### 问题 3b: 用自然语言而非结构化字段

DeepSeek 把 blockers 写成自由文本，没有与 reproducibility_audit 的 10 个结构化字段（stochastic_model_params、kalman_filter_config 等）对应。validate_kb.py 的 `check_reproduction_blockers` 检查这 10 个字段是否为 NOT_MENTIONED，发现 6 项缺失但 blockers 列表中没有一一对应的条目，于是报 `repro:missing_not_blocked`。

### 问题 3c: score 计算逻辑不一致

当前 paper JSON 中 `reproducibility_score = 0`（合理，因为几乎没有可复现信息）。但 validate_kb.py 计算 `expected_score = 10 - 6 = 4`, 并报 `score_inconsistent`。**validator 的 expected_score 公式过于简单**：它假设每项权重相同，但 code_repository=NOT_MENTIONED 和 metric_definitions=NOT_MENTIONED 对复现的影响完全不同。

### 问题 3d: validate_kb.py 对 reproduction_blockers 的检测规则正确但执行效果差

`check_reproduction_blockers()` 检测逻辑本身是正确的：
1. 检查 10 项是否 NOT_MENTIONED
2. 缺失且不在 blockers 中的 → 报 `repro:missing_not_blocked`
3. blockers 为空但 ≥5 项缺失 → 报 `repro:blockers_empty_but_X_items_missing`

问题在于 merge 阶段把 blockers 列表变成了无结构的自然语言 dump，validator 无法精确匹配。

---

## 4. 综合根因总结

| # | 问题 | 根因 | 层级 |
|---|------|------|------|
| 1 | 44/120 unmatched quotes | PDF 文本粘连 + DeepSeek 补空格 → 非 exact substring | PDF 提取 + LLM 边界 |
| 2 | Quote 无法 repair | 当前无 repair 机制，直接失败 | Pipeline 缺失 |
| 3 | QZSS 分类模糊 | Schema 缺少 QZSS_CLAS 等枚举 | Schema 设计 |
| 4 | product_source conflict_flag 语义错误 | Validator 认为 claimed≠actual 即 conflict | 校验逻辑 |
| 5 | 200+ conflicting_evidence 噪音 | Merge 不区分语义差异和措辞差异 | Merge 逻辑 |
| 6 | reproduction_blockers 冗余 | Merge 不做去重和结构化 | Merge + Schema |
| 7 | Score 计算不一致 | Validator 使用简单线性公式 | 校验逻辑 |
| 8 | validate_kb.py 不阻止失败论文 | 即使 44/120 quotes 失败，状态仍是 CRITICAL 而非 BLOCKED | 校验门槛 |
