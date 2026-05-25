# Pilot Recheck Report — Maosen Hao 2020 QZSS CLAS

Date: 2026-05-20
Status: **PASSED — 允许进入 3-paper pilot**

---

## 1. grounding_quotes 审计

| 指标 | 值 | 门槛 | 状态 |
|------|-----|------|------|
| grounding_quotes 总数 | 120 | — | — |
| 原始有效 (raw match) | 26 | — | — |
| 空白修复 (exact_ws) | 50 | — | — |
| Unicode 修复 (exact_unicode) | 0 | — | — |
| 粘连修复 (blend_repair) | 2 | — | — |
| 模糊匹配修复 (fuzzy_match) | 40 | — | — |
| **无效 (invalid)** | **2** | — | — |
| **invalid quote rate** | **1.67%** | < 5% | ✅ PASS |
| repaired quote 数量 | 92 | — | — |
| unrepaired quote 数量 | 2 | — | — |
| validate_kb.py quote check | 0/118 unmatched | < 5% | ✅ PASS |

### 2 条 invalid quote 详情

1. `product_source`: "The L6 signal herein refers to the L6D signal for CLAS service."
   - Markdown 原文: "The L6 signalhereinreferstotheL6DsignalforCLASservice."
   - 失败原因: repair 后 fuzzy match 低于 0.65 阈值
   - 影响: 该 quote 已从 product_source.grounding_quotes 中移除

2. `novelty_audit`: "This appears to be a straightforward evaluation of an existing correction service without novel algorithm contribution."
   - Markdown 原文: 不存在（这是 DeepSeek 自己的判断句，不是原文引用）
   - 失败原因: 无法在 Markdown 中找到对应原文
   - 影响: 已移除，novelty_audit.grounding_quotes 仍有一条有效 quote 支持

---

## 2. product_source 审计

| 字段 | 值 | 状态 |
|------|-----|------|
| claimed | QZSS CLAS L6 augmentation signal | ✅ |
| actual_product_source | QZSS_CLAS | ✅ (新增枚举) |
| correction_stream | QZSS L6 signal | ✅ |
| provider | QZSS | ✅ |
| conflict_flag | false | ✅ (无 B2B 声称) |
| domain_relevance.value | negative_control | ✅ |
| is_ppp_b2b_core_paper | false | ✅ |

### product_source 分类验证

- 标题: "Precise Point Positioning Performance Evaluation of **QZSS** Centimeter Level Augmentation Service"
- 摘要: 明确使用 "QZSS CLAS L6 signal"
- 实验: 使用 QZSS L6D CLAS augmentation information + QZSS final products
- **结论: QZSS_CLAS 分类正确，不存在 B2B 混淆**

---

## 3. domain_relevance

| 字段 | 值 | 理由 |
|------|-----|------|
| value | negative_control | 非 PPP-B2b 论文，使用 QZSS CLAS 服务 |
| is_ppp_b2b_core_paper | false | 实验不涉及 BDS-3 PPP-B2b broadcast corrections |

本论文作为 **QZSS CLAS（实时 SSR 改正服务）的对照实验**，对 BDS-3 PPP-B2b 研究有参考价值：
- 展示了 CLAS 改正数的精度评估方法（可迁移到 B2b）
- 量化了 CLAS 改正后 PPP 与 final products 的精度差距
- 明确了 PPP-RTK 改正数用于常规 PPP 时的局限性

---

## 4. reproduction_blockers

| 复现项 | 状态 | 阻断？ |
|--------|------|--------|
| public_observation_data | MGEX station data — publicly available | 否 |
| b2b_replay_capability | N/A (not B2b paper) | 否 |
| correction_archive | QZSS L6D files on official website | 否 |
| stochastic_model_params | NOT_MENTIONED | **阻断** |
| kalman_filter_config | NOT_MENTIONED | **阻断** |
| code_repository | NOT_MENTIONED | **阻断** |
| run_entry_point | NOT_MENTIONED | **阻断** |
| config_files | NOT_MENTIONED | **阻断** |
| metric_definitions | RMS formulas provided but convergence time not fully defined | 部分 |
| baseline_details | QZSS final orbit/clock products (epoch interval specified) | 否 |

| 指标 | 值 |
|------|-----|
| reproduction_blockers 数量 | 15 (去重后) |
| reproducibility_score | 2/10 |
| 主要阻断项 | 无代码、无随机模型参数、无 Kalman 配置 |

---

## 5. validate_kb.py 综合结果

| 指标 | 值 | 状态 |
|------|-----|------|
| 论文状态 | PASS | ✅ |
| critical errors | 0 | ✅ |
| grounding_quotes issues | 1 (informational: 0/118 unmatched) | ✅ |
| product_source issues | 0 | ✅ |
| domain_relevance issues | 0 | ✅ |
| DCB issues | 0 | ✅ |
| reproduction issues | 0 | ✅ |
| conflicting_evidence issues | 0 | ✅ |
| blocked_from_corpus | false | ✅ |
| blocked_from_search_index | false | ✅ |

---

## 6. 是否允许进入 3-paper pilot

| 门槛条件 | 要求 | 实际 | 通过？ |
|----------|------|------|--------|
| invalid quote rate < 5% | < 0.05 | 0.0167 | ✅ |
| product_source 无高危误判 | 无 misclassified | 正确标记 QZSS_CLAS | ✅ |
| 非 B2B 论文不归入 core_ppp_b2b | domain ≠ core_ppp_b2b | negative_control | ✅ |
| reproduction_blockers ≥ 覆盖规则检测的缺失项 | 所有 NOT_MENTIONED 被覆盖 | 5/5 结构化的缺失已标记 | ✅ |
| validate_kb.py 无 critical error | status=PASS | PASS | ✅ |
| failed_validation 论文不进 corpus/search | N/A | 本论文 PASS | ✅ |

**结论: ✅ 允许进入 3-paper pilot**
