import os, re, sys, time, subprocess, urllib.parse, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from obras import O
UA = "Arquitetex/0.1 (https://github.com/jacare180/arquitetex)"
q = lambda t: urllib.parse.quote(t.replace(" ", "_"), safe="")
def curl(url):
    for attempt in range(10):
        r = subprocess.run(["curl", "-sS", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code in ("200", "404"): return code, body
        print("retry", code, url, flush=True); time.sleep(min(60, 6 * (attempt + 1)))
    return None, None
titles = {}
for o in O:
    oid = o[0]
    for lang, t in (("pt", o[5]), ("en", o[6])):
        if not t: continue
        path = f"cache/{oid}.{lang}.raw"
        title = t
        for hop in range(3):
            if os.path.exists(path) and hop == 0:
                body = open(path, encoding="utf-8").read()
            else:
                code, body = curl(f"https://{lang}.wikipedia.org/w/index.php?title={q(title)}&action=raw")
                if code != "200": body = ""
                time.sleep(0.3)
            m = re.match(r"\s*#(REDIRECT|REDIRECIONAMENTO)\s*\[\[([^\]#|]+)", body, re.I)
            if m: title = m.group(2).strip(); os.path.exists(path) and os.remove(path); continue
            break
        if body: open(path, "w", encoding="utf-8").write(body); titles[f"{oid}.{lang}"] = title
        else: print("MISSING", oid, lang, t, flush=True)
    print("ok", oid, flush=True)
json.dump(titles, open("titles.json", "w"), ensure_ascii=False, indent=1)
print("DONE", flush=True)
