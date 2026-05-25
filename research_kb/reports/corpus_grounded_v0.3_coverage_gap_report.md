# Corpus Grounded v0.3 — Coverage Gap Report

**Date:** 2026-05-22

---

## Gap Assessment

### 1. Galileo HAS 独立类别

| 属性 | 值 |
|------|-----|
| Severity | **MEDIUM** |
| Affected analysis | product_source taxonomy 粒度不足 |
| Current state | 3 CNES_OR_OTHER_RTS papers (2 Galileo HAS + 1 general PPP) |
| Recommended action | 细分 CNES_OR_OTHER_RTS → GALILEO_HAS / NON_B2B_GENERAL_PPP |
| Phase C needed | NO — 通过 taxonomy refinement 解决，不需新论文 |
| Suggested candidate | N/A |

### 2. QZSS CLAS 覆盖

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | non-B2b augmentation 多样性 |
| Current state | 2 papers (Euiho Kim CLAS PPP, Taro Suzuki QZSS L6) |
| Recommended action | 当前 2 篇足够区分 B2b 与 non-B2b |
| Phase C needed | NO |
| Suggested candidate | N/A |

### 3. 中文高风险 PDF

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | extraction robustness, language diversity |
| Current state | 1 paper (Liu Wei 72-page thesis, 0 B2b mentions) |
| Recommended action | 当前 1 篇已验证 pipeline 可处理中文 PDF |
| Phase C needed | NO |
| Suggested candidate | N/A |

### 4. Single-Frequency PPP-B2b

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | frequency diversity in B2b evaluation |
| Current state | 1 paper (Single_Frequency_PPP_B2b_Time_Transfer) |
| Recommended action | 当前 1 篇 + Quad-Frequency 1 篇覆盖单频/多频 |
| Phase C needed | NO |

### 5. PPP-B2b Time Transfer 细分

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | time transfer application depth |
| Current state | 3 papers (Quad-Freq, Single-Freq, Comparative Broadcast) |
| Recommended action | 3 篇覆盖单频/四频/对比 |
| Phase C needed | NO |

### 6. Toolbox / Open-Source Implementation

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | reproducibility |
| Current state | 3 papers (GKit, NavDecoder, Lu SDR) |
| Recommended action | 2 decoder + 1 SDR 工具链覆盖充分 |
| Phase C needed | NO |

### 7. BDS3_B2B 占比过高

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | corpus balance |
| Current state | 25/37 (67.6%) BDS3_B2B |
| Recommended action | 预期结果 — 项目目标是 PPP-B2b 审计。边界和 non-B2b 论文用于防止分类漂移。 |
| Phase C needed | NO |

### 8. MIXED_PRODUCTS 边界验证

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | classification robustness |
| Current state | 7 papers with MIXED_PRODUCTS |
| Recommended action | 7 篇边界论文已充分验证 MIXED 分类规则 |
| Phase C needed | NO |

### 9. Difficult PDFs

| 属性 | 值 |
|------|-----|
| Severity | **LOW** |
| Affected analysis | extraction robustness |
| Current state | 1 Chinese thesis (72 pages, 49000+ chars) + multiple special-char filenames |
| Recommended action | Pipeline 已处理 special chars, large PDF, Chinese text |
| Phase C needed | NO |

### 10. 37 篇是否足够支持主线综述

| 属性 | 值 |
|------|-----|
| Severity | — |
| Affected analysis | overall project scope |
| Current state | 37 papers covering 2020-2025, 4 product categories, 8+ technical routes |
| Recommended action | **37 篇足够支持全面的 PPP-B2b 文献综述** |
| Phase C needed | **NO** |

---

## Summary

| Gap | Severity | Phase C Needed |
|-----|----------|----------------|
| Galileo HAS 独立类别 | MEDIUM | NO (taxonomy fix) |
| QZSS CLAS 覆盖 | LOW | NO |
| 中文 PDF | LOW | NO |
| Single-freq B2b | LOW | NO |
| Time transfer 细分 | LOW | NO |
| Toolbox | LOW | NO |
| B2b 占比过高 | LOW | NO |
| MIXED 边界 | LOW | NO |
| Difficult PDF | LOW | NO |
| 主线综述支持 | — | NO |

**结论：0 HIGH severity gaps。37 篇无需 Phase C 补充。**
