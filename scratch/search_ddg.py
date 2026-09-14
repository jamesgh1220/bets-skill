import urllib.request
import urllib.parse
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8'
}

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract snippets
            snippets = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL)
            titles = re.findall(r'<a class="result__url"[^>]*>(.*?)</a>', html, re.DOTALL)
            print(f"Results for '{query}': {len(snippets)} snippets found")
            for t, s in zip(titles[:5], snippets[:5]):
                clean_s = re.sub(r'<[^>]+>', '', s).strip()
                clean_t = re.sub(r'<[^>]+>', '', t).strip()
                print(f"  [{clean_t}] {clean_s}\n")
    except Exception as e:
        print(f"Error DDG search '{query}': {e}")

search_ddg("partidos 14 de septiembre 2026 premier league laliga serie a liga colombiana liga argentina")
search_ddg("fixtures 14 september 2026 football matches")
search_ddg("partidos de futbol 14 septiembre 2026 betplay espana italia argentina portugal premier")
