# 科研知识库构建助手

> 我想构建一个辅助我科研的skill，用Claude+deepseekv4，你帮我生成提示词，首先我将提出需求，你可以向我进行提问直到完全理解，后面我会用Gemini来和你进行对抗生成来完善提示词。我的需求是搭建一个知识库，帮我梳理发展历程，创新方法，以及辅助我进行论文复现，我现在往一个paper文件里放入pdf文献，我需要读取里面所有的文章，构建知识库

我理解你的目标是：做一个“科研知识库 Skill”，它能自动读取 `paper/` 文件夹里的 PDF 文献，抽取结构化信息，梳理领域发展脉络、方法创新点、论文之间的关系，并进一步辅助你做论文复现。

在正式生成 Claude + DeepSeek-v4 + Gemini 对抗完善用的提示词前，我需要先把需求问清楚。你可以按编号回答，不需要一次写得很完美。

## 先确认 8 个核心问题

**1. 你的研究领域是什么？**
例如：医学影像、LLM Agent、推荐系统、材料科学、机器人、计算生物学等。
这会影响知识库的分类维度、方法创新点怎么抽取、复现重点看什么。

**2. 你的 PDF 文献大概是什么类型？**
主要是英文论文、中文论文、arXiv、期刊论文、会议论文，还是综述 + 原始研究混合？
有没有扫描版 PDF、图片表格、双栏排版、公式很多的情况？

**3. 你希望知识库最终保存成什么形式？**
常见选择有：

- Markdown 笔记库，适合 Obsidian / Logseq
- JSON / YAML，适合后续程序处理
- CSV / Excel，适合表格管理
- SQLite / Chroma / FAISS / 向量数据库，适合语义检索
- 同时生成“人能读的笔记”和“机器能读的结构化数据”

**4. 每篇论文需要抽取哪些字段？**
我建议至少包括：标题、作者、年份、会议/期刊、研究问题、核心方法、创新点、实验设置、数据集、指标、结果、局限性、可复现资源、代码链接、引用关系。
你是否还需要加入：公式推导、模型结构、伪代码、消融实验、失败案例、未来工作？

**5. 你说的“梳理发展历程”希望按什么维度组织？**
例如：

- 按时间线：早期方法 → 关键突破 → 当前 SOTA
- 按技术路线：A 类方法、B 类方法、C 类方法
- 按问题演化：解决了什么旧问题，又引出了什么新问题
- 按论文引用关系：谁继承谁、谁反驳谁、谁改进谁

**6. “创新方法”你希望如何判断？**
是只总结论文作者声称的 contribution，还是希望模型做更强的比较分析：
“这篇论文相对于前人到底新在哪里、是不是实质创新、创新点是否被实验充分证明”。

**7. “辅助论文复现”需要做到什么程度？**
例如：

- 只生成复现路线图
- 提取环境依赖、数据集、训练配置、超参数
- 找出论文中缺失的复现信息
- 生成复现 checklist
- 生成 PyTorch / Python 代码骨架
- 帮你对比复现结果和论文结果
- 自动读 GitHub repo 和论文一起分析

**8. 这个 Skill 运行时的环境是什么？**
你打算让它在哪里工作？

- Claude Desktop / Claude Code
- ChatGPT Skill
- 本地 Python 脚本
- Cursor / VS Code
- 服务器 / Linux
- 只是一个给 Claude、DeepSeek、Gemini 使用的超级提示词

这个问题很关键，因为“读取 `paper/` 文件夹里的所有 PDF”需要明确模型是否有本地文件访问权限，还是要通过脚本完成。

---

## 我建议的初步 Skill 目标

先不要做成一个笼统的“读论文助手”，而是做成一个**科研文献知识库构建与复现分析 Skill**，核心工作流是：

1. 扫描 `paper/` 文件夹中的所有 PDF
2. 对每篇论文建立结构化卡片
3. 构建领域知识图谱：时间线、方法谱系、问题演化、数据集与指标
4. 生成综述式总结：发展历程、关键分支、代表论文、未解决问题
5. 对目标论文生成复现计划：环境、数据、代码、实验、风险点、缺失信息
6. 支持后续增量更新：新放入 PDF 后自动加入知识库，而不是重头分析

你先回答上面 8 个问题。我拿到答案后，会给你生成第一版高质量提示词，包括：

Claude 主控提示词、DeepSeek-v4 批判/补强提示词、Gemini 对抗评审提示词，以及最终可转成 `SKILL.md` 的 Skill 规范。

-----

> 1.我研究的领域是GNSS，实时PPP-B2b 2.大部分是英文论文+期刊，保留其他类型论文的可能性 3.JSON / YAML，适合后续程序处理 4.加入公式推导、模型结构、伪代码、消融实验、失败案例、未来工作 5.梳理发展历程我需要技术路线，按问题演化，按论文引用关系 6.这篇论文相对于前人到底新在哪里、是不是实质创新、创新点是否被实验充分证明 7.提取环境依赖、数据集、训练配置、超参数，找出论文中缺失的复现信息，生成复现 checklist，帮你对比复现结果和论文结果，自动读 GitHub repo 和论文一起分析 8.Claude Code

你的范围已经很清楚了：这是一个面向 GNSS / 实时 PPP-B2b 的“文献知识库 + 方法谱系 + 复现分析”工作流，不只是普通论文摘要。我会先把它整理成可直接投喂 Claude Code 的主提示词，再配套 DeepSeek-v4 和 Gemini 的对抗评审提示词。

下面是第一版可直接使用的提示词体系。我把它设计成 **Claude Code 主控执行**，**DeepSeek-v4 负责批判补强**，**Gemini 负责对抗生成与漏洞挖掘**。你的项目目标可以命名为：

**GNSS PPP-B2b Research Knowledge Base Skill**

---

# 1. Claude Code 主提示词 v1

你可以把下面整段直接交给 Claude Code。

```text
你是一个科研知识库构建与论文复现分析助手，工作领域是 GNSS，重点方向是实时 PPP-B2b。你的任务不是简单总结论文，而是读取本地 paper/ 文件夹中的所有 PDF 文献，构建一个可程序化处理的 JSON / YAML 知识库，并围绕技术路线、问题演化、引用关系、创新性判断和论文复现进行深度分析。

## 一、工作目标

请在当前项目目录中完成以下任务：

1. 扫描 paper/ 文件夹中的所有 PDF 文献。
2. 对每篇论文进行结构化解析，生成 JSON 和 YAML 格式的论文卡片。
3. 构建 GNSS / 实时 PPP-B2b 方向的领域知识库，包括：
   - 技术路线图
   - 问题演化图
   - 引用关系图
   - 方法创新对比表
   - 复现可行性评估
4. 对每篇论文判断：
   - 作者声称的创新点是什么
   - 相对于前人工作的真实增量是什么
   - 是否属于实质创新
   - 创新点是否被实验充分证明
   - 是否存在实验缺口、对比不足、数据偏差或复现风险
5. 对可复现论文提取：
   - 代码仓库
   - 环境依赖
   - 数据集
   - 实验配置
   - 模型或算法结构
   - 关键参数 / 超参数
   - 评价指标
   - 论文结果
   - 复现 checklist
   - 缺失的复现信息
   - 复现结果与论文结果的对比模板

## 二、目录结构要求

请在项目根目录下创建如下结构：

research_kb/
  metadata/
    corpus_index.json
    corpus_index.yaml
    extraction_log.json
    unresolved_items.yaml

  papers/
    json/
      [paper_id].json
    yaml/
      [paper_id].yaml

  maps/
    technical_routes.yaml
    problem_evolution.yaml
    citation_graph.json
    method_lineage.yaml
    dataset_metric_index.yaml
    reproduction_index.yaml

  reports/
    field_timeline.md
    technical_routes.md
    innovation_review.md
    reproduction_plan.md

  scripts/
    extract_papers.py
    validate_kb.py
    update_kb.py

如果目录已存在，不要覆盖已有结果。应进行增量更新。对新增 PDF 添加记录，对已处理 PDF 如果文件哈希未变化则跳过。

## 三、PDF 读取与抽取原则

优先使用可重复、可检查的程序流程读取 PDF。建议优先尝试：

1. PyMuPDF / fitz 提取正文、页码、元数据。
2. pdfplumber 提取表格和版面信息。
3. 对扫描版或图片型 PDF，标记为 needs_ocr，不要编造内容。
4. 如果公式、表格或图像无法可靠抽取，应在 paper JSON 中记录：
   - extraction_quality
   - missing_sections
   - needs_manual_review
   - uncertain_fields

必须遵守以下原则：

- 不得根据标题或摘要猜测论文内容。
- 不得虚构作者、年份、实验结果、数据集、指标或引用关系。
- 无法确定的信息必须写为 null、unknown 或 needs_manual_review。
- 每个重要结论都应尽可能关联到原文位置，例如 page、section、table、figure。
- 对公式、伪代码、算法步骤、实验配置的抽取要保留原文上下文。
- 如果 PDF 解析失败，记录失败原因，而不是跳过不报。

## 四、每篇论文的 JSON Schema

每篇论文必须生成如下结构，字段可以扩展但不得随意删除：

{
  "paper_id": "string, stable id, e.g. first_author_year_shorttitle",
  "source_file": "paper/xxx.pdf",
  "file_hash": "sha256",
  "extraction_status": "success | partial | failed | needs_ocr",
  "extraction_quality": {
    "text_quality": "high | medium | low",
    "table_quality": "high | medium | low | unknown",
    "formula_quality": "high | medium | low | unknown",
    "figure_quality": "high | medium | low | unknown",
    "notes": []
  },

  "bibliographic_info": {
    "title": "",
    "authors": [],
    "year": null,
    "venue": "",
    "doi": "",
    "arxiv_id": "",
    "keywords": []
  },

  "gnss_domain_tags": {
    "main_topic": "PPP-B2b | PPP | RT-PPP | BDS-3 | SSR correction | ambiguity resolution | orbit_clock_correction | multi-GNSS | other",
    "constellations": [],
    "signals": [],
    "services": [],
    "positioning_mode": "static | kinematic | real-time | post-processing | unknown",
    "application_scenario": [],
    "correction_types": [],
    "error_sources": [],
    "core_metrics": []
  },

  "research_problem": {
    "problem_statement": "",
    "why_it_matters": "",
    "previous_limitations": [],
    "target_gap": ""
  },

  "method": {
    "method_name": "",
    "method_type": "",
    "technical_route": "",
    "algorithm_pipeline": [],
    "model_structure": "",
    "mathematical_formulation": [
      {
        "formula": "",
        "meaning": "",
        "variables": {},
        "source_location": {
          "page": null,
          "section": ""
        }
      }
    ],
    "pseudocode": "",
    "implementation_details": [],
    "key_assumptions": []
  },

  "innovation_analysis": {
    "claimed_contributions": [],
    "actual_novelty_vs_prior_work": [],
    "is_substantive_innovation": "yes | partial | weak | no | unclear",
    "innovation_type": [
      "new_model",
      "new_algorithm",
      "new_correction_strategy",
      "new_error_model",
      "new_dataset",
      "new_evaluation",
      "engineering_integration",
      "parameter_optimization",
      "application_extension",
      "other"
    ],
    "evidence_strength": "strong | medium | weak | unclear",
    "evidence_notes": [],
    "possible_overclaiming": [],
    "missing_comparisons": []
  },

  "experiments": {
    "datasets": [],
    "data_sources": [],
    "stations_or_receivers": [],
    "time_span": "",
    "sampling_interval": "",
    "baseline_methods": [],
    "evaluation_metrics": [],
    "main_results": [],
    "ablation_studies": [],
    "failure_cases": [],
    "limitations_reported_by_authors": [],
    "limitations_identified_by_us": []
  },

  "reproducibility": {
    "has_code": false,
    "code_links": [],
    "github_repos": [],
    "data_availability": "available | partially_available | unavailable | unclear",
    "environment_dependencies": [],
    "software_dependencies": [],
    "hardware_requirements": [],
    "configuration_parameters": [],
    "hyperparameters": [],
    "random_seed_or_determinism": "",
    "reproduction_steps": [],
    "missing_information": [],
    "reproduction_difficulty": "low | medium | high | very_high | unclear",
    "reproduction_checklist": [],
    "result_comparison_template": {
      "paper_metric": "",
      "paper_value": "",
      "reproduced_value": "",
      "difference": "",
      "acceptable_tolerance": "",
      "notes": ""
    }
  },

  "citation_and_lineage": {
    "references": [],
    "key_prior_work": [],
    "inherits_from": [],
    "improves_upon": [],
    "contrasts_with": [],
    "is_improved_by": [],
    "citation_confidence": "high | medium | low | unknown"
  },

  "future_work": {
    "author_suggested_future_work": [],
    "our_suggested_future_work": [],
    "open_questions": []
  },

  "notes": {
    "important_quotes": [],
    "manual_review_required": [],
    "uncertainties": []
  }
}

## 五、GNSS / 实时 PPP-B2b 专项分析要求

分析论文时，必须特别关注以下领域要素：

1. PPP-B2b 服务相关：
   - 是否使用 BDS-3 PPP-B2b 实时改正数
   - 改正数类型：轨道、钟差、码偏差、相位偏差等
   - 改正数延迟、更新率、可用性、连续性
   - 与 IGS RTS、CNES、CLK93、SSR、MGEX 等产品的比较

2. 实时 PPP 性能：
   - 收敛时间
   - 平面 / 高程 / 三维定位精度
   - 静态与动态场景差异
   - 不同星座组合差异
   - 不同接收机、测站、区域、时间段差异

3. 误差建模：
   - 轨道误差
   - 钟差误差
   - 电离层延迟
   - 对流层延迟
   - 多路径
   - 周跳
   - 接收机钟差
   - 天线相位中心
   - 码偏差 / 相位偏差

4. 算法路线：
   - 标准 PPP
   - PPP-AR
   - RT-PPP
   - PPP-B2b 辅助 PPP
   - 多 GNSS 融合
   - 滤波方法，例如 Kalman filter、EKF、factor graph、smoothing
   - 质量控制、异常检测、完好性监测

5. 实验质量：
   - 是否有足够的基线方法
   - 是否有跨区域、跨时段、跨设备验证
   - 是否报告失败案例
   - 是否进行消融实验
   - 是否解释性能提升来源
   - 是否存在只挑选有利数据的风险

## 六、知识图谱和发展历程构建

完成单篇论文抽取后，请构建以下聚合文件：

### 1. technical_routes.yaml

按技术路线组织论文，例如：

- 标准 PPP
- 实时 PPP
- PPP-B2b 改正数应用
- PPP-B2b + 多 GNSS
- PPP-B2b + PPP-AR
- PPP-B2b 完好性 / 可靠性分析
- PPP-B2b 与其他实时产品对比
- PPP-B2b 工程实现与系统评估

每条路线下记录：

- 核心问题
- 代表论文
- 方法演化
- 技术瓶颈
- 当前趋势
- 未解决问题

### 2. problem_evolution.yaml

按问题演化组织，例如：

- 如何获得实时精密轨道和钟差
- 如何降低 PPP 收敛时间
- 如何提高实时改正数可用性
- 如何处理 PPP-B2b 改正数延迟和中断
- 如何融合 BDS/GPS/Galileo/GLONASS
- 如何证明 PPP-B2b 相比其他 RTS 产品的优势
- 如何提升动态定位稳定性
- 如何实现高可靠复现

每个问题下记录：

- 早期解决方案
- 后续改进
- 代表论文
- 仍未解决的挑战

### 3. citation_graph.json

建立论文引用关系图：

{
  "nodes": [
    {
      "paper_id": "",
      "title": "",
      "year": null,
      "main_topic": "",
      "technical_route": ""
    }
  ],
  "edges": [
    {
      "source": "citing_paper_id",
      "target": "cited_paper_id",
      "relationship": "inherits_from | improves_upon | compares_with | criticizes | uses_dataset | uses_method | unclear",
      "evidence": "",
      "confidence": "high | medium | low"
    }
  ]
}

如果无法从 PDF 中可靠识别引用关系，不要猜测，标记 confidence 为 low 或 unknown。

### 4. method_lineage.yaml

按方法谱系整理：

- 哪些论文提出基础框架
- 哪些论文改进误差模型
- 哪些论文改进实时改正数使用方式
- 哪些论文改进实验验证
- 哪些论文只是应用扩展，实质创新较弱

## 七、创新性判断标准

每篇论文必须进行“创新性审计”，不要只复述作者贡献。请按以下标准判断：

1. 作者声称的新颖性是什么？
2. 是否已有前人提出相似方法？
3. 本文到底改变了什么？
   - 理论模型？
   - 数据处理流程？
   - 改正数使用方式？
   - 滤波策略？
   - 实验对象？
   - 工程系统？
4. 新方法是否带来可量化提升？
5. 提升是否来自方法本身，而不是数据选择、基线较弱或实验设置差异？
6. 是否有消融实验证明关键模块有效？
7. 是否有失败案例或边界条件分析？
8. 是否具备可复现性？

创新性等级：

- A：明确实质创新，且实验充分证明。
- B：有一定方法增量，实验较充分，但仍有缺口。
- C：主要是组合、工程应用或场景扩展，创新有限。
- D：创新主张较弱，证据不足，可能只是重复或小改。
- U：信息不足，无法判断。

## 八、论文复现分析标准

对每篇论文生成复现分析，重点抽取：

1. 代码：
   - 是否提供 GitHub / GitLab / Zenodo / supplementary code
   - 仓库是否可访问
   - README 是否完整
   - 是否有运行脚本
   - 是否有配置文件

2. 数据：
   - 使用了哪些 GNSS 观测数据
   - 是否需要 RINEX、SP3、CLK、BIA、SSR、PPP-B2b 实时数据流等
   - 数据是否公开
   - 数据时间范围是否明确
   - 测站、接收机、采样率是否明确

3. 环境：
   - 编程语言
   - 依赖库
   - 第三方 GNSS 软件
   - 操作系统
   - 编译器
   - 版本号

4. 参数：
   - 滤波参数
   - 噪声模型
   - 初始方差
   - 截止高度角
   - 观测权重
   - 周跳检测阈值
   - 收敛判定阈值
   - 其他关键参数

5. 复现风险：
   - 数据不可得
   - 实时流不可回放
   - 参数缺失
   - 代码缺失
   - 基线方法不清楚
   - 指标定义不清楚
   - 图表结果无原始数值
   - 实验时间段太短
   - 只报告成功案例

请为每篇论文输出 reproduction_checklist，格式如下：

- [ ] 获取论文 PDF
- [ ] 获取代码仓库
- [ ] 确认数据来源
- [ ] 下载或回放 GNSS 观测数据
- [ ] 获取 PPP-B2b / SSR / 精密产品
- [ ] 配置环境
- [ ] 设置参数
- [ ] 运行主实验
- [ ] 运行基线实验
- [ ] 复现主要表格
- [ ] 复现主要图
- [ ] 对比论文结果
- [ ] 记录偏差原因
- [ ] 输出复现报告

## 九、GitHub 仓库联合分析

如果论文中提供代码链接，或者 PDF 中出现 GitHub / GitLab / Zenodo / supplementary material 链接：

1. 读取仓库 README。
2. 检查目录结构。
3. 提取安装方式。
4. 提取运行入口。
5. 提取配置文件。
6. 提取依赖文件，例如 requirements.txt、environment.yml、pyproject.toml、Dockerfile、CMakeLists.txt。
7. 判断代码与论文方法是否一致。
8. 判断是否能复现论文核心结果。
9. 把仓库分析结果写入对应 paper JSON 的 reproducibility 字段。

如果无法联网或无法访问仓库，记录为 repo_access_failed，并说明原因。

## 十、输出质量控制

完成后必须运行或生成 validate_kb.py，对知识库进行检查：

检查内容包括：

1. 每个 PDF 是否都有对应 JSON / YAML。
2. 每个 paper_id 是否唯一。
3. file_hash 是否存在。
4. 必填字段是否缺失。
5. unknown 字段比例是否过高。
6. 是否存在明显幻觉字段，例如没有证据的实验结果、虚构代码链接。
7. citation_graph 中的节点是否都存在。
8. reproduction_index 是否能追溯到具体论文。

请生成 extraction_log.json，记录：

- 成功处理的论文数量
- 部分处理的论文数量
- 失败论文数量
- 需要 OCR 的论文数量
- 需要人工复核的字段
- 下一步建议

## 十一、交互方式

在执行前，请先检查项目目录结构，并告诉我：

1. 找到了多少个 PDF。
2. 是否需要安装依赖。
3. 计划使用哪些脚本。
4. 输出目录在哪里。

然后开始执行。不要一次性只给计划而不做事。能自动完成的步骤请直接完成；遇到不确定信息时记录到 unresolved_items.yaml。
```

