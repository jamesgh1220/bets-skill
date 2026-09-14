import urllib.request
import json
import time

dates = ["20260912", "20260913", "20260914", "20260919", "20260920"]

leagues_of_interest = {
    "england": ["premier league"],
    "spain": ["laliga", "primera division"],
    "italy": ["serie a"],
    "germany": ["bundesliga"],
    "france": ["ligue 1"],
    "holland": ["eredivisie"],
    "portugal": ["primeira liga", "liga portugal"],
    "usa": ["mls", "major league soccer"],
    "argentina": ["liga profesional"],
    "colombia": ["liga betplay", "primera a"]
}

headers = {'User-Agent': 'Mozilla/5.0'}

print("=== VERIFICACIÓN DETALLADA DE DÍAS Y LIGAS ===")

for dt in dates:
    formatted_date = f"{dt[:4]}-{dt[4:6]}-{dt[6:]}"
    url = f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{dt}/0?MD=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            stages = data.get("Stages", [])
            print(f"\n==================== FECHA: {formatted_date} ====================")
            matches_found_today = 0
            for st in stages:
                ccode = str(st.get("Ccd", "")).lower()
                cname = str(st.get("Cname", "")).lower()
                sname = str(st.get("Snm", "")).lower()
                league_full = f"{ccode} - {cname} - {sname}"
                
                # Check if it matches top tier league
                is_target = False
                for country, kw_list in leagues_of_interest.items():
                    if country in ccode or country in cname:
                        for kw in kw_list:
                            if kw in sname or kw in cname:
                                is_target = True
                                break
                
                if is_target:
                    events = st.get("Events", [])
                    matches_found_today += len(events)
                    print(f"  [{st.get('Cname')} - {st.get('Snm')}] ({len(events)} partidos):")
                    for ev in events:
                        t1 = ev.get("T1", [{}])[0].get("Nm", "Home")
                        t2 = ev.get("T2", [{}])[0].get("Nm", "Away")
                        time_val = ev.get("Esd", "")
                        print(f"     * {t1} vs {t2} (UTC: {time_val})")
            if matches_found_today == 0:
                print("  (Ningún partido de 1ª división en las 10 ligas objetivo)")
    except Exception as e:
        print(f"Error fetching {dt}: {e}")
    time.sleep(0.5)
