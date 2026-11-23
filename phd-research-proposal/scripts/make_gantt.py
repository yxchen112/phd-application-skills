"""Plain Gantt chart for a research proposal (month grid, light-blue rounded bars, no milestones).

Usage: python3 make_gantt.py gantt.json
gantt.json:
{
  "lang": "en",                 # "en" -> M1..M12 header, "zh" -> 1月..12月
  "months": 12,
  "out": "fig_gantt.png",
  "tasks": [
    {"label": "Step 1: solver validation; pilot at Re$_\\tau$ = 180", "start": 1, "end": 3},
    {"label": "Manuscript writing", "start": 10, "end": 12}
  ]
}
start/end are inclusive month numbers. Inline math such as Re$_\\tau$ may sit next to Chinese text:
labels are drawn piece by piece, so CJK glyphs never go through mathtext.
The label column is sized from the longest label, so labels never run into the month grid.
"""
import json, re, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

spec = json.load(open(sys.argv[1], encoding="utf-8"))
ZH = spec.get("lang", "en") == "zh"
from matplotlib import font_manager
_have = {f.name for f in font_manager.fontManager.ttflist}
_cjk = [f for f in ("SimSong", "Songti SC", "STSong", "Heiti SC", "PingFang SC", "Noto Serif CJK SC") if f in _have]
plt.rcParams["font.family"] = [f for f in ("Times New Roman",) if f in _have] + _cjk[:1] or ["serif"]
plt.rcParams["mathtext.fontset"] = "stix"
INK, LINE, BAR = "#222222", "#B8C2CC", "#7FA8D6"
FS = 9.6
ncol = int(spec.get("months", 12))
tasks = spec["tasks"]
nrow, top = len(tasks), 1.0


def pieces(label):
    return [p for p in re.split(r"(\$[^$]+\$)", label) if p]


def draw(label_w, measure_only=False):
    fig, ax = plt.subplots(figsize=(8.2, 0.35 * (nrow + 1) + 0.35), dpi=300)
    ax.set_xlim(-label_w, ncol); ax.set_ylim(top + nrow + 0.02, -0.02); ax.axis("off")
    renderer = fig.canvas.get_renderer(); inv = ax.transData.inverted()
    widest = 0.0
    for r, t in enumerate(tasks):
        x = -label_w + 0.15; yc = top + r + 0.5
        for pc in pieces(t["label"]):
            txt = ax.text(x, yc, pc, ha="left", va="center", fontsize=FS, color=INK)
            bb = txt.get_window_extent(renderer=renderer)
            x0, _ = inv.transform((bb.x0, bb.y0)); x1, _ = inv.transform((bb.x1, bb.y0))
            x += x1 - x0
        widest = max(widest, x - (-label_w))
    if measure_only:
        plt.close(fig); return widest
    for c in range(ncol + 1):
        ax.plot([c, c], [0, top + nrow], color=LINE, lw=0.7)
    ax.plot([-label_w, -label_w], [0, top + nrow], color=LINE, lw=0.7)
    for r in range(nrow + 1):
        ax.plot([-label_w, ncol], [top + r, top + r], color=LINE, lw=0.7)
    ax.plot([-label_w, ncol], [0, 0], color=LINE, lw=0.7)
    ax.text(-label_w / 2, top / 2, "任务" if ZH else "Task", ha="center", va="center",
            fontsize=10.5, color=INK, weight="normal" if ZH else "bold")
    for m in range(ncol):
        ax.text(m + 0.5, top / 2, f"{m + 1}月" if ZH else f"M{m + 1}", ha="center", va="center",
                fontsize=8.3 if ZH else 8.8, color=INK, weight="normal" if ZH else "bold")
    for r, t in enumerate(tasks):
        a, b = t["start"] - 1, t["end"]
        yc = top + r + 0.5
        ax.add_patch(FancyBboxPatch((a + 0.1, yc - 0.2), b - a - 0.2, 0.4,
                                    boxstyle="round,pad=0,rounding_size=0.18", fc=BAR, ec="none", zorder=3))
    out = spec.get("out", "fig_gantt_zh.png" if ZH else "fig_gantt.png")
    plt.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.04)
    plt.close(fig)
    return out


# two passes: measure the widest label, then size the label column to fit it
lw = 10.0
for _ in range(3):
    need = draw(lw, measure_only=True) + 0.7
    if abs(need - lw) < 0.05:
        break
    lw = need
print("saved", draw(lw), "| label column", round(lw, 2), "months wide")