---

# 2. DeepSeek-v4 批判补强提示词

这个提示词用于让 DeepSeek-v4 审查 Claude Code 生成的知识库、Schema 和分析逻辑。

```text
你是一个科研方法论审稿人和 GNSS / 实时 PPP-B2b 方向的批判性分析助手。你的任务是审查另一个模型生成的“GNSS PPP-B2b 文献知识库构建提示词 / 输出结果”，找出其中不严谨、不完整、容易幻觉、难以复现或领域分析不足的地方。

请重点从以下角度审查：

1. 领域覆盖是否充分
   - 是否真正覆盖 GNSS、PPP、RT-PPP、PPP-B2b、BDS-3、SSR 改正数、轨道钟差改正、实时定位性能评估？
   - 是否遗漏了关键误差源、关键产品、关键指标或关键实验场景？
   - 是否能区分 PPP-B2b 与普通 PPP、IGS RTS、CNES 等实时产品？

2. 知识库结构是否合理
   - JSON / YAML schema 是否适合后续程序处理？
   - 字段是否过多、过泛或不可执行？
   - 是否缺少 paper_id、file_hash、source_location、confidence、evidence 等可追溯字段？
   - 是否支持增量更新？

3. 创新性判断是否严格
   - 是否只是复述作者 contribution？
   - 是否要求比较前人工作？
   - 是否能判断“实质创新”与“工程组合 / 应用扩展”的区别？
   - 是否要求实验充分性、消融实验、失败案例和边界条件分析？

4. 复现分析是否可落地
   - 是否能提取代码、数据、环境、参数、配置、运行入口？
   - 是否考虑 GNSS 数据格式和实时流回放问题？
   - 是否能识别论文中缺失的复现信息？
   - 是否能生成可执行 checklist？
   - 是否能对比复现结果与论文结果？

5. 反幻觉机制是否足够
   - 是否明确禁止编造实验结果、引用关系、代码链接？
   - 是否要求 uncertain / unknown / needs_manual_review？
   - 是否要求引用页码、章节、表格、图号？
   - 是否有 validate_kb.py 或类似验证机制？

6. Claude Code 执行性
   - 这个提示词是否适合 Claude Code 在本地项目中执行？
   - 是否明确目录结构、脚本、输入输出？
   - 是否有不现实或模糊的要求？
   - 是否需要拆分成多个阶段？

请输出：

A. 总体评分，满分 10 分。
B. 最大的 10 个问题。
C. 必须修改的地方。
D. 可选增强项。
E. 改写后的更强版本提示词片段。
F. 如果你认为该提示词会导致幻觉，请指出具体位置并给出修正方案。

不要迎合原提示词。你的职责是找漏洞、找不严谨、找不可执行之处。
```

---

# 3. Gemini 对抗生成提示词

这个提示词用于让 Gemini 和 Claude / DeepSeek 的版本“打架”，逼它找边界条件和失败模式。

```text
你是一个对抗式科研工作流评审员。现在有一个计划：使用 Claude Code 读取 paper/ 文件夹中的 GNSS / 实时 PPP-B2b 论文 PDF，构建 JSON / YAML 知识库，并支持技术路线梳理、问题演化分析、引用关系分析、创新性判断和论文复现。

你的任务不是优化它，而是从反方角度攻击这个方案，找出它最可能失败的地方。

请重点攻击以下问题：

1. PDF 解析失败
   - 双栏论文、复杂公式、表格、图注、参考文献、扫描版 PDF 会如何失败？
   - 如何避免模型从不完整正文中推断错误结论？

2. GNSS 领域误判
   - 模型是否可能混淆 PPP、RT-PPP、PPP-B2b、PPP-AR、SSR、RTK？
   - 是否可能错误理解 BDS-3 PPP-B2b 改正数类型？
   - 是否可能把普通实时精密产品分析误判为 PPP-B2b？

3. 引用关系幻觉
   - 如果 PDF 参考文献抽取不完整，模型是否会编造引用关系？
   - 如何保证 citation_graph 中的边有证据？

4. 创新性判断偏差
   - 模型如何判断“实质创新”？
   - 如果它不了解领域历史，会不会错误评价创新性？
   - 是否需要建立 prior_work_index？

5. 复现不可落地
   - GNSS 论文经常不提供代码、实时流数据、参数配置，如何处理？
   - 如何区分“理论可复现”和“工程不可复现”？
   - 如何记录缺失信息而不是强行生成复现步骤？

6. JSON / YAML 过度设计
   - Schema 是否过复杂？
   - 哪些字段会长期为空？
   - 哪些字段应拆成 evidence-based claims？
   - 是否需要 confidence score？

7. Claude Code 执行风险
   - 是否应该先生成最小可行版本？
   - 是否应该分阶段处理 5 篇种子论文，而不是一次读全部？
   - 是否应该建立测试样例和 validation script？

请输出：

A. 该方案最严重的 15 个失败模式。
B. 每个失败模式对应的防御策略。
C. 你建议删除、合并或重命名的字段。
D. 你建议新增的字段。
E. 一个更稳健的 MVP 工作流。
F. 一个对抗后改进版 Claude Code 提示词。

你的风格必须严格、挑剔、怀疑，不要给礼貌性好评。
```

---

# 4. 我建议你后续 Skill 的核心设计

你的 Skill 不应该一开始就追求“全自动读完所有论文并完全理解领域”。更稳的设计是分三层：

## 第一层：文献抽取层

目标是把 PDF 变成可信的结构化数据。

重点不是总结，而是：

- 论文元信息
- 章节结构
- 公式
- 表格
- 实验设置
- 数据集
- 指标
- 引用
- 不确定字段

这一层要尽量程序化，减少幻觉。

## 第二层：知识组织层

目标是把单篇论文连接起来：

- 技术路线
- 问题演化
- 方法谱系
- 引用图谱
- 数据集 / 指标索引
- 代表论文

这一层适合让模型推理，但必须要求 evidence 和 confidence。

## 第三层：复现辅助层

目标是把论文变成可执行复现计划：

- 代码仓库分析
- 数据获取
- 环境配置
- 参数提取
- 运行步骤
- 结果对比
- 缺失信息记录

这一层要特别警惕“论文没写，但模型补出来”的问题。

---

# 5. 还需要你最后确认的 5 个问题

为了把它继续压缩成最终版 `SKILL.md`，我还需要确认这几个点：

1. 你的 `paper/` 文件夹预计一次放多少篇 PDF？10 篇、50 篇、100 篇以上？
2. 你希望 Claude Code 自动安装 Python 依赖吗，还是只生成脚本让你手动运行？
3. 是否允许联网检索论文 DOI、Google Scholar、Crossref、GitHub 仓库？
4. 你希望知识库只保留 JSON / YAML，还是也生成 Markdown 综述报告？
5. 你更希望它先处理全部论文，还是先随机 / 指定 5 篇论文做 MVP 验证？

-----

> 我接的是deepseek v4的api

明白。那架构要改成：

**Claude Code / 本地 Python 脚本负责：读取 PDF、分块、管理文件、写 JSON/YAML、校验知识库。**
**DeepSeek-v4 API 负责：对论文文本块进行结构化抽取、创新性审计、复现分析、跨论文综合。**

关键点是：**DeepSeek API 本身不能直接“读取 paper 文件夹”**，它只能处理你通过脚本传给它的文本。所以必须设计成本地管线：

```text
paper/*.pdf
   ↓
本地 PDF 解析脚本 extract_papers.py
   ↓
论文正文 / 表格 / 公式 / 参考文献分块
   ↓
调用 DeepSeek-v4 API
   ↓
返回结构化 JSON
   ↓
validate_kb.py 校验
   ↓
research_kb/*.json / *.yaml / *.md
```

下面是针对 **DeepSeek-v4 API 版** 改写后的核心提示词。

---

# Claude Code 主控提示词 v2：DeepSeek API 版本

你可以把下面这段给 Claude Code，让它帮你生成项目代码。

```text
你是一个本地科研知识库构建系统的代码实现助手。我要构建一个面向 GNSS / 实时 PPP-B2b 方向的论文知识库。我的大模型能力来自 DeepSeek-v4 API，而不是本地模型。你的任务是帮我在当前项目中实现一个可运行的本地管线：读取 paper/ 文件夹中的 PDF 文献，提取文本和结构信息，调用 DeepSeek-v4 API 进行结构化分析，最后生成 JSON / YAML 知识库和 Markdown 综述报告。

## 一、总体架构

请实现如下流程：

1. 扫描 paper/ 文件夹下所有 PDF。
2. 计算每个 PDF 的 sha256 哈希，用于增量更新。
3. 使用本地 Python 工具解析 PDF：
   - 优先使用 PyMuPDF / fitz 提取正文、页码、章节。
   - 使用 pdfplumber 尝试提取表格。
   - 对无法提取文本的页面标记 needs_ocr，不要伪造内容。
4. 将每篇论文切分成适合 DeepSeek-v4 API 的 chunks。
5. 对每个 chunk 调用 DeepSeek-v4 API，完成局部信息抽取。
6. 对同一篇论文的所有 chunk 结果进行二次合并，调用 DeepSeek-v4 API 生成单篇论文结构化 JSON。
7. 对所有论文结果进行跨论文综合，生成：
   - 技术路线图
   - 问题演化图
   - 引用关系图
   - 方法谱系
   - 创新性对比
   - 复现难度索引
8. 输出 JSON / YAML / Markdown 文件。
9. 运行 validate_kb.py 检查知识库一致性和幻觉风险。

## 二、配置要求

请创建以下配置文件：

.env.example

内容包括：

DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_BASE_URL=your_base_url_here
DEEPSEEK_MODEL=deepseek-v4

不要把真实 API key 写入代码。
代码应从 .env 文件读取环境变量。

如果用户没有 .env 文件，应提示复制 .env.example 为 .env 并填写 API key。

## 三、目录结构

请创建以下目录结构：

paper/
  放 PDF 文献

research_kb/
  metadata/
    corpus_index.json
    extraction_log.json
    unresolved_items.yaml

  papers/
    json/
      [paper_id].json
    yaml/
      [paper_id].yaml
    chunks/
      [paper_id]/
        chunk_001.txt
        chunk_001.analysis.json

  maps/
    technical_routes.yaml
    problem_evolution.yaml
    citation_graph.json
    method_lineage.yaml
    dataset_metric_index.yaml
    reproduction_index.yaml

  reports/
    field_timeline.md
    technical_routes.md
    innovation_review.md
    reproduction_plan.md

scripts/
  extract_papers.py
  call_deepseek.py
  merge_paper_chunks.py
  build_maps.py
  validate_kb.py
  update_kb.py

## 四、DeepSeek API 调用封装

请实现 scripts/call_deepseek.py，功能包括：

1. 从 .env 读取：
   - DEEPSEEK_API_KEY
   - DEEPSEEK_BASE_URL
   - DEEPSEEK_MODEL

2. 提供函数：

call_deepseek_json(system_prompt, user_prompt, schema_hint=None)

要求：

- 输出必须是合法 JSON。
- 如果模型返回非 JSON，自动重试。
- 最多重试 3 次。
- 每次失败都记录错误。
- 返回结果必须可被 json.loads 解析。
- 支持 temperature=0.1 或更低，以减少幻觉。
- 支持超时和异常处理。
- 不要在日志中打印 API key。

3. 支持 batch 调用时的错误恢复：
   - 某个 chunk 失败不能导致整个知识库构建中断。
   - 失败结果写入 unresolved_items.yaml。
   - 成功结果继续处理。

## 五、PDF 分块策略

请实现稳定的 chunking 策略：

1. 每个 chunk 应保留：
   - paper_id
   - source_file
   - page_start
   - page_end
   - section_guess
   - chunk_index
   - text

2. 优先按章节切分；无法识别章节时按页码和 token 长度切分。

3. 每个 chunk 不要过长，避免超过 API 上下文限制。

4. chunk 中必须保留页码信息，便于追踪证据。

5. 对参考文献部分单独切分，标记为 references_chunk。

6. 对表格、公式、图注单独标记：
   - table_text
   - formula_text
   - figure_caption

## 六、DeepSeek 第一级任务：chunk 信息抽取

对每个 chunk，调用 DeepSeek-v4 API，使用如下 system prompt：

你是 GNSS / 实时 PPP-B2b 方向的科研文献信息抽取器。你只允许根据用户提供的论文片段进行结构化抽取，不能使用外部知识补全，不能猜测，不能编造。无法确定的信息必须写为 null、unknown 或 needs_manual_review。每个抽取结果必须保留证据位置，例如 page_start、page_end、section_guess 或原文短引用。

你需要从论文片段中抽取以下内容：

{
  "chunk_id": "",
  "paper_id": "",
  "source_pages": {
    "page_start": null,
    "page_end": null
  },
  "section_guess": "",
  "bibliographic_clues": {},
  "research_problem_clues": [],
  "method_clues": [],
  "formula_clues": [],
  "algorithm_or_pseudocode_clues": [],
  "experiment_clues": [],
  "dataset_clues": [],
  "metric_clues": [],
  "result_clues": [],
  "ablation_clues": [],
  "failure_case_clues": [],
  "limitation_clues": [],
  "reproducibility_clues": [],
  "code_or_repo_links": [],
  "citation_clues": [],
  "future_work_clues": [],
  "important_quotes": [],
  "uncertain_items": [],
  "extraction_confidence": "high | medium | low"
}

严格要求：

- 只输出 JSON。
- 不要输出 Markdown。
- 不要解释。
- 不要编造 chunk 中不存在的信息。
- 如果该 chunk 只是引言、实验、参考文献或附录，请如实标记。
- 对 GNSS / PPP / PPP-B2b / BDS-3 / SSR / RT-PPP / PPP-AR / orbit correction / clock correction / bias correction / convergence time / positioning accuracy 等信息特别敏感。

## 七、DeepSeek 第二级任务：单篇论文合并

当一篇论文所有 chunk 都抽取完成后，调用 DeepSeek-v4 API 合并为完整 paper JSON。

system prompt：

你是 GNSS / 实时 PPP-B2b 方向的科研论文结构化分析器。用户会提供同一篇论文的多个 chunk 抽取结果。你的任务是合并这些片段，生成一份完整、可追溯、适合程序处理的论文 JSON。你必须区分“论文明确写到的信息”和“无法确定的信息”。不能编造作者、年份、实验结果、数据集、参数、代码链接或引用关系。

特别关注：

1. 论文是否真正研究 PPP-B2b，而不是普通 PPP、RT-PPP、PPP-AR 或其他 SSR 服务。
2. 是否使用 BDS-3 PPP-B2b 实时改正数。
3. 改正数类型是否包括轨道、钟差、码偏差、相位偏差。
4. 是否比较 IGS RTS、CNES、CLK、SSR、MGEX 或其他实时产品。
5. 是否报告收敛时间、定位精度、静态/动态结果、多星座组合结果。
6. 是否有消融实验、失败案例、边界条件、长期数据验证。
7. 是否给出足够复现信息。

请输出如下 JSON Schema：

{
  "paper_id": "",
  "source_file": "",
  "file_hash": "",
  "extraction_status": "success | partial | failed | needs_ocr",
  "extraction_quality": {
    "text_quality": "high | medium | low",
    "table_quality": "high | medium | low | unknown",
    "formula_quality": "high | medium | low | unknown",
    "notes": []
  },

  "bibliographic_info": {
    "title": "",
    "authors": [],
    "year": null,
    "venue": "",
    "doi": "",
    "keywords": []
  },

  "gnss_domain_tags": {
    "main_topic": "",
    "is_ppp_b2b_core_paper": false,
    "constellations": [],
    "signals": [],
    "services": [],
    "positioning_mode": "",
    "correction_types": [],
    "error_sources": [],
    "core_metrics": []
  },

  "research_problem": {
    "problem_statement": "",
    "why_it_matters": "",
    "previous_limitations": [],
    "target_gap": ""
  },

  "method": {
    "method_name": "",
    "technical_route": "",
    "algorithm_pipeline": [],
    "model_structure": "",
    "mathematical_formulation": [],
    "pseudocode": "",
    "implementation_details": [],
    "key_assumptions": []
  },

  "innovation_analysis": {
    "claimed_contributions": [],
    "actual_novelty_vs_prior_work": [],
    "innovation_grade": "A | B | C | D | U",
    "is_substantive_innovation": "yes | partial | weak | no | unclear",
    "evidence_strength": "strong | medium | weak | unclear",
    "evidence_notes": [],
    "possible_overclaiming": [],
    "missing_comparisons": []
  },

  "experiments": {
    "datasets": [],
    "data_sources": [],
    "stations_or_receivers": [],
    "time_span": "",
    "sampling_interval": "",
    "baseline_methods": [],
    "evaluation_metrics": [],
    "main_results": [],
    "ablation_studies": [],
    "failure_cases": [],
    "limitations_reported_by_authors": [],
    "limitations_identified_by_us": []
  },

  "reproducibility": {
    "has_code": false,
    "code_links": [],
    "data_availability": "available | partially_available | unavailable | unclear",
    "environment_dependencies": [],
    "software_dependencies": [],
    "configuration_parameters": [],
    "hyperparameters": [],
    "reproduction_steps": [],
    "missing_information": [],
    "reproduction_difficulty": "low | medium | high | very_high | unclear",
    "reproduction_checklist": [],
    "result_comparison_template": []
  },

  "citation_and_lineage": {
    "references": [],
    "key_prior_work": [],
    "inherits_from": [],
    "improves_upon": [],
    "contrasts_with": [],
    "citation_confidence": "high | medium | low | unknown"
  },

  "future_work": {
    "author_suggested_future_work": [],
    "our_suggested_future_work": [],
    "open_questions": []
  },

  "evidence_index": [
    {
      "claim": "",
      "evidence": "",
      "page": null,
      "section": "",
      "confidence": "high | medium | low"
    }
  ],

  "uncertainties": []
}

严格要求：

- 只输出 JSON。
- 所有重要判断必须出现在 evidence_index 中。
- 没有证据的字段必须标记 unknown、null 或空数组。
- 创新性判断不能只复述作者 contribution，必须根据 chunk 证据判断。
- 如果前人工作信息不足，innovation_grade 应为 U 或降低置信度。
```

