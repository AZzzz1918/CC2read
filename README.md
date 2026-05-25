# GNSS / PPP-B2b 科研论文知识库构建系统

面向 GNSS、实时 PPP、BDS-3 PPP-B2b 方向的科研文献知识库，基于 DeepSeek-v4 API 进行严格信息抽取和科研审计。

## 目录结构

```
├── paper/                          # 放入待处理 PDF
├── prompts/
│   └── deepseek_system_prompt.txt  # DeepSeek 系统提示词
├── schemas/
│   └── paper_schema.json           # 知识库 JSON Schema
├── scripts/
│   ├── update_kb.py                # 总入口
│   ├── pdf_to_markdown.py          # PDF → Markdown
│   ├── chunk_markdown.py           # Markdown 分块
│   ├── extract_chunks.py           # DeepSeek 逐 chunk 抽取
│   ├── merge_paper_chunks.py       # 单篇合并
│   ├── build_corpus_maps.py        # 跨论文图谱
│   └── validate_kb.py              # 校验
├── research_kb/
│   ├── markdown/                   # PDF 转换的 Markdown
│   ├── chunks/                     # 分块 JSON
│   ├── extractions/                # DeepSeek 原始抽取结果
│   ├── papers/
│   │   ├── json/                   # 单篇论文 JSON
│   │   └── yaml/                   # 单篇论文 YAML
│   ├── corpus/                     # 跨论文图谱
│   └── reports/                    # 综合报告
├── unresolved_items.yaml           # 失败 chunk 记录
├── extraction_log.json             # 校验日志
├── .env                            # API 配置（需自建）
├── .env.example                    # API 配置模板
└── requirements.txt
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置 .env

复制 `.env.example` 为 `.env`，填入真实的 DeepSeek API 信息：

```
DEEPSEEK_API_KEY=sk-xxxxxxxx
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEEPSEEK_MODEL=deepseek-v4
```

## 使用方式

### 1. 将 PDF 放入 paper/ 目录

把需要处理的论文 PDF 文件放入 `paper/` 文件夹。

### 2. 运行知识库更新

```bash
python scripts/update_kb.py
```

### 3. 查看输出

- **单篇论文结果**：`research_kb/papers/json/`、`research_kb/papers/yaml/`
- **跨论文图谱**：`research_kb/corpus/`
- **综合报告**：`research_kb/reports/`
- **校验日志**：`extraction_log.json`

## 增量更新

系统通过 SHA256 hash 判断文件是否变更：
- 新增 PDF：自动处理
- 修改过的 PDF：重新处理
- 未变更的 PDF：跳过（保留已有 Markdown 和抽取结果）

## DeepSeek API 返回非 JSON 的处理

- `call_deepseek.py` 自动重试最多 3 次
- 重试时会追加纠正提示
- 3 次均失败后写入 `unresolved_items.yaml`，不中断整体流程

## 反幻觉测试

系统内置了一个对抗性测试套件，用人工构造的论文片段验证反幻觉防线是否生效。

### 运行测试

```bash
pip install pytest
python -m pytest tests/ -v
```

### 测试覆盖的 10 个风险点

| # | 测试 | 对抗场景 |
|---|------|---------|
| 1 | `test_experiment_epoch_pubyear_mistake` | experiment_epoch 填的年份==出版年份，无 quote 支撑 |
| 2 | `test_grounding_quotes_unmatched` | DeepSeek 生成的 quote 与 Markdown 原文不完全一致 |
| 3 | `test_paper_id_missing_markdown` | paper_id 找不到对应 Markdown 文件 |
| 4 | `test_product_source_fake_b2b_no_quotes` | actual=BDS3_PPP_B2B_BROADCAST 但无 grounding_quotes |
| 5 | `test_title_b2b_but_actual_igs` | 标题含 PPP-B2b 但实际使用 IGS RTS/CLK93 |
| 6 | `test_missing_dcb_uncombined_ppp` | UC 模型缺 DCB 来源且 dcb_missing_flag=false |
| 7 | `test_empty_blockers_with_massive_missing` | blockers=[] 但 8/10 项复现信息缺失 + score=8 虚高 |
| 8 | `test_overclaimed_novelty_no_evidence` | audit_grade=A 但所有创新证据 boolean 为 false |
| 9 | `test_citation_graph_bad_reference` | citation_graph 引用不存在的 paper_id |
| 10 | `test_conflicting_evidence_not_resolved` | conflicting_evidence 存在未解决的 CONFLICTING_EVIDENCE |
| 集成 | `test_validate_full_pipeline_detects_all_issues` | 全量 validate() 对所有 bad_case 应返回 CRITICAL/FAIL |

### 测试不依赖 DeepSeek API

所有测试使用 `tests/fixtures/` 中的人工 JSON + Markdown，不需要 API key，可离线反复运行。

### 防线验证原则

1. **good_case 必须通过校验**：正确标注 NOT_MENTIONED 且有 grounding_quotes 支撑的 paper 不应被误报
2. **bad_case 必须触发预期错误**：所有对抗性 JSON 应被 validate_kb.py 正确识别
3. **不依赖 DeepSeek 自报字段做关键判断**：experiment_epoch 独立比对 publication_year
4. **grounding_quotes 必须逐字匹配 Markdown**：子串匹配，不模糊
5. **product_source 必须有正文 quote 支撑**
6. **DCB 缺失检测区分 IF/UC/SF**

## 人工复核

运行完成后，检查以下文件：

1. **`unresolved_items.yaml`**：列出所有 API 抽取失败的 chunk，包含 paper_id、chunk_id
2. **`extraction_log.json`**：全量校验结果，包括：
   - PDF ↔ Markdown 覆盖情况
   - grounding_quotes 匹配情况
   - DCB 缺失警告
   - experiment_epoch 审计结果
3. **`research_kb/reports/overview.md`**：论文概览
4. **`research_kb/reports/reproduction_index.md`**：复现难度排序表

对于 `unresolved_items.yaml` 中的失败项，可手动检查对应的 Markdown 和 chunk，直接调用 DeepSeek 补抽。
