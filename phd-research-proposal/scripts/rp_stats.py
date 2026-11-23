"""Length and consistency report for a proposal draft.

Usage: python3 rp_stats.py rp.md [--terms terms.json]
Prints: body word count (English words, or Chinese characters + English words for zh drafts),
words per section, number of distinct citations, and, if a terms file is given, every place where a
banned variant of a term still appears.

terms.json maps the chosen term to its banned variants, e.g.
{"explicit wall function": ["closure", "wall law"], "held-out surface family": ["unseen surface families"]}
"""
import json, re, sys

src = sys.argv[1]
text = open(src, encoding="utf-8").read()
text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
cites = set(re.findall(r"\{([A-Za-z0-9_\-]+)\}", text))
plain = re.sub(r"\{[A-Za-z0-9_\-]+\}", "", text)


def count(s):
    zh = len(re.findall(r"[一-鿿]", s))
    en = len(re.findall(r"[A-Za-z0-9ΔκδτÀ-ž⁺_'’\-]+", re.sub(r"[一-鿿]", " ", s)))
    return zh, en


zh, en = count(plain)
print(f"total: {en} English words" + (f" + {zh} Chinese characters" if zh else ""))
print(f"distinct citations: {len(cites)}\n")
sections = re.split(r"^(#{2,3} .+)$", plain, flags=re.M)
for i in range(1, len(sections), 2):
    z, e = count(sections[i + 1])
    print(f"  {sections[i][:48]:<50} {e:>5} w" + (f" {z:>5} 字" if z else ""))

if "--terms" in sys.argv:
    terms = json.load(open(sys.argv[sys.argv.index("--terms") + 1], encoding="utf-8"))
    print("\nterm consistency:")
    hits = 0
    for keep, banned in terms.items():
        for b in banned:
            for m in re.finditer(re.escape(b), plain, flags=re.I):
                line = plain.count("\n", 0, m.start()) + 1
                ctx = plain[max(0, m.start() - 40): m.end() + 40].replace("\n", " ")
                print(f"  line {line}: '{b}' -> use '{keep}': ...{ctx}...")
                hits += 1
    print(f"  {hits} variant(s) found" if hits else "  no banned variants")