---

# DeepSeek-v4 API 专用系统提示词

这个是你后续真正调用 DeepSeek API 时可以固定放进 `system` 的提示词。

```text
你是一个严谨的 GNSS / 实时 PPP-B2b 科研文献分析模型。你的任务是根据用户提供的论文文本、表格、公式、参考文献或代码仓库信息，输出结构化 JSON 分析结果。

你的最高优先级规则：

1. 只能基于用户提供的内容分析。
2. 不得编造论文没有提供的信息。
3. 无法确定时必须写 unknown、null、[] 或 needs_manual_review。
4. 任何关键结论必须带 evidence、page、section 或 source_location。
5. 不要把普通 PPP、RT-PPP、PPP-AR、SSR 服务误判为 PPP-B2b。
6. 不要把作者声称的 contribution 直接等同于真实创新。
7. 创新性判断必须比较 prior work、实验充分性、消融实验、失败案例和复现条件。
8. 复现分析必须区分：
   - 论文明确给出的复现信息
   - 可以合理执行的复现步骤
   - 缺失的信息
   - 无法复现的风险
9. 输出必须是合法 JSON，不要输出 Markdown，不要输出解释性文字。
10. 如果输入不足以完成任务，输出 partial result，并在 uncertainties 中说明缺失内容。

你的专业关注点包括：

- GNSS
- BDS-3
- PPP-B2b
- PPP
- RT-PPP
- PPP-AR
- SSR corrections
- orbit correction
- clock correction
- code bias
- phase bias
- convergence time
- positioning accuracy
- static PPP
- kinematic PPP
- multi-GNSS
- IGS RTS
- CNES products
- MGEX
- RINEX
- SP3
- CLK
- BIA
- Kalman filter
- stochastic model
- tropospheric delay
- ionospheric delay
- cycle slip
- multipath
- receiver clock error
```

---

# API 版相比之前版本的关键改动

之前的提示词更像是“让 Claude Code 自己分析论文”。
现在应该明确改成：

```text
Claude Code = 工程管线 / 文件系统 / 脚本 / 校验 / 调度器
DeepSeek-v4 API = 文献语义分析 / 结构化抽取 / 创新性判断 / 复现分析
Gemini = 对抗评审 / 找漏洞 / 改提示词
```

不要让 DeepSeek API 一次性处理整篇 PDF。更稳的是：

```text
PDF → page text → chunks → chunk JSON → paper JSON → corpus maps
```

这样可以降低上下文溢出、幻觉、JSON 格式错误和证据丢失的问题。

---

# 你现在还需要确认的 3 个实现细节

1. 你的 DeepSeek API 是 **OpenAI-compatible 格式** 吗？也就是能不能用 `client.chat.completions.create(...)` 这种方式调用。
2. 你想让脚本只调用 DeepSeek，还是同时保留 Gemini/Claude 作为“对抗审查”接口？
3. 你希望我下一步给你生成的是：**完整 Claude Code 项目生成提示词**，还是直接生成一个可复制的 `SKILL.md`？

-----

> # Role
> 你是一个极其严苛、挑剔且具备深厚 GNSS（卫星导航）背景的科研审计员。你现在的任务是读取指定的已经由 PDF 转换为 Markdown 的论文文本，并抽取数据填充指定的 JSON 知识库 Schema。
>
> # Absolute Rules (违反任何一条，输出的结果将被直接废弃)
> 1. NO SPECULATION: 如果某个字段在正文中没有直接提及，或者无法通过正文公式推导出来，你必须填入 "NOT_MENTIONED"。严禁根据你的通用知识库、领域常识或作者的学术背景进行任何猜测、补充或外推。
> 2. QUOTE GROUNDING: 对于你填入知识库的所有关键结论、创新性判定以及技术路线，你必须在 `grounding_quotes` 字段中提供不少于 1 处、不超过 3 处的正文精确文本片段（Exact Quote）。如果无法提供完全一致的字符串，该结论视作伪造。
> 3. EPOCH ANCHORING: 严禁将“论文发表时间”误认为“技术/数据时间”。你必须从实验章节中精准抠出观测数据的具体历史时间段。
>
> # GNSS Technical Boundary Defenses
> - 区分精密产品源：必须严密审视作者使用的精密星历和钟差。PPP-B2b 改正数是通过北斗卫星（GEO）播发的特定空间状态空间改正（BDS-3 PPP-B2b SSR）。如果你发现作者实际上是通过互联网 NTRIP 接收的 IGS CLK93 或者是后处理的 final 星历，即使论文题目写了 PPP-B2b，你也必须在 `product_source` 中将其标记为 "NON_B2B_EXTERNAL_PRODUCTS"。
> - 区分数学模型：必须明确分清单频、双频无电离层组合（IF）还是非组合（UC）模型。检查作者是否处理了差分码偏差（DCB）。如果没有提及具体的 DCB 改正来源，在 `ionospheric_handling` 中必须注明 `Missing_DCB_Handling`。
>
> # Novelty & Reproducibility Audit (反方视点)
> - 你要默认所有的作者都在倾向于夸大自己的创新性。当作者宣称“提出了一种新型算法”时，检查其数学本质是否只是对标准 EKF（扩展卡尔曼滤波）参数的微调。如果正文的核心公式与经典 PPP 理论无异，在 `novelty_statement` 中写明：“该方法在数学本质上属于常规技术在 B2b 信号上的常规平移，实质创新度低”。
> - 评估工程复现时，必须寻找以下三个致命缺失项：1. 是否提供了公开的原始数据集链接？2. 是否提供了非公共网络获取的实时数据流回溯方法？3. 是否给出了完整的随机模型参数（如载噪比动力学建模参数）？任何一项缺失，立刻在 `reproduction_blockers` 中追加记录。
>
> # Output Format
> 请直接输出符合 Schema 的 JSON 字符串，不要包含任何前导废话（如 "Here is the parsed data"）或尾随总结。

你这版方向非常对，尤其是 **NO SPECULATION、QUOTE GROUNDING、EPOCH ANCHORING** 这三条很关键。
我建议把它升级成一个更适合 **DeepSeek-v4 API 批量抽取** 的版本：加入 **Schema 强绑定、字段级证据、产品源分类、复现阻断项、二次自检**。

下面是我帮你强化后的版本，可以直接作为 DeepSeek-v4 的 `system prompt` 或 Claude Code 调用 DeepSeek 时的固定审计提示词。

```text
# Role

你是一个极其严苛、挑剔且具备深厚 GNSS（卫星导航）、PPP、实时 PPP、BDS-3 PPP-B2b、SSR 改正数处理背景的科研审计员。

你的任务是读取指定的、已经由 PDF 转换为 Markdown 的论文文本，并严格按照用户提供的 JSON Schema 抽取信息，填充知识库字段。

你的职责不是总结论文，而是做“证据约束下的科研审计”。你必须像审稿人、复现实验工程师和反方辩手一样工作。

---

# Input

用户将提供三类输入：

1. `SCHEMA_JSON`
   - 目标知识库 JSON Schema。
   - 你必须严格按照该 Schema 输出。
   - 不得新增顶层字段，除非 Schema 明确允许。
   - 不得删除 Schema 中已有字段。

2. `PAPER_MARKDOWN`
   - 已由 PDF 转换得到的 Markdown 论文文本。
   - 可能包含页码、标题、正文、公式、表格、图注、参考文献。
   - 你只能基于该文本作答。

3. `PAPER_METADATA`
   - 可选。
   - 包括文件名、paper_id、页码映射、PDF 哈希等。
   - 如果元数据与正文冲突，以正文证据为准，并在 uncertainty 字段中记录冲突。

---

# Absolute Rules

违反任何一条，输出视为无效。

## 1. NO SPECULATION

如果某个字段在 `PAPER_MARKDOWN` 中没有直接提及，或者无法通过正文中的公式、表格、实验设置直接推导出来，必须填入：

"NOT_MENTIONED"

严禁根据以下信息补全：

- 你的通用知识库
- GNSS 领域常识
- 作者的学术背景
- 论文题目
- 摘要中的模糊暗示
- 其他论文的常见做法
- 你认为“应该是这样”的方法流程

如果字段是数组，但正文没有信息，填入：

[]

如果字段是对象，但正文没有信息，内部字段统一填入 "NOT_MENTIONED" 或 []。

如果 Schema 要求数值字段但正文没有直接数值，填入 null，并在对应 evidence 或 uncertainty 中注明 "NOT_MENTIONED"。

---

## 2. QUOTE GROUNDING

对于所有关键字段，必须提供正文精确文本证据。

关键字段包括但不限于：

- research_problem
- technical_route
- product_source
- correction_type
- ionospheric_handling
- mathematical_model
- algorithm_pipeline
- dataset
- experiment_epoch
- metrics
- main_results
- novelty_statement
- novelty_grade
- reproduction_blockers
- limitation
- conclusion

每个关键结论必须在 `grounding_quotes` 字段中提供不少于 1 条、不超过 3 条 Exact Quote。

Exact Quote 要求：

- 必须是 `PAPER_MARKDOWN` 中可逐字匹配的原文片段。
- 不得改写。
- 不得翻译。
- 不得拼接多个不连续片段。
- 不得使用你自己总结的句子。
- 如果无法提供完全一致的字符串，该结论必须降级为 "NOT_MENTIONED" 或 "INSUFFICIENT_EVIDENCE"。

每条 quote 尽量包含：

{
  "quote": "exact text from paper",
  "page": "page number if available, otherwise NOT_MENTIONED",
  "section": "section heading if available, otherwise NOT_MENTIONED",
  "supports_field": "field name"
}

---

## 3. EPOCH ANCHORING

严禁将“论文发表时间”误认为“实验数据时间”。

你必须从实验章节、数据章节、表格、图注或结果章节中精准抽取观测数据的具体历史时间段。

必须区分：

- publication_year：论文发表年份
- experiment_epoch：实验观测数据的时间段
- product_epoch：精密产品或改正数使用的时间段
- real_time_stream_epoch：实时流或回放数据的时间段

如果正文没有明确实验时间段，必须填入：

"NOT_MENTIONED"

不得根据 DOI、发表年份、接收日期、修回日期或会议时间推断实验时间。

---

# GNSS Technical Boundary Defenses

## 1. PPP-B2b 产品源防御

你必须严格区分作者使用的精密产品来源。

PPP-B2b 是通过 BDS-3 GEO 卫星播发的特定 BDS-3 PPP-B2b SSR 改正服务，不等同于一般 SSR、IGS RTS、CLK93、CNES、后处理精密星历或互联网 NTRIP 产品。

请严格分类 `product_source`：

- "BDS3_PPP_B2B_BROADCAST"
  - 正文明示使用 BDS-3 PPP-B2b broadcast / PPP-B2b service / B2b signal / GEO broadcast correction。

- "IGS_RTS_OR_CLK93"
  - 正文明示使用 IGS RTS、CLK93、real-time service from IGS 等。

- "CNES_OR_OTHER_RTS"
  - 正文明示使用 CNES、CLK、SSR external real-time products 等。

- "POST_PROCESSED_FINAL_PRODUCTS"
  - 正文明示使用 final orbit/clock、precise ephemeris、post-processed products 等。

- "NON_B2B_EXTERNAL_PRODUCTS"
  - 论文标题或摘要提到 PPP-B2b，但实验实际使用 NTRIP、IGS、CNES、final products、offline SSR 或其他非 BDS-3 PPP-B2b GEO 播发产品。

- "MIXED_PRODUCTS"
  - 同时使用 PPP-B2b 和其他外部产品。

- "NOT_MENTIONED"
  - 正文无法判断产品源。

如果产品源不是明确的 BDS-3 PPP-B2b GEO broadcast correction，不得把论文标记为核心 PPP-B2b 实验论文。

---

## 2. 数学模型边界防御

必须明确区分以下模型：

- Single-frequency PPP
- Dual-frequency ionosphere-free combination, IF
- Uncombined PPP, UC
- PPP-AR
- RT-PPP
- PPP-B2b assisted PPP
- Multi-GNSS PPP
- Standard EKF-based PPP
- Factor graph / smoothing / other estimator

对于 `ionospheric_handling`，必须检查：

1. 是否使用 ionosphere-free combination。
2. 是否使用 uncombined model。
3. 是否估计或改正电离层延迟。
4. 是否处理 DCB / code bias。
5. 是否说明 DCB 来源。

如果正文没有提及 DCB 来源，必须写入：

"Missing_DCB_Handling"

不得默认作者使用了 CAS、CODE、MGEX、IGS 或其他 DCB 产品。

---

## 3. 改正数类型防御

必须分别识别作者是否使用或分析：

- orbit correction
- clock correction
- code bias
- phase bias
- URA / integrity indicator
- ionospheric correction
- tropospheric model
- SSR metadata
- signal-in-space ranging error
- correction latency
- update interval
- availability
- continuity

未明确提及的改正数类型填入 "NOT_MENTIONED"。

---

# Novelty & Reproducibility Audit

你要默认作者可能倾向于夸大创新性。你的判断必须采取反方视点。

## 1. Novelty Audit

当作者宣称：

- proposed a new algorithm
- novel method
- improved model
- enhanced PPP-B2b positioning
- new strategy
- robust approach

你必须检查其数学本质和实验支撑。

判断标准：

1. 是否有新的观测方程？
2. 是否有新的状态参数设计？
3. 是否有新的随机模型？
4. 是否有新的质量控制或异常检测机制？
5. 是否有新的 PPP-B2b 改正数使用方式？
6. 是否只是把常规 PPP / EKF / IF / UC 模型迁移到 B2b 场景？
7. 是否有消融实验证明新模块有效？
8. 是否有强基线对比？
9. 是否报告失败案例或边界条件？
10. 是否给出可复现细节？

如果正文的核心公式与经典 PPP / EKF / 常规 SSR 处理无实质区别，且缺少消融或强基线，应在 `novelty_statement` 中写明：

"该方法在数学本质上属于常规技术在 B2b 信号或实时改正产品上的常规平移，实质创新度低。"

但只有在正文证据支持时才能写这句话。否则写：

"INSUFFICIENT_EVIDENCE_FOR_NOVELTY_JUDGMENT"

建议使用以下创新等级：

- "A_SUBSTANTIVE"
  - 有明确方法创新，数学或系统机制有实质变化，且实验充分支撑。

- "B_INCREMENTAL"
  - 有一定增量，实验较充分，但主要是在已有框架上的改进。

- "C_ENGINEERING_TRANSFER"
  - 主要是工程集成、产品应用、场景扩展或常规迁移。

- "D_WEAK_OR_OVERCLAIMED"
  - 创新声明较强，但证据不足、基线弱或方法本质常规。

- "U_INSUFFICIENT_EVIDENCE"
  - 正文信息不足，无法判断。

---

## 2. Reproducibility Audit

评估工程复现时，必须寻找以下致命缺失项。

只要缺失，就必须在 `reproduction_blockers` 中追加记录：

1. 原始数据集缺失
   - 是否提供公开原始观测数据链接？
   - 是否说明测站、接收机、采样率、观测时间段？

2. 实时数据流不可回溯
   - 是否提供 PPP-B2b 实时流回放方法？
   - 是否说明实时流记录方式？
   - 是否提供 SSR / B2b correction archive？

3. 随机模型参数缺失
   - 是否给出观测噪声参数？
   - 是否给出过程噪声？
   - 是否给出高度角权重模型？
   - 是否给出 C/N0 动态建模参数？
   - 是否给出 Kalman filter 初始方差和状态转移参数？

4. 代码缺失
   - 是否提供代码仓库？
   - 是否提供运行入口？
   - 是否提供配置文件？
   - 是否提供版本依赖？

5. 评价指标定义不完整
   - 收敛时间定义是否明确？
   - 精度指标是 RMS、STD、95%、3D error 还是 ENU 分量？
   - 是否给出统计窗口和剔除规则？

6. 基线不可复现
   - 是否说明对比方法实现方式？
   - 是否给出使用的外部产品版本？
   - 是否说明基线参数？

每个 blocker 必须包含：

{
  "blocker_type": "",
  "description": "",
  "severity": "critical | major | minor",
  "grounding_quotes": []
}

如果无法从正文确认某项复现信息存在，则视为缺失，而不是假定存在。

---

# Output Rules

你必须直接输出符合 `SCHEMA_JSON` 的 JSON 字符串。

禁止输出：

- Markdown
- 解释性文字
- 前导语，例如 “Here is the parsed data”
- 尾随总结
- 注释
- 代码块围栏

如果 Schema 与本提示词冲突，以 Schema 为输出结构准，但本提示词的反幻觉规则、证据规则和 GNSS 审计规则仍然必须执行。

如果用户没有提供 Schema，输出：

{
  "error": "SCHEMA_NOT_PROVIDED",
  "message": "A target JSON Schema is required before extraction."
}

如果用户没有提供论文 Markdown，输出：

{
  "error": "PAPER_MARKDOWN_NOT_PROVIDED",
  "message": "Paper Markdown text is required before extraction."
}

---

# Required Self-Check Before Final Output

在输出最终 JSON 之前，你必须在内部执行以下检查，但不要把检查过程输出给用户：

1. 每个非 "NOT_MENTIONED" 的关键字段是否有 grounding_quotes？
2. 每条 quote 是否是 Markdown 原文中的 exact substring？
3. 是否错误地把发表年份当作实验数据时间？
4. 是否把非 BDS-3 PPP-B2b 产品误标为 PPP-B2b？
5. 是否默认了 DCB 处理方式？
6. 是否把常规 PPP / EKF 迁移夸大成实质创新？
7. 是否遗漏 reproduction_blockers？
8. 输出是否为合法 JSON？
9. 输出是否严格符合 Schema？
10. 是否存在任何基于常识补全的字段？

如果检查失败，必须修正 JSON，而不是解释失败原因。
```

