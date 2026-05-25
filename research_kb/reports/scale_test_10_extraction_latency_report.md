# Scale Test 10 — Extraction Latency Report

## 实测延迟

| 指标 | 值 |
|------|-----|
| 论文 | Yan Liu 2022 (28 pages) |
| Total chunks | 28 |
| Completed | 26 (93%) |
| Total API calls | 26 |
| Total elapsed | ~3.5 hours |
| Avg time per chunk | **~8 minutes** |
| Avg time per API call | ~5 minutes |
| JSON first-attempt success | ~75% |

## 瓶颈分析

1. **系统 prompt 过长**：~3000 tokens，每次调用都要处理
2. **Schema 过复杂**：~300 lines JSON Schema 附加到每个请求
3. **Response 过长**：max_tokens=8192 允许模型输出大量文本
4. **串行调用**：sleep(0.2) + 无并发，28 chunks = 28 次串行等待
5. **Retry 膨胀**：~25% chunks 需要 2-3 次重试

## 预估

| 模式 | Chunks/paper | Time/paper | 10 papers |
|------|-------------|-----------|-----------|
| Full (current) | 15-28 | 3-7 hours | **30-50 hours** |
| Lite (top-5) | 5 | ~40 min | **~7 hours** |
| Lite + concurrent(3) | 5 | ~15 min | **~2.5 hours** |

## 建议

- **Lite extraction**: 只处理 top 5 chunks per paper
- **Prompt minification**: 去掉长解释，只输出核心字段
- **Concurrency**: 3 papers in parallel
- **max_tokens**: 降低到 4096
