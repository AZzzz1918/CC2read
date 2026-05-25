# Evidence Support Audit Report

生成时间：2026-05-21

## 1. 总体 Match Type 分布

| Match Type | Count | Pct |
|-----------|-------|-----|
| keyword_overlap_repair | 387 | 60.3% |
| semantic_candidate_repair | 97 | 15.1% |
| exact_repair | 81 | 12.6% |
| normalized_repair | 63 | 9.8% |
| unresolved | 8 | 1.2% |
| normalized_repair_v2 | 5 | 0.8% |
| exact_repair_v2 | 1 | 0.2% |

## 2. 总体 Support Status 分布

| Status | Count | Pct |
|--------|-------|-----|
| STRONG_SUPPORT | 218 | 34.0% |
| PARTIAL_SUPPORT | 319 | 49.7% |
| WEAK_SUPPORT | 93 | 14.5% |
| WRONG_SUPPORT | 4 | 0.6% |
| NEEDS_MANUAL_REVIEW | 0 | 0.0% |

## 3. 每篇论文审计

### Ge_yulong_2024_an_investigation_ofppp_time_transfer_viabds3_pppb2b_service

**Status: BLOCKED**
- Total quotes: 230
- High risk evidence: 17
- Wrong support: 4
- Support: STRONG=73, PARTIAL=113, WEAK=39, WRONG=4, REVIEW=1

#### 字段审计

| Field | Total | Strong | Partial | Weak | Wrong | Review |
|-------|-------|--------|---------|------|-------|--------|
| product_source | 35 | 29 | 0 | 2 | 4 | 0 |
| mathematical_model | 15 | 2 | 11 | 2 | 0 | 0 |
| ionospheric_handling | 3 | 0 | 0 | 3 | 0 | 0 |
| correction_types | 19 | 4 | 14 | 0 | 0 | 1 |
| technical_route | 28 | 4 | 24 | 0 | 0 | 0 |
| experiment_epoch | 11 | 1 | 1 | 9 | 0 | 0 |
| datasets | 22 | 16 | 0 | 6 | 0 | 0 |
| metrics | 32 | 17 | 0 | 15 | 0 | 0 |
| main_results | 43 | 0 | 43 | 0 | 0 | 0 |
| novelty_audit | 8 | 0 | 8 | 0 | 0 | 0 |
| reproducibility_audit | 14 | 0 | 12 | 2 | 0 | 0 |

#### 高风险 Evidence

- **product_source**: [WRONG_SUPPORT] quote mentions ['MIXED_PRODUCTS'], not PPP-B2b (match=exact_repair, conf=high)
- **product_source**: [WRONG_SUPPORT] quote mentions ['MIXED_PRODUCTS'], not PPP-B2b (match=normalized_repair, conf=high)
- **product_source**: [WRONG_SUPPORT] quote mentions ['MIXED_PRODUCTS'], not PPP-B2b (match=semantic_candidate_repair, conf=medium)
- **product_source**: [WRONG_SUPPORT] quote mentions ['MIXED_PRODUCTS'], not PPP-B2b (match=semantic_candidate_repair, conf=medium)
- **mathematical_model**: [WEAK_SUPPORT] keyword overlap with low confidence (match=keyword_overlap_repair, conf=low)
- **mathematical_model**: [WEAK_SUPPORT] keyword overlap with low confidence (match=keyword_overlap_repair, conf=low)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)

#### ❌ WRONG_SUPPORT

- **product_source**: quote mentions ['MIXED_PRODUCTS'], not PPP-B2b
  Quote: We collected 29 days of experimental data and compared it with the Centre National d’Etudes 
Spatial
- **product_source**: quote mentions ['MIXED_PRODUCTS'], not PPP-B2b
  Quote: Then, time transfer 
based on BDS-3, GPS, and BDS-3/GPS PPP was investigated.
- **product_source**: quote mentions ['MIXED_PRODUCTS'], not PPP-B2b
  Quote: The CNES real-
