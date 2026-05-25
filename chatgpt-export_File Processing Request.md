# File Processing Request

> [文件不支持导出]
>

I see you uploaded `three_paper_pilot_report.md`. What would you like me to do with it—summarize it, edit it, extract key findings, turn it into slides, or something else?

-----

> [文件不支持导出]
>

I see the new upload: `chatgpt-export_科研知识库构建助手.md`.

The earlier uploaded file context may have expired on the platform side. I can still work with the files that are currently available in this conversation. What would you like me to do with this Markdown export?

-----

> 我接下来要干什么

你**下一步不要直接跑全量论文**。根据 3 篇 pilot 报告，当前唯一真正阻断项是：**PDF → Markdown 文本提取质量差，导致 grounding quotes 无法逐字匹配**；虽然 product_source、epoch、novelty、DCB、reproducibility 审计逻辑基本通过，但 3 篇论文都因为 quote unmatched 被 BLOCKED。fileciteturn0file1

你现在该做这 5 步：

## 1. 先修 PDF 文本提取，不要扩展知识库

让 Claude Code 优先改 pipeline：

```text
请先不要进入全量论文处理。当前 3-paper pilot 的唯一阻断问题是 PDF 文本提取质量导致 grounding_quotes 无法逐字匹配。请优先修复 PDF → Markdown 阶段：

1. 将正文提取从 pdfplumber 优先改为 PyMuPDF/fitz。
2. 保留页码、章节标题、表格、图注。
3. 对 quote validation 增加 fuzzy matching：
   - exact match 优先；
   - exact match 失败时使用 normalized text match；
   - 再失败时使用 difflib / rapidfuzz，相似度阈值暂设 0.90。
4. validator 输出 exact_match_rate、normalized_match_rate、fuzzy_match_rate。
5. 重新跑原来的 3 篇 pilot，不要更换论文。
6. 只有当 invalid quote rate < 5% 时，才允许进入下一阶段。
```

## 2. 重跑同一批 3 篇 pilot

不要换论文，因为这 3 篇刚好覆盖了：

- 核心 PPP-B2b：Ruohua Lan 2022
- 边界 PPP-B2b / CNES 混合产品：Ge Yulong 2024
- 非 BDS-3 PPP-B2b：Maosen Hao 2020

这组 pilot 能测试你最关心的产品源误判、epoch anchoring、创新性压制和复现阻断项。fileciteturn0file1

## 3. 判断是否进入 10 篇小规模扩展

只有满足下面条件，才进入下一步：

| 门槛 | 要求 |
|---|---|
| invalid quote rate | < 5% |
| product_source | 无高危误判 |
| experiment_epoch | 不把发表年份当实验年份 |
| DCB handling | 未提及时必须触发 Missing_DCB_Handling |
| reproduction_blockers | 每篇非空 |
| failed_validation | 不进入 corpus maps |

现在你的报告是 **7/10 通过**，但 quote 问题没解决前，不能进入全量处理。fileciteturn0file1

## 4. 通过后再跑 10 篇，而不是全部

10 篇里建议包含：

- 4 篇明确 PPP-B2b 核心论文
- 2 篇 PPP-B2b + IGS/CNES/RTS 对比论文
- 2 篇普通 RT-PPP / PPP-AR 论文
- 2 篇非 BDS-3 增强服务论文，例如 QZSS CLAS、Galileo HAS

这样能继续防止模型把所有实时精密产品都误归为 PPP-B2b。

## 5. 最后才生成正式 `SKILL.md`

你前面已经有了 DeepSeek-v4 API 架构：Claude Code / 本地脚本负责 PDF、chunk、JSON/YAML、校验；DeepSeek-v4 API 负责结构化抽取、创新审计和复现分析。fileciteturn0file0

所以现在还不是写最终版 Skill 的时候。正确顺序是：

```text
修 PDF 提取
→ 重跑 3-paper pilot
→ quote validation 过关
→ 跑 10-paper pilot
→ 固化 schema 和 validator
→ 再写正式 SKILL.md
→ 最后全量处理 paper/
```

另外，有些之前上传的文件已过期；如果你还需要我基于那些旧文件继续分析，需要重新上传。当前这两个文件已经足够判断下一步。

-----

> 为什么chunt提取很慢

我先按你这里的 “chunt” 理解为 **chunk 提取/分块抽取**。从你这个 pipeline 看，慢的主要不是“切块”本身，而是“每个 chunk 调 DeepSeek 做审计抽取 + 校验 quote”。

你这个 **chunk 提取慢**，大概率有 5 个原因：

### 1. 你以为慢在“切 chunk”，其实慢在“每个 chunk 调 DeepSeek”

你现在的流程是：

`PDF → Markdown → chunks → DeepSeek chunk 审计 → paper merge → validate`

pilot 里 3 篇论文就已经产生了：

- Ruohua Lan：25 pages → 25 chunks
- Ge Yulong：17 pages → 17 chunks
- Maosen Hao：13 pages → 13 chunks
- 合计：55 chunks
- DeepSeek 总调用约 65 次，包含重试 fileciteturn0file1

所以实际耗时近似是：

```text
总耗时 ≈ PDF解析时间 + chunk数量 × DeepSeek单次响应时间 + 重试时间 + validate时间
```

也就是说，chunk 越碎，API 调用次数越多，速度就越慢。

---

### 2. 你把 `MAX_CHUNK_CHARS` 从 6000 降到 3000，稳定性提高了，但速度会变慢

报告里写到你把：

```text
max_tokens 4096 → 8192
MAX_CHUNK_CHARS 6000 → 3000
```

这提升了首次成功率，但代价是 chunk 数量增加。chunk 数量越多，DeepSeek 调用次数越多。fileciteturn0file1

也就是说：

```text
3000 chars/chunk = 更稳，但更慢
6000 chars/chunk = 更快，但更容易 JSON 失败或漏证据
```

目前你的设置偏“审计稳定性”，不是偏速度。

---

### 3. quote grounding 太严格，导致校验和返工成本很高

你的提示词要求所有关键结论都要有 exact quote，而且 quote 必须能在 Markdown 中逐字匹配。这个规则本身是对的，但非常耗时。

pilot 报告里最大 blocker 是：

```text
pdfplumber 文本提取丢失词间空格，导致 ~75% DeepSeek quotes 无法在 markdown 中逐字匹配
```

所以模型可能抽得对，但因为 PDF 转 Markdown 时空格丢失，validate 认为 quote 不匹配，导致论文被 BLOCKED。fileciteturn0file1

这会让流程变成：

```text
提取 → DeepSeek生成quote → validate匹配失败 → 标记问题 → 可能重跑/人工检查
```

慢的根因不是 DeepSeek 一定慢，而是 **PDF 文本质量差 + exact quote 校验太硬**。

---

### 4. pdfplumber 对论文排版、双栏、公式、表格处理慢且容易破坏文本

报告已经指出建议换用 PyMuPDF/fitz，因为 pdfplumber 会出现词间空格丢失，比如：

```text
CentimeterLevelAugmentationService
```

这类文本会让 quote matching 很难通过。fileciteturn0file1

建议改成：

```text
正文提取：PyMuPDF / fitz
表格提取：pdfplumber
quote校验：原始Markdown + normalized text 双轨校验
```

不要让 pdfplumber 负责所有正文提取。

---

### 5. 你的 chunk prompt 太重，每个 chunk 都在做“科研审计”

你现在不是普通摘要，而是让每个 chunk 都检查：

- PPP-B2b 产品源
- experiment epoch
- DCB handling
- 数学模型边界
- novelty audit
- reproducibility blockers
- grounding quotes

这相当于每个 chunk 都做小型审稿。质量会高，但速度自然慢。

---

## 直接优化方案

我建议你这样改：

### A. 把流程拆成两级，不要每个 chunk 都做完整审计

第一级 chunk 只做轻量抽取：

```text
bibliographic clues
method clues
experiment clues
dataset clues
result clues
quote candidates
uncertain items
```

第二级 paper merge 再做重审计：

```text
product_source
novelty_grade
reproduction_blockers
DCB handling
experiment_epoch
```

这样会减少每个 chunk 的输出长度和思考时间。

---

### B. chunk 大小调到 4000–5000 chars，而不是固定 3000

你现在 3000 比较稳，但太碎。

可以试：

```text
MAX_CHUNK_CHARS=4500
CHUNK_OVERLAP=300
MAX_TOKENS=8192
temperature=0
```

如果 JSON 失败率还能接受，速度会明显提升。

---

### C. 并发调用 DeepSeek

如果你现在是串行：

```text
chunk_001 → chunk_002 → chunk_003 → ...
```

会很慢。

建议改成异步并发：

```text
CONCURRENCY=3 或 5
```

不要太高，避免触发 API rate limit。

---

### D. quote matching 改成“两级校验”

不要一开始就 exact match 卡死。

建议：

```text
level 1: exact match
level 2: normalized match，去除多余空格、换行、连字符
level 3: fuzzy match，ratio > 0.90 标记为 weak_match
```

但是最终入库时要区分：

```json
"quote_match_type": "exact | normalized | fuzzy | failed"
```

这样不会因为 PDF 提取空格问题把整篇论文 BLOCKED。

---

### E. 先缓存 chunk 分析结果

每个 chunk 算 hash：

```text
chunk_hash = sha256(chunk_text)
```

如果 chunk 没变，就不要重新调 DeepSeek。

否则你每次改 schema 或 validate 都会重新跑很多 API，速度会崩。

---

## 你现在最该改的顺序

1. **正文提取从 pdfplumber 换成 PyMuPDF/fitz**
2. **quote 校验加 normalized / fuzzy 模式**
3. **DeepSeek chunk 调用加并发**
4. **chunk 轻量抽取，paper merge 再做重审计**
5. **chunk 结果缓存，避免重复 API 调用**

核心判断：你现在慢不是坏事，而是因为 pipeline 走的是“高可信科研审计模式”。但当前最大瓶颈已经不是模型能力，而是 **PDF 文本质量 + chunk 过碎 + 串行 API + quote 校验过硬**。

-----

> pdf文本提取质量能否通过安装skill来改善

可以，但要分清楚：

**安装 Skill 不能“神奇提高 PDF 本身的可读性”，但可以显著改善你的 PDF 文本提取流程。**

你现在的问题根因不是 DeepSeek，而是 **PDF → Markdown 阶段的文本质量太差**。你的 pilot 报告里已经定位到：`pdfplumber` 提取时丢失词间空格，导致约 75% 的 quote 无法逐字匹配，所以 3 篇论文都被 BLOCKED。fileciteturn0file1L67-L74

所以 Skill 能改善的是这几件事：

## 1. 把提取器从单一 pdfplumber 改成多引擎

建议 Skill 里规定：

```text
正文文本：PyMuPDF / fitz 优先
表格：pdfplumber
参考文献：GROBID 或正则 + section parser
扫描页：OCR fallback
公式/图注：保留原始文本 + 标记 needs_manual_review
```

你的报告里也明确建议换用 **PyMuPDF/fitz**，因为 pdfplumber 会合并词间空格。fileciteturn0file1L67-L74

## 2. Skill 可以自动做文本清洗

例如：

```text
去除断行连字符
修复单词间空格
合并错误换行
保留页码
保留 section heading
保留 table / figure caption
生成 normalized_text
生成 raw_text
```

特别是 quote 校验时，不应该只用 exact match。

应该变成：

```json
{
  "quote_match_type": "exact | normalized | fuzzy | failed",
  "match_score": 0.94
}
```

这样可以避免因为 PDF 提取空格错误，把本来正确的审计结果全部 BLOCKED。

## 3. Skill 可以规定“提取质量门控”

每篇 PDF 先做 extraction quality check：

```text
text_coverage_ratio
space_loss_score
garbled_text_ratio
page_count_matched
reference_section_detected
table_extraction_success
ocr_needed_pages
```

如果文本质量不够，就不要直接送 DeepSeek 审计，而是先进入：

```text
repair_text → re-extract → fallback extractor → OCR → manual_review
```

这能避免浪费 API 调用。

## 4. Skill 可以把你的 pipeline 固化成标准流程

比较适合写成 Claude Code Skill：

```text
PDF ingest
→ multi-engine extraction
→ text quality validation
→ Markdown normalization
→ chunking
→ DeepSeek extraction
→ quote validation
→ paper merge
→ corpus map
```

这样每次处理新论文时，就不会重复踩 pdfplumber 的坑。

## 5. 但 Skill 不能解决所有 PDF 问题

这些情况仍然很难完全自动化：

```text
扫描版 PDF
双栏严重错序
公式变乱码
表格跨页
图中嵌入文字
参考文献格式混乱
出版商 PDF 带隐藏层错误
```

这些最多只能通过 Skill 标记为：

```text
needs_ocr
needs_manual_review
formula_quality: low
table_quality: low
quote_confidence: weak
```

不能靠模型猜。

## 我建议你的结论

**值得安装/编写一个专门的 PDF extraction Skill。**

但它的目标不是“让 DeepSeek 更聪明”，而是：

```text
让 PDF → Markdown → chunk 这一步更稳定、更可追踪、更少污染后续审计。
```

你现在最该做的是把 Skill 的重点放在这 4 个能力上：

1. **PyMuPDF 优先正文提取**
2. **pdfplumber 只负责表格**
3. **quote matching 支持 exact / normalized / fuzzy 三档**
4. **低质量 PDF 先阻断，不进入 DeepSeek 审计**

一句话：**Skill 能明显改善 PDF 文本提取质量，但本质上是通过安装和编排更好的工具链，而不是靠提示词本身解决 PDF 解析问题。**

-----

> 结果
>
>   Quote 匹配率（fitz 提取 + 5 级匹配）
>
>   ┌───────────────────┬───────┬────────────┬───────┬─────────┬─────────┐
>   │       论文        │ Exact │ Normalized │ Fuzzy │ Invalid │  状态   │
>   ├───────────────────┼───────┼────────────┼───────┼─────────┼─────────┤
>   │ Maosen Hao (QZSS) │ 21.2% │ 87.6%      │ 87.6% │ 12.4%   │ FAIL    │
>   ├───────────────────┼───────┼────────────┼───────┼─────────┼─────────┤
>   │ Ruohua Lan (B2b)  │ 26.2% │ 71.3%      │ 71.3% │ 28.7%   │ BLOCKED │
>   ├───────────────────┼───────┼────────────┼───────┼─────────┼─────────┤
>   │ Ge Yulong (B2b)   │ 13.0% │ 65.2%      │ 65.2% │ 34.8%   │ BLOCKED │
>   └───────────────────┴───────┴────────────┴───────┴─────────┴─────────┘
>
>   关键发现
>
>   1. fitz 替换 pdfplumber 有效：invalid rate 从 ~75% 降至 12-35%
>   2. 多级标准化是主力：exact → normalized 跳变最大（21→88% for Maosen Hao）
>   3. difflib fuzzy 零增量：normalized = fuzzy rate，说明剩余的 unmatched quotes 不是文本噪声问题
>   4. 剩余 invalid 根因：DeepSeek 有时生成近似引用而非精确引用（paraphrasing），以及跨页内容无法在一个 chunk 的 markdown
>   中找到
>   5. <5% 阈值未达成：最低 12.4% (Maosen Hao)。2/3 论文仍 BLOCKED
>
>   改进效果
>
>   ┌───────────────────────────┬─────────────────┬───────────┐
>   │           指标            │ pdfplumber (旧) │ fitz (新) │
>   ├───────────────────────────┼─────────────────┼───────────┤
>   │ invalid rate (Maosen Hao) │ ~75%            │ 12.4%     │
>   ├───────────────────────────┼─────────────────┼───────────┤
>   │ invalid rate (avg)        │ ~75%            │ 25%       │
>   ├───────────────────────────┼─────────────────┼───────────┤
>   │ grounding_quotes issues   │ 305             │ 179       │
>   ├───────────────────────────┼─────────────────┼───────────┤
>   │ BLOCKED papers            │ 3/3             │ 2/3       │
>   └───────────────────────────┴─────────────────┴───────────┘
>
>   结论：fitz 改进显著但不足以突破 <5% 门槛。剩余 unmatched quotes 根因是 DeepSeek 的 paraphrasing 行为，需从 prompt
>   层强化"exact quote o

你这轮结果其实已经定位得很清楚：**PDF 提取器问题已大幅缓解，剩下的主因已经转移到 DeepSeek quote 生成策略**。下一步不要继续堆 PDF 工具，应该改“证据引用机制”。

你的结论基本正确，但我建议把最后一句改得更激进一点：

**不要只从 prompt 层强化 “exact quote only”，而是把 quote 从“模型生成”改成“模型选择”。**

也就是说，**不要让 DeepSeek 自己写 quote**。它只应该从你预先提供的 quote bank 里选择 `quote_id`。

---

## 现在的瓶颈判断

你这轮结果说明：

```text
pdfplumber → fitz：有效
exact → normalized：有效
normalized → fuzzy：无增量
```

所以剩下的 invalid 不是 PDF 噪声，而是两类问题：

1. **DeepSeek paraphrasing**
   它把原文改写成“看起来像引用”的句子，但不是逐字 quote。

2. **chunk 局部上下文不完整**
   quote 跨页、跨 chunk，导致验证器只在当前 chunk 里找不到。

因此下一步继续调 fuzzy 没意义。核心要改成：

```text
自由生成 quote ❌
从候选 quote bank 选择 quote_id ✅
```

---

## 推荐的新机制：Quote Bank

在送 DeepSeek 之前，先由脚本把 chunk 切成可引用单元：

```json
{
  "quote_bank": [
    {
      "quote_id": "Lan2022_p03_s012",
      "page": 3,
      "section": "Methods",
      "text": "The BDS-3 PPP-B2b corrections include orbit corrections, clock corrections and differential code bias corrections."
    },
    {
      "quote_id": "Lan2022_p04_s003",
      "page": 4,
      "section": "Experimental data",
      "text": "The experiment was conducted from December 20 to December 23, 2021."
    }
  ]
}
```

然后要求 DeepSeek 输出：

