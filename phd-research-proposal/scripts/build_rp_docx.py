"""Build a research-proposal .docx from a Markdown draft and a reference dictionary.

Usage:
  python3 build_rp_docx.py --src rp.md --refs refs.py --info info.json --lang en --out RP.docx
  python3 build_rp_docx.py --src rp_zh.md --refs refs.py --info info_zh.json --lang zh --out RP_zh.docx

Draft syntax (Markdown subset):
  # Title                       -> title block ("Research Proposal" / "研究计划" + title + info lines)
  ## 1. Section / ### 1.1 Sub   -> headings (kept with next paragraph)
  **Bold run-in.** text         -> bold lead-in
  (1) **Label.** text           -> hanging-indent numbered item; kept with the next item in the same list
  EQ U(h)/u_τ = ... ,           -> centred, auto-numbered equation (1), (2), ...
  **Table 1.** caption          -> table caption (kept with the table)
  | a | b |  pipe table         -> three-line table, column widths from content, header repeats across pages
  [[FIG: path | width_cm | optional caption]]  -> centred picture
  {citekey}                     -> numbered citation in order of first appearance, from refs REFS dict
  _x subscripts (k_s, Re_τ), ⁺ superscripts as Unicode; <!-- comments --> are skipped.

refs file: a Python file defining REFS = {"key": "Full reference string with DOI link", ...}
           or a JSON object with the same shape.
info file: JSON list of [label, value] pairs, e.g. [["Student's Name", "<Your Name>"], ...].
"""
import argparse, json, re, runpy
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ap = argparse.ArgumentParser()
ap.add_argument("--src", required=True)
ap.add_argument("--refs", required=True)
ap.add_argument("--info", required=True)
ap.add_argument("--lang", choices=["en", "zh"], default="en")
ap.add_argument("--out", required=True)
ap.add_argument("--font", default="Times New Roman")
a = ap.parse_args()

ZH = a.lang == "zh"
FONT = a.font
EA_BODY, EA_HEAD = "SimSun", "SimHei"
TEXT_W = 16.2  # cm, A4 with 2.4 cm margins
L = {"title": "研究计划" if ZH else "Research Proposal",
     "refs": "参考文献" if ZH else "References",
     "keywords": ("**关键词", "**Keywords"),
     "caption": ("**Table ", "**表 ")}

REFS = (json.load(open(a.refs, encoding="utf-8")) if a.refs.endswith(".json")
        else runpy.run_path(a.refs)["REFS"])
INFO = json.load(open(a.info, encoding="utf-8"))
text = open(a.src, encoding="utf-8").read()
text = re.sub(r"<!--.*?-->", "", text, flags=re.S)

# ---- numbered citations in order of first appearance ----
order = []
for k in re.findall(r"\{([A-Za-z0-9_\-]+)\}", text):
    if k not in REFS:
        raise SystemExit(f"missing ref: {k}")
    if k not in order:
        order.append(k)
num = {k: i + 1 for i, k in enumerate(order)}


def cite_group(m):
    ns = sorted(num[k] for k in re.findall(r"\{([A-Za-z0-9_\-]+)\}", m.group(0)))
    return "[" + ", ".join(map(str, ns)) + "]"


text = re.sub(r"\{[A-Za-z0-9_\-]+\}(?:\s*\{[A-Za-z0-9_\-]+\})*", cite_group, text)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.4)
sec.top_margin = sec.bottom_margin = Cm(2.3)
st = doc.styles["Normal"]
st.font.name = FONT; st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), EA_BODY)
st.paragraph_format.space_after = Pt(5)
st.paragraph_format.line_spacing = 1.3 if ZH else 1.15


def add_runs(p, s, bold=False, italic=False, size=None, color=None):
    """Plain text with **bold**, *italic* and _sub subscripts."""
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|_[a-zA-Zτ]+)", s):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = p.add_run(part[1:-1]); r.italic = True
        elif re.fullmatch(r"_[a-zA-Zτ]+", part):
            r = p.add_run(part[1:]); r.font.subscript = True
        else:
            r = p.add_run(part)
        if bold: r.bold = True
        if italic: r.italic = True
        r.font.name = FONT
        r._element.get_or_add_rPr().get_or_add_rFonts().set(
            qn("w:eastAsia"), EA_HEAD if (ZH and (bold or r.bold)) else EA_BODY)
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = RGBColor.from_string(color)
    return p


def page_number_footer():
    p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(); r.font.name = FONT; r.font.size = Pt(10)
    for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), tag)
        else:
            el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = txt
        r._r.append(el)


def heading(s, level):
    p = doc.add_paragraph(); pf = p.paragraph_format; pf.keep_with_next = True
    if level == 2:
        pf.space_before = Pt(12); pf.space_after = Pt(5); add_runs(p, s, bold=True, size=13.5)
    else:
        pf.space_before = Pt(7); pf.space_after = Pt(3); add_runs(p, s, bold=True, size=11.5)


def picture(path, width_cm, caption=None):
    if doc.paragraphs:
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = bool(caption); p.paragraph_format.space_before = Pt(4)
    p.add_run().add_picture(path, width=Cm(width_cm))
    if caption:
        c = doc.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_runs(c, caption, italic=True, size=9.5)


def _border(parent, tag, edges):
    b = OxmlElement(tag)
    for edge, (val, sz, color) in edges.items():
        el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), val)
        if val != "nil":
            el.set(qn("w:sz"), str(sz)); el.set(qn("w:space"), "0"); el.set(qn("w:color"), color)
        b.append(el)
    parent.append(b)