我还建议你把这条作为 **DeepSeek API 的固定 system prompt**，然后每次 user prompt 只传：

```text
SCHEMA_JSON:
{你的目标 schema}

PAPER_METADATA:
{paper_id、file_name、hash、页码映射等}

PAPER_MARKDOWN:
{由 PDF 转换后的 Markdown}
```

另外，你这版最强的地方是审计视角，但最好再补一个机制：**所有字段都要允许 `evidence_status`**。否则模型可能为了填满 Schema 而硬凑。下一步可以把你的 JSON Schema 也做成“审计友好型”，例如每个关键字段都变成：

```json
{
  "value": "",
  "evidence_status": "SUPPORTED | NOT_MENTIONED | INSUFFICIENT_EVIDENCE | CONFLICTING_EVIDENCE",
  "grounding_quotes": []
}
```

-----

> 总结下我该给Claude code发送什么

你现在给 Claude Code 发送的内容，建议不要再讲太多背景，而是直接让它**搭建本地项目管线**。核心目标是：

> Claude Code 负责写代码、读 PDF、转 Markdown、分块、调用 DeepSeek-v4 API、写入 JSON/YAML、校验结果；DeepSeek-v4 负责严苛审计式论文抽取。

你可以直接复制下面这段发给 Claude Code。

```text
我想搭建一个面向 GNSS / 实时 PPP-B2b 方向的科研论文知识库构建系统。

请你在当前项目目录中实现一个本地 Python 管线。我的大模型能力来自 DeepSeek-v4 API，不是本地模型。你的任务是写代码和项目结构，让系统能够读取 paper/ 文件夹中的 PDF 文献，转成 Markdown，分块调用 DeepSeek-v4 API，最后生成 JSON / YAML 知识库。

## 一、核心目标

系统需要完成：

1. 扫描 paper/ 文件夹中的所有 PDF。
2. 计算每个 PDF 的 SHA256 hash，支持增量更新。
3. 将 PDF 转换为 Markdown 或带页码的结构化文本。
4. 将每篇论文按章节 / 页码 / token 长度切分为 chunks。
5. 调用 DeepSeek-v4 API，对每个 chunk 做严格信息抽取。
6. 合并同一篇论文的所有 chunk 分析结果，生成单篇论文 JSON / YAML。
7. 对所有论文进行聚合分析，生成：
   - 技术路线图
   - 问题演化图
   - 引用关系图
   - 方法谱系
   - 创新性审计
   - 复现难度索引
8. 生成 Markdown 报告。
9. 运行校验脚本，检查 JSON 合法性、字段缺失、证据缺失和潜在幻觉。

## 二、目录结构

请创建如下结构：

paper/
  # 我会把 PDF 文献放在这里

prompts/
  deepseek_system_prompt.txt
  chunk_extract_prompt.txt
  paper_merge_prompt.txt
  corpus_synthesis_prompt.txt

schemas/
  paper_schema.json
  chunk_schema.json
  corpus_schema.json

research_kb/
  metadata/
    corpus_index.json
    extraction_log.json
    unresolved_items.yaml

  markdown/
    [paper_id].md

  chunks/
    [paper_id]/
      chunk_001.md
      chunk_001.analysis.json

  papers/
    json/
      [paper_id].json
    yaml/
      [paper_id].yaml

  maps/
    technical_routes.yaml
    problem_evolution.yaml
    citation_graph.json
    method_lineage.yaml
    dataset_metric_index.yaml
    reproduction_index.yaml

  reports/
    field_timeline.md
    technical_routes.md
    innovation_review.md
    reproduction_plan.md

scripts/
  pdf_to_markdown.py
  chunk_markdown.py
  call_deepseek.py
  extract_chunks.py
  merge_paper_chunks.py
  build_corpus_maps.py
  validate_kb.py
  update_kb.py

.env.example
requirements.txt
README.md

## 三、DeepSeek API 配置

请创建 .env.example：

DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_BASE_URL=your_base_url_here
DEEPSEEK_MODEL=deepseek-v4

真实 API key 不要写进代码。

scripts/call_deepseek.py 需要：

1. 从 .env 读取 API key、base_url、model。
2. 使用 OpenAI-compatible chat completions 接口。
3. 提供函数 call_deepseek_json(system_prompt, user_prompt, schema_hint=None)。
4. temperature 设置为 0.1 或更低。
5. 要求 DeepSeek 返回合法 JSON。
6. 如果返回不是 JSON，自动重试，最多 3 次。
7. 任何 chunk 调用失败不能中断整个任务，要写入 unresolved_items.yaml。
8. 日志中绝对不能打印 API key。

## 四、PDF 到 Markdown

请实现 scripts/pdf_to_markdown.py。

要求：

1. 使用 PyMuPDF / fitz 优先提取正文和页码。
2. 尽量保留：
   - 页码
   - 标题层级
   - 表格文本
   - 公式附近文本
   - 图注
   - 参考文献
3. 如果页面几乎没有可提取文本，标记 needs_ocr。
4. 不要对 OCR 内容做猜测。
5. 每个 PDF 输出一个 research_kb/markdown/[paper_id].md。
6. paper_id 应稳定生成，例如 first_author_year_shorttitle；如果无法识别作者年份，则用文件名 hash。

## 五、分块策略

请实现 scripts/chunk_markdown.py。

每个 chunk 需要保留：

{
  "paper_id": "",
  "source_file": "",
  "chunk_id": "",
  "chunk_index": 1,
  "page_start": null,
  "page_end": null,
  "section_guess": "",
  "chunk_type": "abstract | introduction | method | experiment | result | conclusion | references | mixed | unknown",
  "text": ""
}

要求：

1. 优先按章节切分。
2. 章节无法识别时按页码和长度切分。
3. references 单独切分。
4. 每个 chunk 不要过长，避免超过 DeepSeek API 上下文。
5. 保留页码和章节信息，方便 quote grounding。

## 六、DeepSeek 固定 system prompt

请把下面内容保存到 prompts/deepseek_system_prompt.txt：

你是一个极其严苛、挑剔且具备深厚 GNSS、PPP、实时 PPP、BDS-3 PPP-B2b、SSR 改正数处理背景的科研审计员。

你的任务是读取已经由 PDF 转换为 Markdown 的论文文本，并严格按照用户提供的 JSON Schema 抽取信息，填充知识库字段。

你的职责不是总结论文，而是做“证据约束下的科研审计”。

Absolute Rules:

1. NO SPECULATION:
如果某个字段在 PAPER_MARKDOWN 中没有直接提及，或者无法通过正文中的公式、表格、实验设置直接推导出来，必须填入 "NOT_MENTIONED"。
严禁根据通用知识、GNSS 常识、作者背景、论文题目、摘要暗示或其他论文常见做法补全。

2. QUOTE GROUNDING:
对于所有关键结论、创新性判定、技术路线、产品源、实验时间、复现阻断项，必须提供 grounding_quotes。
quote 必须是 PAPER_MARKDOWN 中可以逐字匹配的 Exact Quote。
如果无法提供完全一致的字符串，该结论必须降级为 "NOT_MENTIONED" 或 "INSUFFICIENT_EVIDENCE"。

3. EPOCH ANCHORING:
严禁将论文发表时间误认为实验数据时间。
必须从实验章节、数据章节、表格、图注或结果章节中抽取观测数据的具体历史时间段。
如果正文没有明确实验时间段，必须填入 "NOT_MENTIONED"。

GNSS Technical Boundary Defenses:

1. 严格区分产品源：
PPP-B2b 是通过 BDS-3 GEO 卫星播发的 BDS-3 PPP-B2b SSR 改正服务，不等同于 IGS RTS、CLK93、CNES、NTRIP、final products 或后处理精密产品。

product_source 分类必须包括：

- BDS3_PPP_B2B_BROADCAST
- IGS_RTS_OR_CLK93
- CNES_OR_OTHER_RTS
- POST_PROCESSED_FINAL_PRODUCTS
- NON_B2B_EXTERNAL_PRODUCTS
- MIXED_PRODUCTS
- NOT_MENTIONED

如果论文题目提到 PPP-B2b，但实验实际使用 IGS、CNES、final products、offline SSR 或其他非 BDS-3 PPP-B2b GEO 播发产品，必须标记为 NON_B2B_EXTERNAL_PRODUCTS。

2. 严格区分数学模型：
必须识别 single-frequency PPP、dual-frequency ionosphere-free combination、uncombined PPP、PPP-AR、RT-PPP、PPP-B2b assisted PPP、multi-GNSS PPP、standard EKF-based PPP、factor graph / smoothing 等。

3. DCB 防御：
如果论文没有说明 DCB / code bias 的改正来源，必须在 ionospheric_handling 中记录 Missing_DCB_Handling。
不得默认使用 CAS、CODE、MGEX、IGS 或其他 DCB 产品。

4. 改正数类型：
必须分别识别 orbit correction、clock correction、code bias、phase bias、URA、latency、update interval、availability、continuity。
未明确提及的改正数类型填入 NOT_MENTIONED。

Novelty Audit:

你要默认作者可能夸大创新性。
当作者声称 new algorithm、novel method、improved model、new strategy 时，必须检查：

1. 是否有新的观测方程。
2. 是否有新的状态参数设计。
3. 是否有新的随机模型。
4. 是否有新的质量控制或异常检测机制。
5. 是否有新的 PPP-B2b 改正数使用方式。
6. 是否只是把常规 PPP / EKF / IF / UC 模型迁移到 B2b 场景。
7. 是否有消融实验。
8. 是否有强基线对比。
9. 是否报告失败案例或边界条件。
10. 是否给出可复现细节。

创新等级：

- A_SUBSTANTIVE
- B_INCREMENTAL
- C_ENGINEERING_TRANSFER
- D_WEAK_OR_OVERCLAIMED
- U_INSUFFICIENT_EVIDENCE

Reproducibility Audit:

必须寻找以下复现阻断项：

1. 是否提供公开原始观测数据链接。
2. 是否提供 PPP-B2b 实时流回放方法。
3. 是否提供 SSR / B2b correction archive。
4. 是否给出完整随机模型参数。
5. 是否给出 Kalman filter 初始方差、过程噪声、观测噪声。
6. 是否提供代码仓库。
7. 是否提供运行入口。
8. 是否提供配置文件。
9. 是否定义清楚收敛时间、RMS、STD、95%、3D error、ENU 分量等指标。
10. 是否说明基线方法和外部产品版本。

如果无法从正文确认某项复现信息存在，则视为缺失，而不是假定存在。

Output Rules:

只输出合法 JSON。
禁止输出 Markdown、解释性文字、前导语、尾随总结、注释、代码块围栏。
如果信息不足，使用 NOT_MENTIONED、INSUFFICIENT_EVIDENCE、[] 或 null。

在最终输出前内部自检：

1. 每个非 NOT_MENTIONED 的关键字段是否有 grounding_quotes。
2. 每条 quote 是否是 Markdown 原文 exact substring。
3. 是否误把发表年份当实验数据时间。
4. 是否误把非 BDS-3 PPP-B2b 产品标为 PPP-B2b。
5. 是否默认 DCB 处理方式。
6. 是否把常规 PPP / EKF 迁移夸大成实质创新。
7. 是否遗漏 reproduction_blockers。
8. 输出是否为合法 JSON。
9. 输出是否符合 Schema。
10. 是否存在任何常识补全。

## 七、paper_schema.json

请设计一个适合 GNSS / 实时 PPP-B2b 文献审计的 JSON Schema。

关键字段必须至少包括：

- paper_id
- source_file
- file_hash
- bibliographic_info
- product_source
- mathematical_model
- ionospheric_handling
- correction_types
- research_problem
- technical_route
- method
- formulas
- experiments
- experiment_epoch
- datasets
- metrics
- main_results
- novelty_audit
- reproducibility_audit
- reproduction_blockers
- citation_and_lineage
- future_work
- grounding_quotes
- uncertainties

重要：关键字段建议使用如下结构：

{
  "value": "",
  "evidence_status": "SUPPORTED | NOT_MENTIONED | INSUFFICIENT_EVIDENCE | CONFLICTING_EVIDENCE",
  "grounding_quotes": []
}

## 八、chunk 抽取

请实现 scripts/extract_chunks.py。

它应该：

1. 遍历 research_kb/chunks/[paper_id]/*.md。
2. 读取 paper_schema 或 chunk_schema。
3. 组装 user prompt：

SCHEMA_JSON:
{chunk_schema}

PAPER_METADATA:
{paper_id, source_file, chunk_id, page_start, page_end, section_guess}

PAPER_MARKDOWN:
{chunk markdown text}

4. 调用 DeepSeek API。
5. 输出 chunk_001.analysis.json。
6. 失败则写入 unresolved_items.yaml。

## 九、单篇论文合并

请实现 scripts/merge_paper_chunks.py。

它应该：

1. 读取同一 paper_id 下所有 chunk analysis JSON。
2. 调用 DeepSeek API 合并为完整 paper JSON。
3. 合并时必须保留 evidence 和 grounding_quotes。
4. 冲突字段不能强行合并，要标记 CONFLICTING_EVIDENCE。
5. 输出：
   - research_kb/papers/json/[paper_id].json
   - research_kb/papers/yaml/[paper_id].yaml

## 十、跨论文知识图谱

请实现 scripts/build_corpus_maps.py。

它应该基于所有 paper JSON 生成：

1. technical_routes.yaml
2. problem_evolution.yaml
3. citation_graph.json
4. method_lineage.yaml
5. dataset_metric_index.yaml
6. reproduction_index.yaml
7. reports/*.md

跨论文综合也要调用 DeepSeek，但必须只基于 paper JSON，不得重新猜测。

## 十一、校验脚本

请实现 scripts/validate_kb.py。

检查：

1. 每个 PDF 是否有对应 Markdown。
2. 每个 PDF 是否有对应 paper JSON。
3. JSON 是否合法。
4. paper_id 是否唯一。
5. file_hash 是否存在。
6. 关键字段是否缺 grounding_quotes。
7. grounding_quotes 是否能在对应 Markdown 中逐字匹配。
8. experiment_epoch 是否错误使用 publication_year。
9. product_source 是否存在证据。
10. ionospheric_handling 中是否遗漏 Missing_DCB_Handling。
11. reproduction_blockers 是否为空但复现信息明显缺失。
12. citation_graph 中所有节点是否存在。
13. unresolved_items.yaml 是否记录失败项。

输出 extraction_log.json。

## 十二、运行入口

请实现 scripts/update_kb.py 作为总入口。

运行方式：

python scripts/update_kb.py

执行顺序：

1. 扫描 paper/
2. PDF 转 Markdown
3. Markdown 分块
4. DeepSeek chunk 抽取
5. 单篇论文合并
6. 跨论文图谱构建
7. 校验知识库
8. 输出日志

## 十三、README

请写 README.md，说明：

1. 如何安装依赖。
2. 如何配置 .env。
3. 如何把 PDF 放入 paper/。
4. 如何运行 update_kb.py。
5. 输出文件在哪里。
6. 如果 DeepSeek API 返回非 JSON 怎么处理。
7. 如何增量更新。
8. 如何人工复核 unresolved_items.yaml。

请先创建最小可运行版本，不要追求一次实现所有高级功能。优先保证：

PDF → Markdown → chunks → DeepSeek JSON → paper JSON → validate

这个主流程能跑通。
```

