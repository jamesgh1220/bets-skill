"""Fetch current-season xG per team (Understat 2026) and Elo (ClubElo ranking)."""
import json, os, re, gzip, zlib, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

US = {"EPL": "England Premier League", "La_liga": "Spain La Liga",
      "Bundesliga": "Germany Bundesliga", "Serie_A": "Italy Serie A",
      "Ligue_1": "France Ligue 1"}


def us_league(code, year):
    url = f"https://understat.com/getLeagueData/{code}/{year}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://understat.com/league/{code}/{year}",
        "Accept-Encoding": "gzip"})
    raw = urllib.request.urlopen(req, timeout=40).read()
    for dec in (gzip.decompress, zlib.decompress):
        try:
            return json.loads(dec(raw).decode())
        except Exception:
            pass
    raise RuntimeError("decode failed " + code)


teams = {}
for code, label in US.items():
    try:
        d = us_league(code, 2026)
    except Exception as e:
        print("ERR", code, e); continue
    for t in d.get("teams", {}).values():
        h = t.get("history", [])
        if not h:
            continue
        n = len(h)
        teams[t["title"]] = {
            "league": label, "understat": code, "matches": n,
            "xg_for": round(sum(float(m["xG"]) for m in h) / n, 3),
            "xg_against": round(sum(float(m["xGA"]) for m in h) / n, 3),
            "goals_for": round(sum(int(m["scored"]) for m in h) / n, 3),
            "goals_against": round(sum(int(m["missed"]) for m in h) / n, 3),
            "pts": sum(int(m["pts"]) for m in h),
        }
    print(f"{label:26s} teams={len(d.get('teams', {}))}")

with open(os.path.join(HERE, "understat_2026.json"), "w") as f:
    json.dump(teams, f, ensure_ascii=False, indent=1)
print("understat teams total:", len(teams))

# ---- ClubElo ----
req = urllib.request.Request("http://clubelo.com/Ranking",
                             headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
rows = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S)
elo = {}
for r in rows:
    cells = [re.sub(r"<[^>]+>", " ", c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
    cells = [re.sub(r"\s+", " ", c).strip() for c in cells]
    if len(cells) < 2:
        continue
    name_raw = cells[0]
    val = cells[-1]
    if not re.fullmatch(r"\d{3,4}", val or ""):
        continue
    # name like "2045  ARSArsenal" -> split "ARSArsenal"
    nm = re.split(r"\d+\s+", name_raw)[-1]
    nm = re.sub(r"^[A-Z]{2,4}(?=[A-Z][a-z])", "", nm)  # strip 3-letter prefix
    elo[nm.strip()] = int(val)
with open(os.path.join(HERE, "clubelo.json"), "w") as f:
    json.dump(elo, f, ensure_ascii=False, indent=1)
print("clubelo clubs:", len(elo))
print("samples:", {k: elo[k] for k in list(elo)[:5]})
