# Corpus Grounded v0.2 — Final Status Report

**Release:** `research_kb/releases/corpus_grounded_v0.2/`
**Date:** 2026-05-22

---

## 1. Batch 1 + Batch 2 是否成功合并为 17-paper baseline

✅ **成功。** 17 篇论文合并完成。
- Batch 1: 7 papers (6 core + 1 addendum Yan Liu)
- Batch 2: 10 papers (5 core + 3 boundary + 2 non-B2b)
- Total: 17 papers in `corpus_grounded_v0.2/`

## 2. 17 篇是否全部 PASS

✅ **17/17 PASS。**
- 0 BLOCKED
- 0 WRONG_SUPPORT
- 0 product_source misclassifications
- 0 epoch conflicts

## 3. Cross-batch consistency check 是否通过

✅ **通过。** 9 structural format differences (false positives), 0 semantic inconsistencies.
- product_source taxonomy: consistent (BDS3_B2B, MIXED, CNES, QZSS_CLAS)
- classification: consistent across batches
- experiment_epoch: no publication year contamination
- DCB status: consistent labeling
- quote_id: 0 cross-paper conflicts

## 4. Regression tests 是否建立

✅ **建立并全部通过。**
- 17 golden verdicts in `research_kb/tests/regression_goldens/`
- Test runner: `scripts/run_regression_tests.py`
- Results: **17/17 PASS**

## 5. Corpus maps 是否重新生成

✅ **7 maps 已生成** in `corpus_grounded_v0.2/maps/`:
- `technical_routes.yaml` — 6 technical routes
- `problem_evolution.yaml` — timeline 2020-2025
- `product_source_taxonomy.yaml` — 4 product categories
- `method_lineage.yaml` — 7 method categories
- `dataset_metric_index.yaml` — common datasets & metrics
- `reproduction_index.yaml` — 17 paper reproducibility scores
- `citation_graph.json` — 17 nodes

## 6. 是否允许进入 Batch 3

✅ **允许。**
- 17/17 PASS baseline established
- Cross-batch consistency verified
- Regression tests operational (17/17)
- Corpus maps clean (0 BLOCKED papers)
- Circuit breaker rules defined and operational

## 7. Batch 3 推荐规模

**推荐：20 篇**（Phase A: 10 + Phase B: 10）。

30 篇仅当：
- Phase A + B 全部 PASS (20/20)
- 0 WRONG_SUPPORT
- invalid_quote_id_rate < 5%

## 8. 当前主要风险

| Risk | Severity | Mitigation |
|------|----------|------------|
| Batch 1/2 format inconsistency | LOW | Regression tests catch semantic drift regardless of format |
| Batch 2 zero grounding_quotes | MEDIUM | Classification validated via keyword analysis; enrichment needed before final KB merge |
| keyword_overlap ratio (Batch 1: 55.6%) | MEDIUM | Monitored; future batches should reduce through better quote extraction |
| Chinese-language PDF (刘威) | HIGH | Needs PDF quality check; may require OCR |
| Phase C over-expansion | LOW | Circuit breaker rules prevent runaway |

## Release Structure

```
corpus_grounded_v0.2/
├── manifest.json
├── corpus_index.json
├── corpus_index.yaml
├── limitations.md
├── semantic_corrections.yaml
├── manual_review_queue.yaml
├── json_repaired/ (17 files)
├── yaml_repaired/ (17 files)
├── quote_banks/ (17 files)
├── reports/
│   ├── cross_batch_consistency.json
│   └── cross_batch_consistency.yaml
├── maps/ (7 files)
└── tests/ → research_kb/tests/regression_goldens/ (17 files)
```

**Corpus Grounded v0.2: READY FOR BATCH 3.**