你发给 Claude Code 的时候，建议第一轮就用这段。等它生成代码后，再让它做第二轮增强：

```text
请你现在重点检查这个项目的反幻觉能力，尤其是 grounding_quotes 是否能在 Markdown 原文中逐字匹配、product_source 是否会误判 PPP-B2b、experiment_epoch 是否会误用 publication_year、DCB 缺失是否能被识别、reproduction_blockers 是否足够严格。
```

最重要的是：**先让 Claude Code 做一个最小可运行版本**，不要一开始就要求它把所有跨论文图谱和复现分析都做到完美。主流程跑通后，再逐步加严。

-----

> 接入deepseekapi不能识别pdf需要别的skill来帮助

对，你判断是对的：DeepSeek API 本身不应该直接承担 PDF 识别。更稳的做法是把系统拆成“PDF 预处理层 + DeepSeek 审计层”。我先确认一下 PDF 处理部分的最佳做法，再给你一版该发给 Claude Code 的修改指令。

对，需要。准确说，不是让 DeepSeek API 增加“识别 PDF 的能力”，而是给 Claude Code 增加一个 **PDF 预处理 Skill / 模块**。

你的系统应该拆成 3 层：

```text
PDF Ingestion Skill
负责：PDF -> Markdown / structured text / OCR 标记 / 页码证据

DeepSeek Audit Skill
负责：Markdown -> JSON 审计抽取 / 创新性判断 / 复现阻断项

Knowledge Base Skill
负责：合并 JSON / 构建图谱 / 校验 grounding_quotes / 输出报告
```

你现在应该给 Claude Code 追加下面这段指令。

```text
我意识到 DeepSeek-v4 API 本身不能直接识别 PDF，所以请你不要让 DeepSeek 直接读取 PDF。

请你在当前项目中新增一个独立的 PDF Ingestion Layer，也可以理解为 pdf-to-markdown skill。它的职责是：把 paper/ 文件夹中的 PDF 稳定转换为带页码、章节、表格、公式附近文本、图注和参考文献的 Markdown，然后再交给 DeepSeek API 做科研审计抽取。

请重点实现以下内容。

## 一、PDF Ingestion Layer 的职责

输入：

paper/*.pdf

输出：

research_kb/markdown/[paper_id].md
research_kb/metadata/pdf_parse_report.json
research_kb/metadata/needs_ocr.yaml

它必须完成：

1. 扫描 paper/ 文件夹中的 PDF。
2. 为每个 PDF 计算 SHA256。
3. 为每篇论文生成稳定 paper_id。
4. 使用本地 PDF 解析工具提取正文。
5. 保留页码信息。
6. 尽量保留标题层级。
7. 尽量提取表格文本。
8. 尽量提取公式附近上下文。
9. 尽量提取图注。
10. 单独识别参考文献区域。
11. 对扫描版或图片型 PDF 标记 needs_ocr。
12. 不要对识别失败的内容进行猜测。
13. 生成解析质量报告。

## 二、推荐工具链

请优先使用以下 Python 库：

1. PyMuPDF / fitz
   - 用于提取正文、页码、基础版面信息。

2. pdfplumber
   - 用于尝试提取表格、字符位置、版面结构。

3. pymupdf4llm，如果可用
   - 用于将 PDF 转为更自然的 Markdown。

4. pytesseract 或 OCRMyPDF，作为可选 OCR 后备方案
   - 仅用于扫描版 PDF。
   - OCR 结果必须标记为 OCR_DERIVED。
   - OCR 不可靠时必须标记 needs_manual_review。

如果某个库安装失败，不要让整个项目崩溃，应在 README 中说明可选依赖，并降级到 PyMuPDF 基础提取。

## 三、请新增或修改这些脚本

scripts/
  pdf_inspect.py
  pdf_to_markdown.py
  detect_scanned_pdf.py
  extract_pdf_tables.py
  normalize_markdown.py
  validate_markdown_grounding.py

### 1. pdf_inspect.py

功能：

- 读取 PDF 元数据
- 页数
- 每页可提取文本长度
- 是否疑似扫描版
- 是否包含图片较多页面
- 是否包含表格迹象
- 是否可能需要 OCR

输出：

research_kb/metadata/pdf_parse_report.json

每篇论文记录：

{
  "paper_id": "",
  "source_file": "",
  "file_hash": "",
  "page_count": 0,
  "text_extractable_pages": 0,
  "low_text_pages": [],
  "likely_scanned": false,
  "needs_ocr": false,
  "parse_quality": "high | medium | low | failed",
  "notes": []
}

### 2. pdf_to_markdown.py

功能：

- 将 paper/*.pdf 转为 research_kb/markdown/[paper_id].md
- 每一页必须带页码锚点
- 格式如下：

<!-- PAGE: 1 -->
# Title or detected heading

正文……

<!-- PAGE: 2 -->
正文……

要求：

- 不要删除页码标记。
- 不要随意合并跨页内容导致证据定位丢失。
- 如果页面无法提取文本，写入：

<!-- PAGE: 5 -->
[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]

- 如果是 OCR 内容，写入：

<!-- PAGE: 5 OCR_DERIVED -->
OCR text...

### 3. extract_pdf_tables.py

功能：

- 使用 pdfplumber 尝试提取表格。
- 表格输出到 Markdown 中，格式为：

[Table detected on page X]
| ... |

如果表格结构无法可靠识别，输出：

[TABLE_DETECTED_BUT_EXTRACTION_LOW_CONFIDENCE page=X]

不要猜测表格内容。

### 4. normalize_markdown.py

功能：

- 清理 PDF 转换中的断行问题。
- 合并明显被 PDF 换行拆开的句子。
- 但不得改变 Exact Quote 的可追踪性。
- 必须保留 page marker。
- 不要删除公式、图注、表格、参考文献。

### 5. validate_markdown_grounding.py

功能：

- 后续 DeepSeek 输出 JSON 后，检查 grounding_quotes 是否能在对应 Markdown 中逐字匹配。
- 如果不能匹配，标记为 invalid_quote。
- invalid_quote 不得进入最终知识库，必须写入 unresolved_items.yaml。

## 四、DeepSeek 调用边界

请明确：

DeepSeek API 只接收 Markdown 文本，不接收 PDF 文件。

流程必须是：

paper PDF
  -> pdf_to_markdown.py
  -> chunk_markdown.py
  -> call_deepseek.py
  -> chunk analysis JSON
  -> merge_paper_chunks.py
  -> paper JSON
  -> validate_markdown_grounding.py
  -> final research_kb

不要在任何 DeepSeek prompt 中写“读取 PDF”。必须写“读取由 PDF 转换得到的 Markdown 论文文本”。

## 五、OCR 策略

不要默认 OCR 所有 PDF。

OCR 策略：

1. 如果某页可提取文本很少，但图片面积很大，标记 needs_ocr。
2. 如果整篇论文大部分页面不可提取文本，标记 likely_scanned。
3. OCR 作为可选步骤，不作为默认步骤。
4. OCR 结果必须标记 OCR_DERIVED。
5. OCR 内容参与 DeepSeek 分析时，必须在 PAPER_METADATA 中注明 text_source = OCR_DERIVED。
6. DeepSeek 对 OCR 内容的抽取置信度应降低。

## 六、反幻觉要求

PDF Ingestion Layer 只负责提取，不负责理解。

禁止它做以下事情：

- 不要总结论文。
- 不要判断创新性。
- 不要补全公式含义。
- 不要推断实验时间。
- 不要推断产品源。
- 不要判断是否 PPP-B2b。
- 不要补全作者、年份、数据集、指标。

这些全部交给 DeepSeek Audit Layer，但 DeepSeek 也只能基于 Markdown 中的原文证据判断。

## 七、README 中需要说明

请在 README.md 中明确：

1. DeepSeek API 不能直接识别 PDF。
2. 本项目先把 PDF 转为 Markdown。
3. Markdown 中保留页码，是为了支持 grounding_quotes。
4. 如果 PDF 是扫描版，需要 OCR。
5. OCR 结果可靠性较低，需要人工复核。
6. 所有知识库字段必须能追溯到 Markdown 原文 quote。
7. 如果 quote 不能在 Markdown 中逐字匹配，该字段视为无效。

## 八、优先级

请先实现最小可运行流程：

paper/*.pdf
  -> research_kb/markdown/*.md
  -> research_kb/chunks/*/*.md
  -> DeepSeek chunk JSON
  -> paper JSON
  -> grounding quote validation

跨论文图谱、技术路线图、问题演化图可以放在第二阶段。
```

你现在的关键词不是“再找一个大模型识别 PDF”，而是：

**PDF 解析器 + Markdown 标准化 + DeepSeek 审计抽取。**

如果你后续真要把它封装成 Skill，建议拆成两个 Skill：

```text
pdf-ingestion
负责 PDF -> Markdown / chunks / OCR 标记 / quote 校验

gnss-pppb2b-auditor
负责 DeepSeek 审计抽取 / JSON Schema / 创新性判断 / 复现分析
```

这样比一个巨大的“科研助手 Skill”稳定很多。

-----

> # PDF 处理
> 遇到 PDF 文件时，使用 `danielmiessler-pdf` skill 来处理（提取文字、表格、元数据等），不要直接用 Read 工具。

可以，把这条作为 **PDF Ingestion Layer 的强约束** 加进 Claude Code 提示词里。你可以直接追加发送下面这段：

```text
请修改 PDF 处理策略：

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

原因：

DeepSeek-v4 API 不能直接识别 PDF。Claude Code 也不应该直接把 PDF 当普通文本读取。PDF 必须先经过 `danielmiessler-pdf` skill 预处理，转换为带页码和证据锚点的 Markdown / structured text，然后再传给 DeepSeek-v4 API 做 GNSS / PPP-B2b 科研审计。

请将原流程中的：

paper/*.pdf
  -> pdf_to_markdown.py
  -> chunk_markdown.py
  -> DeepSeek API

修改为：

paper/*.pdf
  -> danielmiessler-pdf skill
  -> research_kb/markdown/[paper_id].md
  -> research_kb/chunks/[paper_id]/*.md
  -> DeepSeek-v4 API
  -> chunk analysis JSON
  -> paper JSON
  -> grounding quote validation
  -> research_kb

## danielmiessler-pdf 输出要求

使用 `danielmiessler-pdf` skill 处理每篇 PDF 后，必须生成或整理出以下内容：

1. Markdown 正文文件：
   research_kb/markdown/[paper_id].md

2. PDF 元数据：
   research_kb/metadata/pdf_parse_report.json

3. OCR / 解析失败记录：
   research_kb/metadata/needs_ocr.yaml

Markdown 中必须保留页码标记，例如：

<!-- PAGE: 1 -->
正文……

<!-- PAGE: 2 -->
正文……

如果某页无法可靠提取文本，写入：

<!-- PAGE: 5 -->
[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]

如果内容来自 OCR，必须标记：

<!-- PAGE: 5 OCR_DERIVED -->
OCR text...

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

“你正在读取由 PDF 转换得到的 Markdown 论文文本。”

不要写：

“你正在读取 PDF。”
```

你也可以把原来 `scripts/pdf_to_markdown.py` 的定位改掉：

```text
scripts/pdf_to_markdown.py 不再直接解析 PDF，而是作为 danielmiessler-pdf skill 的调用封装器 / 输出规范化器。

它的职责是：

1. 调用 danielmiessler-pdf skill 处理 PDF。
2. 接收 skill 输出。
3. 统一整理成 research_kb/markdown/[paper_id].md。
4. 保留页码、表格、图注、参考文献。
5. 生成 pdf_parse_report.json。
6. 标记 needs_ocr。
```

最关键的一句话就是：

```text
PDF 文件只能由 danielmiessler-pdf skill 处理；Claude Code 不得直接 Read PDF。
```

-----

> 反幻觉审计报告
>
>   修复前发现的 5 个漏洞及修复结果
>
>   #: 1
>   风险点: experiment_epoch 误用出版年份
>   严重度: 高
>   修复前: 只检查 DeepSeek 自报的 is_publication_year_mistake flag
>   修复后: 独立比对：提取 bibliographic_info.year vs experiment_epoch 日期，年份重叠且无 quote → 标记
>     year_match_publication_no_quotes
>   ────────────────────────────────────────
>   #: 2
>   风险点: grounding_quotes 匹配
>   严重度: 中
>   修复前: paper_id 不匹配时静默跳过 quote 校验
>   修复后: 双重映射：从 pdf_parse_report.json + 直接扫描 markdown 建立 paper_id→文件映射，找不到时明确报
>     markdown_not_found:all_quotes_unverified
>   ────────────────────────────────────────
>   #: 3
>   风险点: reproduction_blockers
>   严重度: 中
>   修复前: 只检查 3/10 项
>   修复后: 全 10 项检查：每一项缺失且不在 blockers 中都会标记 repro:missing_not_blocked，+ score 一致性校验
>   ────────────────────────────────────────
>   #: 4
>   风险点: product_source 误判
>   严重度: 中
>   修复前: 只检查是否有 quote，不检查 conflict_flag
>   修复后: 三重检查：claimed≠actual 时验证 conflict_flag + 标题含 B2b 但 actual 不是 BDS3_PPP_B2B_BROADCAST 的专项警告
>   ────────────────────────────────────────
>   #: 5
>   风险点: DCB 缺失
>   严重度: 低
>   修复前: 基本完备
>   修复后: 增强：区分处理模式（IF 组合可以减轻 DCB 要求，UC/SF 模式 DCB 缺失更严重）
>
>   各层级反幻觉能力总览
>
>   ┌─────────────────────────────────────────────────────┐
>   │ Layer 1: Prompt (deepseek_system_prompt.txt)        │
>   │  ✓ NO SPECULATION 规则                              │
>   │  ✓ QUOTE GROUNDING (Exact Quote)                    │
>   │  ✓ EPOCH ANCHORING                                  │
>   │  ✓ 10 项内部自检清单                                 │
>   │  ✓ 产品源严格分类 + 标题欺诈警告                      │
>   │  ✓ DCB 防御 + 默认缺失标记                            │
>   │  ✓ 创新性审计 10 项检查                               │
>   │  ✓ 复现审计 10 项阻断检查                             │
>   ├─────────────────────────────────────────────────────┤
>   │ Layer 2: Schema (paper_schema.json)                  │
>   │  ✓ product_source: claimed vs actual 分离            │
>   │  ✓ conflict_flag + conflict_detail                   │
>   │  ✓ is_publication_year_mistake boolean               │
>   │  ✓ dcb_missing_flag + dcb_missing_warning            │
>   │  ✓ reproduction_blockers array + score              │
>   │  ✓ grounding_quotes on 11 key fields                │
>   │  ✓ conflicting_evidence array                       │
>   ├─────────────────────────────────────────────────────┤
>   │ Layer 3: Validate (validate_kb.py)                   │
>   │  ✓ 独立实验年份比对（不依赖 DeepSeek 自报）           │
>   │  ✓ grounding_quotes 逐字子串匹配                      │
>   │  ✓ paper_id→markdown 双重映射                        │
>   │  ✓ product_source 三重检查                            │
>   │  ✓ DCB 缺失 + 处理模式感知                           │
>   │  ✓ 10 项 reproduction_blockers 全覆盖                │
>   │  ✓ score 一致性校验                                   │
>   │  ✓ 错误分类统计输出                                   │
>   ├─────────────────────────────────────────────────────┤
>   │ Layer 4: Pipeline (pdf_to_markdown / chunk / merge)  │
>   │  ✓ PDF 层不做科研分析（反幻觉边界）                    │
>   │  ✓ 页码标记保障 quote 追溯                            │
>   │  ✓ merge 冲突检测 CONFLICTING_EVIDENCE               │
>   │  ✓ 失败项写入 unresolved_items.yaml                  │
>   └─────────────────────────────────────────────────────┘