```json
{
  "product_source": {
    "value": "MIXED_PRODUCTS",
    "grounding_quote_ids": ["Lan2022_p03_s012"]
  }
}
```

最后由你的程序回填：

```json
{
  "quote_id": "Lan2022_p03_s012",
  "quote": "The BDS-3 PPP-B2b corrections include orbit corrections, clock corrections and differential code bias corrections.",
  "page": 3,
  "section": "Methods",
  "match_type": "quote_bank_exact"
}
```

这样 **invalid quote 字符串问题基本会消失**，因为 quote 不再由模型生成，而是由程序从原文复制。

---

## DeepSeek prompt 应该这样改

把原来的：

```text
你必须提供 Exact Quote
```

升级成：

```text
你不能自己生成、改写、翻译、压缩或拼接 quote。

用户会提供 quote_bank。你只能引用 quote_bank 中已经存在的 quote_id。

如果没有任何 quote_id 能直接支持某个字段，必须填入 "NOT_MENTIONED" 或 "INSUFFICIENT_EVIDENCE"。

grounding_quotes 字段中禁止输出自由文本 quote，只允许输出 quote_id。最终 exact quote 将由外部程序根据 quote_id 回填。
```

再加一条强约束：

```text
如果你输出的 quote_id 不存在于 quote_bank，结果视为无效。
```

---

## Schema 也要小改

不要让模型直接写：

```json
"grounding_quotes": [
  {
    "quote": "...",
    "page": 3
  }
]
```

改成：

```json
"grounding_quote_ids": [
  "Lan2022_p03_s012",
  "Lan2022_p04_s003"
]
```

然后由 merge/validate 脚本生成最终字段：

```json
"grounding_quotes": [
  {
    "quote_id": "Lan2022_p03_s012",
    "quote": "exact text copied by program",
    "page": 3,
    "section": "Methods",
    "match_type": "quote_bank_exact"
  }
]
```

这个改动非常关键。**quote 的精确性应该由程序保证，不应该交给 LLM 保证。**

---

## 跨页 / 跨 chunk 问题怎么处理

你现在有一部分 invalid 是因为 quote 不在当前 chunk 的 markdown 中。

解决方式：

### 方案 A：chunk overlap

设置：

```text
CHUNK_OVERLAP_SENTENCES=5
```

不要只按字符 overlap，要按句子或段落 overlap。

### 方案 B：全局 quote bank

每篇论文建立一个全局 quote bank：

```text
paper_quote_bank.json
```

DeepSeek 处理 chunk 时只看到当前 chunk 的 quote bank；paper merge 时可以看到整篇论文的 quote bank。

这样 merge 阶段判断 `experiment_epoch`、`product_source`、`novelty` 时，不会被单个 chunk 限制。

### 方案 C：禁止跨 quote 拼接

要求：

```text
一个 grounding quote 必须来自一个 quote_id。
不得把多个 quote 拼成一句。
```

如果一个结论需要多个证据，就输出多个 quote_id。

---

## validate 规则也要改

现在 validate 是：

```text
DeepSeek quote string 是否能在 markdown 中找到
```

建议改成：

```text
quote_id 是否存在于 quote_bank
quote_id 对应 text 是否来自 canonical_markdown
quote_id 是否真的支持该字段
```

前两个是程序校验，第三个可以交给二次审计模型或人工抽查。

新的质量门槛应该是：

```text
invalid_quote_id_rate < 1%
unsupported_evidence_rate < 5%
```

也就是说，字符串匹配问题不应该再作为主要 blocker。

---

## 你现在最该做的 4 个修改

按优先级：

1. **建立 quote_bank，不再让 DeepSeek 自由写 quote**
2. **Schema 中 `grounding_quotes` 改为 `grounding_quote_ids`**
3. **merge 后由程序回填 exact quote**
4. **paper 级别建立 global quote bank，解决跨页/跨 chunk 问题**

---

## 修改后的 pipeline

建议变成：

```text
PDF
→ fitz extraction
→ canonical markdown
→ sentence / paragraph quote bank
→ chunk text + quote_bank subset
→ DeepSeek outputs structured fields + quote_ids
→ script resolves quote_ids into exact quotes
→ validate quote_id existence
→ validate evidence support
→ merge paper JSON
```

---

## 对你当前结果的判断

你已经从：

```text
~75% invalid
```

降到：

```text
12%–35% invalid
```

说明 PDF 提取问题已经明显改善。

但要突破 `<5%`，继续靠：

```text
更强 prompt
更强 fuzzy
更换 PDF extractor
```

收益都会很有限。

真正的解法是：

```text
让 LLM 不再生成 quote，只选择 quote。
```

一句话：**下一版不要再优化 quote matching，而要重构 quote generation。**

-----

> 我不想重新生成chunk，这花费的时间太多了，后面我该给claude code什么指令

你现在不该让 Claude Code “重跑 pipeline”。应该让它做一个 **post-hoc quote repair**：复用已有 chunk 分析结果，只修复 grounding quotes 和 validate 逻辑。

给 Claude Code 的核心指令应该是：

**不要重新生成 chunk，不要重跑 DeepSeek chunk extraction，只做 quote repair。**

你可以直接把下面这段发给 Claude Code。

```text
你现在的任务不是重新跑 pipeline，也不是重新生成 chunks。

严格禁止：
1. 不要重新 PDF → chunk。
2. 不要重新调用 DeepSeek 做 chunk extraction。
3. 不要覆盖已有 chunk analysis。
4. 不要改变已有 paper JSON 中的语义字段，例如 product_source、experiment_epoch、novelty_grade、reproduction_blockers。
5. 不要因为 quote repair 失败而重新抽取整篇论文。

你的任务是基于已有结果做 post-hoc quote repair。

背景：
当前 fitz 提取 + 5 级匹配后，quote invalid rate 已从约 75% 降到 12%–35%，说明 PDF 文本提取问题已大幅缓解。剩余 invalid 的主要原因是：
- DeepSeek 生成了 paraphrased quote，而不是 exact quote；
- 部分 quote 跨页或跨 chunk，导致在当前 chunk markdown 中找不到；
- difflib fuzzy 对 normalized 无增量，说明继续调 fuzzy 没意义。

现在请实现一个不重跑 chunk 的 quote repair 管线。

目标：
把模型自由生成的 grounding_quotes，转换为基于 quote_bank 的 grounding_quote_ids。
quote 的精确文本必须由程序从 canonical markdown / fitz markdown 中回填，而不是由 DeepSeek 生成。

请按以下步骤执行。

一、备份已有结果

在修改前，创建备份目录：

research_kb/backup_before_quote_repair/

备份以下内容：
- research_kb/papers/json/
- research_kb/papers/yaml/
- research_kb/papers/chunks/
- research_kb/metadata/
- research_kb/maps/
- research_kb/reports/

不要覆盖原始结果。

二、检查现有文件

检查并报告：
1. 已有 paper JSON 数量。
2. 已有 chunk analysis 数量。
3. 已有 fitz 提取 markdown 或 canonical markdown 文件路径。
4. 当前 validate 报告中的 invalid grounding quote 数量。
5. 哪些论文是 BLOCKED / FAIL。

如果缺少 fitz markdown，不要重新调用 DeepSeek，只允许重新从 PDF 用 fitz 生成 canonical markdown 和 quote_bank。

三、建立 quote_bank

为每篇论文基于 fitz/canonical markdown 生成 quote_bank：

输出路径：

research_kb/quote_bank/[paper_id].quote_bank.json

quote_bank 单元可以按段落和句子混合生成。

每个 quote 单元格式：

{
  "quote_id": "paperid_p003_q00012",
  "paper_id": "",
  "page": 3,
  "section": "section heading or NOT_MENTIONED",
  "text": "exact text copied from canonical markdown",
  "normalized_text": "normalized text for matching",
  "char_start": null,
  "char_end": null
}

要求：
- quote_id 必须稳定。
- text 必须来自 canonical markdown 的原文。
- 不允许由 LLM 生成 quote text。
- 保留 page 信息。
- 尽量保留 section heading。
- paragraph quote 不要过长，建议 80–600 characters。
- sentence quote 不要太碎，必要时保留前后邻接句作为 context_quote。

四、修复已有 grounding_quotes

读取已有 paper JSON 和 chunk analysis。

对每个已有 grounding_quote 执行匹配：

1. exact match
2. normalized match
3. punctuation-insensitive match
4. whitespace-insensitive match
5. fuzzy match

如果匹配成功，替换为：

{
  "quote_id": "...",
  "quote": "exact text copied from quote_bank",
  "page": 3,
  "section": "...",
  "match_type": "exact | normalized | punctuation_normalized | whitespace_normalized | fuzzy",
  "match_score": 0.0-1.0,
  "original_model_quote": "old quote from DeepSeek"
}

注意：
- quote 字段必须从 quote_bank 回填。
- original_model_quote 只用于审计，不再作为权威证据。
- 不要改动字段值本身，只改 grounding evidence。

五、处理 paraphrased quote

如果 existing quote 无法匹配，不要立刻重跑 DeepSeek。

先做本地候选检索：

对 invalid quote 或其所在字段的 claim/value，用 quote_bank 做 top-k 检索：

- rapidfuzz / difflib
- BM25 或 TF-IDF
- keyword overlap
- page / section hint 优先

为每个 invalid quote 输出 top 10 candidates：

research_kb/quote_repair/candidates/[paper_id].invalid_quote_candidates.json

如果 top candidate 分数足够高，例如：
- normalized similarity >= 0.85
- 或 token overlap >= 0.75
- 且 candidate 所在 section 与字段类型一致

则自动修复为：

"match_type": "semantic_candidate_repair"
"repair_confidence": "medium"

如果分数不够，标记为：

"repair_status": "needs_evidence_repick"

六、可选：只对 unresolved evidence 做小范围 DeepSeek repick

允许调用 DeepSeek，但只允许对 unresolved evidence 做局部 quote repick，不允许重新抽取 chunk。

调用 DeepSeek 时，输入只能包括：
1. 字段名
2. 当前字段值
3. 当前 claim
4. top 20 quote_bank candidates
5. 原 invalid quote

DeepSeek 只能输出 quote_id，不能输出自由文本 quote。

DeepSeek prompt 必须包含：

你不能生成 quote。
你不能改写 quote。
你不能翻译 quote。
你只能从 quote_bank candidates 中选择 quote_id。
如果没有候选 quote 能直接支持该字段，输出 "NO_VALID_QUOTE"。
不要修改字段值。
不要新增事实。
不要做新的论文抽取。

输出格式：

{
  "field_path": "",
  "selected_quote_ids": [],
  "decision": "selected | no_valid_quote",
  "reason": ""
}

七、修改 Schema

将内部 evidence 表示从：

"grounding_quotes": [
  {
    "quote": "...",
    "page": ...
  }
]

改为优先使用：

"grounding_quote_ids": [
  "paperid_p003_q00012"
]

最终导出的 paper JSON 可以同时保留：

"grounding_quotes": [
  {
    "quote_id": "",
    "quote": "",
    "page": "",
    "section": "",
    "match_type": "",
    "match_score": "",
    "original_model_quote": ""
  }
]

但权威来源必须是 quote_id。

八、更新 validate_kb.py

不要再把旧的 model-generated quote string exact match 作为唯一 blocker。

新的验证规则：

1. quote_id 必须存在于 quote_bank。
2. quote_bank[quote_id].text 必须来自 canonical markdown。
3. 每个关键字段至少有一个 valid quote_id，除非字段值为 NOT_MENTIONED / INSUFFICIENT_EVIDENCE。
4. invalid_quote_id_rate < 1%。
5. unresolved_required_evidence_rate < 5%。
6. 对 fuzzy / semantic_candidate_repair 的 quote 单独标记 weak_evidence，不直接删除。
7. 如果字段值没有任何可支持 quote_id，则不要自动通过，标记为 needs_manual_review。
8. 不要因为旧 quote 字符串无法 exact match 而 BLOCKED，只看 quote_id 是否可解析。

九、输出修复结果

不要覆盖原始 JSON。

输出到：

research_kb/papers/json_repaired/[paper_id].json
research_kb/papers/yaml_repaired/[paper_id].yaml

生成报告：

research_kb/reports/quote_repair_report.md

报告必须包含：

- 每篇论文原 invalid rate
- 修复后 invalid_quote_id_rate
- exact / normalized / fuzzy / semantic_candidate_repair 数量
- unresolved evidence 数量
- 仍需人工确认的字段
- 哪些论文可以从 BLOCKED 改为 PASS_WITH_WEAK_EVIDENCE
- 哪些论文仍然 BLOCKED
- 是否修改了任何非 evidence 字段；正常情况下应为 0

十、绝对约束

本次任务只做 quote repair。

禁止：
- 重跑 chunk extraction
- 重写已有论文分析结论
- 重新生成 paper JSON 主体内容
- 根据常识补 quote
- 根据字段值伪造 quote
- 把 paraphrase 当 exact quote
- 删除 unresolved evidence 来降低 invalid rate
- 直接放宽阈值让论文通过

如果无法修复某个 quote，保留它并标记 needs_manual_review。
```

你后面可以再追加一句更硬的约束：

```text
这次的成功标准不是重新跑出更漂亮的 JSON，而是在不重跑 chunk、不改变分析结论的前提下，把 grounding evidence 从“LLM 自由生成 quote”迁移到“程序 quote_bank exact quote_id”。
```

我建议你先让 Claude Code 做 **dry run**：

```text
先不要写入 repaired JSON。先 dry-run，输出 quote_repair_report.md，告诉我如果执行修复，三篇论文的 invalid_quote_id_rate 会降到多少。
```

如果 dry run 结果可接受，再让它实际写入 repaired 文件。

-----

> ●结果 — 全部 <5%！
>
>   ┌────────────┬──────┬────────┬──────────┬────────┬──────────────┐
>   │    论文    │ 总计 │ 已修复 │ 新增(KW) │ 未解决 │ Invalid Rate │
>   ├────────────┼──────┼────────┼──────────┼────────┼──────────────┤
>   │ Ge Yulong  │ 230  │ 229    │ 115      │ 1      │ 0.4% ✅      │
>   ├────────────┼──────┼────────┼──────────┼────────┼──────────────┤
>   │ Maosen Hao │ 137  │ 136    │ 92       │ 1      │ 0.7% ✅       │
>   ├────────────┼──────┼────────┼──────────┼────────┼──────────────┤
>   │ Ruohua Lan │ 275  │ 269    │ 180      │ 6      │ 2.2% ✅       │
>   └────────────┴──────┴────────┴──────────┴────────┴──────────────┘
>
>   现在生成最终报告。
>
> ●Write(research_kb\reports\quote_repair_report.md)
>   ⎿  Wrote 102 lines to research_kb\reports\quote_repair_report.md
>        1 # Quote Repair Report
>        2
>        3 生成时间：2026-05-21
>        4 方法：Post-hoc quote repair — 不重跑 chunk，不修改语义字段
>        5
>        6 ---
>        7
>        8 ## 1. 修复前状态
>        9
>       10 | 论文 | 原 invalid rate | 原 unmatched quotes | 原状态 |
>      … +93 lines (ctrl+o to expand)
>
> ●---
>   Quote Repair 完成
>
>   关键数字
>
>   ┌────────────┬─────────────────────────┬─────────────┐
>   │            │         修复前          │   修复后    │
>   ├────────────┼─────────────────────────┼─────────────┤
>   │ Ge Yulong  │ 34.8% invalid (BLOCKED) │ 0.4% (PASS) │
>   ├────────────┼─────────────────────────┼─────────────┤
>   │ Maosen Hao │ 12.4% invalid (FAIL)    │ 0.7% (PASS) │
>   ├────────────┼─────────────────────────┼─────────────┤
>   │ Ruohua Lan │ 28.7% invalid (BLOCKED) │ 2.2% (PASS) │
>   └────────────┴─────────────────────────┴─────────────┘
>
>   修复方式
>
>   ┌─────────┬──────────────────────────────┬────────┐
>   │   层    │             方法             │ 修复数 │
>   ├─────────┼──────────────────────────────┼────────┤
>   │ Phase 1 │ exact + normalized + difflib │ 247    │
>   ├─────────┼──────────────────────────────┼────────┤
>   │ Phase 2 │ keyword overlap （突破性）   │ 387    │
>   ├─────────┼──────────────────────────────┼────────┤
>   │ 未解决  │ needs_evidence_repick        │ 8      │
>   └─────────┴──────────────────────────────┴────────┘
>
>   未修改任何语义字段
>
>   - product_source ✅
>   - experiment_epoch ✅
>   - novelty_grade ✅
>   - reproduction_blockers ✅
>   - 0 字段被修改
>
>   输出位置
>
>   - 修复后 JSON：research_kb/papers/json_repaired/
>   - 修复后 YAML：research_kb/papers/yaml_repaired/
>   - 报告：research_kb/reports/quote_repair_report.md
>   - 备份：research_kb/backup_before_quote_repair/
>
>   8 条 unresolved evidence 留待人工审核
>
>   分布在 datasets、experiments、metrics、formulas、main_results 字段，保留 repair_status: needs_evidence_repick。

很好，这说明你的判断路线是对的：**瓶颈已经从 PDF 提取质量，成功迁移并解决为 evidence repair 问题**。

现在不要急着全量跑，下一步建议做 **二次质量门控**，因为 Phase 2 的 `keyword overlap` 虽然把 invalid rate 压下来了，但它可能引入一个新风险：

```text
quote_id 存在 ≠ quote 真的支持该字段
```

也就是说，字符串问题解决了，接下来要验证 **support correctness**。

你后面给 Claude Code 的指令可以是这个：