time products were received and recovered by BNC software 
(Weber et al.
- **product_source**: quote mentions ['MIXED_PRODUCTS'], not PPP-B2b
  Quote: Final products and ultra-rapid products 
released from Wuhan university were downloaded from 
ftp://

### Maosen_Hao_2020_pppperformanceevaluationofqzsscentimeterlevelaugmentationser

**Status: PASS_WITH_WEAK_EVIDENCE**
- Total quotes: 137
- High risk evidence: 10
- Wrong support: 0
- Support: STRONG=52, PARTIAL=62, WEAK=22, WRONG=0, REVIEW=1

#### 字段审计

| Field | Total | Strong | Partial | Weak | Wrong | Review |
|-------|-------|--------|---------|------|-------|--------|
| product_source | 24 | 23 | 0 | 1 | 0 | 0 |
| mathematical_model | 6 | 0 | 6 | 0 | 0 | 0 |
| ionospheric_handling | 6 | 1 | 0 | 5 | 0 | 0 |
| correction_types | 24 | 4 | 19 | 0 | 0 | 1 |
| technical_route | 17 | 3 | 14 | 0 | 0 | 0 |
| experiment_epoch | 3 | 0 | 0 | 3 | 0 | 0 |
| datasets | 11 | 5 | 0 | 6 | 0 | 0 |
| metrics | 18 | 16 | 0 | 2 | 0 | 0 |
| main_results | 17 | 0 | 17 | 0 | 0 | 0 |
| novelty_audit | 3 | 0 | 3 | 0 | 0 | 0 |
| reproducibility_audit | 8 | 0 | 3 | 5 | 0 | 0 |

#### 高风险 Evidence

- **product_source**: [WEAK_SUPPORT] quote from references/acknowledgment section (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **datasets**: [WEAK_SUPPORT] quote from references/acknowledgment section (match=normalized_repair, conf=high)
- **reproducibility_audit**: [WEAK_SUPPORT] quote shows info IS provided, contradicting blocker (match=keyword_overlap_repair, conf=high)
- **reproducibility_audit**: [WEAK_SUPPORT] quote shows info IS provided, contradicting blocker (match=keyword_overlap_repair, conf=high)
- **reproducibility_audit**: [WEAK_SUPPORT] quote shows info IS provided, contradicting blocker (match=keyword_overlap_repair, conf=high)
- **reproducibility_audit**: [WEAK_SUPPORT] quote shows info IS provided, contradicting blocker (match=keyword_overlap_repair, conf=high)
- **reproducibility_audit**: [WEAK_SUPPORT] quote from references/acknowledgment section (match=normalized_repair, conf=high)

### Ruohua_Lan_2022_evaluation_of_bds-3_b1cb2b_singledual-frequency_pp

**Status: PASS_WITH_WEAK_EVIDENCE**
- Total quotes: 275
- High risk evidence: 12
- Wrong support: 0
- Support: STRONG=93, PARTIAL=144, WEAK=32, WRONG=0, REVIEW=6

#### 字段审计

| Field | Total | Strong | Partial | Weak | Wrong | Review |
|-------|-------|--------|---------|------|-------|--------|
| product_source | 40 | 28 | 8 | 4 | 0 | 0 |
| mathematical_model | 30 | 1 | 28 | 1 | 0 | 0 |
| ionospheric_handling | 16 | 11 | 0 | 4 | 0 | 1 |
| correction_types | 28 | 2 | 26 | 0 | 0 | 0 |
| technical_route | 20 | 0 | 20 | 0 | 0 | 0 |
| experiment_epoch | 5 | 0 | 0 | 5 | 0 | 0 |
| datasets | 33 | 23 | 0 | 9 | 0 | 1 |
| metrics | 40 | 28 | 0 | 8 | 0 | 4 |
| main_results | 49 | 0 | 49 | 0 | 0 | 0 |
| novelty_audit | 3 | 0 | 3 | 0 | 0 | 0 |
| reproducibility_audit | 11 | 0 | 10 | 1 | 0 | 0 |

#### 高风险 Evidence

- **product_source**: [WEAK_SUPPORT] no product keywords in quote (match=keyword_overlap_repair, conf=medium)
- **product_source**: [WEAK_SUPPORT] no product keywords in quote (match=keyword_overlap_repair, conf=high)
- **product_source**: [WEAK_SUPPORT] no product keywords in quote (match=semantic_candidate_repair, conf=low)
- **product_source**: [WEAK_SUPPORT] quote from references/acknowledgment section (match=semantic_candidate_repair, conf=medium)
- **mathematical_model**: [WEAK_SUPPORT] keyword overlap with low confidence (match=keyword_overlap_repair, conf=low)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)
- **experiment_epoch**: [WEAK_SUPPORT] no date in quote; may just mention experiment setup (match=keyword_overlap_repair, conf=high)

## 4. 高风险字段汇总

| Paper | Issues |
|-------|--------|
| Ge_yulong_2024_an_investigation_ofp | WRONG_SUPPORT:product_source:quote mentions ['MIXED_PRODUCTS'], not PPP-B2b |
| Ge_yulong_2024_an_investigation_ofp | WRONG_SUPPORT:product_source:quote mentions ['MIXED_PRODUCTS'], not PPP-B2b |
| Ge_yulong_2024_an_investigation_ofp | WRONG_SUPPORT:product_source:quote mentions ['MIXED_PRODUCTS'], not PPP-B2b |
| Ge_yulong_2024_an_investigation_ofp | WRONG_SUPPORT:product_source:quote mentions ['MIXED_PRODUCTS'], not PPP-B2b |
| Ge_yulong_2024_an_investigation_ofp | WEAK_SUPPORT_ON_HIGH_RISK:product_source |
| Ge_yulong_2024_an_investigation_ofp | ... (41 total) |
| Maosen_Hao_2020_pppperformanceevalu | WEAK_SUPPORT_ON_HIGH_RISK:product_source |
| Maosen_Hao_2020_pppperformanceevalu | WEAK_SUPPORT_ON_HIGH_RISK:ionospheric_handling |
| Maosen_Hao_2020_pppperformanceevalu | WEAK_SUPPORT_ON_HIGH_RISK:ionospheric_handling |
| Maosen_Hao_2020_pppperformanceevalu | WEAK_SUPPORT_ON_HIGH_RISK:ionospheric_handling |
| Maosen_Hao_2020_pppperformanceevalu | WEAK_SUPPORT_ON_HIGH_RISK:ionospheric_handling |
| Maosen_Hao_2020_pppperformanceevalu | ... (22 total) |
| Ruohua_Lan_2022_evaluation_of_bds-3 | WEAK_SUPPORT_ON_HIGH_RISK:product_source |
| Ruohua_Lan_2022_evaluation_of_bds-3 | WEAK_SUPPORT_ON_HIGH_RISK:product_source |
| Ruohua_Lan_2022_evaluation_of_bds-3 | WEAK_SUPPORT_ON_HIGH_RISK:product_source |
| Ruohua_Lan_2022_evaluation_of_bds-3 | WEAK_SUPPORT_ON_HIGH_RISK:product_source |
| Ruohua_Lan_2022_evaluation_of_bds-3 | WEAK_SUPPORT_ON_HIGH_RISK:ionospheric_handling |
| Ruohua_Lan_2022_evaluation_of_bds-3 | ... (31 total) |

## 5. 准入判定

### 判定规则
- invalid_quote_id_rate < 5%: ✅ (quote repair 阶段已验证)
- WRONG_SUPPORT = 0: see per-paper status
- 高风险字段 STRONG+PARTIAL >= 95%: see field audit table
- 语义字段修改数 = 0: ✅
- unresolved evidence 不影响关键字段: see unresolved report

### 结果
- **Ge_yulong_2024_an_investigation_ofppp_time_transfer_viabds3_pppb2b_service**: ❌ BLOCKED (4 WRONG_SUPPORT)
- **Maosen_Hao_2020_pppperformanceevaluationofqzsscentimeterlevelaugmentationser**: ⚠️ PASS_WITH_WEAK_EVIDENCE (22 weak, 1 needs review)
- **Ruohua_Lan_2022_evaluation_of_bds-3_b1cb2b_singledual-frequency_pp**: ⚠️ PASS_WITH_WEAK_EVIDENCE (32 weak, 6 needs review)

## 6. 语义字段修改数

**0** — 本次审计未修改任何语义字段。