def _vis_len(s):
    s = re.sub(r"\*\*|_", "", s)
    return sum(2 if "一" <= ch <= "鿿" else 1 for ch in s)


def make_table(rows, size=8.5):
    """Markdown pipe table -> three-line table; widths proportional to content."""
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows
             if not re.fullmatch(r"\|[\s\-:|]+\|", r.strip())]
    ncol = len(cells[0])
    need = [max(min(_vis_len(row[c]), 40) for row in cells) for c in range(ncol)]
    need = [max(n, 6) for n in need]
    widths = [TEXT_W * n / sum(need) for n in need]
    t = doc.add_table(rows=len(cells), cols=ncol)
    t.alignment = 1; t.autofit = False
    _border(t._tbl.tblPr, "w:tblBorders", {"top": ("single", 10, "222222"), "bottom": ("single", 10, "222222"),
                                           "left": ("nil", 0, ""), "right": ("nil", 0, ""),
                                           "insideH": ("single", 2, "C9CED3"), "insideV": ("nil", 0, "")})
    for ri, row in enumerate(cells):
        tr = t.rows[ri]; trPr = tr._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        if ri == 0:
            trPr.append(OxmlElement("w:tblHeader"))
        for ci, txt in enumerate(row):
            cell = tr.cells[ci]; cell.width = Cm(widths[ci])
            p = cell.paragraphs[0]; pf = p.paragraph_format
            pf.space_before = Pt(1); pf.space_after = Pt(1); pf.line_spacing = 1.0
            if ri == 0:
                pf.keep_with_next = True
                _border(cell._tc.get_or_add_tcPr(), "w:tcBorders", {"bottom": ("single", 6, "222222")})
            add_runs(p, txt, bold=(ri == 0), size=size)
    sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(2); sp.paragraph_format.line_spacing = 0.6


page_number_footer()

# ---- title block ----
title = next(l for l in text.splitlines() if l.startswith("# "))[2:].strip()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(8)
add_runs(p, L["title"], bold=True, size=18 if ZH else 17)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(12)
add_runs(p, title, bold=True, size=13.5)
for i, (k, v) in enumerate(INFO):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1 if i < len(INFO) - 1 else 8)
    add_runs(p, f"{k}{'：' if ZH else ': '}", bold=True); add_runs(p, v)

# ---- body ----
NUM = re.compile(r"^\((\d+)\) ")
lines = [x.rstrip() for x in text.splitlines()]
eq_n = 0; no_indent_next = False
li = 0


def next_nonempty(i):
    while i < len(lines) and not lines[i].strip():
        i += 1
    return lines[i] if i < len(lines) else ""


while li < len(lines):
    l = lines[li]; li += 1
    if l.startswith("|"):
        rows = [l]
        while li < len(lines) and lines[li].startswith("|"):
            rows.append(lines[li]); li += 1
        make_table(rows); continue
    if not l.strip() or l.startswith("# "):
        continue
    if l.startswith(L["caption"]):
        p = doc.add_paragraph(); p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(3)
        add_runs(p, l, size=10); continue
    if l.startswith("## "):
        heading(l[3:], 2); continue
    if l.startswith("### "):
        heading(l[4:], 3); continue
    m = re.fullmatch(r"\[\[FIG:\s*([^|\]]+?)\s*\|\s*([\d.]+)\s*(?:\|\s*(.+?))?\s*\]\]", l.strip())
    if m:
        picture(m.group(1), float(m.group(2)), m.group(3)); continue
    if l.startswith("EQ "):
        eq = l[3:].strip(); tail = "," if eq.endswith(",") else ("." if eq.endswith(".") else "")
        eq = eq.rstrip(",.").strip(); eq_n += 1
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
        p = doc.add_paragraph(); p.paragraph_format.keep_with_next = True
        ts = p.paragraph_format.tab_stops
        ts.add_tab_stop(Cm(TEXT_W / 2), WD_TAB_ALIGNMENT.CENTER); ts.add_tab_stop(Cm(TEXT_W), WD_TAB_ALIGNMENT.RIGHT)
        p.add_run("\t"); add_runs(p, eq, italic=True); p.add_run(f"{tail}\t({eq_n})")
        no_indent_next = True; continue
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if NUM.match(l):
        pf = p.paragraph_format
        pf.left_indent = Cm(0.9); pf.first_line_indent = Cm(-0.9); pf.keep_together = True
        if NUM.match(next_nonempty(li)):
            pf.keep_with_next = True
        n = NUM.match(l).group(0)
        add_runs(p, n.strip() + "\t" + l[len(n):]); continue
    if l.startswith(L["keywords"]):
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    elif ZH and not no_indent_next:
        p.paragraph_format.first_line_indent = Pt(22)
    no_indent_next = False
    add_runs(p, l)

# ---- references ----
heading(L["refs"], 2)
for k in order:
    p = doc.add_paragraph(); pf = p.paragraph_format
    pf.left_indent = Cm(0.8); pf.first_line_indent = Cm(-0.8); pf.tab_stops.add_tab_stop(Cm(0.8))
    pf.right_indent = Cm(0.15); pf.space_after = Pt(2); pf.line_spacing = 1.05
    add_runs(p, f"[{num[k]}]\t{REFS[k]}", size=9.5)

doc.save(a.out)
print("saved", a.out, "| refs cited:", len(order), "| equations:", eq_n)