```text
现在不要重新生成 chunk，不要重新调用 DeepSeek chunk extraction，也不要修改语义字段。

Quote repair 已经把 invalid rate 降到 <5%。下一步任务是做 evidence support audit。

目标：
检查 repaired JSON 中每个 grounding_quote_id 是否真的支持对应字段值，而不仅仅是文本相似或关键词重合。

输入：
- research_kb/papers/json_repaired/
- research_kb/quote_bank/
- research_kb/reports/quote_repair_report.md

禁止：
1. 不要重新跑 PDF extraction。
2. 不要重新生成 chunk。
3. 不要重跑原始 DeepSeek extraction。
4. 不要修改 product_source、experiment_epoch、novelty_grade、reproduction_blockers 等语义字段。
5. 不要为了通过验证删除 evidence。
6. 不要把 keyword overlap 证据直接视为强证据。

请执行以下步骤：

一、统计 evidence match_type 分布

对每篇论文统计：
- exact
- normalized
- punctuation_normalized
- whitespace_normalized
- fuzzy
- semantic_candidate_repair
- keyword_overlap
- unresolved / needs_evidence_repick

特别标记 Phase 2 keyword overlap 修复的证据，因为这是当前最高风险来源。

二、建立 support audit 规则

对每条 evidence 判断其是否支持对应字段值。

输出 support_status：

- STRONG_SUPPORT
  quote 直接包含字段值或直接描述该结论。
- PARTIAL_SUPPORT
  quote 与字段相关，但不能完全支持字段值。
- WEAK_SUPPORT
  quote 只含关键词，不能单独证明结论。
- WRONG_SUPPORT
  quote 与字段不符或支持相反结论。
- NEEDS_MANUAL_REVIEW
  无法程序判断。

三、优先审计高风险字段

请优先检查以下字段：

1. product_source / actual_product_source
2. experiment_epoch
3. novelty_grade / novelty_statement
4. is_mere_migration
5. reproduction_blockers
6. dcb_missing_flag / ionospheric_handling
7. datasets
8. metrics
9. main_results
10. mathematical_formulation

四、程序化初筛

先用程序规则筛选高风险 evidence：

高风险条件包括：
- match_type == keyword_overlap
- match_score < 0.75
- quote 文本长度过短
- quote 不包含字段值中的关键实体
- quote 来自 references section
- quote 来自 unrelated section
- quote_id page 与字段原始 page hint 相差过大
- 一个 quote 被过度复用支持多个不同字段
- product_source 字段的 quote 不含 PPP-B2b / B2b / IGS / CNES / RTS / CLAS 等关键产品词
- experiment_epoch 字段的 quote 不含日期、DOY、时间段或观测周期
- reproduction_blocker 的 quote 只证明“论文提到了数据/方法”，但不能证明“缺失复现信息”

五、对高风险 evidence 做局部 LLM audit

允许调用 DeepSeek，但只允许做 evidence support audit，不允许重新抽取论文。

每次输入：
- field_path
- field_value
- quote text
- quote page
- quote section
- original_model_quote if available

DeepSeek 只能输出：

{
  "field_path": "",
  "field_value": "",
  "quote_id": "",
  "support_status": "STRONG_SUPPORT | PARTIAL_SUPPORT | WEAK_SUPPORT | WRONG_SUPPORT | NEEDS_MANUAL_REVIEW",
  "reason": "",
  "suggested_action": "keep | downgrade_to_weak | replace_quote | manual_review | remove_if_non_required"
}

禁止 DeepSeek：
- 修改 field_value
- 新增事实
- 生成新 quote
- 删除 blocker
- 重写论文结论

六、处理 8 条 unresolved evidence

对目前 8 条 unresolved evidence 单独输出：

research_kb/reports/unresolved_evidence_review.md

每条包含：
- paper_id
- field_path
- field_value
- 原始 invalid quote
- top candidates 如果有
- 是否可人工确认
- 建议：manual_keep / manual_replace / mark_not_mentioned / leave_unresolved

七、生成最终 evidence audit 报告

输出：

research_kb/reports/evidence_support_audit.md

报告必须包含：

1. 总体 PASS / PASS_WITH_WEAK_EVIDENCE / BLOCKED。
2. 每篇论文 support_status 分布。
3. keyword_overlap evidence 中有多少被判为 STRONG / PARTIAL / WEAK / WRONG。
4. 高风险字段审计结果。
5. 8 条 unresolved evidence 的处理建议。
6. 是否有任何语义字段被修改；正常应为 0。
7. 哪些论文可以进入 corpus maps。
8. 哪些字段必须人工复核后再进入正式知识库。

八、更新通过规则

不要只用 invalid rate 判定通过。

新的通过条件：

- invalid_quote_id_rate < 5%
- WRONG_SUPPORT = 0
- 高风险字段 STRONG_SUPPORT + PARTIAL_SUPPORT >= 95%
- product_source、experiment_epoch、novelty_grade、reproduction_blockers 不能有 WRONG_SUPPORT
- unresolved evidence 不得影响关键字段
- 语义字段修改数必须为 0

如果满足条件：
- PASS

如果只有少量 keyword_overlap evidence 是 WEAK_SUPPORT，但不影响关键字段：
- PASS_WITH_WEAK_EVIDENCE

如果关键字段存在 WRONG_SUPPORT：
- BLOCKED
```

你现在的状态可以概括为：

```text
第一阶段：PDF 文本提取修复 ✅
第二阶段：quote_id repair ✅
第三阶段：evidence support audit ⬅️ 下一步
第四阶段：重新生成 corpus maps
第五阶段：扩大到 10–20 篇小批量
```

**最关键提醒**：不要因为 `<5% invalid rate` 就直接全量处理。你现在过的是“引用可解析”门槛，还要再过“引用确实支持结论”门槛。

-----

> [文件不支持导出]
> Evidence Support Audit 完成
>
>   总体结果
>
>   ┌────────────┬──────────────┬──────────┬──────────┬────────┬──────────┬────────┐
>   │    论文    │    Status    │ 正确支持 │ 部分支持 │ 弱支持 │ 错误支持 │ 待审核 │
>   ├────────────┼──────────────┼──────────┼──────────┼────────┼──────────┼────────┤
>   │ Ge Yulong  │ ❌  BLOCKED   │ 73       │ 113      │ 39     │ 4        │ 1      │
>   ├────────────┼──────────────┼──────────┼──────────┼────────┼──────────┼────────┤
>   │ Maosen Hao │ ⚠️ PASS_WEAK │ 52       │ 62       │ 22     │ 0        │ 1      │
>   ├────────────┼──────────────┼──────────┼──────────┼────────┼──────────┼────────┤
>   │ Ruohua Lan │ ⚠️ PASS_WEAK │ 93       │ 144      │ 32     │ 0        │ 6      │
>   └────────────┴──────────────┴──────────┴──────────┴────────┴──────────┴────────┘
>
>   关键发现
>
>   Ge Yulong — 4 条 WRONG_SUPPORT：
>   - product_source.actual_product_source = BDS3_PPP_B2B_BROADCAST
>   - 但 4 条 supporting quote 都指向 MIXED_PRODUCTS（CNES、"and"、"comparison"）
>   - DeepSeek 分类与证据矛盾：论文实际使用 B2b+CNES 混合产品，应标记为 MIXED_PRODUCTS
>   - 这是一个真实的分类错误，不是 quote repair 问题
>
>   Maosen Hao — 22 条 WEAK（非阻断）：
>   - experiment_epoch: 3 条 quote 不含日期
>   - ionospheric_handling: 5 条（DCB 相关，属正常 QZSS CLAS 论文）
>   - reproducibility: 5 条（quote 显示信息存在而非缺失，与 blocker 矛盾）
>
>   Ruohua Lan — 32 条 WEAK（非阻断）：
>   - experiment_epoch: 5 条不含日期
>   - product_source: 4 条缺产品关键词
>   - datasets/metrics: 多处来自 references section
>
>   8 条 Unresolved Evidence
>
>   详见 research_kb/reports/unresolved_evidence_review.md
>
>   语义字段完整性
>
>   0 字段被修改（backup 与 repaired 全字段比对通过）

这次审计结果很好，因为它发现了一个真正的问题：**Ge Yulong 不是 quote repair 问题，而是语义分类错误**。报告里明确写到 Ge Yulong 有 4 条 `WRONG_SUPPORT`，都集中在 `product_source`，证据指向 CNES / final products / comparison 等混合产品，而不是纯 `BDS3_PPP_B2B_BROADCAST`。fileciteturn1file0L31-L62

下一步不要再修 quote，也不要重跑 chunk。应该进入 **targeted semantic correction**。

你可以把下面这段给 Claude Code：

```text id="0gmby5"
现在不要重新生成 chunk，不要重新调用 DeepSeek extraction，也不要重跑 quote repair。

Evidence Support Audit 已完成。当前结论：

1. Ge Yulong 被 BLOCKED，原因是 product_source 存在 4 条 WRONG_SUPPORT。
2. 这不是 quote repair 问题，而是真实语义分类错误。
3. 当前字段 product_source.actual_product_source = BDS3_PPP_B2B_BROADCAST。
4. 但 supporting quotes 指向 MIXED_PRODUCTS：论文使用/比较了 PPP-B2b、CNES real-time products、final products、ultra-rapid products 等。
5. Maosen Hao 和 Ruohua Lan 当前为 PASS_WITH_WEAK_EVIDENCE，不需要修改语义字段，只需要保留 weak evidence 标记。
6. unresolved evidence 共 8 条，建议均为 manual_replace。

你的任务是做 targeted semantic correction，只允许修正 Evidence Support Audit 已明确证明错误的字段。

输入：
- research_kb/papers/json_repaired/
- research_kb/papers/yaml_repaired/
- research_kb/reports/evidence_support_audit.md
- research_kb/reports/unresolved_evidence_review.md
- research_kb/quote_bank/

输出：
- research_kb/papers/json_corrected/
- research_kb/papers/yaml_corrected/
- research_kb/reports/semantic_correction_report.md
- research_kb/metadata/semantic_corrections.yaml

绝对禁止：
1. 不要重新 PDF extraction。
2. 不要重新生成 chunks。
3. 不要重新调用 DeepSeek chunk extraction。
4. 不要重写整篇 paper JSON。
5. 不要批量修改语义字段。
6. 不要为了通过验证删除 evidence。
7. 不要把 weak evidence 自动升级为 strong evidence。
8. 不要修改 Maosen Hao 和 Ruohua Lan 的语义字段。

一、创建 correction layer

创建：

research_kb/metadata/semantic_corrections.yaml

记录所有语义修正，不要静默覆盖。

格式：

corrections:
  - paper_id: "Ge_yulong_2024_an_investigation_ofppp_time_transfer_viabds3_pppb2b_service"
    field_path: "product_source.actual_product_source"
    old_value: "BDS3_PPP_B2B_BROADCAST"
    new_value: "MIXED_PRODUCTS"
    correction_type: "evidence_support_audit_semantic_error"
    reason: "Evidence support audit found 4 WRONG_SUPPORT items: supporting quotes indicate mixed use/comparison of PPP-B2b, CNES real-time products, final products, and ultra-rapid products rather than pure BDS-3 PPP-B2b broadcast-only product source."
    source_report: "research_kb/reports/evidence_support_audit.md"
    evidence_quote_ids: []
    status: "applied"

二、只修正 Ge Yulong 的 product_source

在 Ge Yulong 的 corrected JSON/YAML 中，将：

product_source.actual_product_source

从：

"BDS3_PPP_B2B_BROADCAST"

改为：

"MIXED_PRODUCTS"

同时检查是否存在类似字段，例如：
- gnss_domain_tags.product_source
- product_source.category
- product_source.is_core_ppp_b2b
- is_ppp_b2b_core_paper
- corpus_classification

如果这些字段与 MIXED_PRODUCTS 冲突，只允许做最小一致性修正，并全部写入 semantic_corrections.yaml。

建议规则：
- actual_product_source = MIXED_PRODUCTS
- is_core_ppp_b2b 或 is_ppp_b2b_core_paper 不一定改为 false；如果论文主体仍研究 PPP-B2b，但使用外部产品对比，可保持 true 或改为 "core_ppp_b2b_with_external_comparison"
- 不要把它误标为 NON_B2B_EXTERNAL_PRODUCTS
- corpus 分类应为 "core_ppp_b2b_with_mixed_products" 或类似边界类别

三、不要修改 Maosen Hao 和 Ruohua Lan 的语义字段

对 Maosen Hao：
- 保持 PASS_WITH_WEAK_EVIDENCE
- 不改 product_source
- 不改 novelty_grade
- 不改 experiment_epoch
- 保留 weak evidence 标记

对 Ruohua Lan：
- 保持 PASS_WITH_WEAK_EVIDENCE
- 不改 product_source
- 不改 novelty_grade
- 不改 experiment_epoch
- 保留 weak evidence 标记

四、处理 8 条 unresolved evidence

不要自动猜。

根据 unresolved_evidence_review.md，将 8 条 unresolved evidence 记录到：

research_kb/metadata/manual_review_queue.yaml

每条包含：
- paper_id
- field_path
- original_quote
- suggestion: manual_replace
- status: pending_manual_review

如果这些 unresolved evidence 不影响关键字段 product_source、experiment_epoch、novelty_grade、reproduction_blockers，则不要阻断 corpus maps。

五、重新运行 validator

基于 corrected JSON/YAML 运行 validate。

新的准入规则：

1. invalid_quote_id_rate < 5%
2. WRONG_SUPPORT = 0
3. 关键字段无 WRONG_SUPPORT：
   - product_source
   - experiment_epoch
   - novelty_grade
   - reproduction_blockers
   - ionospheric_handling
4. unresolved evidence 不影响关键字段
5. weak evidence 可以存在，但必须保留标记
6. semantic corrections 必须可追溯

预期结果：
- Ge Yulong: PASS_WITH_CORRECTION 或 PASS_WITH_WEAK_EVIDENCE
- Maosen Hao: PASS_WITH_WEAK_EVIDENCE
- Ruohua Lan: PASS_WITH_WEAK_EVIDENCE

六、重新生成 corpus maps

只有在 corrected validate 通过后，重新生成：

research_kb/maps/technical_routes.yaml
research_kb/maps/problem_evolution.yaml
research_kb/maps/citation_graph.json
research_kb/maps/method_lineage.yaml
research_kb/maps/dataset_metric_index.yaml
research_kb/maps/reproduction_index.yaml

要求：
- 使用 json_corrected 作为输入。
- 不使用原始 BLOCKED JSON。
- 在 corpus_index 中记录每篇论文状态：
  - PASS_WITH_CORRECTION
  - PASS_WITH_WEAK_EVIDENCE
  - BLOCKED
- Ge Yulong 的产品源必须显示为 MIXED_PRODUCTS 或 core_ppp_b2b_with_mixed_products，不得显示为纯 BDS3_PPP_B2B_BROADCAST。

七、生成 semantic_correction_report.md

报告必须包含：

1. 修改了哪些字段。
2. 每个字段的 old_value / new_value。
3. 修改原因。
4. 使用的 evidence audit 证据。
5. 是否修改了非目标字段。
6. Maosen Hao / Ruohua Lan 是否保持语义字段不变。
7. 8 条 unresolved evidence 是否进入 manual_review_queue。
8. corrected validate 结果。
9. corpus maps 是否重新生成。
```

你现在的阶段判断是：

```text id="4z1m7d"
Quote 可解析性：已通过
Evidence 支持性：发现 1 个真实语义错误
下一步：定点修 Ge Yulong product_source
之后：重新生成 corpus maps
```

另外，`unresolved_evidence_review` 里 8 条都建议 `manual_replace`，主要集中在 `correction_types`、`ionospheric_handling`、`datasets`、`metrics`，不是目前最核心的产品源分类问题。fileciteturn1file1L1-L14

所以现在不要全量处理。先把 **Ge Yulong 的 product_source 语义错误修正并记录成 correction layer**，再让 3 篇 pilot 全部进入 corpus maps。

-----

> [文件不支持导出]
> ●---
>   Targeted Correction 完成
>
>   修改内容
>
>   ┌────────────┬──────────────────────────────────────┬────────────────────────┬────────────────┐
>   │    论文    │                 字段                 │          旧值          │      新值      │
>   ├────────────┼──────────────────────────────────────┼────────────────────────┼────────────────┤
>   │ Ge Yulong  │ product_source.actual_product_source │ BDS3_PPP_B2B_BROADCAST │ MIXED_PRODUCTS │
>   ├────────────┼──────────────────────────────────────┼────────────────────────┼────────────────┤
>   │ Ge Yulong  │ product_source.conflict_flag         │ false                  │ true           │
>   ├────────────┼──────────────────────────────────────┼────────────────────────┼────────────────┤
>   │ Maosen Hao │ —                                    │ 无修改                 │ —              │
>   ├────────────┼──────────────────────────────────────┼────────────────────────┼────────────────┤
>   │ Ruohua Lan │ —                                    │ 无修改                 │ —              │
>   └────────────┴──────────────────────────────────────┴────────────────────────┴────────────────┘
>
>   Corrected Validate
>
>   ┌────────────┬────────────────────────────────┐
>   │    论文    │             Status             │
>   ├────────────┼────────────────────────────────┤
>   │ Ge Yulong  │ PASS (PASS_WITH_CORRECTION)    │
>   ├────────────┼────────────────────────────────┤
>   │ Maosen Hao │ PASS (PASS_WITH_WEAK_EVIDENCE) │
>   ├────────────┼────────────────────────────────┤
>   │ Ruohua Lan │ PASS (PASS_WITH_WEAK_EVIDENCE) │
>   └────────────┴────────────────────────────────┘
>
>   3/3 PASS，0 BLOCKED，corpus maps 已生成。

很好，现在这个 pilot 已经从“抽取失败”推进到 **可控通过** 了。当前状态可以这样判断：

```text
PDF 提取问题：已解决到可用水平
Quote repair：已通过
Evidence support audit：已发现并修正真实语义错误
3-paper pilot：3/3 PASS
但正式入库前仍是 Overall WARN
```

报告里显示，Ge Yulong 的 `product_source.actual_product_source` 已从 `BDS3_PPP_B2B_BROADCAST` 修正为 `MIXED_PRODUCTS`，`conflict_flag` 也改为 `true`；3 篇论文都已进入 corpus maps，但仍有 13 个 manual review 项，其中 8 个 unresolved evidence、5 个 keyword overlap low confidence。fileciteturn2file0L8-L37 fileciteturn2file0L64-L70

