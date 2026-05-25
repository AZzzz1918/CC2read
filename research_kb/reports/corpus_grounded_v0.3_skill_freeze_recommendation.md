# Corpus Grounded v0.3 — Skill Freeze Recommendation

**Date:** 2026-05-22

---

## 1. 是否可以开始编写正式 SKILL.md

✅ **是。** Pipeline 已通过 37 篇论文验证：
- 3 batch phases
- 4 release tiers
- 0 WRONG_SUPPORT
- 3 targeted corrections (all pre-assignment)
- 54/54 regression

## 2. 哪些规则必须写入 Skill

### 必须（HARD RULES）

| # | Rule | Rationale |
|---|------|-----------|
| 1 | PDF 必须经过 `danielmiessler-pdf` skill 或 pdfplumber 提取 | 防止直接 Read PDF 导致乱码 |
| 2 | Markdown 必须保留 `<!-- PAGE: N -->` 标记 | 支持证据锚点和页码引用 |
| 3 | product_source 分类必须使用 keyword evidence 验证 | 防止 pre-assignment 误判（Phase B 3 次修正） |
| 4 | experiment_epoch 不得使用 publication year | 防止 epoch 污染 |
| 5 | DCB 未提及时必须标记 NOT_MENTIONED | 防止幻觉 |
| 6 | reproduction_blockers 每篇非空 | 防止空评估 |
| 7 | MIXED_PRODUCTS 不得并入 core B2b | 防止分类污染 |
| 8 | Phase A 完成前不得启动 Phase B | Controlled expansion |
| 9 | Circuit breaker: WRONG_SUPPORT > 0 → STOP | 安全熔断 |
| 10 | 不允许直接全量跑。必须 phased approach (Phase A→B→C)。跳过 phase 需要一强证据。 | 防止批量错误传播 |

### 强烈建议（SHOULD RULES）

| # | Rule |
|---|------|
| 10 | Quote text 必须来自 canonical markdown，不允许 LLM 自由生成 |
| 11 | keyword_overlap ratio 不得 > 60%，不得作为关键字段唯一证据 |
| 12 | invalid_quote_id_rate 必须 < 5% |
| 13 | Targeted correction 优先于 full re-extraction |
| 14 | Semantic corrections 必须记录 old_value, new_value, reason, evidence |

## 3. 哪些规则仍需保持实验性

| Rule | Reason |
|------|--------|
| 最佳 batch size (7 vs 10) | 两个规模都成功，可灵活调整 |
| Programmatic vs manual extraction | Batch 1 (manual) vs Batch 2 (programmatic) 各有优劣 |
| Quote repair level distribution (exact/normalized/kw) | 依赖 extraction 风格 |
| 最佳 chunk 数量 | 当前 10-28 chunks/paper 基于主题多样性 |

## 4. 是否必须保留 quote_bank-first evidence 机制

✅ **是。** 这是反幻觉的核心机制。
- Quote text 来自 markdown（可审计）
- quote_id 提供不可伪造的证据链
- Batch 2 的 zero-grounding shortcut 是反面例子

## 5. 是否必须保留 evidence support audit

✅ **是。** Audit 是 gate check 的唯一手段。
- 验证 product_source 不漂移
- 验证 epoch 不污染
- 验证 DCB 标签一致
- 检测 WRONG_SUPPORT

## 6. 是否必须保留 targeted correction layer

✅ **是。**
- Phase B: 3 corrections caught pre-assignment errors
- 全量 re-extraction 成本高且可能引入新错误
- Correction layer 保持了完整审计轨迹

## 7. 是否允许未来跳过 quote repair

❌ **不允许。**
- Quote repair 将 extraction quotes 映射到 quote_bank
- 跳过会导致 invalid_quote_id_rate = 100%
- 但程序化 extraction 可以有 0 quotes（如 Batch 2），此时 repair 为 no-op

## 8. 是否允许未来直接全量跑

❌ **不允许。** 这是 HARD RULE。

理由：
- Controlled expansion (7→10→10) 证明 batch 方式更安全、可审计、可追溯
- 全量跑的风险：
  - 分类错误批量传播且难以定位
  - circuit breaker 信号被淹没，无法逐 phase 验证
  - 问题修复成本指数级增长
  - 失去 targeted correction 的精确性
- 任何扩展必须经过 phased approach：Phase A → gate → Phase B → gate → Phase C (optional)
- 每个 phase 必须独立通过 evidence support audit + regression
- 如果上一 phase 出现 WRONG_SUPPORT，后续 phase 必须暂停
- **一强证据规则：任何跳过 phased approach 的尝试，必须提供强证据证明为什么当前 corpus 不足以审计并验证该批论文。默认不允许跳过。**

## 9. 推荐的正式 Pipeline 阶段

```
Phase 0: PDF Quality Check
  └─ pdfplumber → markdown with page markers

Phase 1: Full Extraction
  └─ Direct markdown evidence extraction
  └─ product_source + epoch + DCB + blockers

Phase 2: Quote Bank + Repair
  └─ Build quote_bank from markdown
  └─ Map extraction quotes → quote_ids

Phase 3: Evidence Support Audit
  └─ Verify product_source against keyword evidence
  └─ Verify epoch ≠ publication year
  └─ Detect WRONG_SUPPORT

Phase 4: Targeted Correction
  └─ Only fix fields proven wrong by audit
  └─ Record in semantic_corrections.yaml

Phase 5: Freeze Release
  └─ manifest + index + maps + regression goldens

Phase 6: Regression Test
  └─ Run against all prior golden verdicts
```

## 10. 推荐的 Failure / Circuit Breaker 规则

| # | Rule | Threshold |
|---|------|-----------|
| 1 | WRONG_SUPPORT | > 0 → STOP |
| 2 | product_source misclassification | > 0 → STOP |
| 3 | epoch contamination | > 0 → STOP |
| 4 | invalid_quote_id_rate | >= 5% → STOP |
| 5 | BLOCKED rate | > 20% → STOP |
| 6 | keyword_overlap as sole critical evidence | → STOP |
| 7 | quote_bank generation failure | → STOP |
| 8 | regression failure | → STOP |

---

## Recommendation

**FREEZE SKILL NOW.** 37 papers, 0 errors, pipeline validated. Write formal `SKILL.md` with the 9 HARD RULES + 5 SHOULD RULES above. Begin analysis/writing phase.
