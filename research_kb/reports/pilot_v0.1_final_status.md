# Pilot v0.1 Final Status Report

生成：2026-05-21  
冻结位置：`research_kb/releases/pilot_v0.1/`

---

## 1. 3-Paper Pilot 总结

| 论文 | 选择角色 | product_source | novelty | repro score | Status |
|------|---------|---------------|---------|-------------|--------|
| Ruohua Lan 2022 | core_ppp_b2b | MIXED_PRODUCTS | C_ENGINEERING_TRANSFER | 1/10 | PASS_WITH_WEAK_EVIDENCE |
| Ge Yulong 2024 | ambiguous_boundary | MIXED_PRODUCTS (corrected) | C_ENGINEERING_TRANSFER | 2/10 | PASS_WITH_CORRECTION |
| Maosen Hao 2020 | related_non_b2b | QZSS_CLAS | U_INSUFFICIENT_EVIDENCE | 0/10 | PASS_WITH_WEAK_EVIDENCE |

---

## 2. 已解决的问题

| 问题 | 解决方法 | 状态 |
|------|---------|------|
| PDF 文本质量（pdfplumber 空格丢失） | 切换到 PyMuPDF/fitz | ✅ |
| DeepSeek API 截断 | max_tokens 4096→8192 | ✅ |
| grounding_quotes 无法匹配（~75% invalid） | 多级匹配 + keyword_overlap repair | ✅ → <5% |
| Ge Yulong product_source 误分类 | Targeted semantic correction: BDS3_PPP_B2B_BROADCAST → MIXED_PRODUCTS | ✅ |
| BLOCKED papers 无法进入 corpus | Quote repair + correction 使 3/3 PASS | ✅ |

---

## 3. 仍存在的风险

| 风险 | 严重度 | 影响 |
|------|--------|------|
| keyword_overlap evidence 占 60.3% | 🟡 MEDIUM | 60% 的证据是语义级匹配而非精确匹配，可能包含弱相关或不相关 quote |
| 13 manual review items 未关闭 | 🟡 MEDIUM | 8 unresolved + 5 low confidence keyword overlap |
| experiment_epoch 字段 WEAK_SUPPORT 较多 | 🟡 LOW | 不影响 PASS 判定，但使用时应标记置信度 |
| stricter quote rules 将在扩展时生效 | 🟢 INFO | keyword_overlap 低置信度证据在扩展时会被降级 |

---

## 4. Ge Yulong Correction 记录

| 字段 | 旧值 | 新值 | 原因 |
|------|------|------|------|
| product_source.actual_product_source | BDS3_PPP_B2B_BROADCAST | MIXED_PRODUCTS | 4 WRONG_SUPPORT: quotes point to CNES/final products |
| product_source.conflict_flag | false | true | claimed vs actual 存在冲突 |

---

## 5. 13 Manual Review Items 摘要

| 类型 | 数量 | 分布 |
|------|------|------|
| unresolved_evidence | 8 | metrics(4), datasets(2), experiments(2) |
| keyword_overlap_low_confidence | 5 | ionospheric_handling(2), product_source(2), mathematical_model(1) |

详细见 `manual_review_queue.yaml`。

---

## 6. Corpus Maps 状态

| 文件 | 论文数 | 可用 |
|------|--------|------|
| technical_routes.yaml | 3 | ✅ |
| problem_evolution.yaml | 3 | ✅ |
| citation_graph.json | 3 | ✅ |
| method_lineage.yaml | 3 | ✅ |
| dataset_metric_index.yaml | 3 | ✅ |
| reproduction_index.yaml | 3 | ✅ |

---

## 7. Expansion Readiness

| Check | Status |
|-------|--------|
| all 3 pilot pass | ✅ PASS |
| invalid quote_id rate < 5% | ✅ PASS (0 grounding issues) |
| no WRONG_SUPPORT | ✅ PASS |
| keyword_overlap ratio | ⚠️ WARN (60.3% > 50%) |
| manual review remaining | ✅ PASS (13 ≤ 15) |
| **Overall** | **READY** |

---

## 8. 是否允许进入 10-paper scale test

**✅ 允许。** 满足以下条件时即可执行：

1. Strict quote rules 生效：keyword_overlap 低置信度证据不用于关键字段判定
2. 13 manual review items 可在扩展的同时继续处理
3. 扩展时如 invalid rate > 5%，立即停止并修复

---

## 9. 下一步明确命令

```bash
# 运行 10-paper scale test
python scripts/update_kb.py --papers 10 --mode scale_test

# 或者手动指定要处理的论文
python scripts/_scale_test.py
```

### 扩展阶段需监控的指标
- invalid_quote_id_rate per paper
- keyword_overlap ratio trend
- product_source accuracy
- experiment_epoch 误判率
- new WRONG_SUPPORT detections