下一步不要立刻全量跑。你现在应该让 Claude Code 做 **pilot freeze + manual review closure + scale test**。

---

## 下一步给 Claude Code 的指令

直接发这个：

```text
现在 3-paper pilot 已通过 targeted semantic correction。下一步不要重新生成 chunks，不要重新跑 DeepSeek extraction，不要修改已经通过审计的语义字段。

你的任务是做 pilot freeze、manual review closure 和小批量扩展准备。

输入：
- research_kb/papers/json_repaired/
- research_kb/papers/yaml_repaired/
- research_kb/reports/quote_repair_report.md
- research_kb/reports/evidence_support_audit.md
- research_kb/reports/semantic_correction_report.md
- research_kb/manual_review_queue.yaml
- research_kb/maps/

目标：
把当前 3-paper pilot 固化为 v0.1 baseline，并清理进入正式知识库前必须处理的风险项。

请按以下步骤执行。

一、冻结当前 pilot 版本

创建：

research_kb/releases/pilot_v0.1/

复制以下内容进去：
- repaired JSON
- repaired YAML
- corpus maps
- quote banks
- reports
- manual_review_queue.yaml
- validate log
- semantic_correction_report.md

生成：

research_kb/releases/pilot_v0.1/manifest.json

manifest 必须包含：
- release_name
- generation_time
- paper_count
- pass_count
- blocked_count
- pass_with_correction_count
- pass_with_weak_evidence_count
- semantic_field_corrections
- manual_review_item_count
- corpus_map_files
- pipeline_config_summary
- known_limitations

二、处理 manual_review_queue

读取 manual_review_queue.yaml。

对 13 个 item 分类：

1. unresolved_evidence
2. keyword_overlap_low_confidence
3. critical_field
4. non_critical_field
5. can_enter_corpus_with_warning
6. must_fix_before_corpus

注意：
- 不要删除 manual review item。
- 不要为了通过而降低风险级别。
- 不要自动修改语义字段。
- 对 metrics / formulas / datasets 类 evidence，如果只是证据弱但字段不影响 product_source、experiment_epoch、novelty_grade、reproduction_blockers，可标记为 non_critical_weak_evidence。
- 对 product_source、experiment_epoch、novelty_grade、reproduction_blockers、dcb_missing_flag 相关 item，必须标记为 critical_field。

输出：

research_kb/reports/manual_review_triage.md

三、建立正式准入规则

创建：

research_kb/metadata/admission_policy.yaml

规则包括：

1. PASS
   - invalid_quote_id_rate < 5%
   - WRONG_SUPPORT = 0
   - critical_field unresolved = 0
   - semantic_conflict = 0 或已显式 conflict_flag
   - grounding issues = 0

2. PASS_WITH_CORRECTION
   - 允许 targeted semantic correction
   - 必须记录 old_value、new_value、evidence、reason
   - correction 不得超过高风险字段审计已证明的范围

3. PASS_WITH_WEAK_EVIDENCE
   - 允许非关键字段存在 weak evidence
   - 必须进入 manual_review_queue
   - 不得影响 corpus maps 的核心分类

4. BLOCKED
   - WRONG_SUPPORT > 0 且未修正
   - product_source 与 evidence 冲突
   - experiment_epoch 无任何有效证据
   - quote_id 无法解析
   - 核心字段 unsupported

四、更新 corpus index

更新：

research_kb/metadata/corpus_index.json
research_kb/metadata/corpus_index.yaml

每篇论文必须包含：

- paper_id
- title
- year
- status
- admission_status
- correction_status
- weak_evidence_count
- unresolved_evidence_count
- manual_review_required
- product_source.actual_product_source
- product_source.conflict_flag
- novelty_grade
- reproduction_score
- included_in_maps

五、重新生成 corpus maps，但加 status 标记

重新生成 maps：

- technical_routes.yaml
- problem_evolution.yaml
- citation_graph.json
- method_lineage.yaml
- dataset_metric_index.yaml
- reproduction_index.yaml

要求：
每个 paper node 必须带：
- admission_status
- evidence_quality
- correction_status

不要把 PASS_WITH_WEAK_EVIDENCE 伪装成完全干净的 PASS。

六、生成小批量扩展计划

创建：

research_kb/reports/scale_test_plan.md

计划下一批处理 10 篇论文，而不是全量处理。

要求：
- 选择 10 篇时覆盖 core_ppp_b2b、boundary_ppp_ssr、non_b2b_augmentation 三类
- 每批最多 10 篇
- 如果 BLOCKED rate > 20%，停止扩展
- 如果 WRONG_SUPPORT 出现在 product_source，停止扩展并修 prompt/schema
- 如果 quote repair 后 invalid rate > 5%，停止扩展
- 如果 keyword_overlap evidence 占比 > 50%，触发 stricter quote selection

七、输出最终状态报告

生成：

research_kb/reports/pilot_v0.1_final_status.md

报告必须包含：
1. 3-paper pilot 总结
2. 已解决的问题
3. 仍存在的风险
4. Ge Yulong correction 记录
5. 13 个 manual review item 摘要
6. corpus maps 是否可用
7. 是否允许进入 10-paper scale test
8. 下一步明确命令
```

---

## 你现在的决策

我建议你把当前状态定为：

```text
pilot_v0.1 = ACCEPTED_WITH_WARNINGS
```

不是完全干净的 `PASS`，因为报告里还有：

```text
Overall: WARN
13 manual review items
PASS_WITH_CORRECTION / PASS_WITH_WEAK_EVIDENCE
```

但它已经足够支持下一阶段：**10 篇小批量扩展**。

不要现在全量跑 50 篇或 100 篇。下一步最合理的是：

```text
3-paper pilot freeze
→ manual review triage
→ admission policy 固化
→ 10-paper scale test
→ 如果通过，再进入 30–50 篇
```

最重要的一点：**这次 Ge Yulong 的错误非常有价值**。它证明你的 evidence support audit 真的能抓出语义分类错，而不只是修 quote。这个流程应该保留为正式 pipeline 的强制门控。

-----

> [文件不支持导出]
> ●核心步骤均成功。生成最终状态报告。
>
> ●Write(research_kb\reports\pilot_v0.1_final_status.md)
>   ⎿  Wrote 112 lines to research_kb\reports\pilot_v0.1_final_status.md
>        1 # Pilot v0.1 Final Status Report
>        2
>        3 生成：2026-05-21
>        4 冻结位置：`research_kb/releases/pilot_v0.1/`
>        5
>        6 ---
>        7
>        8 ## 1. 3-Paper Pilot 总结
>        9
>       10 | 论文 | 选择角色 | product_source | novelty | repro score | Status |
>      … +107 lines (ctrl+o to expand)
>
>  Searched for 1 pattern (ctrl+o to expand)
>
> ●---
>   Pilot v0.1 Freeze Complete
>
>   发布内容 (29 files)
>
>   ┌─────────────────┬────────┬─────────────────────────────────────┐
>   │      类别       │ 文件数 │                位置                 │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Repaired JSON   │ 3      │ releases/pilot_v0.1/json/           │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Corrected JSON  │ 3      │ releases/pilot_v0.1/json_corrected/ │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Repaired YAML   │ 3      │ releases/pilot_v0.1/yaml/           │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Corrected YAML  │ 3      │ releases/pilot_v0.1/yaml_corrected/ │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Corpus maps     │ 6      │ releases/pilot_v0.1/corpus/         │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Quote banks     │ 3      │ releases/pilot_v0.1/quote_banks/    │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Reports         │ 6      │ releases/pilot_v0.1/reports/        │
>   ├─────────────────┼────────┼─────────────────────────────────────┤
>   │ Manifest + logs │ 2      │ releases/pilot_v0.1/                │
>   └─────────────────┴────────┴─────────────────────────────────────┘
>
>   Expansion Readiness: ✅  READY
>
>   ┌───────────────────────┬───────────────────────┐
>   │         Check         │        Result         │
>   ├───────────────────────┼───────────────────────┤
>   │ 3/3 pilot pass        │ ✅                     │
>   ├───────────────────────┼───────────────────────┤
>   │ invalid quote_id rate │ ✅  0 grounding issues │
>   ├───────────────────────┼───────────────────────┤
>   │ no WRONG_SUPPORT      │ ✅                     │
>   ├───────────────────────┼───────────────────────┤
>   │ keyword_overlap ratio │ ⚠️ 60.3% (>50%)       │
>   ├───────────────────────┼───────────────────────┤
>   │ manual review pending │ 13 items              │
>   └───────────────────────┴───────────────────────┘
>
>   ⚠️ 1 warning: keyword_overlap evidence 占 60.3%，strict quote rules 已生效。
>
>   Pre-expansion candidates
>
>   20 papers scanned, top picks:
>   1. Yan Liu 2022 — Comprehensive Analyses of PPP-B2b (score=10)
>   2. Jianfei Zang 2024 — Performance assessment of BDS-3 PPP-B2b (score=10)
>   3. Yangyuanxi 2022 — Principle and performance of BDSBAS-B2b (score=10)
>   4. Tang Chenggan 2022 — Orbit determination, clock estimation (score=10)
>   5. Zhao Lewen 2025 — Python toolbox for BDS B2b (score=10)

可以进入 **10-paper scale test**，但我建议你不要直接用普通全量模式跑，而是用 **受控扩展模式**。你现在的 v0.1 已经可以冻结：3/3 pilot 通过、0 grounding issues、无 WRONG_SUPPORT，corpus maps 已生成；但仍有 60.3% keyword_overlap evidence 和 13 个 manual review items，所以扩展时必须加熔断。fileciteturn3file0

给 Claude Code 的下一条指令可以这样写：

```text id="ndz7gt"
Pilot v0.1 已冻结，不要再修改 releases/pilot_v0.1/ 下的任何文件。

现在进入 10-paper scale test，但必须使用受控扩展模式，不允许直接全量处理。

目标：
在不破坏 pilot_v0.1 release 的前提下，处理下一批 10 篇候选论文，验证 pipeline 是否可扩展。

输入：
- paper/
- research_kb/releases/pilot_v0.1/
- scripts/update_kb.py
- scripts/_scale_test.py
- 当前 quote_bank / validate / evidence_support_audit 规则

输出：
- research_kb/releases/scale_test_10/
- research_kb/reports/scale_test_10_status.md

严格要求：

1. 不要修改 pilot_v0.1 release
   - releases/pilot_v0.1/ 只读
   - 所有新结果写入 releases/scale_test_10/

2. 使用 strict quote rules
   - LLM 不允许自由生成 quote
   - 只能选择 quote_bank quote_id
   - quote text 必须由程序从 quote_bank 回填
   - keyword_overlap_low_confidence 不允许支持关键字段

3. 关键字段不得使用低置信 keyword_overlap 证据
   以下字段必须至少 PARTIAL_SUPPORT，且不能依赖 low-confidence keyword_overlap：
   - product_source.actual_product_source
   - experiment_epoch
   - novelty_grade
   - reproduction_blockers
   - dcb_missing_flag / ionospheric_handling
   - mathematical_model
   - main_results

4. 设置熔断条件
   任一论文出现以下情况，立即暂停 scale test，不要继续处理剩余论文：
   - invalid_quote_id_rate > 5%
   - WRONG_SUPPORT > 0 且涉及关键字段
   - product_source 证据矛盾
   - experiment_epoch 被 publication_year 或 received/revised date 误用
   - keyword_overlap evidence ratio > 70%
   - DeepSeek JSON failure 重试后仍失败
   - 某篇论文 needs_manual_review 项 > 10

5. 每处理完 1 篇论文，立即生成 per-paper mini report
   保存到：
   research_kb/releases/scale_test_10/reports/per_paper/

   每篇报告必须包含：
   - paper_id
   - product_source
   - is_core_ppp_b2b
   - experiment_epoch
   - novelty_grade
   - reproduction_score
   - invalid_quote_id_rate
   - keyword_overlap ratio
   - STRONG / PARTIAL / WEAK / WRONG support 数量
   - unresolved evidence 数量
   - PASS / PASS_WITH_WEAK_EVIDENCE / PASS_WITH_CORRECTION / BLOCKED

6. 10 篇完成后再生成 corpus maps
   不要边处理边把不稳定论文写入正式 corpus maps。
   只有 PASS / PASS_WITH_WEAK_EVIDENCE / PASS_WITH_CORRECTION 的论文进入 maps。
   BLOCKED 论文排除。

7. 保留人工审核队列
   生成：
   research_kb/releases/scale_test_10/manual_review_queue.yaml

   每条 item 必须包含：
   - paper_id
   - field_path
   - reason
   - quote_id
   - quote
   - suggested_action
   - severity

8. 生成最终 scale test 报告
   输出：
   research_kb/reports/scale_test_10_status.md

   必须包含：
   - 10 篇候选清单
   - 实际完成数量
   - PASS / BLOCKED 数量
   - 平均 invalid_quote_id_rate
   - 平均 keyword_overlap ratio
   - WRONG_SUPPORT 数量
   - product_source 错误数量
   - experiment_epoch 错误数量
   - manual review item 数量
   - 是否允许进入 30-paper batch
   - 需要修改的 pipeline 问题

9. 不要自动进入 30-paper 或全量处理
   scale_test_10 完成后停止，等待我确认。
```

然后执行命令建议用这个，而不是直接全量：

```bash
python scripts/update_kb.py --papers 10 --mode scale_test --release scale_test_10 --strict_quote_rules --stop_on_wrong_support
```

你现在最重要的策略是：

```text id="wp1syb"
v0.1 已经证明 pipeline 能跑通；
scale_test_10 要证明 pipeline 不会在更多论文上系统性漂移。
```

尤其要盯住两个指标：

```text id="fa4xmp"
keyword_overlap ratio 是否继续 >60%
product_source 是否还会出现 Ge Yulong 这种“证据指向 MIXED，但字段写成 pure B2b”的错误
```

如果 10 篇里 **WRONG_SUPPORT = 0**，且 keyword_overlap 能压到 **<40–50%**，你再进入 30-paper batch 会比较稳。

-----

> ●9 papers processed (118+ chunks ready). Peida Wu 单独补上较慢，先汇报现状。
>
>   10-Paper Scale Test — Step 1 完成：PDF → Markdown → Chunks
>
>   ┌─────┬────────────────────┬─────────────────────┬───────┬────────┐
>   │  #  │       Paper        │         Cat         │ Pages │ Chunks │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 1   │ Yan Liu 2022       │ core_ppp_b2b        │ 28    │ 28     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 2   │ Jianfei Zang 2024  │ core_ppp_b2b        │ 14    │ 14     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 3   │ Pan Lin 2025       │ boundary_mixed      │ 11    │ 11     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 4   │ Zhao Lewen 2025    │ core_ppp_b2b_tool   │ 10    │ 10     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 5   │ Tang Chenggan 2022 │ related_orbit       │ 17    │ 17     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 6   │ Pedro Pintor 2023  │ non_b2b_galileo     │ 13    │ 13     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 7   │ Zhou Linghao 2025  │ ppp_b2b_application │ 15    │ 15     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 8   │ Taro Suzuki 2023   │ non_b2b_qzss        │ 14    │ 14     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 9   │ Yangyuanxi 2022    │ related_sbas        │ 10    │ 10     │
>   ├─────┼────────────────────┼─────────────────────┼───────┼────────┤
>   │ 10  │ Peida Wu 2023      │ related_rtk         │ ⏳     │ ⏳      │
>   └─────┴────────────────────┴─────────────────────┴───────┴────────┘
>
>   ~132 chunks ready for DeepSeek extraction（预估 2.5-4 小时）
>
>   是否启动 DeepSeek extraction？还是调整选文？

我建议**不要直接一次性启动 132 个 chunks 的完整 DeepSeek extraction**。Pilot 虽然已 READY，但你还有一个关键风险：keyword_overlap evidence 之前占比 60.3%，所以 10-paper 阶段应该分批、带中止门槛跑。

建议：**启动 DeepSeek extraction，但不要一次性全量启动。**

你现在的选文结构是合理的，不需要马上调整。9 篇里已经覆盖了：

```text
core_ppp_b2b
boundary_mixed
core_ppp_b2b_tool
related_orbit
non_b2b_galileo
non_b2b_qzss
related_sbas
ppp_b2b_application
```

这正好适合测试分类边界。真正要控制的是 **运行方式**：分批、设中止条件、强制 quote_bank evidence。你之前 Pilot v0.1 已经允许进入 10-paper scale test，但条件是 strict quote rules 生效、invalid rate 超过 5% 立即停止。fileciteturn3file0

你可以直接给 Claude Code 下面这段指令：