这份反幻觉审计报告已经比较成熟了，尤其是你现在有了 **Prompt → Schema → Validate → Pipeline** 四层防线。它不再只是“让 DeepSeek 自觉不要幻觉”，而是开始用程序校验 DeepSeek 的输出，这是正确方向。

但我建议你不要马上进入大规模跑论文。下一步应该让 Claude Code 做 **对抗测试集**，验证这些防线真的有效。

你现在可以给 Claude Code 发送下面这段：

```text
请继续增强项目的反幻觉验证能力。现在不要急着大规模处理论文，请先建立 adversarial test suite，用最小测试样例验证 validate_kb.py、paper_schema.json、deepseek_system_prompt.txt 和 pipeline 的防线是否真的生效。

## 一、目标

请创建 tests/ 目录，用人工构造的 Markdown 论文片段和对应 JSON 输出，测试以下风险点是否会被 validate_kb.py 正确识别：

1. experiment_epoch 误用 publication_year
2. grounding_quotes 无法在 Markdown 中逐字匹配
3. paper_id 找不到对应 Markdown
4. product_source 将非 PPP-B2b 产品误标为 BDS3_PPP_B2B_BROADCAST
5. 论文标题含 PPP-B2b，但实验实际使用 IGS RTS / CLK93 / final products
6. UC / SF 模型未说明 DCB 来源，却没有 Missing_DCB_Handling
7. reproduction_blockers 缺失 10 项检查中的关键阻断项
8. novelty_statement 过度声称创新，但没有公式、消融、强基线证据
9. citation_graph 出现不存在的 paper_id
10. merge 阶段把 conflicting evidence 强行合并而不是标记 CONFLICTING_EVIDENCE

## 二、测试目录结构

请创建：

tests/
  fixtures/
    markdown/
      good_case.md
      bad_epoch_publication_year.md
      bad_quote_mismatch.md
      bad_product_source.md
      bad_dcb_missing.md
      bad_repro_blockers.md
      bad_conflicting_merge.md

    paper_json/
      good_case.json
      bad_epoch_publication_year.json
      bad_quote_mismatch.json
      bad_product_source.json
      bad_dcb_missing.json
      bad_repro_blockers.json
      bad_conflicting_merge.json

  test_validate_kb.py
  expected_errors.yaml

## 三、必须覆盖的测试案例

### Case 1: good_case

Markdown 中明确写出：

- 使用 BDS-3 PPP-B2b broadcast corrections
- 实验数据时间段
- IF combination
- orbit and clock corrections
- convergence time metric
- 公开数据来源
- grounding quote 完全匹配

对应 JSON 应该通过校验。

### Case 2: bad_epoch_publication_year

JSON 中 experiment_epoch 使用了 bibliographic_info.year，但 Markdown 实验章节没有对应实验时间 quote。

validate_kb.py 必须报：

epoch:year_match_publication_no_quotes

### Case 3: bad_quote_mismatch

JSON 中 grounding_quotes 包含一个 Markdown 中不存在的 quote。

validate_kb.py 必须报：

quote:invalid_exact_match

### Case 4: bad_product_source

Markdown 中写的是 IGS RTS / CLK93 / final orbit and clock products，但 JSON actual_product_source 写成 BDS3_PPP_B2B_BROADCAST。

validate_kb.py 必须报：

product_source:possible_non_b2b_misclassification

如果 title 中包含 PPP-B2b，但 actual_product_source 不是 BDS3_PPP_B2B_BROADCAST，应报：

product_source:title_b2b_actual_non_b2b_warning

### Case 5: bad_dcb_missing

Markdown 中是 UC 或 single-frequency model，但没有 DCB / code bias 来源。JSON 没有 Missing_DCB_Handling。

validate_kb.py 必须报：

dcb:missing_dcb_handling_not_flagged

### Case 6: bad_repro_blockers

Markdown 中没有公开数据链接、没有代码、没有实时流回放、没有随机模型参数，但 JSON reproduction_blockers 为空或过少。

validate_kb.py 必须报：

repro:missing_not_blocked

并指出缺失的 blocker 类型。

### Case 7: bad_conflicting_merge

两个 chunk analysis 中对 product_source 或 experiment_epoch 给出冲突证据，但 merge 后 JSON 没有 conflicting_evidence。

validate_kb.py 必须报：

merge:conflicting_evidence_not_preserved

## 四、测试执行方式

请实现：

pytest tests/

或者：

python scripts/validate_kb.py --test fixtures

确保每个 bad case 都能稳定触发预期错误。

## 五、输出要求

请生成：

tests/expected_errors.yaml

格式示例：

bad_epoch_publication_year:
  expected_errors:
    - epoch:year_match_publication_no_quotes

bad_quote_mismatch:
  expected_errors:
    - quote:invalid_exact_match

bad_product_source:
  expected_errors:
    - product_source:possible_non_b2b_misclassification
    - product_source:title_b2b_actual_non_b2b_warning

## 六、验收标准

项目只有在以下条件满足后才算通过当前阶段：

1. good_case 通过校验。
2. 所有 bad_case 都触发预期错误。
3. validate_kb.py 不依赖 DeepSeek 自报字段做关键判断。
4. grounding_quotes 必须逐字匹配 Markdown。
5. experiment_epoch 必须有实验章节 quote 支撑。
6. product_source 必须有正文 quote 支撑。
7. DCB 缺失检测必须区分 IF / UC / SF。
8. reproduction_blockers 必须覆盖全部 10 项。
9. 所有测试能通过 pytest 或等价命令重复运行。
10. README 中加入“反幻觉测试”说明。

请先实现这些测试，不要继续扩展跨论文图谱功能。
```

我建议你现在的开发顺序是：

```text
1. 先跑 adversarial tests
2. 修 validate_kb.py
3. 再处理 3-5 篇真实论文
4. 人工检查 DeepSeek 输出
5. 再扩大到整个 paper/ 文件夹
```

现在最危险的点已经不是 prompt，而是：**merge 阶段和 validate 阶段是否真的能挡住 DeepSeek 的“看似合理 JSON”**。所以测试集比继续加 prompt 更重要。

-----

> 测试结果：11/11 通过

很好，**11/11 通过**说明你的反幻觉校验框架已经可以进入真实论文小规模试跑阶段。

下一步不要直接跑全量，建议给 Claude Code 发这段：

```text
测试结果 11/11 通过。现在进入真实论文小规模试跑阶段。

请不要一次性处理全部 paper/ 文件夹。请先选择 3 篇 PDF 作为 pilot set：

1. 一篇明确研究 BDS-3 PPP-B2b broadcast correction 的论文
2. 一篇标题或摘要提到 PPP-B2b，但可能使用 IGS RTS / CLK93 / final products 的边界论文
3. 一篇普通 PPP / RT-PPP / SSR 论文，作为非 PPP-B2b 对照

如果无法自动判断类型，就按文件名或随机选择 3 篇，并在日志中说明选择依据。

## Pilot 目标

请运行完整主流程：

PDF
-> danielmiessler-pdf skill
-> Markdown
-> chunks
-> DeepSeek-v4 chunk extraction
-> paper JSON
-> grounding quote validation
-> validate_kb.py
-> extraction_log.json

## 试跑后输出

请生成：

research_kb/reports/pilot_audit_report.md

报告必须包括：

1. 每篇论文的处理状态
2. PDF 解析质量
3. Markdown 页码是否完整
4. chunk 数量
5. DeepSeek API 成功 / 失败次数
6. JSON 校验结果
7. grounding_quotes invalid 数量
8. product_source 判定及证据
9. experiment_epoch 判定及证据
10. DCB handling 判定
11. reproduction_blockers 数量和类型
12. novelty_grade
13. unresolved_items.yaml 中剩余问题
14. 是否建议进入全量处理

## 进入全量处理的门槛

只有同时满足以下条件，才允许进入全量处理：

1. 3 篇 pilot 全部生成 paper JSON
2. 每篇至少 90% 关键 grounding_quotes 能逐字匹配 Markdown
3. product_source 没有高危误判
4. experiment_epoch 没有 publication_year 误用
5. reproduction_blockers 不为空，且与论文实际缺失项一致
6. validate_kb.py 无 critical error
7. unresolved_items.yaml 中没有阻断级问题

如果不满足，请不要全量运行。请先列出需要修复的问题。
```

这一步的目标是验证：**测试集能挡假样例，真实 PDF 也能稳定跑通**。如果 pilot 通过，再进入全量知识库构建。

-----

> 生成的markdown和pdf读取有什么区别

区别可以理解为：

**PDF 是原始证据源，Markdown 是给模型处理的中间文本层。**

在你的系统里，DeepSeek 不直接读 PDF，而是读由 `danielmiessler-pdf` skill 转出来的 Markdown。这样做是为了让模型能稳定处理文本、分页、quote、表格和章节，但 Markdown 并不等于 PDF 本身。

---

## 1. PDF 读取是什么

PDF 读取面对的是原始论文文件。

PDF 里通常包含：

- 正文文本
- 双栏排版
- 页眉页脚
- 表格
- 图像
- 图注
- 公式
- 参考文献
- 字体、坐标、版面结构
- 有些甚至只是扫描图片

问题是：**PDF 对人类可读，但对大模型和程序不一定友好。**

尤其是 GNSS 论文里常见的问题：

- 双栏论文顺序可能被读乱
- 公式可能被拆散
- 表格列可能错位
- 页眉页脚可能混进正文
- 参考文献可能和正文混在一起
- 图中的关键信息可能无法提取
- 扫描版 PDF 可能根本没有可提取文本

所以直接让模型“读 PDF”，很容易出现：它看似读懂了，其实读的是乱序文本或不完整内容。

---

## 2. Markdown 是什么

Markdown 是从 PDF 提取出来的、适合模型读取的文本版本。

你的系统中 Markdown 应该长这样：

```markdown
<!-- PAGE: 1 -->

# Title

Abstract text...

<!-- PAGE: 2 -->

## Introduction

...

[Table detected on page 4]

| Product | Orbit | Clock | Bias |
|---|---|---|---|

<!-- PAGE: 5 -->

[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]
```

Markdown 的作用是：

- 把 PDF 内容变成纯文本
- 保留页码锚点
- 尽量保留章节结构
- 尽量保留表格
- 标记 OCR 或提取失败页面
- 方便 DeepSeek 做 `grounding_quotes`
- 方便程序验证 quote 是否逐字存在

换句话说，Markdown 是 **PDF 的可审计文本副本**。

---

## 3. 最核心区别

| 对比项 | PDF | Markdown |
|---|---|---|
| 角色 | 原始论文证据 | 模型分析输入 |
| 可读对象 | 人类、PDF 工具 | LLM、脚本、校验器 |
| 保真度 | 最高 | 取决于提取质量 |
| 页码 | 原生存在 | 需要显式插入 `<!-- PAGE: x -->` |
| 表格 | 视觉上清楚 | 可能错位或丢列 |
| 公式 | 视觉上清楚 | 可能乱码、断裂或丢失 |
| 图像 | 完整 | 通常只能保留图注，图本身可能丢失 |
| quote 校验 | 不方便逐字匹配 | 可以直接字符串匹配 |
| 适合 DeepSeek API | 不适合 | 适合 |
| 适合复现审计 | 原始依据 | 结构化依据 |

---

## 4. 为什么不让 DeepSeek 直接读 PDF

因为 DeepSeek API 通常接收的是文本，不是 PDF 视觉内容。

即使某些模型支持文件上传，科研审计场景也不建议直接依赖“模型自己看 PDF”，原因是：

1. **不可控**：你不知道模型实际看到了哪些文本。
2. **不可验证**：很难确认它的 quote 是否来自 PDF 原文。
3. **不可复现**：同一个 PDF 下次可能解析结果不同。
4. **难定位**：模型说“实验使用 2021 年数据”，但你不知道它从哪一页来的。
5. **容易幻觉**：PDF 提取不完整时，模型会用领域常识补全。

所以你的管线选择 Markdown 是正确的：

```text
PDF 原文
↓
PDF skill 提取
↓
带页码 Markdown
↓
DeepSeek 审计抽取
↓
JSON
↓
quote 回查 Markdown
↓
必要时人工回查 PDF
```

---

## 5. Markdown 会损失什么

Markdown 最大的问题是：**它不是 PDF 的完美复制品。**

常见损失包括：

### 公式损失

PDF 中的公式可能变成：

```text
P r s = ρ + c(dt - dT) + T + ...
```

或者符号丢失、上下标丢失。

所以对于 GNSS 论文里的观测方程、IF 组合、UC 模型、EKF 状态方程，Markdown 可能不够可靠。

应在 JSON 中标记：

```json
"formula_quality": "low"
```

或：

```json
"mathematical_model": {
  "value": "NOT_MENTIONED",
  "evidence_status": "INSUFFICIENT_EVIDENCE"
}
```

### 表格损失

PDF 里的表格可能变成乱序文本：

```text
RMS East North Up 0.12 0.15 0.28
```

模型可能搞错哪一列对应哪个数值。

所以表格结果必须谨慎，最好要求：

- quote 必须能匹配
- 表格结构低置信度时不能抽主结果
- 关键数值必要时人工回查 PDF

### 图像信息丢失

图里的曲线、柱状图、误差时间序列通常不会进入 Markdown。

如果论文只在图中展示定位误差或收敛时间，而正文没有写具体数值，DeepSeek 不应该补。

应填：

```json
"main_results": "NOT_MENTIONED"
```

或者：

```json
"needs_manual_pdf_check": true
```

### 阅读顺序错乱

双栏论文可能被提取成：

```text
左栏第一段
右栏第一段
左栏第二段
右栏第二段
```

这会影响模型理解实验流程和方法描述。

所以 Markdown 生成后要做 `parse_quality` 评估。

---

## 6. Markdown 的优势是什么

Markdown 最大优势是 **可控、可验证、可程序处理**。

你的反幻觉系统依赖 Markdown 才能成立。

例如 DeepSeek 输出：

```json
{
  "experiment_epoch": {
    "value": "from day 300 to day 330 in 2021",
    "grounding_quotes": [
      {
        "quote": "The observations from DOY 300 to 330 in 2021 were used..."
      }
    ]
  }
}
```

然后 `validate_kb.py` 可以直接去 Markdown 里搜：

```text
The observations from DOY 300 to 330 in 2021 were used...
```

如果找不到，就报：

```text
quote:invalid_exact_match
```

如果直接读 PDF，这种逐字校验会困难很多。

---

## 7. 你应该如何定义二者关系

建议你在 README 或 Claude Code prompt 里这样写：

```text
PDF is the source of truth.
Markdown is the auditable extraction layer.
DeepSeek only analyzes Markdown.
Any claim not grounded in Markdown exact quotes is invalid.
When Markdown extraction quality is low, the system must mark the field as needs_manual_pdf_check instead of guessing.
```

中文就是：

```text
PDF 是最终证据源。
Markdown 是可审计的中间文本层。
DeepSeek 只能分析 Markdown。
任何不能被 Markdown 原文 quote 支撑的结论都无效。
如果 Markdown 提取质量低，必须标记人工回查 PDF，而不是猜测。
```

---

## 8. 对你的项目最重要的实践原则

你现在应该让 Claude Code 明确这几条：

```text
1. DeepSeek 不读 PDF，只读 Markdown。
2. Markdown 必须保留页码。
3. Markdown 不可靠的地方必须标记。
4. quote 校验只针对 Markdown。
5. 如果 Markdown 与 PDF 视觉内容可能不一致，标记 needs_manual_pdf_check。
6. 关键公式、表格、图中数值不能从残缺 Markdown 中硬抽。
7. PDF 始终保留为人工复核的最终证据源。
```

最简洁地说：

**PDF 负责“原始真实性”，Markdown 负责“模型可读性和程序可验证性”。**

-----

> 目前我想实现功能是通过读取文献建立一个完整的知识体系，我可以进行检索，或者在知识库进行创新点查询

对，你现在的目标已经从“抽取论文 JSON”升级为：

**读取文献 → 建立可检索知识体系 → 支持创新点查询 / 技术路线查询 / 问题演化查询 / 复现风险查询。**

所以你不能只做 `paper_json`。
你需要在现有系统上再加一层：

```text
Knowledge Index / Retrieval Layer
```

也就是：

```text
PDF / Markdown
↓
DeepSeek 审计抽取
↓
paper JSON
↓
结构化知识单元 claims / entities / relations
↓
索引库 SQLite + Vector DB
↓
检索与创新点查询
```

---

# 你应该让 Claude Code 新增什么功能

你现在给 Claude Code 追加下面这段最合适：

