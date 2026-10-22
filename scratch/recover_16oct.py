"""Recupera los resultados de los 6 subagentes explore de la sesion 2026-10-16
desde la base SQLite de opencode (session_message) y los vuelca a scratch/recovered/.
Solo lectura sobre la base; escritura solo en scratch/recovered/.
"""
import json
import os
import sqlite3

DB = os.path.expanduser("~/.local/share/opencode/opencode.db")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recovered")

SESSIONS = {
    "stats_argentina": "ses_ebb3effd5ffdDoJ6qPOAHWYrxZ",
    "stats_ligue1_eredivisie": "ses_ebb3effd5ffeVN4rdUg6JksxzD",
    "stats_bundesliga_seriea_laliga": "ses_ebb3effd6ffeonLmDnQJC7ejj3",
    "odds_ladders_7": "ses_ebb3effcfffeqo8D4rs0w9o7Em",
    "cerrar_ligue1": "ses_ebb2aec54ffehDMB2UpPWMS0Ss",
    "lineas_ou_corners": "ses_ebb2aec53ffeEFPbOTfqlagKD0",
}

os.makedirs(OUT, exist_ok=True)
con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
cur = con.cursor()

for name, sid in SESSIONS.items():
    rows = cur.execute(
        "SELECT seq, data FROM session_message WHERE session_id=? AND type='assistant' ORDER BY seq",
        (sid,),
    ).fetchall()
    texts = []
    for seq, data in rows:
        try:
            payload = json.loads(data)
        except Exception:
            continue
        content = payload.get("content") or []
        chunk = "\n".join(
            c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"
        )
        if chunk.strip():
            texts.append((seq, chunk))

    with open(os.path.join(OUT, f"{name}__final.txt"), "w", encoding="utf-8") as f:
        f.write(texts[-1][1] if texts else "")
    with open(os.path.join(OUT, f"{name}__all.txt"), "w", encoding="utf-8") as f:
        for seq, chunk in texts:
            f.write(f"\n\n===== seq {seq} =====\n")
            f.write(chunk)

    print(f"{name}: {len(rows)} assistant msgs, {len(texts)} with text; "
          f"final={len(texts[-1][1]) if texts else 0} chars")

con.close()