```text
不要一次性全量启动 132 chunks 的 DeepSeek extraction。

现在进入 10-paper scale test 的 Step 2，但采用 staged extraction + gate validation。

目标：
在不重跑 PDF → Markdown → chunks 的前提下，复用当前已生成的 markdown、chunks、quote_bank，分批调用 DeepSeek，验证 10-paper 扩展稳定性。

一、不要调整选文

当前 9 篇先跑，不等待 Peida Wu。
Peida Wu 作为 late-add paper，等当前 9 篇通过第一轮 gate 后再补入。

当前 9 篇保留：
1. Yan Liu 2022 — core_ppp_b2b
2. Jianfei Zang 2024 — core_ppp_b2b
3. Pan Lin 2025 — boundary_mixed
4. Zhao Lewen 2025 — core_ppp_b2b_tool
5. Tang Chenggan 2022 — related_orbit
6. Pedro Pintor 2023 — non_b2b_galileo
7. Zhou Linghao 2025 — ppp_b2b_application
8. Taro Suzuki 2023 — non_b2b_qzss
9. Yangyuanxi 2022 — related_sbas

二、运行方式：分三批

Batch A：先跑 3 篇 sentinel papers
- Yan Liu 2022，core_ppp_b2b
- Pan Lin 2025，boundary_mixed
- Pedro Pintor 2023 或 Taro Suzuki 2023，non_b2b

目的：
先测试 product_source 分类、PPP-B2b / non-B2b 边界、quote repair 是否稳定。

Batch B：如果 Batch A 通过，再跑 3 篇
- Jianfei Zang 2024
- Zhao Lewen 2025
- Tang Chenggan 2022

Batch C：最后跑剩余 3 篇
- Zhou Linghao 2025
- Taro Suzuki 2023 或 Pedro Pintor 2023
- Yangyuanxi 2022

Peida Wu 2023 暂时不阻塞当前 scale test。等 Step 2 初步完成后再作为 Batch D 补跑。

三、严格禁止

1. 不要重新生成 chunks。
2. 不要重新做 PDF extraction。
3. 不要覆盖 pilot_v0.1 release。
4. 不要让 DeepSeek 自由生成 grounding quote。
5. 不要把 keyword_overlap evidence 自动用于关键字段强判定。
6. 不要在 validate 失败后自动放宽阈值。
7. 不要把 non-B2b 论文误归入 core_ppp_b2b。

四、DeepSeek extraction 必须使用 quote_bank 机制

DeepSeek 只能输出：
- structured field values
- grounding_quote_ids
- uncertainty
- needs_manual_review

禁止输出自由文本 quote。

如果找不到支持字段的 quote_id，必须输出：
- NOT_MENTIONED
- INSUFFICIENT_EVIDENCE
- needs_manual_review

不要让模型自己编 quote。

五、关键字段必须强审计

每篇论文必须重点检查：

1. product_source.actual_product_source
2. product_source.conflict_flag
3. is_core_ppp_b2b
4. experiment_epoch
5. correction_types
6. mathematical_model
7. ionospheric_handling
8. dcb_missing_flag
9. novelty_grade
10. reproduction_blockers

尤其注意：
- PPP-B2b broadcast correction
- IGS RTS / CLK93
- CNES products
- final / ultra-rapid products
- QZSS CLAS
- Galileo HAS
- BDSBAS-B2b
- RTK / PPP-RTK

六、每批完成后立即 gate validation

每一批完成后，立刻运行：

1. quote_id validation
2. evidence support audit
3. product_source boundary audit
4. experiment_epoch audit
5. reproduction blocker sanity check
6. corpus inclusion check

每批输出报告：

research_kb/reports/scale_test_batch_A_report.md
research_kb/reports/scale_test_batch_B_report.md
research_kb/reports/scale_test_batch_C_report.md

七、中止条件

如果任何一批出现以下情况，立即停止后续 batch：

1. invalid_quote_id_rate > 5%
2. WRONG_SUPPORT > 0 on critical fields
3. product_source 误分类数量 >= 1
4. non-B2b paper 被归入 core_ppp_b2b
5. experiment_epoch 使用 publication year 或接收日期
6. keyword_overlap evidence 在关键字段中占比 > 30%
7. DeepSeek JSON failure rate > 20%
8. 单篇论文 unresolved evidence > 15

停止后不要继续跑剩余论文，先生成 failure report。

八、通过条件

Batch 通过条件：

1. invalid_quote_id_rate < 5%
2. product_source 无错误分类
3. WRONG_SUPPORT = 0 for critical fields
4. non-B2b / related papers 不进入 core_ppp_b2b
5. experiment_epoch 不误用 publication_year
6. 所有关键字段至少有 STRONG 或 PARTIAL support
7. 语义修正必须记录到 semantic_correction_report_scale_test.md

九、运行参数建议

使用低并发，避免 API 不稳定：

CONCURRENCY=3
MAX_RETRIES=3
TEMPERATURE=0
MAX_TOKENS=8192
BATCH_SIZE=3 papers

保留所有中间结果：
- chunk analysis
- paper json
- quote repair output
- evidence audit output
- validation logs

十、先执行 Batch A

现在只启动 Batch A，不要直接跑全部 9 篇。

Batch A 完成后输出：
1. 每篇论文 DeepSeek 调用成功率
2. JSON parse failure rate
3. invalid_quote_id_rate
4. keyword_overlap ratio
5. product_source 判定
6. WRONG_SUPPORT 数量
7. 是否允许进入 Batch B

如果 Batch A PASS，再继续 Batch B。
```

我的建议很明确：

```text
不要调整选文。
不要等待 Peida Wu。
不要全量启动。
先跑 Batch A 三篇 sentinel papers。
```

如果 Batch A 通过，再让 Claude Code 继续 Batch B/C。这样即使有问题，也只损失 30–50 个 chunks，而不是一次性烧完整个 132 chunks。

-----

> Batch A 状态报告 — 提取受阻
>
>   执行情况
>
>   ┌─────────────────────┬──────────────────────────────────────────┐
>   │        指标         │                   结果                   │
>   ├─────────────────────┼──────────────────────────────────────────┤
>   │ PDF → Markdown      │ ✅  9/10 papers (118 chunks ready)        │
>   ├─────────────────────┼──────────────────────────────────────────┤
>   │ Quote banks         │ ✅  3 Batch A papers                      │
>   ├─────────────────────┼──────────────────────────────────────────┤
>   │ DeepSeek extraction │ ⚠️ 26/28 Yan Liu chunks processed (~93%) │
>   ├─────────────────────┼──────────────────────────────────────────┤
>   │ 耗时                │ ~3.5 小时                                │
>   ├─────────────────────┼──────────────────────────────────────────┤
>   │ 平均每 chunk        │ ~8 分钟                                  │
>   ├─────────────────────┼──────────────────────────────────────────┤
>   │ 预估 Batch A 全量   │ ~7 小时 (52 chunks)                      │
>   └─────────────────────┴──────────────────────────────────────────┘
>
>   受阻原因
>
>   DeepSeek API 调用延迟过高（每 chunk 3-8 分钟），导致单篇 28-page 论文就需要 3+ 小时提取。对于 10-paper scale
>   test（~132 chunks），预计需要 15-20 小时连续运行。
>
>   当前可用的 10-paper 扩展资产
>
>   ┌─────────────────┬─────────────┬────────────────────────────┐
>   │      资产       │    状态     │            位置            │
>   ├─────────────────┼─────────────┼────────────────────────────┤
>   │ Markdown (fitz) │ ✅  9 papers │ scale_test_10/markdown/    │
>   ├─────────────────┼─────────────┼────────────────────────────┤
>   │ Chunks          │ ✅  9 papers │ scale_test_10/chunks/      │
>   ├─────────────────┼─────────────┼────────────────────────────┤
>   │ Quote banks     │ ✅  3 papers │ scale_test_10/quote_banks/ │
>   ├─────────────────┼─────────────┼────────────────────────────┤
>   │ Pilot v0.1      │ ✅  frozen   │ releases/pilot_v0.1/       │
>   └─────────────────┴─────────────┴────────────────────────────┘
>
>   建议
>
>   目前 pipeline 的 PDF→Markdown→Chunks 阶段已证明可扩展（9 papers，无失败）。真正的瓶颈是 DeepSeek API 延迟。要继续
>   scale test，需要：
>
>   1. 降低并发等待时间（去掉 sleep(0.2)，因为 API 本身已经够慢）
>   2. 减少每篇论文的 chunk 数（增大 MAX_CHUNK_CHARS）
>   3. 或者接受 overnight extraction（后台持续运行 10-15 小时）
>
>   是否调整策略？

建议调整。现在不是选文问题，而是 extraction 调用策略问题；继续按 1 chunk = 1 次完整科研审计跑，会把 scale test 变成 API 耐力测试。

要调整。**不要接受 overnight extraction 作为主策略**，否则你只是在测试 DeepSeek 延迟，不是在测试知识库 pipeline。

核心改法是：

```text
不重跑已完成的 26/28 chunks
不调整选文
不继续按 1 chunk = 1 DeepSeek 完整审计
改成 speed-rescue mode：
先完成 Yan Liu 剩余 2 chunks → 合并验证 Yan Liu
然后对剩余 Batch A 采用 paper-level / section-level lite extraction
```

给 Claude Code 发这段：

```text
现在暂停继续按 chunk-by-chunk full extraction 跑 Batch A。

当前问题不是 PDF、Markdown、chunk、quote_bank，而是 DeepSeek extraction 延迟过高：
- Yan Liu 26/28 chunks 已完成
- 平均每 chunk 约 8 分钟
- 如果继续 1 chunk = 1 full audit，10-paper scale test 会变成 15-20 小时 API 耐力测试

现在进入 scale_test_10_speed_rescue mode。

绝对禁止：
1. 不要重跑已完成的 26 个 Yan Liu chunk extraction。
2. 不要删除或覆盖已有 chunk outputs。
3. 不要重新 PDF → Markdown。
4. 不要重新生成已有 chunks。
5. 不要修改 pilot_v0.1 release。
6. 不要让 DeepSeek 自由生成 quote。
7. 不要继续无脑跑完全部 132 chunks。

一、先保存当前状态

创建：

research_kb/releases/scale_test_10/checkpoints/batch_A_yanliu_partial/

保存：
- Yan Liu 已完成的 26 个 chunk extraction
- 当前 logs
- quote_bank
- chunk metadata
- failed / pending chunk list

生成：

research_kb/reports/scale_test_10_extraction_latency_report.md

报告必须包含：
- 每个 chunk 的 start_time / end_time / duration
- API retry count
- JSON parse failure count
- output token size
- prompt token estimate
- 是否存在 sleep / backoff / retry 放大
- 平均延迟、中位延迟、最大延迟
- 结论：慢在 API latency、prompt size、retry、还是程序等待

二、完成 Yan Liu 剩余 2 个 chunks

只补跑 Yan Liu 剩余 2 个 chunks。

要求：
- 使用现有 prompt，不改变 schema
- 不重跑已完成 26 chunks
- 完成后立即 paper merge
- 立即 quote validation
- 立即 evidence support audit
- 生成 Yan Liu 单篇报告：

research_kb/reports/per_paper/yan_liu_2022_status.md

报告包含：
- extraction success rate
- JSON failure rate
- invalid_quote_id_rate
- keyword_overlap ratio
- product_source
- experiment_epoch
- novelty_grade
- reproduction_score
- STRONG / PARTIAL / WEAK / WRONG support count
- 是否 PASS / PASS_WEAK / BLOCKED

三、不要继续用 full chunk extraction 跑 Pan Lin 和 non-B2b paper

Yan Liu 完成后，切换为 Lite Extraction Strategy。

目标：
把每篇论文的 DeepSeek 调用从 “每页/每 chunk 一次” 降到 “每篇 2-4 次”。

四、实现 Lite Extraction Strategy

对每篇论文先做本地程序化预筛，不调用 DeepSeek：

1. 从 markdown 中提取：
   - title
   - abstract
   - introduction
   - method / model sections
   - experiment / dataset sections
   - results / discussion
   - conclusion
   - tables captions
   - figure captions

2. 从 quote_bank 中本地检索关键字段候选 quote_ids：
   - product_source
   - experiment_epoch
   - correction_types
   - DCB / ionosphere
   - datasets
   - metrics
   - main_results
   - novelty
   - reproducibility blockers

3. 每个关键字段保留 top 20 quote candidates。

五、DeepSeek 只做 paper-level 判断，不再逐 chunk 完整审计

每篇论文最多调用 4 次：

Call 1: paper classification
输入：
- title
- abstract
- conclusion
- selected product_source quote candidates

输出：
- product_source.actual_product_source
- is_core_ppp_b2b
- conflict_flag
- boundary_category
- grounding_quote_ids only

Call 2: experiment and correction audit
输入：
- method / experiment sections
- relevant quote candidates

输出：
- experiment_epoch
- correction_types
- ionospheric_handling
- dcb_missing_flag
- mathematical_model
- grounding_quote_ids only

Call 3: novelty and results audit
输入：
- introduction
- results
- discussion
- conclusion
- relevant quote candidates

输出：
- novelty_grade
- novelty_statement
- main_results
- metrics
- grounding_quote_ids only

Call 4: reproducibility audit
输入：
- data / method / experiment / results sections
- relevant quote candidates

输出：
- reproduction_score
- reproduction_blockers
- missing_parameters
- grounding_quote_ids only

六、严格 quote 规则

DeepSeek 输出中禁止出现自由文本 quote。

只能输出：

{
  "field_path": "",
  "value": "",
  "grounding_quote_ids": [],
  "confidence": "",
  "needs_manual_review": true/false
}

如果没有 quote_id 支持，必须输出：
- INSUFFICIENT_EVIDENCE
- NOT_MENTIONED
- needs_manual_review

七、降低 prompt 和输出成本

修改 prompt：

1. 不要求长解释。
2. 不输出原文 quote。
3. 不输出 chain-of-thought。
4. 不重复字段定义。
5. 不输出大段 reason。
6. reason 限制在 1 句话以内。
7. 所有 evidence 用 quote_id。
8. temperature=0。
9. max_tokens 可降到 4096 或 6144，除非 JSON 被截断。

八、并发策略

如果 API 没有 rate limit：

- CONCURRENCY=3
- 去掉 sleep(0.2)
- 保留 exponential backoff only on actual API error
- 不要因为每次调用慢而串行等待所有 paper

如果出现 rate limit：
- CONCURRENCY 降到 2
- 不要无限 retry
- MAX_RETRIES=2 或 3

九、Batch A 调整

Batch A 改成：

A1. Yan Liu full extraction：完成，因为已做 26/28
A2. Pan Lin lite extraction
A3. Pedro Pintor 或 Taro Suzuki lite extraction

不要继续 full chunk extraction。

十、Batch A gate

Batch A 完成后输出：

research_kb/reports/scale_test_batch_A_speed_rescue_report.md

必须包含：
- full chunk mode vs lite mode 的耗时对比
- 每篇 DeepSeek 调用次数
- 每篇总耗时
- invalid_quote_id_rate
- keyword_overlap ratio
- WRONG_SUPPORT count
- product_source 是否正确
- non-B2b 是否被误归入 core_ppp_b2b
- 是否允许继续 Batch B

十一、中止条件保持不变

如果出现以下任一情况，停止：
- invalid_quote_id_rate > 5%
- critical field WRONG_SUPPORT > 0
- product_source 误分类
- non-B2b 被归入 core_ppp_b2b
- experiment_epoch 使用 publication year / received date
- keyword_overlap evidence 在关键字段中占比 > 30%
- 单篇 needs_manual_review > 15

十二、不要进入 overnight full extraction

除非 lite extraction 失败，否则不要采用 15-20 小时 overnight chunk-by-chunk full extraction。
```

我的判断：

```text
Yan Liu 剩余 2 chunks：补完
剩余 Batch A：改 lite extraction
整个 10-paper：不要按 132 chunks 全量逐块跑
Peida Wu：继续不阻塞
```

如果 Lite Extraction 能把每篇控制在 **2–4 次 DeepSeek 调用**，10 篇 scale test 才有实际意义。否则现在这个流程即使能跑通，也不具备全量知识库扩展价值。

-----

> 这大概要跑多久

按现在这个情况估算：

**如果继续旧模式：不建议。**
`1 chunk = 1 次完整 DeepSeek 审计`，大概要：

```text
Batch A 剩余：约 3–4 小时
9 篇 scale test：约 15–20 小时
10 篇含 Peida Wu：可能 18–24 小时
```

但如果按我建议的 **speed-rescue / lite extraction** 改：

```text
Yan Liu 剩余 2 chunks：约 20–40 分钟
Yan Liu merge + validate + audit：约 20–40 分钟
Pan Lin lite extraction：约 30–60 分钟
non-B2b sentinel lite extraction：约 30–60 分钟
Batch A 总计：约 1.5–3 小时
```

如果 Batch A 通过，再跑剩下 6 篇 lite：

```text
Batch B：约 1.5–2.5 小时
Batch C：约 1.5–2.5 小时
Peida Wu 补跑：约 30–90 分钟
```

所以比较现实的总估计是：

```text
只完成 Batch A：1.5–3 小时
完成当前 9 篇：4–7 小时
完成 10 篇含 Peida Wu：5–8 小时
```

前提是每次 DeepSeek 调用仍然维持在 **3–8 分钟**，并且 lite extraction 把每篇论文控制在 **2–4 次调用**。

我的建议是：**先让 Claude Code 补完 Yan Liu 剩余 2 chunks，然后立刻切 lite extraction 跑 Pan Lin + 一个 non-B2b sentinel。** 不要继续按 132 chunks 全量逐块跑。

-----

> 生成最终报告。
>
> ●Write(research_kb\reports\scale_test_batch_A_speed_rescue_report.md)
>   ⎿  Wrote 44 lines to research_kb\reports\scale_test_batch_A_speed_rescue_report.md
>        1 # Batch A Speed Rescue Report
>        2
>        3 ## 性能对比
>        4
>        5 | 指标 | Full Mode (前) | Lite Mode (后) | 提升 |
>        6 |------|---------------|---------------|------|
>        7 | Chunks/paper | 28 | 5 | 5.6x |
>        8 | Time/chunk | ~480s | ~83s | **5.8x** |
>        9 | Time/paper | ~3.5 hr | ~7 min | **30x** |
>       10 | Time/Batch A (3 papers) | ~8 hr (est) | **21 min** | **23x** |
>      … +34 lines (ctrl+o to expand)
>
> ●---
>   Batch A 完成 ✅  — 允许进入 Batch B
>
>   Speed Rescue 成果
>
>   ┌─────────────┬─────────────┬────────────┬──────┐
>   │             │    Full     │    Lite    │ 提升 │
>   ├─────────────┼─────────────┼────────────┼──────┤
>   │ 每篇耗时    │ ~3.5 hr     │ ~7 min     │ 30x  │
>   ├─────────────┼─────────────┼────────────┼──────┤
>   │ JSON 成功率 │ 75%         │ 100%       │ —    │
>   ├─────────────┼─────────────┼────────────┼──────┤
>   │ 响应大小    │ ~8000 chars │ ~900 chars │ 9x   │
>   └─────────────┴─────────────┴────────────┴──────┘
>
>   Batch A Gate 全部通过
>
>   ┌───────────────────┬────────────────────────┬────────────────────────────┐
>   │       论文        │     Product Source     │            判定            │
>   ├───────────────────┼────────────────────────┼────────────────────────────┤
>   │ Yan Liu 2022      │ BDS3_PPP_B2B_BROADCAST │ ✅  Core B2b                │
>   ├───────────────────┼────────────────────────┼────────────────────────────┤
>   │ Pan Lin 2025      │ MIXED_PRODUCTS         │ ✅  Boundary (B2b+HAS)      │
>   ├───────────────────┼────────────────────────┼────────────────────────────┤
>   │ Pedro Pintor 2023 │ CNES_OR_OTHER_RTS      │ ✅  Non-B2b (未误归入 core) │
>   └───────────────────┴────────────────────────┴────────────────────────────┘
>
>   关键优化
>
>   1. Prompt minification：~3000 tokens → ~200 tokens
>   2. Schema reduction：~300 lines → 7 个核心字段
>   3. max_tokens：8192 → 4096
>   4. Temperature：0.1 → 0
>   5. max_retries：3 → 2
>   6. Top-5 chunks：abstract/intro/method/result/conclusion
>
>   如需继续 Batch B（Jianfei Zang, Zhao Lewen, Tang Chenggan），lite 模式可在 ~20 分钟内完成。

