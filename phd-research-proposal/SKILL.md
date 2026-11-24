---
name: phd-research-proposal
description: 申博 Research Proposal（RP）全流程 skill（中英双语）。用于给任何学校、任何导师写或打磨博士申请 RP，也适用于把 RP 改写成网申系统里有字数限制的文本框（如香港 HKPFS 研究计划与愿景陈述）：读导师聊天记录和主页挖出真实意图、选方法并论证"为什么不用别的"、核实全部文献、按固定框架写英文主版本和中文对照版、多轮审稿迭代、压缩篇幅、生成 docx/PDF/甘特图、写保姆级讲解教程和给导师的消息。触发词：申博 RP、research proposal、研究计划、导师给了方向、套磁后写 RP、润色 RP、RP 审稿、RP 讲解、给导师发 RP。
---

# 申博 RP 全流程（phd-research-proposal）

这份 skill 蒸馏自一次真实的博士 RP 写作（工程/流体力学 + 科学机器学习方向，七轮审稿，从约 4,000 词压到约 2,700 词），以及之后把 RP 改写成多个网申系统文本框的经验。规则来自真实踩过的坑；文中案例已匿名化。非工程领域同样适用：把"物理约束/求解器"换成本领域的"已知理论/标准方法"即可（见下方"领域适配"）。

## 何时用、何时转给别的 skill

- 导师已经给了方向或项目，要写/改 RP：用本 skill，从阶段 0 开始。
- 还没选题，只有导师主页：先用 `advisor-topic-rp` 做选题对比（只取它的选题、核实、套磁邮件部分；它的七段式结构、RQ1 标签、"理论框架"一节与本 skill 冲突，以本 skill 为准）。
- 只需要套磁邮件：`advisor-topic-rp` 第 9 节或 `apply-cold-email-drafter`。
- 面试准备深挖：`apply-interview-prep`；本 skill 只做 RP 配套的高频问题。
- **去 AI 味是每次必做的默认步骤，不用等用户提**：每份草稿、每次修改、每次中译英后，都按 [references/08-de-ai.md](references/08-de-ai.md) 过一遍（融合 humanizer、stop-slop、no-ai-slop 和用户亲手改过的句子），交付时附一行去 AI 打分。反防御性见 [references/04-writing-rules.md](references/04-writing-rules.md)，需要时再调 `anti-defensive-writing`。

## 不可违反的规则

1. **先对齐导师，再写一个字。** 逐条读聊天截图，分清谁说的话（微信：右侧绿色是用户，左侧白色是导师）。曾把导师的"symbolic regression 我自己调研了一些，就是不确定有没有其他更好的方法"误当成用户的话，差点答错核心问题。
2. **导师每一个明确要求都要在 RP 里有可指认的回应**，做一张"导师要求 → RP 位置"对照表（见 01）。
3. **方案必须真的可行**：先低成本打通全链条的试点、算力数量级、预算不足时先砍什么后砍什么、哪些必须保留。
4. **所有文献逐条核实**（Crossref/arXiv + 摘要/全文核对具体数字和说法）。没核实的不引；数字说错比不引更糟。
5. **一个概念只用一个名字**，中英文各建一张术语表，定稿前用 `rp_stats.py --terms` 扫一遍。
6. **去 AI 味 + 反防御性 + 不夸大**三者同时满足：直接陈述，不写"we do not claim"，但也不写"cannot be predicted""first ever"这类绝对化表述。
7. **不写期刊名、不写投几篇、不写"第一年之后/博士后续"**，除非用户要求。预期成果只写"期刊论文：一篇关于…，一篇关于…"。
8. **主版本控制在约 2,500–2,800 英文词（不含参考文献）**；详细实施方案另存为内部底稿，不发给导师。
9. **不改用户明确定下的偏好**：外部审稿意见和用户偏好冲突时听用户的，并在回复里说明没采纳哪条、为什么。
10. 每轮修改前备份（`*_vNN_backup.md`），交付前导出 PDF **逐页看图**检查版面。

## 工作流（按阶段推进，每阶段结束给用户一句话结论）

### 阶段 0：收集材料
导师聊天截图/邮件、导师主页链接、用户 CV 与代表作、目标学校的 RP 模板或要求（例如港大工学院模板只要求 Background / Methodology / Outcomes and Value / References）、语言（默认英文主版本 + 中文对照版）、项目周期（导师给的是一个具体项目时默认 12 个月）。

### 阶段 1：导师对齐 → [references/01-advisor-alignment.md](references/01-advisor-alignment.md)
输出：导师背景摘要、要求对照表、"深层意图"判断、导师提到的第三方工作的核实结果。

### 阶段 2：方法与研究设计 → [references/03-method-design.md](references/03-method-design.md)
核心思想：保留已知物理/结构，只学未知部分；按"交付物要满足什么要求"对比方法族，每个方法给一个明确角色；数据三层分工；公平对照；算力上限与退路；受控实验检验机制；可证伪假设。

### 阶段 3：文献核实 → [references/05-literature-verification.md](references/05-literature-verification.md)
`scripts/verify_refs.py refs.py --only-cited rp.md` 先查记录真伪，再对每条"承重"引用核对原文里的具体数字和结论。

