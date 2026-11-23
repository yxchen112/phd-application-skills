# PhD Application Skills (Claude Code)

Two Claude Code skills for PhD applications, distilled from a real 2026–27 application cycle (engineering / fluid mechanics + scientific ML), with personal details removed.

| Skill | What it does |
|---|---|
| [`phd-sop-structured`](phd-sop-structured/SKILL.md) | Writes or restructures a PhD Statement of Purpose into the standard admissions shape: research topic in sentence 2, project paragraphs (motivation → my role → implication-level finding → outcome), PhD plan, faculty fit with verified work, school-swap test. Merges the Wordvice SOP guide, Lucy Lai's PhD application notes, a common paragraph template, and genre research on doctoral SOPs (Samraj & Monk 2008; Chiu 2015, 2016). |
| [`phd-research-proposal`](phd-research-proposal/SKILL.md) | End-to-end research proposal workflow (Chinese instructions, English + Chinese output): advisor alignment table, method design (keep known structure, learn only the unknown; data splits; pilot-then-scale; fallback plan), Crossref/arXiv reference verification script, review loop with a sub-agent rubric, compression to ~2,700 words, docx/PDF/Gantt builders, and a form-box mode for online systems with character limits (e.g. Hong Kong PhD Fellowship). |

## Install

```bash
git clone https://github.com/yxchen112/phd-application-skills.git
cp -R phd-application-skills/phd-sop-structured phd-application-skills/phd-research-proposal ~/.claude/skills/
```

Scripts need Python 3; `build_rp_docx.py` needs `python-docx`, `make_gantt.py` needs `matplotlib`, `export_pdf.sh` uses Microsoft Word on macOS.

## Principles shared by both skills

- Science story, not life story; concrete facts over adjectives.
- Every claim about a professor's work or a cited paper is verified first.
- No fabrication; the applicant's own facts and voice stay. Disclose AI use truthfully where a program asks.

## 中文说明

两个用于申博的 Claude Code skill：`phd-sop-structured`（标准结构的 SOP 写作与改写）和 `phd-research-proposal`（RP 全流程：导师对齐、方法设计、文献核实、审稿迭代、压缩、生成 docx/PDF/甘特图，以及网申文本框改写）。案例均已匿名化。

## License

MIT