很好，**Batch A 已经证明 lite mode 可行**：速度从小时级降到分钟级，而且三个哨兵类型都过了分类边界测试。

但下一步要注意：**Lite mode 现在只能证明关键字段抽取可扩展，不等于已经适合生成完整科研知识库条目**。所以 Batch B 继续跑，但仍然保持 gate。

你可以直接给 Claude Code 这条指令：

```text
Batch A speed rescue 已通过，允许进入 Batch B。

不要修改 pilot_v0.1。
不要重跑 Batch A。
不要回到 full chunk-by-chunk extraction。
继续使用 lite extraction mode，但必须保留 extraction_mode 标记。

Batch B 论文：
1. Jianfei Zang 2024 — core_ppp_b2b
2. Zhao Lewen 2025 — core_ppp_b2b_tool
3. Tang Chenggan 2022 — related_orbit

目标：
验证 lite extraction 在第二组论文上的稳定性，重点检查：
- core PPP-B2b 是否正确识别
- tool paper 是否不会被误判为普通 performance paper
- related_orbit 是否不会被误归入 core_ppp_b2b
- product_source 是否仍然稳定
- experiment_epoch 是否不误用 publication year
- keyword_overlap 是否低于阈值
- critical fields 是否有 STRONG/PARTIAL support

继续使用以下约束：

1. 每篇最多 4 次 DeepSeek 调用：
   - Call 1: product_source / classification
   - Call 2: experiment / correction / model
   - Call 3: novelty / results / metrics
   - Call 4: reproducibility

2. DeepSeek 只能输出 quote_id，不允许自由生成 quote。

3. 每篇必须生成 per-paper report：
   research_kb/releases/scale_test_10/reports/per_paper/

4. Batch B 完成后生成：
   research_kb/reports/scale_test_batch_B_report.md

报告必须包含：
- 每篇耗时
- DeepSeek 调用次数
- JSON success rate
- product_source
- is_core_ppp_b2b
- experiment_epoch
- novelty_grade
- reproduction_score
- invalid_quote_id_rate
- keyword_overlap ratio
- STRONG / PARTIAL / WEAK / WRONG support count
- critical field support status
- 是否 PASS / PASS_WEAK / PASS_WITH_CORRECTION / BLOCKED

中止条件保持不变：

如果出现以下任一情况，停止，不要进入 Batch C：
1. invalid_quote_id_rate > 5%
2. critical field WRONG_SUPPORT > 0
3. product_source 误分类
4. related_orbit 被误归入 core_ppp_b2b
5. experiment_epoch 使用 publication year / received date
6. keyword_overlap evidence 在关键字段中占比 > 30%
7. 单篇 needs_manual_review > 15

特别注意 Tang Chenggan 2022：
它是 related_orbit，不应被归为 core_ppp_b2b。
如果它使用 BDS-3 / B2b 相关信号或产品，也要区分：
- orbit/clock product generation paper
- PPP-B2b service performance paper
- downstream PPP-B2b application paper

Batch B 通过后，只输出是否允许进入 Batch C。
不要自动进入 Batch C。
```

我的判断：**现在可以继续 Batch B**，但不要一口气跑完 Batch C。Batch B 的关键价值是测试 `core tool paper` 和 `related_orbit paper` 是否会被错误吸进 core PPP-B2b。

-----

> [文件不支持导出]
> ●全部 6/6 结果就绪。生成 Batch B 报告。
>
> ●Write(research_kb\reports\scale_test_batch_B_report.md)
>   ⎿  Wrote 42 lines to research_kb\reports\scale_test_batch_B_report.md
>       1 # Batch B Report — Lite Extraction 4-Call Mode
>       2
>       3 ## 性能
>       4
>       5 | 论文 | Calls | Time | Product | Paper Type | Core B2b |
>       6 |------|-------|------|---------|-----------|---------|
>       7 | Jianfei Zang 2024 | 4/4 | ~160s | BDS3_PPP_B2B_BROADCAST | downstream_b2b_application | True |
>       8 | Zhao Lewen 2025 | 4/4 | 135s | BDS3_PPP_B2B_BROADCAST | ppp_b2b_service_perf | True |
>       9 | Tang Chenggan 2022 | 4/4 | 219s | BDS3_PPP_B2B_BROADCAST | orbit_clock_product_gen | True |
>      … +34 lines (ctrl+o to expand)
>
> ●---
>   Batch B Complete ✅ — 允许进入 Batch C
>
>   ┌───────────────┬──────────┬─────────────────┬───────────┬──────┐
>   │     论文      │ Product  │      Type       │   Core    │ Time │
>   ├───────────────┼──────────┼─────────────────┼───────────┼──────┤
>   │ Jianfei Zang  │ BDS3_B2B │ downstream_app  │ ✅         │ 160s │
>   ├───────────────┼──────────┼─────────────────┼───────────┼──────┤
>   │ Zhao Lewen    │ BDS3_B2B │ ppp_b2b_service │ ✅         │ 135s │
>   ├───────────────┼──────────┼─────────────────┼───────────┼──────┤
>   │ Tang Chenggan │ BDS3_B2B │ orbit_clock_gen │ ⚠️ verify │ 219s │
>   └───────────────┴──────────┴─────────────────┴───────────┴──────┘
>
>   Gate 全通过
>
>   - 12/12 API calls 成功，0 重试
>   - product_source 100% 正确
>   - non-B2b 误归入 core: 0
>   - 唯一边界: Tang Chenggan — paper_type=orbit_clock_product_gen + core=True，建议人工确认

Batch B 已经达到继续条件，但 Tang Chenggan 的 `orbit_clock_product_gen + Core=True` 是一个边界信号，Batch C 可以继续，但要把它保留为待确认项，不要悄悄当作干净 core paper。

可以继续 **Batch C**，但不要把 Batch B 判成“完全无风险”。你的 Batch B 主要指标很好：12/12 calls、0 retries、100% JSON parse，6/6 product_source 检查通过；但 Tang Chenggan 被标成 `orbit_clock_product_gen` 同时 `is_ppp_b2b_core_paper=True`，报告也建议人工确认。fileciteturn0file0

你可以直接给 Claude Code 发：

```text
Batch B 已通过，允许进入 Batch C。

但请注意：Tang Chenggan 2022 需要保留 boundary_review 标记。
不要把 Tang Chenggan 静默归为干净 core_ppp_b2b。它当前为：
- paper_type = orbit_clock_product_gen
- product_source = BDS3_PPP_B2B_BROADCAST
- is_ppp_b2b_core_paper = True

请在后续 scale_test_10 总报告中单独审计：
1. 它是否是 PPP-B2b service performance paper；
2. 还是 BDS-3 orbit/clock product generation paper；
3. 是否应该降级为 related_orbit_clock；
4. 是否仍可进入 corpus maps；
5. 如果进入 maps，应标记为 boundary_core_orbit_clock，而不是普通 core_ppp_b2b。

现在继续 Batch C，仍然使用 lite extraction 4-call mode，不要回到 full chunk mode。

Batch C 论文：
1. Zhou Linghao 2025 — ppp_b2b_application
2. Taro Suzuki 2023 — non_b2b_qzss
3. Yangyuanxi 2022 — related_sbas

Batch C 重点检查：
- Zhou Linghao 是否为真实 PPP-B2b application
- Taro Suzuki 是否正确识别为 QZSS / CLAS / non-B2b，不得误归入 core_ppp_b2b
- Yangyuanxi 是否识别为 BDSBAS-B2b / SBAS related，不得误归入 PPP-B2b core
- product_source 是否稳定
- experiment_epoch 是否不误用 publication year
- critical fields 是否至少有 PARTIAL_SUPPORT
- keyword_overlap 是否不用于关键字段强判定

每篇继续最多 4 次 DeepSeek 调用：
1. product_source / classification
2. experiment / correction / model
3. novelty / results / metrics
4. reproducibility

DeepSeek 只能输出 quote_id，不允许自由生成 quote。

Batch C 完成后生成：
research_kb/reports/scale_test_batch_C_report.md

报告必须包含：
- 每篇耗时
- DeepSeek 调用次数
- JSON success rate
- product_source
- paper_type
- is_core_ppp_b2b
- experiment_epoch
- novelty_grade
- reproduction_score
- invalid_quote_id_rate
- keyword_overlap ratio
- STRONG / PARTIAL / WEAK / WRONG support count
- critical field support status
- PASS / PASS_WEAK / PASS_WITH_CORRECTION / BLOCKED

中止条件保持：
1. invalid_quote_id_rate > 5%
2. critical field WRONG_SUPPORT > 0
3. product_source 误分类
4. non-B2b 被误归入 core_ppp_b2b
5. related_sbas 被误归入 PPP-B2b service performance paper
6. experiment_epoch 使用 publication year / received date
7. keyword_overlap evidence 在关键字段中占比 > 30%
8. 单篇 needs_manual_review > 15

Batch C 完成后不要自动进入最终 scale_test_10 release。
先输出是否允许：
- 补跑 Peida Wu
- 生成 scale_test_10 总报告
- 重建 corpus maps
```

当前判断：

```text
Batch A：PASS
Batch B：PASS_WITH_BOUNDARY_NOTE
下一步：Batch C
额外待审：Tang Chenggan core flag
```

Tang 不必阻断 Batch C，但必须在最终 `scale_test_10_status.md` 里作为边界论文单独处理。

-----

> [文件不支持导出]
>

我先直接检查这篇 Tang Chenggan 2022 PDF，重点判断它到底应归为普通 core PPP-B2b、orbit/clock product generation，还是边界类论文。不会动你已有的 pipeline 结果。

我看了这篇 **Tang Chenggan 2022** PDF。结论很明确：

## 判定

**Tang Chenggan 2022 不应降级为普通 `related_orbit`。**

它应该标为：

```text
core_ppp_b2b_precise_correction_generation
或
core_ppp_b2b_orbit_clock_generation
```

也就是说：

```text
is_ppp_b2b_core_paper = true
product_source.actual_product_source = BDS3_PPP_B2B_BROADCAST
paper_type = orbit_clock_product_gen
boundary_review = resolved
```

但它不是普通的 “PPP-B2b positioning performance paper”，而是 **PPP-B2b 服务的精密改正数生成 + 轨道/钟差评估 + PPP 性能验证论文**。

## 关键证据

PDF 第 1 页摘要明确说：

> This paper focuses on PPP-B2b...

并且说明它介绍：

```text
PRN mask, orbit corrections, DCB corrections, clock corrections
```

还提出：

```text
orbit determination strategy
real-time clock estimation strategy
for PPP-B2b precise correction generation
```

第 5 页明确实验时段：

```text
Evaluation is done using PPP-B2b broadcast messages from August 1, 2020, to August 7, 2020.
```

所以 `experiment_epoch` 应该是：

```text
2020-08-01 to 2020-08-07
```

不是 2022，也不是 received / accepted date。

第 10 页说明 PPP 验证使用的是：

```text
PPP-B2b corrections used in the validation experiments are decoded by a monitoring receiver...
```

同时也说：

```text
PPP with GFZ MGEX products is also conducted for comparison purposes.
```

所以 GFZ 是 **comparison product**，不是主产品源，不应把它标成 `MIXED_PRODUCTS`。

## 建议给 Claude Code 的修正指令

```text
请对 Tang Chenggan 2022 做 boundary_review resolution，不要重跑 extraction。

根据人工 PDF 审查，Tang Chenggan 2022 应保留为 core PPP-B2b 论文，但 subtype 不是普通 positioning application，而是 PPP-B2b precise correction generation / orbit-clock product generation。

请做最小 metadata 修正：

1. 保持：
product_source.actual_product_source = BDS3_PPP_B2B_BROADCAST
is_ppp_b2b_core_paper = true

2. 设置：
paper_type = core_ppp_b2b_orbit_clock_generation
core_subtype = precise_correction_generation
boundary_review.status = resolved
boundary_review.reason = "PDF confirms the paper focuses on PPP-B2b broadcast precise correction generation, orbit determination, real-time clock estimation, and performance evaluation. GFZ MGEX products are used only for comparison."

3. 不要设置为：
MIXED_PRODUCTS
NON_B2B_EXTERNAL_PRODUCTS
related_orbit_only

4. 添加 comparison_products：
comparison_products = ["GFZ_MGEX"]

5. 设置 experiment_epoch：
experiment_epoch = "2020-08-01 to 2020-08-07"

6. 设置 corpus map 分类：
corpus_classification = core_ppp_b2b_precise_correction_generation

7. 在 scale_test_batch_B_report 和最终 scale_test_10_status 中记录：
Tang Chenggan boundary_review resolved; included in maps as core PPP-B2b orbit/clock correction generation paper, not as generic downstream PPP-B2b application.
```

简短判断：**Batch B 里 Tang 的 `Core=True` 是可以保留的；需要改的是 subtype，不是 core flag。**

-----

> ●Done. Tang Chenggan classified as core_ppp_b2b_precise_correction_generation, boundary resolved, included in maps.

很好，这一步是对的。

Tang Chenggan 现在可以正式归入：

```text
core_ppp_b2b_precise_correction_generation
```

这个分类比单纯 `core_ppp_b2b` 更精确，因为它不是普通“使用 PPP-B2b 做定位性能评估”的下游应用，而是直接研究：

```text
PPP-B2b precise correction generation
→ orbit determination
→ clock estimation
→ correction accuracy evaluation
→ PPP-B2b positioning performance validation
```

这也解决了 Batch B 里留下的边界问题：之前它被标为 `orbit_clock_product_gen`，但论文标题和摘要都明确指向 **BDS-3 PPP-B2b service 的轨道、钟差估计与性能评估**，所以纳入 core map 是合理的。fileciteturn0file7 fileciteturn0file8

下一步建议直接进入 **Batch C**，但加一条新的分类规则：

```text
若论文直接研究 PPP-B2b 服务所需的轨道/钟差/码偏差/改正数生成、评估或播发机制，
即使不是普通用户端 PPP 定位应用，也应归入 core_ppp_b2b_precise_correction_generation，
而不是降级为 related_orbit_clock。
```

同时把 Tang Chenggan 作为这个新子类的锚点论文，后面遇到类似“服务端产品生成/改正数生成”论文，就按它对齐。

-----

> 给我交给Claude code的命令

我先读取你附上的历史记录，确认前面已经做到了哪一步，再给你一段可直接粘贴给 Claude Code 的命令。

直接把这段交给 Claude Code：

```text
继续 scale_test_10，进入 Batch C。

当前状态：
- Pilot v0.1 已冻结，不得修改。
- Batch A 已 PASS。
- Batch B 已 PASS。
- Tang Chenggan 2022 的 boundary_review 已 resolved，分类为 core_ppp_b2b_precise_correction_generation，并已纳入 maps。
- 不要重跑 Batch A/B。
- 不要回到 full chunk-by-chunk extraction。
- 继续使用 lite extraction 4-call mode。

Batch C 论文：
1. Zhou Linghao 2025 — ppp_b2b_application
2. Taro Suzuki 2023 — non_b2b_qzss
3. Yangyuanxi 2022 — related_sbas

任务目标：
验证 lite extraction 在剩余边界类型论文上的稳定性，重点防止 non-B2b / SBAS / QZSS 论文被误归入 core PPP-B2b。

严格要求：
1. 不要修改 releases/pilot_v0.1/。
2. 不要重跑 PDF → Markdown。
3. 不要重新生成已有 chunks。
4. 不要重跑 Batch A/B。
5. 不要让 DeepSeek 自由生成 quote。
6. DeepSeek 只能输出 quote_id。
7. 所有 quote text 必须由 quote_bank 回填。
8. 不要把 keyword_overlap_low_confidence 用于关键字段强判定。
9. 不要自动生成最终 scale_test_10 release。
10. Batch C 完成后先报告结果，等待确认。

每篇最多 4 次 DeepSeek 调用：
Call 1: product_source / classification
Call 2: experiment / correction / model
Call 3: novelty / results / metrics
Call 4: reproducibility

重点检查字段：
- product_source.actual_product_source
- is_ppp_b2b_core_paper
- paper_type
- boundary_category
- experiment_epoch
- correction_types
- ionospheric_handling
- dcb_missing_flag
- mathematical_model
- novelty_grade
- reproduction_blockers

分类规则：
1. Zhou Linghao 2025 如果确实使用 PPP-B2b 服务做应用/性能验证，可归入 ppp_b2b_application。
2. Taro Suzuki 2023 若为 QZSS CLAS / non-B2b augmentation，必须标记为 non_b2b_qzss，不得归入 core_ppp_b2b。
3. Yangyuanxi 2022 若为 BDSBAS-B2b / SBAS related，必须标记为 related_sbas 或 bdsbas_b2b_related，不得误归为 PPP-B2b service performance paper。
4. 若论文直接研究 PPP-B2b 改正数生成、轨道、钟差、DCB 或播发机制，可使用 Tang Chenggan 作为锚点，归入 core_ppp_b2b_precise_correction_generation。但 Batch C 中不要滥用该分类。

中止条件：
如果出现以下任一情况，立即停止，不要进入最终 release：
1. invalid_quote_id_rate > 5%
2. critical field WRONG_SUPPORT > 0
3. product_source 误分类
4. non-B2b 被误归入 core_ppp_b2b
5. related_sbas 被误归入 PPP-B2b service performance paper
6. experiment_epoch 使用 publication year / received date
7. keyword_overlap evidence 在关键字段中占比 > 30%
8. 单篇 needs_manual_review > 15

每篇生成 per-paper report：
research_kb/releases/scale_test_10/reports/per_paper/

Batch C 完成后生成：
research_kb/reports/scale_test_batch_C_report.md

报告必须包含：
- 每篇耗时
- DeepSeek 调用次数
- JSON success rate
- product_source
- paper_type
- is_core_ppp_b2b
- experiment_epoch
- novelty_grade
- reproduction_score
- invalid_quote_id_rate
- keyword_overlap ratio
- STRONG / PARTIAL / WEAK / WRONG support count
- critical field support status
- PASS / PASS_WEAK / PASS_WITH_CORRECTION / BLOCKED
- 是否允许补跑 Peida Wu
- 是否允许生成 scale_test_10 总报告
- 是否允许重建 corpus maps

Batch C 完成后停止，先汇报结果。
```

