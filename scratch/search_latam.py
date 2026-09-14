import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            snippets = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL)
            titles = re.findall(r'<a class="result__title"[^>]*>(.*?)</a>', html, re.DOTALL)
            print(f"Results for '{query}': {len(snippets)} snippets found")
            for t, s in zip(titles[:10], snippets[:10]):
                clean_s = re.sub(r'<[^>]+>', '', s).strip()
                clean_t = re.sub(r'<[^>]+>', '', t).strip()
                print(f"  Title: {clean_t}\n  Snippet: {clean_s}\n")
    except Exception as e:
        print(f"Error DDG search '{query}': {e}")

search_ddg("partidos 14 septiembre 2026 liga argentina LPF")
search_ddg("partidos 14 septiembre 2026 liga colombiana betplay")
search_ddg("fixtures 2026-09-14 Liga Profesional Argentina")
search_ddg("fixtures 2026-09-14 Liga BetPlay")
