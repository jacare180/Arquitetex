"""Monta as respostas do Achado: resolve cada candidata na Wikipedia, confere a categoria e define a faixa."""
import re, sys, json, importlib
import wiki
FAIXAS = [(0.10, "Cartão-postal"), (0.30, "Clássico"), (0.60, "Repertório"), (0.85, "Arquivo"), (1.01, "Achado")]
FATOR_EN = 0.12     # pessoas: peso das visualizações em inglês somadas às em português
FATOR_SO_EN = 0.05  # sem página em português: visualizações em inglês x este fator

def parse_linha(l):
    nome, _, extras = l.partition("|")
    nome, _, alvo = nome.partition("=")
    grafias = [g.strip() for g in extras.split(";") if g.strip()]
    return nome.strip(), alvo.strip(), grafias

def resolver(nome, alvo):
    if alvo.startswith("@en:"):
        return "en", wiki.page("en", alvo[4:])
    p = wiki.page("pt", alvo or nome)
    if p and not p.get("desambig"): return "pt", p
    p2 = wiki.page("en", alvo or nome)
    if p2 and not p2.get("desambig"): return "en", p2
    return None, None

def montar(cid, d):
    vistos, titulos, linhas, falhas = set(), set(), [], []
    for l in d["respostas"].strip().splitlines():
        if not l.strip(): continue
        nome, alvo, grafias = parse_linha(l)
        if nome in vistos: continue
        vistos.add(nome)
        lang, p = resolver(nome, alvo)
        if not p: falhas.append((nome, "sem página")); continue
        if p["title"] in titulos: continue
        titulos.add(p["title"])
        texto = wiki.fold(p["text"][:8000] if d.get("lead", True) else p["text"])
        if not re.search(d["verifica"], texto): falhas.append((nome, "não confirma: " + d["verifica"])); continue
        if lang == "pt":
            vpt = wiki.views30("pt", p["title"])
            pen = wiki.page("en", alvo or nome) if d.get("tipo") == "pessoa" else None
            ok_en = pen and not pen.get("desambig") and re.search(d["verifica"], wiki.fold(pen["text"][:8000]))
            ven = wiki.views30("en", pen["title"]) if ok_en else 0
        else:
            vpt, ven = 0, wiki.views30("en", p["title"])
        v = vpt + ven
        peso = vpt + ven * FATOR_EN if vpt else ven * FATOR_SO_EN
        titulo = re.sub(r"\s*\([^)]*\)$", "", p["title"])
        if wiki.fold(titulo) != wiki.fold(nome) and titulo not in grafias: grafias.append(titulo)
        linhas.append(dict(nome=nome, grafias=grafias, lang=lang, titulo=p["title"], views=v, vpt=vpt, ven=ven, peso=peso))
    linhas.sort(key=lambda x: -x["peso"])
    n = len(linhas)
    for i, x in enumerate(linhas):
        frac = (i + 0.5) / n
        x["faixa"] = next(f for lim, f in FAIXAS if frac < lim)
    for f in d.get("fixar", {}):
        for x in linhas:
            if x["nome"] == f: x["faixa"] = d["fixar"][f]
    return linhas, falhas

if __name__ == "__main__":
    mod = importlib.import_module(sys.argv[1])
    out = {}
    for cid, d in mod.C.items():
        linhas, falhas = montar(cid, d)
        out[cid] = dict(pergunta=d["pergunta"], linhas=linhas)
        print(f"\n## {cid} {d['pergunta']}: {len(linhas)} respostas, {len(falhas)} falhas")
        for x in linhas: print(f"  {x['faixa'][:5]:5} {x['peso']:>7.0f} pt{x['vpt']:>6} en{x['ven']:>7} {x['nome']}  [{x['titulo']}]")
        for f in falhas: print("  FALHA", *f)
    json.dump(out, open(f"saida_{sys.argv[1]}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