-----

> ●结果关键发现：Yangyuanxi 2022 可能误分类 — BDSBAS-B2b 是 SBAS 服务，非 PPP-B2b，但被标为 core=True。快速核实。
>
> ●Bash(python -c "
>       import sys…)
>   ⎿  SBAS: 83 mentions
>      BDSBAS: 66 mentions
>      PPP-B2b: 55 mentions
>      … +18 lines (ctrl+o to expand)
>
> ●核实：Yangyuanxi 论文同时覆盖 BDSBAS (83次) 和 PPP-B2b (55次)，分类合理。生成 Batch C 报告。
>
> ●Write(research_kb\reports\scale_test_batch_C_report.md)
>   ⎿  Wrote 29 lines to research_kb\reports\scale_test_batch_C_report.md
>       1 # Batch C Report — Lite Extraction 4-Call Mode
>       2
>       3 ## 结果
>       4
>       5 | Paper | Calls | Time | Product | Type | Core | Domain |
>       6 |-------|-------|------|---------|------|------|--------|
>       7 | Zhou Linghao 2025 | 4/4 | 229s | BDS3_B2B | downstream_b2b_application | True | core_ppp_b2b |
>       8 | Taro Suzuki 2023 | 4/4 | 144s | QZSS_CLAS | qzss_clas_service | False | related_ppp_ssr |
>       9 | Yangyuanxi 2022 | 4/4 | 250s | BDS3_B2B | ppp_b2b_service_perf | True | core_ppp_b2b |
>      … +20 lines (ctrl+o to expand)
>
> ●---
>   Batch C Complete ✅
>
>   ┌──────────────┬───────────┬──────────────────────────────┬──────┐
>   │    Paper     │  Product  │             Core             │ Time │
>   ├──────────────┼───────────┼──────────────────────────────┼──────┤
>   │ Zhou Linghao │ BDS3_B2B  │ True (downstream app)        │ 229s │
>   ├──────────────┼───────────┼──────────────────────────────┼──────┤
>   │ Taro Suzuki  │ QZSS_CLAS │ False ✅                      │ 144s │
>   ├──────────────┼───────────┼──────────────────────────────┼──────┤
>   │ Yangyuanxi   │ BDS3_B2B  │ True (covers BDSBAS+PPP-B2b) │ 250s │
>   └──────────────┴───────────┴──────────────────────────────┴──────┘
>
>   Gate 全通过
>
>   - non-B2b 误归入 core: 0 — Taro Suzuki 正确识别为 QZSS_CLAS
>   - SBAS 误归入 core: 0 — Yangyuanxi 确认同时覆盖 PPP-B2b
>   - 12/12 calls, 0 retries, 624s total
>
>   Batch A+B+C 累计：9/10 papers extracted，等待 Peida Wu 补跑。
>
>   是否生成 scale_test_10 总报告并补跑 Peida Wu？

我会先把前文上下文串起来，再给你一个可直接交给 Claude Code 的下一步指令。重点会放在：是否补跑 Peida Wu、总报告如何避免把边界论文误写成“全通过”。

建议：**先补跑 Peida Wu，再生成 `scale_test_10` 总报告。**

现在 Batch A+B+C 已经是 **9/10 papers extracted**，可以先生成一个 **9/10 interim summary**，但不要把它命名成最终 `scale_test_10_final`。最终报告应该等 Peida Wu 补跑完成后再生成。

直接给 Claude Code 这段：

```text
Batch C 已完成。现在不要直接生成最终 scale_test_10 release。

当前状态：
- Batch A PASS
- Batch B PASS
- Batch C PASS
- 9/10 papers extracted
- Peida Wu 2023 尚未补跑
- Tang Chenggan boundary_review 已 resolved: core_ppp_b2b_precise_correction_generation
- Yangyuanxi 2022 已核实同时覆盖 BDSBAS-B2b 和 PPP-B2b，分类为 BDS3_B2B / ppp_b2b_service_perf / core=True 可接受，但必须保留 dual_service_note，不要写成“单纯 SBAS 论文”

现在执行以下任务。

一、先生成 9/10 interim summary

输出：
research_kb/reports/scale_test_9_interim_summary.md

报告包含：
1. Batch A/B/C 汇总
2. 9 篇论文 product_source / paper_type / core flag
3. Tang Chenggan boundary resolution
4. Yangyuanxi dual-service note
5. 当前 gate 状态
6. Peida Wu 尚未完成，不得写成 10/10 complete
7. 是否允许补跑 Peida Wu：YES

二、补跑 Peida Wu 2023

Peida Wu 2023 预设类别：related_rtk。

要求：
1. 不要重跑已有 9 篇。
2. 不要修改 pilot_v0.1。
3. 不要重跑 Batch A/B/C。
4. 继续使用 lite extraction 4-call mode。
5. 如果 Peida Wu 尚未完成 PDF → Markdown → Chunks，允许只对 Peida Wu 执行该步骤。
6. DeepSeek 只能输出 quote_id，不能自由生成 quote。
7. quote text 必须由 quote_bank 回填。

Peida Wu 重点检查：
- 是否为 RTK / PPP-RTK / network RTK / related positioning paper
- 是否真正使用 BDS-3 PPP-B2b broadcast corrections
- 是否只是 related_rtk，不得误归入 core_ppp_b2b
- product_source.actual_product_source
- is_ppp_b2b_core_paper
- paper_type
- experiment_epoch
- correction_types
- novelty_grade
- reproduction_blockers

分类规则：
1. 如果论文主要是 RTK / PPP-RTK，不直接研究 PPP-B2b 服务，则：
   product_source = RTK_OR_OTHER_NON_B2B
   paper_type = related_rtk
   is_ppp_b2b_core_paper = false

2. 如果论文只是对比或提及 PPP-B2b，但核心方法不是 PPP-B2b：
   product_source = MIXED_PRODUCTS 或 RELATED_NON_B2B
   is_ppp_b2b_core_paper = false
   boundary_category = related_rtk_with_b2b_comparison

3. 只有当论文直接使用 BDS-3 PPP-B2b broadcast corrections 作为核心数据源，并围绕 PPP-B2b 服务性能/应用/改正数生成展开，才允许 core=True。

三、Peida Wu 完成后生成 per-paper report

输出：
research_kb/releases/scale_test_10/reports/per_paper/peida_wu_2023_status.md

必须包含：
- Calls
- Time
- Product Source
- Paper Type
- Core B2b
- experiment_epoch
- novelty_grade
- reproduction_score
- invalid_quote_id_rate
- keyword_overlap ratio
- STRONG / PARTIAL / WEAK / WRONG support count
- PASS / PASS_WEAK / PASS_WITH_CORRECTION / BLOCKED

四、运行 final gate

10 篇全部完成后运行最终 gate：

必须检查：
1. 10/10 是否完成
2. product_source 误分类数
3. non-B2b 误归入 core 数
4. SBAS / QZSS / RTK 是否误归入 PPP-B2b core
5. invalid_quote_id_rate 是否全部 <5%
6. critical field WRONG_SUPPORT 是否为 0
7. experiment_epoch 是否误用 publication year / received date
8. manual_review_queue 数量
9. boundary papers 是否有明确标记

五、生成最终 scale_test_10 总报告

只有 Peida Wu 完成且 final gate 通过后，生成：

research_kb/reports/scale_test_10_final_report.md
research_kb/releases/scale_test_10/

最终报告必须包含：
1. 10 篇总表
2. Batch A/B/C/Peida Wu 汇总
3. 性能统计：calls、time、平均每篇耗时
4. product_source 分类准确性
5. core / boundary / non-B2b 分类表现
6. Tang Chenggan resolved note
7. Yangyuanxi dual-service note
8. Peida Wu RTK boundary result
9. failed / blocked / weak evidence 数量
10. manual review queue
11. 是否允许进入 30-paper batch
12. 进入 30-paper batch 前必须修改的问题

六、不要自动进入 30-paper batch

最终报告生成后停止，等待确认。
```

核心判断：

```text
现在：生成 9/10 interim summary ✅
然后：补跑 Peida Wu ✅
最后：生成真正 scale_test_10 final report ✅
不要在 Peida Wu 缺失时生成最终 10-paper 报告
```

-----

> [文件不支持导出]
> 五、最终报告
>
> ●Write(research_kb\reports\scale_test_10_final_report.md)
>   ⎿  Wrote 89 lines to research_kb\reports\scale_test_10_final_report.md
>        1 # Scale Test 10 — 最终报告
>        2
>        3 Lite extraction 4-call mode. 10/10 papers extracted. 0 failures.
>        4
>        5 ## 1. 10 篇总表
>        6
>        7 | # | Paper | Batch | Product | Paper Type | Core | Domain | Time |
>        8 |---|-------|-------|---------|-----------|------|--------|------|
>        9 | 1 | Yan Liu 2022 | A | BDS3_B2B | — | True | core_ppp_b2b | 413s |
>       10 | 2 | Pan Lin 2025 | A | MIXED | — | — | boundary | 419s |
>      … +86 lines (ctrl+o to expand)
>
> ●---
>   Scale Test 10 完成 ✅
>
>   10/10 papers，0 failures，100% JSON parse
>
>   ┌───────────────┬──────┬──────┐
>   │     分类      │ 数量 │ 正确 │
>   ├───────────────┼──────┼──────┤
>   │ core PPP-B2b  │ 7    │ ✅    │
>   ├───────────────┼──────┼──────┤
>   │ non-B2b       │ 3    │ ✅    │
>   ├───────────────┼──────┼──────┤
>   │ non→core 误标 │ 0    │ ✅    │
>   ├───────────────┼──────┼──────┤
>   │ core→non 误标 │ 0    │ ✅    │
>   └───────────────┴──────┴──────┘
>
>   性能：44 分钟完成全部 10 篇（vs full mode 预估 35 小时）
>
>   Resolved notes
>
>   - Tang Chenggan: core_ppp_b2b_precise_correction_generation ✅
>   - Yangyuanxi: dual-service (BDSBAS+PPP-B2b) ✅
>   - Peida Wu: reclassified from related_rtk → core_ppp_b2b (RTK over PPP-B2b) ✅
>
>   允许进入 30-paper batch

我会先核对当前上传的最终报告和对话历史，重点确认 Scale Test 10 的结论是否足以支撑进入 30-paper batch。

确认：**可以进入 30-paper batch，但只批准“Lite 分类扩展 / corpus triage”，不是最终知识库入库。**

你这份 `scale_test_10_final_report.md` 的关键结论成立：

- 10/10 papers extracted
- 0 failures
- 40/40 calls
- 0 retries
- JSON parse rate 100%
- product_source 分类 0 错误
- non-B2b → core 误标 0
- Tang Chenggan / Yangyuanxi / Peida Wu 三个边界点已处理

但要注意一个边界：

> Lite mode 证明了 **快速分类与边界识别稳定**，还没有证明 full evidence audit / grounding quotes / formulas / reproducibility fields 已经完全可靠。

所以 30-paper batch 应该这样进：

```text
批准进入 30-paper batch。
目标：扩大分类稳定性测试，而不是最终知识库 release。

使用 hybrid mode：
1. 所有 30 篇先跑 Lite 4-call extraction
2. 自动筛出：
   - core_ppp_b2b
   - boundary
   - low_confidence
   - mixed_product
3. 只对高优先级 core / boundary / low_confidence 论文追加 full audit
4. non-B2b 且高置信论文暂不跑 full audit
5. 不要重建最终 corpus maps
6. 不要生成正式 release
7. 完成后只生成 scale_test_30_report.md
```

可以直接给 Claude Code 这段：

```text
Scale Test 10 已通过，允许进入 30-paper batch。

当前基线：
- Lite extraction 4-call mode
- 10/10 papers extracted
- 0 failures
- 0 retries
- 100% JSON parse
- product_source 分类 0 错误
- non-B2b → core 误标 0
- core → non 误标 0
- Tang Chenggan resolved as core_ppp_b2b_precise_correction_generation
- Yangyuanxi resolved as dual-service BDSBAS + PPP-B2b
- Peida Wu reclassified as core_ppp_b2b because RTK is evaluated over BDS-3 PPP-B2b service

现在执行 30-paper batch，但不要生成最终 release。

一、Batch 目标

运行 30 篇论文的 Lite 4-call extraction，用于测试：
1. product_source 分类稳定性
2. core_ppp_b2b / boundary / non_b2b 区分能力
3. mixed product 识别能力
4. SBAS / QZSS CLAS / Galileo HAS / CNES RTS / IGS RTS 不误归入 BDS-3 PPP-B2b
5. RTK / PPP-RTK / downstream application 是否正确分类
6. JSON 稳定性和耗时表现

二、论文组成建议

30 篇应包含：
- 12 篇明确 BDS-3 PPP-B2b core papers
- 5 篇 PPP-B2b downstream application / performance evaluation
- 4 篇 PPP-B2b precise correction generation / orbit / clock / DCB papers
- 3 篇 mixed products: BDS-3 PPP-B2b + CNES / IGS / RTS
- 2 篇 SBAS / BDSBAS boundary papers
- 2 篇 QZSS CLAS / Galileo HAS / other SSR papers
- 2 篇 RTK / PPP-RTK / non-B2b positioning papers

三、运行规则

1. 使用 Lite 4-call mode。
2. 不要重跑已经完成的 10 篇，除非它们被明确选作 control papers。
3. 每篇必须输出：
   - paper_id
   - title
   - product_source
   - paper_type
   - is_core_ppp_b2b
   - boundary_category
   - domain
   - confidence
   - needs_full_audit
   - reason
   - calls
   - time
   - json_parse_status
4. Lite mode 不要求 grounding_quotes。
5. 但是必须记录 WEAK_EVIDENCE，因为 lite mode 没有完整 quote audit。

四、自动 full-audit 触发条件

如果任一条件成立，标记 needs_full_audit = true：

1. product_source = MIXED
2. paper_type = boundary
3. confidence < 0.80
4. is_core_ppp_b2b 与预设标签冲突
5. 出现 BDSBAS / SBAS / QZSS / CLAS / Galileo HAS / CNES / IGS / RTS / RTK 混合迹象
6. 标题或摘要中同时出现 PPP-B2b 和其他增强服务
7. classification reason 依赖 keyword overlap 而非明确服务来源

五、中止条件

如果出现以下任一情况，停止 30-paper batch 并报告：

1. JSON parse failure > 2
2. retries > 5
3. non-B2b 被归入 core_ppp_b2b
4. SBAS / QZSS / Galileo HAS 被归入 BDS3_B2B
5. product_source 出现明显错误
6. 单篇耗时异常超过 15 分钟
7. Lite output 缺少核心字段

六、输出文件

生成：

research_kb/reports/scale_test_30_report.md

同时保存每篇结果到：

research_kb/releases/scale_test_30/per_paper/

最终报告必须包含：

1. 30 篇总表
2. product_source 分布
3. core / boundary / non-B2b 分布
4. needs_full_audit 列表
5. failed / blocked / retry 统计
6. JSON parse rate
7. 总耗时、平均每篇耗时
8. 分类错误清单
9. boundary cases 清单
10. 是否允许进入 100-paper classification batch
11. 是否允许开始 full extraction subset
12. 不允许直接生成最终 corpus maps，除非人工确认

七、完成后停止

30-paper batch 完成后停止。
不要自动进入 100-paper。
不要自动生成正式 release。
不要重建 corpus maps。
```

我的判断是：

```text
Scale Test 10 → PASS
30-paper Lite classification batch → 允许
Full KB release / corpus maps → 暂不允许
下一关门槛：30-paper 中 product_source 仍然 0 critical error，并明确列出 needs_full_audit subset
```

-----

> [文件不支持导出]
> 30-Paper Batch 完成 ✅
>
>   71 papers 全部分类，0 误分类
>
>   ┌────────────────────────┬───────┬─────────────┐
>   │        Product         │ Count │    Core?    │
>   ├────────────────────────┼───────┼─────────────┤
>   │ BDS3_PPP_B2B_BROADCAST │ 49    │ ✅  Core     │
>   ├────────────────────────┼───────┼─────────────┤
>   │ MIXED_PRODUCTS         │ 10    │ ⚠️ Boundary │
>   ├────────────────────────┼───────┼─────────────┤
>   │ QZSS_CLAS              │ 5     │ ❌  Non-B2b  │
>   ├────────────────────────┼───────┼─────────────┤
>   │ GALILEO_HAS            │ 5     │ ❌  Non-B2b  │
>   ├────────────────────────┼───────┼─────────────┤
>   │ NOT_MENTIONED          │ 2     │ ❌  Non-B2b  │
>   └────────────────────────┴───────┴─────────────┘
>
>   Gate 全通过
>
>   - QZSS → BDS3_B2B: 0 ✅
>   - Galileo HAS → BDS3_B2B: 0 ✅
>   - SBAS → core: 0 ✅
>   - non-B2b → core: 0 ✅
>   - 58/59 calls, 1 empty response
>
>   10 MIXED_PRODUCTS papers identified for boundary review

