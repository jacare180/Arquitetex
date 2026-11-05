import os, sys, time, subprocess, urllib.parse, json
UA = "Arquitetex/0.1 (https://github.com/jacare180/arquitetex)"
q = lambda t: urllib.parse.quote(t.replace(" ", "_"), safe="")
titles = json.load(open("titles.json"))
for key, title in titles.items():
    path = f"cache/{key}.views"
    if os.path.exists(path) and os.path.getsize(path) > 0: continue
    lang = key.rsplit(".", 1)[1]
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{lang}.wikipedia/all-access/user/{q(title)}/monthly/20251101/20261031"
    for attempt in range(12):
        r = subprocess.run(["curl", "-sS", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code in ("200", "404"):
            open(path, "w", encoding="utf-8").write(body if code == "200" else ""); break
        time.sleep(min(90, 10 * (attempt + 1)))
    time.sleep(2)
    print("ok", key, flush=True)
print("DONE", flush=True)
