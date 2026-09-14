import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

urls = [
    'https://www.today-predictions.com/fixtures/2026-09-14',
    'https://www.sportinglife.com/football/fixtures-results/2026-09-14'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"URL: {url} | Length: {len(html)}")
            # print some excerpts or search for league names
            for league in ['Premier', 'La Liga', 'LaLiga', 'Serie A', 'Portugal', 'Primeira', 'Argentina', 'Colombia', 'BetPlay']:
                matches = re.findall(rf'.{{0,50}}{league}.{{0,100}}', html, re.IGNORECASE)
                if matches:
                    print(f"  Found {len(matches)} mentions of {league}")
                    for m in matches[:3]:
                        print(f"    {m.strip()}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
