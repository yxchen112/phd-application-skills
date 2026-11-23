# 04 写作规则：去 AI 味、反防御性、术语一致、读得懂

RP 本质上是一篇作文：用精简的话把整件事讲明白，导师读一遍就懂。

## 1. 读者是导师，不一定是本子领域专家

- 关键概念第一次出现时用一句话说清（例：先说 LES 在工程雷诺数下无法解析近壁流动 → 依赖 wall model → 最常用的是 wall function → 粗糙壁上就是平移的对数律）。
- 缩写第一次出现时写全称，之后只用缩写。
- 一句话一个意思；长句拆短；能用表格就不用长段落列数字。
- 写完问自己：不看软件名，导师能不能用一句话说出这个研究要解决的科学问题？

## 2. 去 AI 味

避免：
- 堆砌形容词和宣传腔：crucial, pivotal, novel, groundbreaking, comprehensive, robust（无实指时）、"paves the way"、"sheds light on"、"in the realm of"、"delve"、"landscape"、"leverage"。
- 机械的三连排比、"not only … but also"、"not X but Y" 反复出现。
- 破折号过多；每段都以"Moreover/Furthermore/Additionally"开头。
- 空泛总结句："This highlights the importance of …"
- 模糊归因："Studies have shown …"（要么给引用，要么删）。
- 反复复述：摘要、文献、方法、成果四处讲同一件事。

用：具体数字、具体对象、具体比较；主动语态和明确主语；平实动词（measure, test, compare, fit, run）。

## 3. 反防御性（但不夸大）

- 直接陈述做什么、怎么做、预期什么。不写 "we do not claim / this study does not attempt / it should be noted that"。
- 限制条件写一次，放在方法里它起作用的位置（例："All tests stay within equilibrium channel flow."），不散落在摘要和引言。
- 同时避免过强表述（审稿会扣分）：
  - "cannot be predicted" → "remains hard to predict reliably"；
  - "ΔU⁺ is the extra skin friction" → "sets the increase in skin friction"；
  - "cannot be checked outside the training range" → "their form says nothing about their behaviour outside the training range"；
  - "no one has studied" → "We found no …"；
  - 假设不要写成已发生的结论。
- 申请人的不足不主动自曝，用方案覆盖（试点阶段先复现文献算例）。

## 4. 术语一致（AI 最常犯的错）

AI 写长文时会把同一个概念换着说法写，读者会以为是不同的东西。做法：

1. 起稿前建术语表 `terms.json`：选定词 → 禁用变体。例（来自案例）：
   - explicit wall function ← closure / explicit closure / wall law / expressions / wall model（"wall model"只用于泛指类别和别人的模型）
   - wall-modelled LES ← coarse-grid LES
   - held-out surface family ← unseen surface families
   - transitional curve ← transitional response / transitional roughness function / ΔU⁺ curve
   - transitionally rough regime ← transitional regime
   - geometric features ← surface features / descriptors
   - peaks ← crests / roughness-element peaks
   - matching point ← matching height
   - fully rough level ← fully rough asymptote
   - spatial organisation ← higher-order organisation
2. 定稿前运行 `python3 scripts/rp_stats.py rp.md --terms terms.json`，逐个处理。
3. 中文版单独一张表（例：显式壁面函数 ← 闭合式/壁面律；壁面模化 LES ← 粗网格 LES；留出表面族 ← 未见过的表面族；峰顶 ← 粗糙元峰顶）。
4. 节标题、研究问题的加粗标签、甘特图标签、讲解教程也要跟着改。
5. 修改阶段名称后（例如 "a posteriori selection" → "solver-informed selection"），全文搜一遍旧名。

## 5. 数字与内部一致

- 同一个数在正文、表格、甘特图、摘要、中文版里必须一致（表面数、Re、k⁺、月份、算例数、训练点数）。
- 新增或删除一类数据后，重算训练样本数（例：留出开发表面后 35–45 → 30–40 块表面，80–100 → 70–90 个点）。
- 表格的行与正文描述一致（例：正文说孪生表面只在 590 算，表格"数据库"行就不能写"全部"）。

## 6. 格式细节

- 研究问题用 (1)(2)(3) + 加粗短标签，不用 RQ1/H1。
- 用词准到专业层面：筛选公式时查的是 "singularities and non-physical predictions"，不是 "singular values"（矩阵概念）。
- 段首加粗引导语以句号结束：**Data gap.** …
- docx 里不能出现 LaTeX 源码；上下标用 Unicode（ΔU⁺、k_s 由构建脚本转下标）。
- 长公式内联容易断行 → 放成编号公式；必须内联的短式用不换行空格。

## 7. 中文对照版

- 与英文主版本逐段对应，不增不减；术语按中文术语表。
- 中文标点；数字与单位、英文之间留空格（Re_τ = 1000、5–9%）。
- 学术书面语，避免口语化和翻译腔（"进行了…的研究"→"研究了…"）。
- 中文版是给用户自己读懂和面谈准备用的，默认不发导师。