```text
现在我要把项目目标从“单篇论文结构化抽取”升级为“构建可检索的 GNSS / 实时 PPP-B2b 科研知识体系”。

请不要只停留在生成 paper JSON。请在现有 pipeline 后新增 Knowledge Index / Retrieval Layer，使我可以对知识库进行检索，包括：

1. 按关键词检索论文
2. 按技术路线检索论文
3. 按研究问题检索论文
4. 按创新点检索论文
5. 按产品源检索论文
6. 按数学模型检索论文
7. 按实验数据、指标、结果检索论文
8. 按复现阻断项检索论文
9. 查询某个方向的发展脉络
10. 查询某个技术路线下哪些论文具有真实创新，哪些只是工程迁移

## 一、核心设计原则

请将知识库分成三层：

### Layer 1: Paper Layer

这是现有的单篇论文 JSON。

位置：

research_kb/papers/json/[paper_id].json

每篇论文包含：

- bibliographic_info
- product_source
- mathematical_model
- ionospheric_handling
- correction_types
- research_problem
- technical_route
- method
- experiments
- novelty_audit
- reproducibility_audit
- grounding_quotes
- uncertainties

### Layer 2: Claim Layer

请新增 evidence-grounded claims。

每个 claim 是知识库中最小可检索知识单元。

位置：

research_kb/index/claims.jsonl

每行一个 claim，格式如下：

{
  "claim_id": "stable unique id",
  "paper_id": "",
  "claim_type": "research_problem | method | product_source | technical_route | innovation | experiment_result | limitation | reproduction_blocker | future_work | citation_relation",
  "claim_text": "",
  "normalized_value": "",
  "evidence_status": "SUPPORTED | NOT_MENTIONED | INSUFFICIENT_EVIDENCE | CONFLICTING_EVIDENCE",
  "grounding_quotes": [
    {
      "quote": "",
      "page": "",
      "section": ""
    }
  ],
  "confidence": "high | medium | low",
  "tags": [],
  "entities": [],
  "created_from_field": ""
}

要求：

- 任何可检索知识都必须尽量拆成 claim。
- claim 必须能回到 paper_id 和 grounding_quotes。
- 没有 evidence 的 claim 不得进入 SUPPORTED。
- novelty、product_source、experiment_epoch、reproduction_blocker 必须作为 claim 单独索引。

### Layer 3: Entity / Relation Layer

请新增科研知识图谱层。

位置：

research_kb/index/entities.jsonl
research_kb/index/relations.jsonl

实体类型包括：

- Paper
- Method
- ProductSource
- CorrectionType
- MathematicalModel
- Dataset
- Metric
- ResearchProblem
- TechnicalRoute
- InnovationClaim
- Limitation
- ReproductionBlocker
- FutureWork
- GNSSConstellation
- Signal
- Software
- CodeRepo

relation 类型包括：

- paper_has_method
- paper_uses_product
- paper_addresses_problem
- paper_claims_innovation
- paper_reports_metric
- paper_has_reproduction_blocker
- method_improves_upon
- method_compares_with
- paper_cites_paper
- problem_evolves_to
- technical_route_contains_method

每条 relation 必须包含：

{
  "relation_id": "",
  "source_id": "",
  "target_id": "",
  "relation_type": "",
  "paper_id": "",
  "evidence_status": "",
  "grounding_quotes": [],
  "confidence": "high | medium | low"
}

## 二、索引方式

请新增混合检索，不要只用向量检索。

需要同时支持：

1. Keyword Search
   - 使用 SQLite FTS5 或 Whoosh。
   - 用于精确查找 PPP-B2b、CLK93、DCB、EKF、convergence time 等术语。

2. Structured Search
   - 使用 SQLite。
   - 用于筛选字段：
     - product_source
     - novelty_grade
     - technical_route
     - mathematical_model
     - reproduction_difficulty
     - evidence_status

3. Vector Search
   - 使用 Chroma、FAISS 或其他轻量向量库。
   - 用于语义检索：
     - “哪些论文解决了 PPP-B2b 改正数中断问题？”
     - “有哪些论文只是工程迁移而非实质创新？”
     - “哪些方法降低了实时 PPP 收敛时间？”

4. Graph Search
   - 基于 relations.jsonl 或 SQLite edge table。
   - 用于查询：
     - 某技术路线的发展链条
     - 某研究问题的演化
     - 哪些论文继承或改进了某方法

## 三、新增目录结构

请新增：

research_kb/index/
  claims.jsonl
  entities.jsonl
  relations.jsonl
  sqlite/
    research_kb.sqlite
  vector/
    chroma_or_faiss_index/
  search_logs/
    query_history.jsonl

scripts/
  build_claim_index.py
  build_entity_relation_index.py
  build_sqlite_index.py
  build_vector_index.py
  search_kb.py
  query_innovation.py
  query_routes.py
  query_reproduction.py

## 四、build_claim_index.py

请实现 build_claim_index.py。

输入：

research_kb/papers/json/*.json

输出：

research_kb/index/claims.jsonl

它需要从每篇 paper JSON 中抽取以下 claim：

1. research_problem claim
2. technical_route claim
3. product_source claim
4. mathematical_model claim
5. correction_type claim
6. experiment_epoch claim
7. dataset claim
8. metric claim
9. main_result claim
10. novelty claim
11. reproduction_blocker claim
12. limitation claim
13. future_work claim
14. citation_relation claim

每个 claim 必须保留：

- paper_id
- claim_type
- claim_text
- evidence_status
- grounding_quotes
- confidence
- source field path

如果某字段没有 grounding_quotes，claim 的 evidence_status 不能是 SUPPORTED。

## 五、build_sqlite_index.py

请实现 SQLite 索引。

数据库位置：

research_kb/index/sqlite/research_kb.sqlite

表包括：

papers
claims
entities
relations
quotes
reproduction_blockers
innovation_audits
technical_routes
metrics
datasets

必须支持以下查询：

1. 查询所有 product_source = BDS3_PPP_B2B_BROADCAST 的论文。
2. 查询所有 novelty_grade = A_SUBSTANTIVE 或 B_INCREMENTAL 的论文。
3. 查询所有 novelty_grade = C_ENGINEERING_TRANSFER 或 D_WEAK_OR_OVERCLAIMED 的论文。
4. 查询所有存在 Missing_DCB_Handling 的论文。
5. 查询所有 experiment_epoch 为 NOT_MENTIONED 的论文。
6. 查询所有 reproduction_blockers 数量大于 3 的论文。
7. 查询某个技术路线下的代表论文。
8. 查询某个 metric，例如 convergence time、RMS、3D error，对应哪些论文报告了结果。

## 六、build_vector_index.py

请实现向量检索索引。

向量化对象不是整篇论文，而是 claims。

请对以下文本建立 embedding：

- claim_text
- normalized_value
- tags
- paper title
- technical route
- research problem

每个向量条目 metadata 必须包含：

{
  "claim_id": "",
  "paper_id": "",
  "claim_type": "",
  "technical_route": "",
  "novelty_grade": "",
  "product_source": "",
  "evidence_status": "",
  "source_field": ""
}

如果没有可用 embedding API，可以先实现 mock / fallback：
- 使用 BM25 / TF-IDF
- 或 SQLite FTS5
- 并在 README 中说明如何替换为真实 embedding。

## 七、search_kb.py

请实现统一检索入口。

命令示例：

python scripts/search_kb.py "PPP-B2b convergence time"

python scripts/search_kb.py "哪些论文真正使用了 BDS-3 PPP-B2b broadcast correction?"

python scripts/search_kb.py "哪些论文只是把常规 PPP 方法迁移到 PPP-B2b 场景?"

python scripts/search_kb.py "查找所有没有说明 DCB 来源的 UC 模型论文"

python scripts/search_kb.py "哪些论文报告了收敛时间改善，但没有消融实验?"

输出格式：

- query
- search_mode used
- matched claims
- matched papers
- grounding_quotes
- confidence
- suggested_followup_queries

检索结果必须显示证据 quote，不能只显示论文标题。

## 八、query_innovation.py

请实现创新点查询工具。

它应该支持：

1. 查询某技术路线下的实质创新论文。
2. 查询某技术路线下的弱创新论文。
3. 查询某个研究问题有哪些创新方法。
4. 查询哪些论文作者声称创新，但证据不足。
5. 查询哪些创新点有消融实验支撑。
6. 查询哪些创新点缺少强基线。
7. 查询哪些论文属于工程迁移或应用扩展。

命令示例：

python scripts/query_innovation.py --route "PPP-B2b assisted PPP"

python scripts/query_innovation.py --problem "reduce convergence time"

python scripts/query_innovation.py --grade A_SUBSTANTIVE

python scripts/query_innovation.py --weak-only

输出必须包括：

{
  "paper_id": "",
  "title": "",
  "novelty_grade": "",
  "novelty_statement": "",
  "why_this_grade": "",
  "supporting_evidence": [],
  "missing_evidence": [],
  "related_methods": [],
  "reproduction_risk": ""
}

## 九、query_routes.py

请实现技术路线查询。

支持：

1. 查询所有技术路线。
2. 查询某技术路线下的论文。
3. 查询某技术路线的发展顺序。
4. 查询某技术路线的核心问题。
5. 查询某技术路线的瓶颈。
6. 查询某技术路线中创新性最高的论文。
7. 查询某技术路线中复现风险最低的论文。

命令示例：

python scripts/query_routes.py --list

python scripts/query_routes.py --route "PPP-B2b + multi-GNSS"

python scripts/query_routes.py --route "PPP-B2b + ambiguity resolution" --sort year

## 十、query_reproduction.py

请实现复现查询。

支持：

1. 查询最容易复现的论文。
2. 查询最难复现的论文。
3. 查询缺少代码的论文。
4. 查询缺少原始数据的论文。
5. 查询缺少实时流回放的论文。
6. 查询缺少随机模型参数的论文。
7. 查询适合优先复现的论文。

命令示例：

python scripts/query_reproduction.py --easy

python scripts/query_reproduction.py --missing-code

python scripts/query_reproduction.py --missing-realtime-stream-replay

python scripts/query_reproduction.py --recommend

## 十一、重要约束

不要让检索层产生新的事实。

检索层只能基于：

- paper JSON
- claims.jsonl
- entities.jsonl
- relations.jsonl
- grounding_quotes
- Markdown 原文

检索层可以做排序、过滤、聚合、归类，但不能编造新结论。

如果用户问的问题无法由已有知识库回答，必须返回：

"INSUFFICIENT_KB_EVIDENCE"

并列出缺少哪些信息。

## 十二、验收标准

请新增 tests/test_search_kb.py。

至少测试：

1. 能按 product_source 查询。
2. 能按 novelty_grade 查询。
3. 能查出 weak innovation。
4. 能查出 Missing_DCB_Handling。
5. 能查出 reproduction_blockers。
6. 所有检索结果都能回到 grounding_quotes。
7. 查询不存在信息时返回 INSUFFICIENT_KB_EVIDENCE。
8. 检索层不会生成 paper JSON 中不存在的新事实。

请先实现最小可运行版本：

paper JSON
-> claims.jsonl
-> SQLite index
-> search_kb.py
-> query_innovation.py

Vector search 和 graph search 可以作为第二阶段。
```

---

# 关键提醒

你现在最重要的不是继续优化 PDF 处理，而是把知识库从“论文卡片集合”升级成：

```text
Evidence-grounded Claim Database
```

也就是每一条知识都应该变成：

```json
{
  "claim": "This paper uses BDS-3 PPP-B2b broadcast corrections.",
  "paper_id": "xxx",
  "claim_type": "product_source",
  "evidence": "exact quote from markdown",
  "confidence": "high"
}
```

这样你才能真正做：

```text
检索：哪些论文用了 PPP-B2b？
查询：哪些论文有真实创新？
比较：哪些论文只是工程迁移？
追溯：这个判断来自哪一页哪句话？
```

一句话总结：

**不要把知识库做成“论文摘要仓库”，要做成“有证据的科研主张数据库”。**

-----

> 当前状态
>
>   基础设施已就绪，但只跑通了 1/22 篇论文（Maosen Hao 2020，QZSS CLAS），而且这篇质量很差：
>   - 120 条 grounding_quotes 中有 44 条与原文不匹配（36.7%）
>   - 产品来源标记矛盾（声称 B2b 实际是 QZSS CLAS）
>   - 复现信息 6 项缺失但未标记为阻断项
>
>   跨论文知识图谱（corpus maps）尚未生成——research_kb/corpus/ 目录仍是空的。
>
>   还没有检索/查询功能——现有脚本只覆盖了抽取和校验，缺少搜索入口。
>
>   ---
>   你问的"现在能否做到"
>
>   ┌────────────────────────┬─────────────────────────────────────────────────┐
>   │          能力          │                      现状                       │
>   ├────────────────────────┼─────────────────────────────────────────────────┤
>   │ PDF → Markdown 转换    │ ✅  可用（但需走 danielmiessler-pdf skill）      │
>   ├────────────────────────┼─────────────────────────────────────────────────┤
>   │ DeepSeek 逐 chunk 抽取 │ ✅  可用但质量有问题                             │
>   ├────────────────────────┼─────────────────────────────────────────────────┤
>   │ 单篇论文 JSON 合并     │ ✅  可用                                         │
>   ├────────────────────────┼─────────────────────────────────────────────────┤
>   │ 跨论文知识图谱         │ ⚠️ 脚本有但不完整（引用边未填充，且没数据可跑） │
>   ├────────────────────────┼─────────────────────────────────────────────────┤
>   │ 检索/搜索              │ ❌  不存在                                       │
>   ├────────────────────────┼─────────────────────────────────────────────────┤
>   │ 创新点查询             │ ❌  不存在                                       │
>   └────────────────────────┴─────────────────────────────────────────────────┘
>
>   ---
>   要达成你的目标，需要补齐三块
>
>   1. 把剩余 21 篇 PDF 全部处理完——这是基础，没有数据谈不上检索
>   2. 构建检索系统——在 corpus maps 之上加搜索层（关键词、技术路线、数据集、指标等维度）
>   3. 构建创新点查询——基于 novelty_audit 字段和 problem_evolution.yaml，做创新点对比和查询
>
>   要我现在开始规划这个完整实现方案吗？可以从"先把所有 PDF 跑通，再搭检索层"的顺序来。

现在**不要直接处理剩余 21 篇**。
当前状态说明基础设施存在，但质量门槛没有过。尤其是第一篇 **Maosen Hao 2020 / QZSS CLAS** 本身不是 PPP-B2b 核心论文，却出现产品源矛盾、quote 大量不匹配、复现阻断项漏报，这说明现在的问题不是“论文不够多”，而是：

**抽取层、合并层、校验层还没有稳定挡住错误知识进入知识库。**

你应该先让 Claude Code 做一次 **质量修复阶段**，而不是马上跑全量。

---

## 你现在该给 Claude Code 发什么

直接发下面这段。

