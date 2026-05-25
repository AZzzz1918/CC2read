# 语言
- 始终用中文回复。

# PDF 处理强制规则

遇到任何 PDF 文件时，必须使用 `danielmiessler-pdf` skill 来处理，包括但不限于：
- 提取正文文本
- 提取表格
- 提取元数据
- 识别页码
- 提取标题、章节、图注、参考文献
- 判断是否需要 OCR
- 输出 Markdown 或结构化文本

严禁直接使用 Claude Code 的 Read 工具读取 PDF 文件。

## 原因

DeepSeek-v4 API 不能直接识别 PDF。Claude Code 也不应该直接把 PDF 当普通文本读取。PDF 必须先经过 `danielmiessler-pdf` skill 预处理，转换为带页码和证据锚点的 Markdown / structured text，然后再传给 DeepSeek-v4 API 做 GNSS / PPP-B2b 科研审计。

## 处理流程

```
paper/*.pdf
  -> danielmiessler-pdf skill
  -> research_kb/markdown/[paper_id].md
  -> research_kb/chunks/[paper_id]/*.md
  -> DeepSeek-v4 API
  -> chunk analysis JSON
  -> paper JSON
  -> grounding quote validation
  -> research_kb
```

## Markdown 输出要求

使用 `danielmiessler-pdf` skill 处理每篇 PDF 后，必须生成：
1. Markdown 正文文件：research_kb/markdown/[paper_id].md
2. PDF 元数据：research_kb/metadata/pdf_parse_report.json
3. OCR/解析失败记录：research_kb/metadata/needs_ocr.yaml

Markdown 中必须保留页码标记：
```
<!-- PAGE: 1 -->
正文...
<!-- PAGE: 2 -->
正文...
```

不可提取文本的页面：
```
<!-- PAGE: 5 -->
[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]
```

OCR 来源内容：
```
<!-- PAGE: 5 OCR_DERIVED -->
OCR text...
```

## 反幻觉边界

`danielmiessler-pdf` skill 只负责 PDF 解析和内容提取，不负责科研理解。

禁止在 PDF 处理阶段做以下事情：
- 不要总结论文
- 不要判断创新性
- 不要判断是否 PPP-B2b
- 不要推断实验时间
- 不要推断产品源
- 不要补全作者、年份、数据集、指标
- 不要解释公式含义
- 不要生成复现建议

这些全部交给 DeepSeek-v4 审计层完成，并且 DeepSeek 只能基于 Markdown 原文证据进行判断。

## DeepSeek 调用边界

DeepSeek-v4 API 永远只接收由 `danielmiessler-pdf` skill 输出的 Markdown / chunk 文本，不直接接收 PDF。

所有传给 DeepSeek 的 prompt 中都应写：
"你正在读取由 PDF 转换得到的 Markdown 论文文本。"

# 识图能力

你的底层模型不具备原生识图能力。遇到图片时，**不要用 Read 工具**，改用 vision.js：

```
node vision.js "<图片路径>" "用中文描述这张图片"
```

## 触发场景

- 用户分享图片路径（本地或网络 URL）
- 消息中出现 "Saved attachments:" 并列出图片
- 用户要求分析、描述、识别图片内容
