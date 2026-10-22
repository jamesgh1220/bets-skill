"""Parse Wikipedia league tables (GF/GA) for Eredivisie, MLS and Argentina 2026."""
import json, os, re
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = {
    "Eredivisie": "/tmp/wiki_2026%E2%80%9327_Eredivisie.html",
    "MLS": "/tmp/wiki_2026_Major_League_Soccer_season.html",
    "ARG": "/tmp/wiki_2026_Argentine_Primera_Divisi%C3%B3n.html",
}


def parse(path):
    soup = BeautifulSoup(open(path, encoding="utf-8", errors="ignore").read(), "html.parser")
    tables = []
    for tbl in soup.find_all("table"):
        head = tbl.find("tr")
        if not head:
            continue
        cols = [re.sub(r"\s+", " ", c.get_text(" ", strip=True)) for c in head.find_all(["th", "td"])]
        if not any(c in ("GF", "GA") for c in cols):
            continue
        idx = {c: i for i, c in enumerate(cols)}
        team_i = idx.get("Team", idx.get("Team v t e", 1))
        rows = []
        for tr in tbl.find_all("tr")[1:]:
            cells = [re.sub(r"\s+", " ", c.get_text(" ", strip=True)) for c in tr.find_all(["td", "th"])]
            if len(cells) < idx["GA"] + 1:
                continue
            try:
                team = re.sub(r"\s*\([^)]*\)\s*$", "", cells[team_i]).strip()
                team = re.sub(r"\s*v t e$", "", team).strip()
                gf = int(re.sub(r"\D", "", cells[idx["GF"]]))
                ga = int(re.sub(r"\D", "", cells[idx["GA"]]))
                pld = int(re.sub(r"\D", "", cells[idx["Pld"]])) if "Pld" in idx else None
            except Exception:
                continue
            rows.append({"team": team, "pld": pld, "gf": gf, "ga": ga})
        if rows:
            tables.append({"cols": cols, "rows": rows})
    return tables


out = {}
for name, path in PAGES.items():
    tables = parse(path)
    print(f"== {name}: {len(tables)} candidate tables ==")
    for t in tables[:6]:
        print("   cols:", t["cols"], "rows:", len(t["rows"]), "sample:", t["rows"][0])
    out[name] = tables
with open(os.path.join(HERE, "wiki_tables.json"), "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