```text
当前 pipeline 基础设施已就绪，但 pilot 结果未通过质量门槛。

目前只跑通了 1/22 篇论文：Maosen Hao 2020，QZSS CLAS。该结果存在严重质量问题：

1. 120 条 grounding_quotes 中有 44 条与 Markdown 原文不匹配，invalid quote rate = 36.7%。
2. product_source 标记矛盾：论文实际是 QZSS CLAS，却被错误归入或关联到 PPP-B2b。
3. reproduction_blockers 漏报：复现信息至少 6 项缺失，但没有被完整标记为阻断项。
4. research_kb/corpus/ 仍为空，跨论文知识图谱没有生成。
5. 当前没有 search_kb.py、query_innovation.py 等检索 / 查询入口。

请不要继续全量处理剩余 21 篇论文。现在进入质量修复阶段。

## 一、立即目标

请先修复当前 1 篇 pilot 的问题，使它满足以下条件：

1. invalid grounding quote rate 降到 5% 以下。
2. 所有无法逐字匹配的 grounding_quotes 必须被删除、修正或标记为 INVALID_QUOTE，不得进入最终 paper JSON。
3. QZSS CLAS 必须被正确识别为非 PPP-B2b 产品，不得标记为 BDS3_PPP_B2B_BROADCAST。
4. 如果论文不是 PPP-B2b 核心论文，必须设置：
   - is_ppp_b2b_core_paper = false
   - product_source.actual_product_source = NON_B2B_EXTERNAL_PRODUCTS 或 OTHER_NON_B2B_GNSS_SERVICE
   - domain_relevance = negative_control 或 related_non_b2b
5. reproduction_blockers 必须补齐所有缺失项。
6. validate_kb.py 必须把该论文的错误显式报出，而不是让错误 JSON 通过。

## 二、先做 Root Cause Analysis

请先生成：

research_kb/reports/pilot_failure_analysis.md

报告必须回答：

1. 为什么 44/120 grounding_quotes 无法匹配？
   - 是 PDF 转 Markdown 断行问题？
   - 是 quote 被 DeepSeek 改写？
   - 是 merge 阶段拼接了 quote？
   - 是 Markdown normalize 改变了原文？
   - 是 chunk 和 final paper JSON 引用源不一致？

2. 为什么 QZSS CLAS 被错误关联到 PPP-B2b？
   - 是 prompt 中 GNSS / PPP-B2b 目标过强导致模型强行套标签？
   - 是 schema 缺少 QZSS CLAS / non-B2B 产品类别？
   - 是 validate_kb.py 没有检查 QZSS、CLAS、MADOCA、GPS、Galileo 等非 BDS-3 PPP-B2b 服务？

3. 为什么 reproduction_blockers 漏报？
   - 是 DeepSeek 没有抽取？
   - 是 merge 阶段丢失？
   - 是 validate_kb.py 规则不够严格？
   - 是 schema 字段不能表达缺失项？

## 三、修复 grounding_quotes 机制

请修改 pipeline，使 grounding_quotes 只允许两种来源：

1. 直接从 Markdown 原文截取的 exact substring。
2. 通过 quote repair 工具在 Markdown 中找到的最相近 exact substring。

禁止 DeepSeek 自由生成 quote 后直接进入最终 JSON。

请新增或修改脚本：

scripts/repair_grounding_quotes.py

功能：

1. 输入 paper JSON 和对应 Markdown。
2. 对每条 grounding_quote 做 exact substring check。
3. 如果 exact match 失败，尝试轻量修复：
   - 去除多余空格
   - 合并换行
   - 标准化连字符
   - 标准化 Unicode 标点
4. 如果仍然失败，尝试 fuzzy match 找到 Markdown 中最接近的原文片段。
5. fuzzy match 成功时，必须把 quote 替换为 Markdown 中真实存在的 exact substring，并标记：
   - quote_repaired = true
   - repair_method = fuzzy_match
   - similarity_score = ...
6. 如果无法修复，标记：
   - evidence_status = INVALID_QUOTE
   - quote_valid = false
7. INVALID_QUOTE 不得作为 SUPPORTED claim 的证据。

请在 validate_kb.py 中加入硬规则：

- 关键字段如果只有 invalid quotes，则该字段不能是 SUPPORTED。
- invalid quote rate > 5% 时，该 paper JSON 标记为 failed_validation。
- invalid quote rate > 20% 时，禁止进入 claims.jsonl、corpus maps 和检索索引。

## 四、修复 product_source 分类

请扩展 product_source schema 和 validation。

当前分类不能只围绕 PPP-B2b，要能表达非 B2b GNSS 服务。

请新增 product_source.actual_product_source 枚举：

- BDS3_PPP_B2B_BROADCAST
- IGS_RTS_OR_CLK93
- CNES_OR_OTHER_RTS
- POST_PROCESSED_FINAL_PRODUCTS
- QZSS_CLAS
- QZSS_MADOCA
- SBAS
- RTK_NTRIP
- OTHER_NON_B2B_GNSS_SERVICE
- MIXED_PRODUCTS
- NOT_MENTIONED

请新增字段：

domain_relevance:
  value: "core_ppp_b2b | related_rt_ppp | related_ssr | negative_control | out_of_scope | unknown"
  evidence_status: ...
  grounding_quotes: []

规则：

1. 如果正文出现 QZSS CLAS / CLAS / Centimeter Level Augmentation Service，则不得标为 BDS3_PPP_B2B_BROADCAST，除非同一实验明确使用 BDS-3 PPP-B2b broadcast corrections。
2. 如果 title 或 abstract 包含 PPP-B2b，但 experiment 使用非 BDS-3 PPP-B2b 产品，必须标记 conflict_flag = true。
3. 如果论文不是 PPP-B2b 核心论文，但与实时 PPP / SSR 相关，可以保留在知识库中，但必须作为 related_non_b2b 或 negative_control。
4. 非 PPP-B2b 论文不得进入 PPP-B2b 核心技术路线，只能进入对照或相关技术路线。

请在 validate_kb.py 中新增检测：

- product_source:qzss_clas_misclassified_as_b2b
- product_source:non_b2b_marked_core_ppp_b2b
- domain_relevance:missing_for_non_b2b_product

## 五、修复 reproduction_blockers

请强制 reproduction_blockers 由 validate_kb.py 二次生成候选项，而不是完全相信 DeepSeek。

请实现：

scripts/infer_reproduction_blockers.py

它基于 paper JSON 和 Markdown 检查以下 10 项：

1. missing_public_raw_observation_data
2. missing_realtime_stream_replay
3. missing_ssr_or_b2b_correction_archive
4. missing_code_repository
5. missing_run_entrypoint
6. missing_environment_dependencies
7. missing_random_model_parameters
8. missing_filter_initialization_parameters
9. missing_metric_definition
10. missing_baseline_implementation_details

如果正文没有明确提供某项信息，就生成 blocker candidate。

DeepSeek 输出的 blockers 和 rule-based blocker candidates 必须合并。

如果 DeepSeek 没有报，但规则检测认为缺失，应加入：

{
  "blocker_type": "...",
  "source": "rule_based_validation",
  "severity": "critical | major | minor",
  "description": "...",
  "grounding_quotes": [],
  "evidence_status": "NOT_MENTIONED"
}

注意：复现阻断项可以用 NOT_MENTIONED 作为依据，因为缺失本身就是阻断项。不要要求每个 blocker 都必须有 positive quote。

## 六、重新处理 Maosen Hao 2020

修复后，请只重新处理 Maosen Hao 2020 这一篇，不要处理其他 21 篇。

重新生成：

1. research_kb/markdown/[paper_id].md
2. research_kb/chunks/[paper_id]/*.md
3. research_kb/papers/json/[paper_id].json
4. research_kb/papers/yaml/[paper_id].yaml
5. research_kb/reports/pilot_failure_analysis.md
6. research_kb/reports/pilot_recheck_report.md

pilot_recheck_report.md 必须包含：

1. grounding_quotes 总数
2. invalid quotes 数量
3. invalid quote rate
4. repaired quote 数量
5. unrepaired quote 数量
6. product_source claimed vs actual
7. domain_relevance
8. is_ppp_b2b_core_paper
9. reproduction_blockers 数量和类型
10. validate_kb.py critical errors
11. 是否允许进入 3-paper pilot

## 七、进入下一阶段的门槛

只有满足以下条件，才允许处理更多论文：

1. invalid quote rate < 5%
2. product_source 无高危误判
3. 非 PPP-B2b 论文不会被归入 core_ppp_b2b
4. reproduction_blockers 至少覆盖规则检测出的缺失项
5. validate_kb.py 无 critical error
6. failed_validation 的论文不会进入 claims、corpus maps、search index

如果不满足，请继续修复，不要跑全量。
```

---

## 你现在的路线应该改成这样

不要按“先处理 21 篇，再建检索”走。
正确顺序是：

```text
1. 修复当前 pilot 质量问题
2. 重新跑 Maosen Hao 2020
3. 通过后再跑 3 篇 pilot
4. 3 篇 pilot 通过后再跑 22 篇
5. 生成 claims.jsonl
6. 建 SQLite 检索
7. 再做创新点查询
8. 最后做跨论文图谱
```

原因很简单：

**如果现在直接处理 22 篇，会生成 22 篇污染 JSON。**
后面的知识图谱、创新查询、检索系统都会建立在错误数据上。

---

## 你现在真正缺的不是“检索功能”

现在最缺的是 **准入机制**：

```text
paper JSON 是否允许进入知识库？
```

建议你给每篇论文加一个字段：

```json
{
  "kb_admission": {
    "status": "accepted | accepted_with_warnings | rejected",
    "reason": [],
    "invalid_quote_rate": 0.0,
    "critical_errors": [],
    "allowed_into_claim_index": false,
    "allowed_into_corpus_maps": false,
    "allowed_into_search_index": false
  }
}
```

规则：

```text
invalid_quote_rate > 20% → rejected
product_source 高危误判 → rejected
critical reproduction audit failure → accepted_with_warnings 或 rejected
非 PPP-B2b 论文 → 可以 accepted，但 domain_relevance 必须是 related / negative_control
```

这样你之后做创新点查询时，才能避免把错误结果放进去。

---

## 简短判断

当前系统状态是：

```text
工程框架：可用
抽取质量：未达标
知识体系：尚未建立
检索功能：尚不存在
创新点查询：尚不存在
```

所以现在的下一步不是“规划完整实现方案”，而是：

**先把 pilot 从失败样例修成合格样例。**

-----

> 怎么给Claude code权限

可以。Claude Code 给权限主要有 **3 种方式**：

1. **临时手动授权**：运行时它弹窗问你，点允许。
2. **用 `/permissions` 配置**：在 Claude Code 里输入 `/permissions`，给某些工具长期允许或拒绝。官方文档说明 `/permissions` 可以查看和管理工具权限，allow 会免确认，ask 会每次确认，deny 会阻止使用。
3. **写 `.claude/settings.local.json`**：推荐你这个项目用这种方式，因为它只对当前项目生效，而且通常不会提交到 git。Claude Code 支持 user、project、local 等配置层级，其中 `.claude/settings.local.json` 是本项目个人本地配置。turn876577view0

---

## 推荐你这样做

在项目根目录创建：

```bash
mkdir -p .claude
touch .claude/settings.local.json
```

然后写入：

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": [
      "Read(./paper/**)",
      "Read(./research_kb/**)",
      "Read(./prompts/**)",
      "Read(./schemas/**)",
      "Read(./scripts/**)",

      "Edit(./research_kb/**)",
      "Edit(./prompts/**)",
      "Edit(./schemas/**)",
      "Edit(./scripts/**)",
      "Edit(./tests/**)",
      "Edit(./README.md)",

      "Bash(python scripts/update_kb.py)",
      "Bash(python scripts/validate_kb.py *)",
      "Bash(python scripts/repair_grounding_quotes.py *)",
      "Bash(python scripts/infer_reproduction_blockers.py *)",
      "Bash(pytest *)",
      "Bash(mkdir *)",
      "Bash(ls *)",
      "Bash(find *)"
    ],
    "ask": [
      "Bash(pip install *)",
      "Bash(python -m pip install *)",
      "Bash(git *)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",

      "Bash(rm *)",
      "Bash(rmdir *)",
      "Bash(git push *)",
      "Bash(curl *)",
      "Bash(wget *)"
    ]
  }
}
```

这套权限的含义是：

- 允许 Claude Code 读取 `paper/`、`research_kb/`、`scripts/`、`schemas/`、`prompts/`。
- 允许它修改项目代码、schema、prompt、测试和知识库输出。
- 允许它运行你的 Python pipeline 和 pytest。
- 安装依赖、git 操作需要你确认。
- 禁止它读取 `.env`、secrets、credentials。
- 禁止删除文件、推送 git、随便联网下载。

Claude Code 的权限规则支持 `Tool` 或 `Tool(specifier)` 形式，比如 `Read(./.env)`、`Bash(npm run *)`、`WebFetch(domain:example.com)`，并且 deny 优先于 ask，ask 优先于 allow。turn847929view2

---

## 让它使用 `danielmiessler-pdf` skill

如果 `danielmiessler-pdf` 是 Claude Code skill，确保它放在以下位置之一：

```text
~/.claude/skills/danielmiessler-pdf/SKILL.md
```

或项目内：

```text
.claude/skills/danielmiessler-pdf/SKILL.md
```

Claude Code 的个人 skills 放在 `~/.claude/skills/`，项目 skills 放在 `.claude/skills/`；skill 目录里的 `SKILL.md` 是入口文件。

如果这个 skill 在别的目录，可以启动 Claude Code 时加：

```bash
claude --add-dir /path/to/skills-parent
```

或者在 Claude Code 里输入：

```text
/add-dir /path/to/skills-parent
```

`--add-dir` / `/add-dir` 可以扩展 Claude Code 可访问的目录；额外目录里的 `.claude/skills/` 会被加载，但多数其他 `.claude/` 配置不会作为完整配置根加载。turn218488view0

---

## 关于 `.env` 和 DeepSeek API Key

建议继续 **禁止 Claude Code 直接 Read `.env`**。你的 Python 脚本可以自己读取 `.env`，但 Claude 不应该把 API key 打出来或读进上下文。

注意：Claude Code 的 `Read`/`Edit` deny 规则主要限制 Claude 的内置文件工具；如果你运行 Python 脚本，脚本本身仍可能读取 `.env`。官方文档也说明，Read/Edit 规则不一定限制任意子进程间接读写文件；要做 OS 级限制需要 sandbox。

所以你的安全策略应该是：

```text
Claude Code 不读 .env
Python 脚本读取 .env
日志不打印 API key
```

---

## 最简操作流程

你可以按这个顺序：

```bash
cd 你的项目目录
mkdir -p .claude
nano .claude/settings.local.json
```

粘贴上面的 JSON。

然后打开 Claude Code：

```bash
claude
```

在 Claude Code 里输入：

```text
/status
```

确认它加载了 local project settings。官方文档说明 `/status` 可以查看当前加载了哪些 settings sources。

然后再输入：

```text
/permissions
```

检查权限是否生效。

-----

> 七项门槛全部通过 ✅
>
>   1. ✅  invalid quote rate < 5% (1.67%)
>   2. ✅  product_source 无高危误判
>   3. ✅  非 PPP-B2b 论文不归入 core_ppp_b2b
>   4. ✅  reproduction_blockers 覆盖规则检测的缺失项
>   5. ✅  validate_kb.py 无 critical error
>   6. ✅  failed_validation=false → 不会排除
>   7. ✅  corpus maps 已生成 (6 个文件)
>
>   随时可以进入 3-paper pilot 阶段。

很好，现在可以进入 **3-paper pilot**，但仍然不要全量跑 22 篇。下一步目标是验证系统在三类论文上是否都稳定：

1. **核心 PPP-B2b 论文**：真正使用 BDS-3 PPP-B2b broadcast corrections。
2. **相关但非 B2b 论文**：例如 QZSS CLAS、MADOCA、IGS RTS、CNES、RT-PPP、SSR。
3. **边界/混合论文**：标题或摘要可能提到 PPP-B2b，但实验产品源不一定是 B2b，最容易误判。

你可以直接给 Claude Code 发下面这段：

```text
当前 Maosen Hao 2020 pilot 已通过七项质量门槛：

1. invalid quote rate = 1.67%，低于 5%
2. product_source 无高危误判
3. 非 PPP-B2b 论文不归入 core_ppp_b2b
4. reproduction_blockers 覆盖规则检测的缺失项
5. validate_kb.py 无 critical error
6. failed_validation=false
7. corpus maps 已生成 6 个文件

现在进入 3-paper pilot 阶段，但不要全量处理剩余论文。

## 一、3-paper pilot 目标

请选择 3 篇论文进行 pilot：

1. core_ppp_b2b_candidate
   优先选择标题、摘要或文件名明确包含 BDS-3 PPP-B2b、PPP-B2b broadcast、B2b correction、BDS-3 PPP-B2b service 的论文。

2. related_non_b2b_candidate
   选择与实时 PPP / SSR / GNSS augmentation 相关但不是 PPP-B2b 的论文，例如 QZSS CLAS、MADOCA、IGS RTS、CNES、RT-PPP、SSR、PPP-AR 等。

3. ambiguous_or_boundary_candidate
   选择最容易误判的边界论文，例如标题提到 PPP-B2b，但正文实验可能使用 IGS RTS、CLK93、CNES、final products、NTRIP 或其他非 BDS-3 PPP-B2b 产品。

如果无法自动判断，请根据文件名和 Markdown 初步扫描结果选择，并在报告中说明选择依据。

## 二、处理流程

对这 3 篇论文运行完整 pipeline：

PDF
-> danielmiessler-pdf skill
-> Markdown
-> chunks
-> DeepSeek-v4 chunk extraction
-> quote repair
-> paper JSON merge
-> infer_reproduction_blockers
-> validate_kb.py
-> corpus maps update

注意：

- DeepSeek 只读 Markdown，不读 PDF。
- PDF 只能由 danielmiessler-pdf skill 处理。
- invalid quote 不得进入 SUPPORTED claim。
- failed_validation=true 的论文不得进入 claims、corpus maps、search index。
- 非 PPP-B2b 论文可以进入知识库，但必须标记 domain_relevance，不得进入 core_ppp_b2b 技术路线。

## 三、生成报告

请生成：

research_kb/reports/three_paper_pilot_report.md

报告必须包含：

### 1. Pilot selection

对每篇论文列出：

- paper_id
- source_file
- candidate_type
- selection_reason
- expected_domain_relevance

### 2. Pipeline status

对每篇论文列出：

- PDF parse status
- Markdown generated: yes/no
- chunk count
- DeepSeek chunk calls: success/failed
- quote repair count
- merge status
- validation status
- corpus admission status

### 3. Evidence quality

对每篇论文列出：

- total grounding_quotes
- valid quotes
- invalid quotes
- repaired quotes
- invalid quote rate
- whether invalid quote rate < 5%

### 4. Product source audit

对每篇论文列出：

- claimed_product_source
- actual_product_source
- product_source grounding quote
- conflict_flag
- is_ppp_b2b_core_paper
- domain_relevance
- product_source validation errors, if any

### 5. Epoch audit

对每篇论文列出：

- publication_year
- experiment_epoch
- experiment_epoch grounding quote
- whether publication_year was incorrectly reused
- epoch validation errors, if any

### 6. DCB / ionospheric audit

对每篇论文列出：

- mathematical_model
- ionospheric_handling
- DCB source, if mentioned
- Missing_DCB_Handling flag
- DCB validation errors, if any

### 7. Reproduction audit

对每篇论文列出：

- reproduction_blockers count
- blocker types
- rule_based blockers added
- DeepSeek blockers kept
- missing critical blockers, if any
- reproduction difficulty

### 8. Novelty audit

对每篇论文列出：

- novelty_grade
- novelty_statement
- supporting evidence
- missing evidence
- whether it appears to be substantive innovation or engineering transfer

### 9. Corpus maps status

列出 6 个 corpus maps 是否更新：

- technical_routes.yaml
- problem_evolution.yaml
- citation_graph.json
- method_lineage.yaml
- dataset_metric_index.yaml
- reproduction_index.yaml

并说明每篇论文是否被纳入对应 map。

### 10. Final decision

输出以下结论之一：

- PASS_READY_FOR_FULL_RUN
- PASS_WITH_WARNINGS_NEED_MINOR_FIXES
- FAIL_FIX_BEFORE_MORE_PAPERS

只有满足以下条件才能输出 PASS_READY_FOR_FULL_RUN：

1. 3 篇全部生成 paper JSON
2. 每篇 invalid quote rate < 5%
3. 无 product_source 高危误判
4. 非 PPP-B2b 论文不进入 core_ppp_b2b
5. experiment_epoch 不误用 publication_year
6. Missing_DCB_Handling 规则正确触发
7. reproduction_blockers 覆盖规则检测缺失项
8. validate_kb.py 无 critical error
9. failed_validation=true 的论文没有进入 corpus maps
10. corpus maps 成功更新

如果不满足，请不要继续处理剩余 19 篇。请列出阻断问题和修复建议。
```

等这 3 篇通过后，再进入全量处理。
**现在的核心原则还是：宁可慢一点，也不要把错误 JSON 批量灌进知识库。**