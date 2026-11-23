# 07 生成文件与交付

## 1. 项目目录约定

```
<school>_rp/
  rp_build/
    rp_draft.md            英文主版本（Markdown，引用写 {key}）
    rp_draft_zh.md         中文对照版
    rp_draft_detailed.md   内部详细版（不发导师）
    refs.py                REFS = {...}
    info_en.json info_zh.json gantt_en.json gantt_zh.json terms.json
    rp_draft_vNN_backup.md 每轮备份
  <Name>_RP_<topic>.docx/.pdf          发导师的英文版
  <Name>_RP_<topic>_中文版.docx/.pdf
  <Name>_RP_详细版_内部底稿.pdf
  RP讲解教程.html
```
从 `assets/` 复制骨架和 JSON 模板起步。

## 2. 构建命令

```bash
S=~/.claude/skills/phd-research-proposal/scripts
python3 $S/make_gantt.py gantt_en.json
python3 $S/make_gantt.py gantt_zh.json
python3 $S/build_rp_docx.py --src rp_draft.md    --refs refs.py --info info_en.json --lang en --out ../X_RP.docx
python3 $S/build_rp_docx.py --src rp_draft_zh.md --refs refs.py --info info_zh.json --lang zh --out ../X_RP_中文版.docx
python3 $S/rp_stats.py rp_draft.md --terms terms.json
python3 $S/verify_refs.py refs.py --only-cited rp_draft.md
$S/export_pdf.sh ../X_RP.docx ../X_RP_中文版.docx
```
Markdown 语法见 `build_rp_docx.py` 顶部说明：`EQ …` 编号公式；`**Table 1.** …` 表题；管道表格；`[[FIG: path | 16.2]]` 插图；`(1) **Label.** …` 编号条目。

## 3. 版面检查（必须读 PDF 每一页的图像）

- 大块空白：常因 keep-with-next 链条（标题 → 段落 → 图/表）把整块推到下一页。编号条目只与下一条编号条目绑定；不要让"意义"列表和下一节标题、甘特图连成一串。
- 表格：跨页时表头重复；单行孤悬在下一页可以接受，整表被推走留下半页空白时，压缩表格或允许跨页。
- 公式：长内联公式会断行 → 改为编号公式；docx 里不能出现 `e^{…}` 之类源码。
- 参考文献：悬挂缩进对齐（脚本已加 0.8 cm 制表位和右缩进，防止某些条目编号后间距被压缩）。
- 甘特图：标签不压网格线（脚本自动按最长标签定宽）；中英文月份标注正确。
- 中文版：首行缩进，公式后的"其中…"不缩进；中英混排字体正常（SimSun/SimHei + Times New Roman）。
- 页数：英文主版本约 5 页正文 + 参考文献。

## 4. 保姆级讲解教程（HTML artifact）

用户自己必须能讲懂 RP。结构：
0. 怎么用这份讲解
1. 一句话看懂项目 + 逻辑链（编号卡片，不依赖 mermaid 等外部库）
2. 必须先懂的基础知识：从零讲起，每个公式拆开讲每个符号；按公式真实计算绘制 1–2 张示意图（内联 SVG，JS 生成）
3. 模拟/实验方法基础
4. 文献地图表：做了什么 / 与本项目关系
5. RP 逐节精读：每节在说什么、为什么这样设计、关键数字从哪来（如 k_t⁺ = Re_τ/12 的表）
6. 核心公式全拆解：逐项含义、两个极限的推导、派生关系
7. 导师可能问的 12–15 个问题 + 参考回答 + "面谈能脱稿讲出的五句话"
8. 中英术语对照表
9. 建议阅读顺序（8–10 篇，每篇读什么、带着什么问题读）

技术要点：数学用 MathJax（cdnjs 固定版本）；图表 CSS 只作用于 `figure > svg`，否则会把 MathJax 的 SVG 放大；发布后在本地 http 服务器里用浏览器检查公式和图。RP 每次改动后同步教程里的数字、表号、方法名。

## 5. 给导师发消息（微信模板）

> X老师好～RP 初稿已经完成了，发您审阅（PDF 附上）。
> 主要按您之前的建议来做的：
> 1. <对应导师第一条要求的做法>；
> 2. <对应求解器/工具的做法>；
> 3. <对应方法疑问的做法，一两句>。
> 计划按 12 个月来安排。有哪些地方需要调整，麻烦您多指点，您方便的时候我们再细聊～

- 发英文 PDF；中文版不主动发；导师要改再补 docx。
- 白天工作时间发；两三天无回复再轻问一次。

## 6. 发出前提醒用户

- 3.5 节个人经历逐条属实；自己的论文条目（作者顺序、卷号、文章号）正确。
- 完整读一遍英文 PDF，配合讲解教程，做到每段都能用自己的话讲出来。
- 按目标学校研究生院的最新要求如实披露 AI 使用（例如部分香港高校的研究生院要求在申请材料中如实说明 AI 的使用方式）。
- 面谈若被问"会不会自己开发新方法"：先用现有方法做公平对比和求解器内筛选，若效果明显，下一步把求解器放进搜索循环——这是读博后与导师商量的方向。
