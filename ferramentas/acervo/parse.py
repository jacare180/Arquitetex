import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from obras import O

def read(k):
    p = os.path.join("cache", k)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None

def infobox(text):
    """Return dict of top-level params of the first Info/Infobox template."""
    m = re.search(r"\{\{\s*(Info|Infobox|Caixa de informação)[^|}]*", text, re.I)
    if not m: return {}
    i, depth, start = m.start(), 0, m.start()
    while i < len(text):
        if text.startswith("{{", i): depth += 1; i += 2; continue
        if text.startswith("}}", i):
            depth -= 1; i += 2
            if depth == 0: break
            continue
        i += 1
    body = text[start + 2:i - 2]
    params, cur, d, dl = [], "", 0, 0
    j = 0
    while j < len(body):
        c2 = body[j:j+2]
        if c2 == "{{": d += 1; cur += c2; j += 2; continue
        if c2 == "}}": d -= 1; cur += c2; j += 2; continue
        if c2 == "[[": dl += 1; cur += c2; j += 2; continue
        if c2 == "]]": dl -= 1; cur += c2; j += 2; continue
        if body[j] == "|" and d == 0 and dl == 0: params.append(cur); cur = ""; j += 1; continue
        cur += body[j]; j += 1
    params.append(cur)
    out = {}
    for p in params[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            out[k.strip().lower().replace(" ", "_")] = v.strip()
    return out

def clean(v):
    v = re.sub(r"<ref[^>]*/>", "", v); v = re.sub(r"<ref.*?</ref>", "", v, flags=re.S)
    v = re.sub(r"<!--.*?-->", "", v, flags=re.S)
    v = re.sub(r"\{\{\s*(convert|converter|cvt)\s*\|\s*([\d.,]+)\s*\|\s*([^|}]+)[^}]*\}\}", r"\2 \3", v, flags=re.I)
    v = re.sub(r"\{\{\s*(start date|end date|start date and age|data de início|dtlink|date)[^|}]*\|\s*(\d{3,4})[^}]*\}\}", r"\2", v, flags=re.I)
    v = re.sub(r"\{\{\s*(?:ubl|unbulleted list|plainlist|flatlist|hlist|nowrap)\s*\|(.*?)\}\}", lambda m: m.group(1).replace("|", ", "), v, flags=re.I | re.S)
    v = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", v)
    v = re.sub(r"\{\{[^{}]*\}\}", "", v)
    v = re.sub(r"<br\s*/?>", ", ", v); v = re.sub(r"<[^>]+>", "", v)
    v = re.sub(r"'''?", "", v); v = re.sub(r"^\s*\*\s*", "", v, flags=re.M)
    v = re.sub(r"\s+", " ", v).strip(" ,;")
    return v

KEYS = {
 "ano": ["inauguração_data","data_inauguração","construção_fim","data_término","fim_constr","completed","complete","years_built","construção_data","data_da_construção","open","abertura","consecration_year","built","data","completion_date","completed","opening","opened","opened_date","inauguration_date","inauguração","inaugurado","conclusão","date_built","built","construction_end_date","year_completed","completion","período_construção","construção","início_construção","date_opened","established","fundação","fundado"],
 "altura": ["height_max","architectural","height","altura","roof","telhado","tip","antenna_spire","pináculo"],
 "andares": ["número_andares","floor_count","floors","andares","contagem_andares","número_de_andares"],
 "area": ["área_m2","floor_area","área_construída","área","area","size"],
 "arquiteto": ["arquitecto","autor","ren_architect","construtor","architect","arquiteto","arquitetos","arquitetura","architecture_firm","designer","architects","projeto","engineer"],
 "estilo": ["estilo_arquitetônico","estilos","architecture_style","architectural_style","style","estilo","estilo_arquitetônico","architecture"],
}
def pick(ib, field):
    for k in KEYS[field]:
        if k in ib and clean(ib[k]):
            return k, clean(ib[k])
    return None, ""

def views(oid):
    tot = 0
    for lang in ("pt", "en"):
        s = read(f"{oid}.{lang}.views")
        if s:
            try: tot += sum(i["views"] for i in json.loads(s)["items"])
            except Exception: pass
    return tot

rows = []
for o in O:
    oid, nome, cidade, pais, tipo, tpt, ten, prim = o
    r = {"id": oid, "nome": nome}
    for lang in ([prim] + [l for l in ("pt","en") if l != prim]):
        raw = read(f"{oid}.{lang}.raw")
        if raw is None: continue
        ib = infobox(raw)
        for f in KEYS:
            if not r.get(f):
                k, v = pick(ib, f)
                if v: r[f] = v; r[f + "_src"] = lang + ":" + k
        s = read(f"{oid}.{lang}.summary")
        if s and "url_" + lang not in r:
            j = json.loads(s); r["url_" + lang] = j["content_urls"]["desktop"]["page"]; r["extract_" + lang] = j.get("extract", "")
    r["views"] = views(oid)
    rows.append(r)
json.dump(rows, open("parsed.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if __name__ == '__main__':
  for r in rows:
    print(r["id"], "|", r.get("ano",""), "|", r.get("altura",""), "|", r.get("andares",""), "|", r.get("area",""), "|", r.get("arquiteto","")[:60], "|", r.get("estilo","")[:30], "|", r["views"])
