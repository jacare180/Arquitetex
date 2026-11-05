"""Acesso à Wikipedia com cache: texto bruto (segue redirecionamentos) e visualizações dos últimos 30 dias."""
import os, re, json, time, subprocess, urllib.parse, unicodedata, html
UA = "Arquitetex/0.1 (https://github.com/jacare180/arquitetex)"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(CACHE, exist_ok=True)
q = lambda t: urllib.parse.quote(t.replace(" ", "_"), safe="")

def _curl(url):
    for attempt in range(8):
        r = subprocess.run(["curl", "-sS", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code in ("200", "404"): return code, body
        time.sleep(min(60, 5 * (attempt + 1)))
    return None, ""

def _cached(key, fn):
    path = os.path.join(CACHE, re.sub(r"[^\w.-]", "_", key)[:180] + ".json")
    if os.path.exists(path): return json.load(open(path, encoding="utf-8"))
    val = fn()
    json.dump(val, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    return val

def page(lang, title):
    """{'title': canonical, 'text': wikitext} ou None."""
    def go():
        t = title
        for _ in range(4):
            code, body = _curl(f"https://{lang}.wikipedia.org/w/index.php?title={q(t)}&action=raw")
            time.sleep(0.25)
            if code != "200" or not body.strip(): return None
            m = re.match(r"\s*#(REDIRECT|REDIRECIONAMENTO)\s*\[\[([^\]#|]+)", body, re.I)
            if m: t = m.group(2).strip(); continue
            if re.search(r"\{\{\s*(desambiguação|disambiguation|desambig|dab|hndis)\b", body[:3000] + body[-2000:], re.I): return {"title": t, "text": body, "desambig": True}
            return {"title": t, "text": body}
        return None
    return _cached(f"raw.{lang}.{title}", go)

def views30(lang, title):
    def go():
        code, body = _curl(f"https://{lang}.wikipedia.org/w/index.php?title={q(title)}&action=info")
        time.sleep(0.25)
        m = re.search(r'mw-pvi-month">.*?>([\d\s., ]+|&#160;|[\d&#;]+)</a>', body or "", re.S)
        if not m: return 0
        return int(re.sub(r"\D", "", html.unescape(m.group(1))) or 0)
    return _cached(f"views.{lang}.{title}", go)

def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")

def url(lang, title):
    return f"https://{lang}.wikipedia.org/wiki/" + title.replace(" ", "_")
