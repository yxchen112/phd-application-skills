# 02 固定框架与篇幅

用户定下的框架（参考一份 GHRM 范本和 RP 写作笔记）。目标学校另有模板时，先对照模板：模板要求的标题必须出现，其余按此框架组织到模板标题之下。

## 抬头

```
Research Proposal
<Title>
Student's Name: …
Department: …
Proposed Degree: Doctor of Philosophy (PhD)
Supervisor: Dr …
```
四行信息，不用表格。中文版标题为"研究计划"，信息行为 姓名 / 院系 / 拟攻读学位 / 导师。

标题：概念 + 方法 + 对象，例如 "Learning Interpretable Wall Functions for Turbulent Flow over Rough Surfaces from Large-Eddy Simulation Data"。

## 正文结构与每节写什么

**Abstract**（150–180 词）+ **Keywords**（5 个）
问题与难点 → 现有做法的缺陷 → 本项目做什么 → 数据怎么来 → 怎么学 → 怎么验证 → 成果一句话。少堆软件名。

**1. Introduction**（三段，约 200–250 词，无小标题，不写 gap）
① 工程/科学背景，引出核心物理量；② 现有做法及其根本缺陷；③ 为什么现在能做 + 本计划是什么 + 核心设计思想一句话（例："keeps what is already known … and learns only what depends on the surface"）。

**2. Research Questions**
- **2.1 Literature Review**（约 300–350 词）：按主题分段，段首加粗引导语。必有一段"Choosing the learning method"类的段落，直接回答导师的方法疑问：先列交付物的要求，再逐类方法说清能/不能满足、在本项目中的角色。
- **2.2 Research Gaps**（约 150–200 词）：通常三条，加粗引导语，例如 Methodological gap / Data gap / Representation gap。写"We found no …"，不写"no one has ever"。
- **2.3 Research Aims and Questions**（约 300 词）：一句总目标；(1)(2)(3) 研究问题，每条带加粗短标签（不用 RQ1）；**Hypotheses.** 可证伪，说清两种结果各意味着什么；**Measures of success.** 带数字和条件。

**3. Methodology**（约 1,200–1,300 词，含表格和 3.5）
开头一句话说清"先在低成本条件下打通全链条再放大"以及哪一步回答哪个问题。
- 3.1 Step 1: Solver/Tool Selection and Pilot：工具选择理由、试点内容、算力数量级、预算不足的取舍顺序。
- 3.2 Step 2: Data（数据库/实验/样本）：设计维度、受控对照组、数据三层分工、一张模拟/实验方案表。
- 3.3 Step 3: Learning/Analysis：保留的结构（公式 1）、学习对象、机制分析、显式模型（公式 2）、选择方法与公平对照。
- 3.4 Step 4: Testing：最终独立检验、外推检验的隔离规则、对照模型、适用范围。
- 3.5 Feasibility and Research Fit：3–4 句，个人经历与项目的对应关系。

**4. Expected Outcomes and Significance**（约 200 词）
- 4.1 Expected Outcomes：(1)–(4)，最后一条写"Journal manuscripts on … and on …"，不写期刊名和篇数承诺。
- 4.2 Research Significance：(1) Theoretical (2) Practical (3) Methodological（可选），每条一两句。

**5. Research Timeline**
一句话说明任务为何重叠 + 甘特图。项目型 RP 默认 12 个月，行对应 Step，末行"Manuscript writing / 论文撰写"。不加"Beyond the first year"段落（用户明确不要）。

**References**：编号制 [1]，按首次出现排序，每条带 DOI 链接；主版本 25–35 篇。

## 篇幅预算（主版本，不含参考文献）

| 部分 | 英文词数 |
|---|---:|
| Abstract | 150–180 |
| 1. Introduction | 200–250 |
| 2.1 Literature Review | 300–350 |
| 2.2–2.3 Gaps, Aims, Hypotheses, Measures | 400–450 |
| 3. Methodology（含表格和 3.5） | 1,200–1,300 |
| 4–5. Outcomes, Significance, Timeline | 200–250 |
| **合计** | **约 2,500–2,800** |

排版后约 5 页正文 + 1–2 页参考文献。不靠缩字号和页边距减页。

## 图表规矩

- 最多 1–2 张表，三线表，表格替代文字，正文不再逐项复述表格内容。最有价值的是"模拟/实验方案表"（条件、样本数、用途）。
- 不画流程图（用户认为不必要且显得 AI 味）。
- 甘特图：单色浅蓝圆角条、细灰网格，不加菱形里程碑、不加里程碑行。
- 公式只放 1–2 个核心式，居中编号，正文不出现 LaTeX 源码（`e^{κC}` 一律写成 `exp(κC)`）。

## 详细版与主版本

审稿中补进去的实施细节（生成算法、阈值、备用求解器、逐参数拟合方式等）全部留在 `rp_draft_detailed.md`，生成"详细版_内部底稿.pdf"给用户面谈前复习用。发导师的是压缩后的主版本。