### 阶段 4：写作 → [references/02-structure-and-length.md](references/02-structure-and-length.md) + [references/04-writing-rules.md](references/04-writing-rules.md)
从 `assets/rp_skeleton_en.md` 起稿。正文 Markdown + `refs.py`，引用写 `{key}`。

### 阶段 5：审稿迭代 → [references/06-review-loop.md](references/06-review-loop.md)
开独立子智能体按 100 分制审（科学问题、物理/建模、验证、可行性、文献、结构）；外部智能体的意见逐条"采纳/改用更好方案/不采纳+理由"，引用的文献自己再查一遍。

### 阶段 6：压缩与定稿
`scripts/rp_stats.py rp.md` 看各节字数，按 02 里的字数预算压缩：删通用方法综述和不用的方法、表格替代文字且正文不重复表格、实施细节移入内部底稿；**不要删**数据分工、参考值来源、候选上限、独立最终检验这类决定可信度的内容。

### 阶段 7：生成文件 → [references/07-build-and-deliver.md](references/07-build-and-deliver.md)
甘特图 `make_gantt.py`，docx `build_rp_docx.py`（中英各一次），PDF `export_pdf.sh`，然后用 Read 读 PDF 每一页检查：大块空白、表格跨页、公式断行、参考文献缩进、甘特图标签溢出。

### 阶段 8：配套交付
中文对照版（同步术语表）、保姆级讲解教程（HTML artifact：物理从零讲 → 公式逐项拆 → 逐节精读 → 导师可能问的问题 → 术语表 → 阅读顺序）、给导师的消息草稿、提醒按目标学校要求如实披露 AI 使用。


## 补充规则（借鉴 luwill/research-skills 的 research-proposal 等公开 skill 后补齐）

- **大纲确认关卡**：正文动笔前，先给用户一份大纲（研究问题、每节要点、拟引的核心文献、字数分配），用户确认后再写全文。避免写完才发现方向不对。
- **文献分桶**：检索到的文献按 5 类整理再写综述：背景/经典、最新进展、明确指出空白的工作、要借用的方法、相邻领域对照。每一桶至少有一条"承重"引用，且全部经过阶段 3 核实。
- **领域适配**：
  - STEM（工程/物理/计算）：保留本 skill 的"保留已知结构、只学未知部分"、试点—扩展、数据分工、算力与退路。
  - 社科/人文：把"求解器检验"换成"方法论辩护 + 资料/样本获取可行性 + 伦理审查"；理论框架一节可以保留。
- **网申文本框模式**（Form-box mode）：很多系统（如香港 HKPFS 的"研究经历 / 题目 / 计划 / 愿景 1–4"）把 RP 拆成有字符上限的文本框。
  1. 先建"框 → 内容 → 字符上限"对照表；题目框通常 ≤500 字符，第二句就要写出具体研究问题。
  2. 计划框按 背景 → 目标 → 研究问题 → 假设 → 方法分步 → 时间表 → 预期成果 → 简短参考文献 组织；参考文献用"作者 年份 期刊 卷 页"短格式省字符。
  3. 按 ASCII 计数（希腊字母、上标、长破折号、重音字母在老系统里会乱码：Δ→Delta、τ→tau、³→^3），留 1–2% 余量。
  4. 不同学校的版本不要整段雷同（同一资助方可能同时看到两份），按导师方向重写，但事实不变。
  5. 如系统要求，AI 使用声明如实写在"其他说明"框；不写"初稿是我自己写的"这类不实表述。
- **RP / SOP / 研究陈述分工**：学校同时要 RP 和 SOP 时，RP 讲"做什么、怎么做、为什么可行"，SOP 讲"我是谁、做过什么、为什么是这里"（SOP 结构见同仓库的 phd-sop-structured）。

## 文件索引

| 文件 | 用途 |
|---|---|
| references/01-advisor-alignment.md | 读聊天、查导师背景、要求对照表、深层意图 |
| references/02-structure-and-length.md | 固定框架、每节写什么、字数预算、表格与图的规矩 |
| references/03-method-design.md | 方法选择论证、数据分工、公平比较、可行性、假设 |
| references/04-writing-rules.md | 去 AI 味、反防御性、术语一致、通俗化、中英版规则 |
| references/08-de-ai.md | 强制去 AI 清单（词、句式、节奏、终读、打分），每次交付前自动执行 |
| references/05-literature-verification.md | 文献核实流程、常见错误、403 时怎么办 |
| references/06-review-loop.md | 审稿评分表、子智能体提示词、外部意见取舍、常见扣分点 |
| references/07-build-and-deliver.md | 构建命令、版面检查清单、教程结构、导师消息模板 |
| scripts/build_rp_docx.py | Markdown + refs → 规范 docx（中英） |
| scripts/make_gantt.py | JSON → 简洁甘特图（中英，自动适配标签宽度） |
| scripts/verify_refs.py | Crossref/arXiv 批量核对文献 |
| scripts/rp_stats.py | 各节字数、引用数、术语变体扫描 |
| scripts/export_pdf.sh | 用 Word 把 docx 导出 PDF |
| assets/ | 中英骨架、refs 模板、info/gantt/terms 示例 JSON |
