"""Check every reference against Crossref (DOI) or arXiv (arXiv ID).

Usage: python3 verify_refs.py refs.py [--only-cited rp.md]
For each entry it reports: OK / CHECK (title or year differs) / NO-ID (no DOI or arXiv ID to check)
/ FAIL (DOI not found). A CHECK is not necessarily wrong (e.g. capitalisation, subtitle) but must be
looked at by hand. This verifies that the record exists and matches; it does NOT verify that the paper
says what the proposal claims it says. Claim-level checks need the abstract or full text.
"""
import json, re, runpy, sys, time, urllib.request, urllib.parse
from difflib import SequenceMatcher

UA = {"User-Agent": "rp-reference-check/1.0"}
src = sys.argv[1]
REFS = json.load(open(src, encoding="utf-8")) if src.endswith(".json") else runpy.run_path(src)["REFS"]
keys = list(REFS)
if "--only-cited" in sys.argv:
    md = open(sys.argv[sys.argv.index("--only-cited") + 1], encoding="utf-8").read()
    cited = []
    for k in re.findall(r"\{([A-Za-z0-9_\-]+)\}", md):
        if k not in cited:
            cited.append(k)
    keys = [k for k in cited if k in REFS]
    missing = [k for k in cited if k not in REFS]
    if missing:
        print("MISSING KEYS in refs:", missing)


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8")


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower())


def ref_title(ref):
    m = re.search(r"\(\d{4}[a-z]?\)\.\s*(.+?)\.\s", ref)
    return m.group(1) if m else ref[:120]


def ref_year(ref):
    m = re.search(r"\((\d{4})", ref)
    return m.group(1) if m else ""


rows = []
for k in keys:
    ref = REFS[k]
    doi = re.search(r"10\.\d{4,9}/[^\s,;]+", ref)
    arx = re.search(r"arXiv[:\s]*(\d{4}\.\d{4,5})", ref)
    try:
        if doi:
            d = doi.group(0).rstrip(".")
            msg = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(d)))["message"]
            title = (msg.get("title") or [""])[0]
            years = set()
            for f in ("issued", "published-print", "published-online", "published"):
                dp = (msg.get(f, {}) or {}).get("date-parts") or [[None]]
                if dp[0][0]:
                    years.add(str(dp[0][0]))
            ji = (msg.get("journal-issue", {}) or {}).get("published-print", {}).get("date-parts") or [[None]]
            if ji[0][0]:
                years.add(str(ji[0][0]))
            year = "/".join(sorted(years))
            sim = SequenceMatcher(None, norm(title), norm(ref_title(ref))).ratio()
            status = "OK" if sim > 0.85 and ref_year(ref) in years else "CHECK"
            rows.append((k, status, f"sim={sim:.2f} year={year}", title[:90]))
        elif arx:
            xml = get("http://export.arxiv.org/api/query?id_list=" + arx.group(1))
            t = re.findall(r"<title>(.*?)</title>", xml, re.S)
            title = re.sub(r"\s+", " ", t[1]) if len(t) > 1 else ""
            sim = SequenceMatcher(None, norm(title), norm(ref_title(ref))).ratio()
            rows.append((k, "OK" if sim > 0.85 else "CHECK", f"sim={sim:.2f} arXiv", title[:90]))
        else:
            rows.append((k, "NO-ID", "", ref[:90]))
    except Exception as e:
        rows.append((k, "FAIL", type(e).__name__, ref[:90]))
    time.sleep(0.3)

w = max(len(r[0]) for r in rows) if rows else 10
for r in rows:
    print(f"{r[0]:<{w}}  {r[1]:<6} {r[2]:<22} {r[3]}")
bad = [r for r in rows if r[1] != "OK"]
print(f"\n{len(rows)} checked, {len(rows) - len(bad)} OK, {len(bad)} need a look")