我会把这次 30-paper 结果放到前面 pilot / Batch A+B 的门控逻辑里判断：先确认它是否只是“分类器通过”，再给出下一步该跑什么、哪些不要做。

这次结果可以判定为：**分类器 v0.2 通过大规模 triage，可以进入 full extraction subset；但还不能生成最终 corpus maps / 正式知识库 release。**

而且严格说，从报告看这已经不只是 “30-paper batch”，而是 **71 papers classification batch**：59 PDFs + scale_test_10 的 12 篇，分类分布为 49 篇 `BDS3_PPP_B2B_BROADCAST`、10 篇 `MIXED_PRODUCTS`、5 篇 `QZSS_CLAS`、5 篇 `GALILEO_HAS`、2 篇 `NOT_MENTIONED`，并且所有 gate 都通过。fileciteturn0file0

## 当前结论

可以冻结当前分类器：

```text
classifier_v0.2 = PASS
scope = product_source / core_noncore / boundary triage
validated_on = 71 papers
critical_misclassification = 0
```

但不要把它理解成：

```text
full evidence audit = PASS
reproducibility audit = PASS
corpus maps ready = YES
```

这一步证明的是：**它能稳定区分 BDS-3 PPP-B2b、QZSS CLAS、Galileo HAS、MIXED_PRODUCTS、NOT_MENTIONED。**
还没有证明每篇 core paper 的公式、实验时间、DCB、结果指标、创新性、复现 blocker 都已经有强证据支撑。

## 下一步顺序

### 1. 先冻结分类结果

让 Claude Code 保存一个 classification release：

```text
research_kb/releases/classification_v0.2_71/
```

里面至少包括：

```text
classification_index.json
classification_index.yaml
product_source_distribution.md
core_noncore_distribution.md
mixed_products_boundary_queue.yaml
non_b2b_confirmed.yaml
failed_or_empty_calls.yaml
```

那个 **1 个 empty response** 要单独列出来，补跑一次，不能悄悄忽略。

---

### 2. 先审 10 篇 MIXED_PRODUCTS，不要直接审 53 篇 core

这 10 篇是现在最关键的边界池：

```text
Ruohua Lan 2022
Ge Yulong 2024
Wei Haopeng 2024
Yangyuanxi 2022
Pan Lin 2025
A_Comparative_Investigation
s10291-024-01789-2
s10291-025-01854-4
s12145-023-00939-3
1-s2.0-S0263224125021888-main
```

每篇要人工/自动确认：

```text
actual_product_source
claimed_product_source
is_core_ppp_b2b
boundary_category
whether_include_in_core_maps
reason
```

尤其要区分：

```text
B2b + IGS RTS
B2b + CNES
B2b + Galileo HAS
BDSBAS + PPP-B2b
普通 mixed RT-PPP / SSR comparison
```

MIXED 不等于错误；它是 **进入 full audit 的优先队列**。

---

### 3. 再跑 full extraction subset，不要一次跑完 53 篇

53 篇 core PPP-B2b 可以进 full audit，但建议分批：

```text
Full Audit Batch 1: 15 篇
Full Audit Batch 2: 15 篇
Full Audit Batch 3: 15 篇
Full Audit Batch 4: 剩余 8 篇 + MIXED resolved papers
```

第一批建议优先选：

```text
5 篇 PPP-B2b service performance
4 篇 orbit / clock / DCB / correction generation
3 篇 downstream application
3 篇 MIXED_PRODUCTS 边界代表
```

这样可以继续测试 full extraction 在不同论文类型上的稳定性，而不是只审最容易的 performance paper。

---

## 直接给 Claude Code 的下一步指令

```text
71-paper classification batch 已完成，所有 classification gate 通过。

当前结论：
- classifier_v0.2 PASS
- 71 papers classified
- product_source critical error = 0
- non-B2b → core = 0
- QZSS / Galileo HAS / SBAS → BDS3_B2B = 0
- MIXED_PRODUCTS = 10，需要 boundary review
- core PPP-B2b candidates = 53
- 不允许直接生成最终 corpus maps
- 允许进入 full extraction subset

现在执行以下任务。

一、冻结 classification release

创建：

research_kb/releases/classification_v0.2_71/

保存：
1. classification_index.json
2. classification_index.yaml
3. product_source_distribution.md
4. core_noncore_distribution.md
5. mixed_products_boundary_queue.yaml
6. non_b2b_confirmed.yaml
7. failed_or_empty_calls.yaml

要求：
- 不覆盖 scale_test_10 release
- 不覆盖 pilot_v0.1 release
- 记录 1 个 empty response，并单独列入补跑队列
- 标记 classifier_version = v0.2
- 标记 release_type = classification_only

二、补跑 empty response

只补跑那 1 篇 empty response。
不要重跑其他 70 篇。

补跑后更新：
- classification_index.json
- failed_or_empty_calls.yaml
- scale_test_30_report.md 或另存为 classification_v0.2_71_report.md

如果补跑仍失败：
- status = CLASSIFICATION_FAILED
- needs_manual_review = true
- 不得猜测分类

三、MIXED_PRODUCTS boundary review

对以下 10 篇执行 boundary review：

- Ruohua Lan 2022
- Ge Yulong 2024
- Wei Haopeng 2024
- Yangyuanxi 2022
- Pan Lin 2025
- A_Comparative_Investigation
- s10291-024-01789-2
- s10291-025-01854-4
- s12145-023-00939-3
- 1-s2.0-S0263224125021888-main

每篇输出：

{
  "paper_id": "",
  "product_source": "MIXED_PRODUCTS",
  "claimed_service": "",
  "actual_services_used": [],
  "contains_bds3_ppp_b2b": true/false,
  "contains_external_products": true/false,
  "external_products": [],
  "is_core_ppp_b2b": true/false,
  "boundary_category": "",
  "include_in_core_maps": true/false,
  "needs_full_audit": true,
  "reason": ""
}

输出文件：

research_kb/releases/classification_v0.2_71/mixed_products_boundary_queue.yaml
research_kb/reports/mixed_products_boundary_review.md

四、选择 Full Audit Batch 1

从 53 篇 core PPP-B2b candidates 中选择 15 篇进入 full extraction。

选择规则：
- 5 篇 PPP-B2b service performance
- 4 篇 orbit / clock / DCB / correction generation
- 3 篇 downstream application
- 3 篇 MIXED_PRODUCTS boundary representatives

不要一次性 full audit 53 篇。

为每篇 full audit 输出：
- product_source evidence
- experiment_epoch evidence
- correction_types
- DCB handling
- mathematical_model
- datasets
- metrics
- main_results
- novelty_audit
- reproducibility_blockers
- quote_id validation
- evidence support status
- manual_review_items

五、Full Audit Batch 1 gate

Batch 1 通过条件：

1. invalid_quote_id_rate < 5%
2. critical field WRONG_SUPPORT = 0
3. product_source WRONG_SUPPORT = 0
4. experiment_epoch 不得使用 publication year / received date
5. DCB handling 未提及时必须标记 NOT_MENTIONED 或 INSUFFICIENT_EVIDENCE
6. reproduction_blockers 每篇非空
7. keyword_overlap evidence 在关键字段中不得超过 30%
8. 每篇 manual_review_items <= 15

六、禁止事项

在 Full Audit Batch 1 gate 通过前：

- 不要生成最终 corpus maps
- 不要生成 field_timeline final
- 不要生成 method_lineage final
- 不要生成 reproduction_index final
- 不要将 53 篇全部写入正式知识库
- 不要把 MIXED_PRODUCTS 直接并入 core_ppp_b2b

完成后停止，输出：
research_kb/reports/full_audit_batch_1_report.md
```

## 我的判断

你现在已经跨过了最重要的一关：**分类器不再把 QZSS / Galileo HAS / SBAS / non-B2b 混进 BDS-3 PPP-B2b core**。

下一关不是“继续扩大到 100 篇”，而是：

```text
71-paper classification PASS
→ freeze classifier_v0.2
→ resolve 10 MIXED_PRODUCTS
→ full audit first 15 papers
→ evidence gate PASS
→ then corpus maps
```

所以现在可以很明确地说：**允许进入 full extraction subset，但不允许直接生成最终知识库。**

-----

> [文件不支持导出]
> Full Audit Batch 1 完成 ✅
>
>   6 core PPP-B2b papers audited
>
>   ┌───────────────┬──────────┬───────────────────────┬────────┐
>   │     Paper     │ Product  │     B2b Evidence      │ Status │
>   ├───────────────┼──────────┼───────────────────────┼────────┤
>   │ Jianfei Zang  │ BDS3_B2B │ 201 mentions          │ PASS   │
>   ├───────────────┼──────────┼───────────────────────┼────────┤
>   │ Peida Wu      │ BDS3_B2B │ 60 mentions           │ PASS   │
>   ├───────────────┼──────────┼───────────────────────┼────────┤
>   │ Tang Chenggan │ BDS3_B2B │ 76 mentions           │ PASS   │
>   ├───────────────┼──────────┼───────────────────────┼────────┤
>   │ Yangyuanxi    │ BDS3_B2B │ 58 mentions + 6 dates │ PASS   │
>   ├───────────────┼──────────┼───────────────────────┼────────┤
>   │ Zhao Lewen    │ BDS3_B2B │ 61 mentions           │ PASS   │
>   ├───────────────┼──────────┼───────────────────────┼────────┤
>   │ Zhou Linghao  │ BDS3_B2B │ 35 mentions + 2 dates │ PASS   │
>   └───────────────┴──────────┴───────────────────────┴────────┘
>
>   Gates all passed
>
>   - product_source: 0 errors ✅
>   - non-B2b误入: 0 ✅
>   - WRONG_SUPPORT: 0 ✅
>   - MIXED_PRODUCTS未并入core ✅
>
>   限制说明
>
>   Lite extraction字段覆盖有限（experiment_epoch多为NOT_MENTIONED）。完整字段需full extraction mode。

我会先核对这次上传的 Batch 1 报告和前文状态，重点看是否真的满足“可进入下一阶段”的门槛，以及有没有需要先修正的记录不一致。

初步看这批结果是可接受的，但它更像是 **core B2b 分类/证据门控 PASS**，还不能等同于“完整字段知识库已完成”。我还发现报告里有一个需要先修的小不一致：标题写“8 core papers”，实际表格和 gate 都是 6/6。

很好，这个 **Full Audit Batch 1 可以判定为 PASS**，但要把它的含义限定清楚：

**它通过的是：6 篇 core PPP-B2b 的 product_source / B2b 证据门控。**
**它还没有通过的是：完整字段级 full extraction 知识库入库。**

你这批结果里最重要的好消息是：

- 6/6 都被确认为 `BDS3_B2B`，没有 non-B2b 误入 core。
- `WRONG_SUPPORT = 0`，说明这批没有出现之前 Ge Yulong 那种 product_source 语义错配。
- `MIXED_PRODUCTS` 没有被强行并入 core，这是非常关键的。
- `manual_review_items = 0`，说明这次 programmatic audit 很干净。
- Lite mode 的限制已经被明确写出来，没有把字段缺失伪装成已抽取完成。fileciteturn0file0

但你需要先修一个报告问题：

```text
报告开头写：8 core PPP-B2b papers
实际表格：6 篇
Gate：6/6
结论：6/6
```

所以应改成：

```text
6 core PPP-B2b papers audited.
```

或者如果原计划确实是 8 篇，就要把另外 2 篇列为：

```text
planned_but_not_audited
reason: markdown path missing / excluded / pending
```

否则后面 release index 会混乱。

---

## 下一步不要直接跑全量

现在正确路线是：

```text
Full Audit Batch 1 PASS
→ 冻结 batch_1 release
→ 补齐 Yan Liu 2022
→ 对 6 篇 core 做 full extraction mode
→ 再跑 Batch 2：边界 / MIXED / non-B2b 对抗批
→ 最后才生成 corpus maps final
```

尤其注意：
**Batch 1 这 6 篇基本都是强 B2b 正例。下一批不能继续只跑强正例，否则 classifier 看起来很准，但边界鲁棒性不够。**

---

## 现在给 Claude Code 的下一条指令

可以直接发：

```text
Full Audit Batch 1 已通过，但当前报告需要先修正并冻结 release。

请执行以下任务：

1. 修正 research_kb/reports/full_audit_batch_1_report.md：
   - 将 “8 core PPP-B2b papers” 改为 “6 core PPP-B2b papers”
   - 如果原计划包含 8 篇，请新增 planned_but_not_audited section，列出未审论文和原因
   - 保留 6/6 PASS 结论
   - 明确本 batch 是 lite extraction evidence audit，不是 full field extraction

2. 冻结 release：
   创建：
   research_kb/releases/full_audit_batch_1/

   保存：
   - full_audit_batch_1_report.md
   - audited_papers_index.json
   - audited_papers_index.yaml
   - product_source_gate_summary.md
   - excluded_mixed_products.yaml
   - skipped_papers.yaml
   - limitations.md

3. 生成 machine-readable verdict：
   对 6 篇论文输出：
   - paper_id
   - product_source
   - b2b_mentions
   - epoch_status
   - support_summary
   - gate_status
   - extraction_mode: lite
   - full_extraction_required: true/false
   - notes

4. 补处理 Yan Liu 2022：
   - 修复 markdown path matching
   - 只补跑 Yan Liu，不重跑已通过的 6 篇
   - 判断是否加入 Batch 1 addendum 或进入 Batch 2

5. 进入 full extraction mode：
   对 Batch 1 的 6 篇执行完整字段抽取，重点补齐：
   - experiment_epoch
   - correction_types
   - DCB handling
   - mathematical_model
   - datasets
   - metrics
   - main_results
   - novelty_audit
   - reproducibility_blockers
   - grounding_quotes

6. Full extraction gate：
   通过条件：
   - critical field WRONG_SUPPORT = 0
   - product_source WRONG_SUPPORT = 0
   - experiment_epoch 不得误用 publication year
   - DCB 未提及时必须标记 NOT_MENTIONED 或 INSUFFICIENT_EVIDENCE
   - reproduction_blockers 每篇非空
   - grounding quote invalid rate < 5%
   - manual_review_items 每篇 ≤ 15

7. 禁止事项：
   - 不要直接生成最终 corpus maps
   - 不要把 lite extraction 结果当作完整知识库
   - 不要把 MIXED_PRODUCTS 直接并入 core
   - 不要一次性 full audit 全部 53 篇
```

---

## 我的判断

你现在已经可以进入下一阶段，但阶段名称应该是：

```text
core_b2b_lite_audit_passed
```

而不是：

```text
full_kb_ready
```

最稳的下一步是 **冻结 Batch 1 + 修正 6/8 不一致 + 对这 6 篇跑 full extraction**。这样你的知识库不会只停留在“分类正确”，而是开始真正变成可用于综述、技术路线和复现分析的结构化库。

-----

> 字数太多无法全部复制到Claude code

我会把你现在这段结果压缩成 Claude Code 能直接执行的短指令，不需要把完整长表格都复制过去。核心是：现在不是继续优化 fitz，而是改“证据抽取策略”。

不用把我前面那大段全复制给 Claude Code。**让 Claude Code 自己读项目里的报告**，你只需要给它一条短命令。

复制这段就够：

```text
请继续当前 research_kb 项目。先读取：
- research_kb/reports/full_audit_batch_1_report.md
- research_kb/reports/scale_test_10_final_report.md
- research_kb/releases/classification_v0.2_71/ 如果存在

然后执行下一步：

1. 修正 full_audit_batch_1_report.md 中“8 papers / 6 papers”的不一致；实际已审计为 6 篇。
2. 冻结 full_audit_batch_1 release 到 research_kb/releases/full_audit_batch_1/。
3. 不要修改 pilot_v0.1、scale_test_10、classification_v0.2_71。
4. 不要重跑已经通过的分类或 lite extraction。
5. 对 Full Audit Batch 1 已 PASS 的 6 篇 core PPP-B2b 论文执行完整字段抽取，补齐：
   - experiment_epoch
   - correction_types
   - DCB handling
   - mathematical_model
   - datasets
   - metrics
   - main_results
   - novelty_audit
   - reproduction_blockers
   - grounding_quotes / quote_ids
6. Full extraction 必须通过 gate：
   - product_source WRONG_SUPPORT = 0
   - critical field WRONG_SUPPORT = 0
   - experiment_epoch 不得误用 publication year / received / accepted date
   - DCB 未提及时必须标记 NOT_MENTIONED 或 INSUFFICIENT_EVIDENCE
   - reproduction_blockers 每篇非空
   - grounding quote invalid rate < 5%
   - manual_review_items 每篇 ≤ 15
7. 不要生成最终 corpus maps。
8. 不要一次性 full audit 全部 53 篇。
9. 完成后生成：
   research_kb/reports/full_extraction_batch_1_report.md

先执行，不要问我是否确认。
```

更短版也可以，只复制这个：

```text
读取当前 research_kb 报告，继续执行 Full Audit Batch 1 后续任务：修正 6/8 不一致，冻结 releases/full_audit_batch_1/，然后只对已 PASS 的 6 篇 core PPP-B2b 论文做完整字段抽取。不得修改 pilot_v0.1、scale_test_10、classification_v0.2_71；不得重跑分类；不得生成最终 corpus maps；不得一次性 full audit 全部 53 篇。完成后输出 research_kb/reports/full_extraction_batch_1_report.md，并按既有 gate 检查 product_source、experiment_epoch、DCB、novelty、reproducibility、grounding evidence。
```

以后同类情况就用这个策略：**不要复制长分析，给 Claude Code 一个短目标 + 让它读本地报告文件。**

---

**✨系统提示：**

**检测到当前聊天的对话轮数较多，提示您注意适时创建新聊天。**

（只是一个小提醒。本提醒不影响模型表现）

> 此为 ChatGPT 网页前端自身渲染特性所致。对话过长可能导致浏览器卡顿、响应变慢，从而影响交互使用体验。

---