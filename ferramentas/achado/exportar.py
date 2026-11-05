"""Junta as saídas e gera as linhas da aba Achado (JSON pronto para a planilha)."""
import json, glob, os, urllib.parse
import wiki
acervo = json.load(open(os.path.join(os.path.dirname(__file__), "..", "acervo", "acervo.json"), encoding="utf-8"))
por_titulo = {}
for a in acervo:
    t = urllib.parse.unquote(a["fonte"].rsplit("/wiki/", 1)[1]).replace("_", " ")
    por_titulo[t] = a["id"]
saidas = {}
for f in sorted(glob.glob("saida_cat_*.json")):
    saidas.update(json.load(open(f, encoding="utf-8")))
rows = []
for cid in sorted(saidas):
    s = saidas[cid]
    for x in s["linhas"]:
        obra = por_titulo.get(x["titulo"], "")
        fonte = wiki.url(x["lang"], x["titulo"])
        rows.append([cid, s["pergunta"], "", x["nome"], "; ".join(dict.fromkeys(x["grafias"])), x["faixa"], None, obra, fonte, f"pt {x['vpt']}; en {x['ven']}"])
json.dump(rows, open("linhas_achado.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(rows), "linhas,", len(saidas), "categorias")
