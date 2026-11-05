"""Gera os arquivos que o jogo lê (dados/achado.json e dados/acervo.json) a partir das saídas das ferramentas.
Rodar da raiz do repositório: python3 ferramentas/gerar_dados.py"""
import csv, json, re, os
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Achado: uma entrada por pergunta, com as respostas e as grafias aceitas.
perguntas = {}
with open(os.path.join(RAIZ, "ferramentas/achado/achado.csv"), encoding="utf-8") as f:
    for linha in csv.reader(f):
        cid, pergunta, _recorte, resposta, grafias, faixa = linha[:6]
        p = perguntas.setdefault(cid, {"id": cid, "pergunta": pergunta, "respostas": []})
        p["respostas"].append({"r": resposta, "g": [g.strip() for g in grafias.split(";") if g.strip()], "f": faixa})
json.dump(list(perguntas.values()), open(os.path.join(RAIZ, "dados/achado.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

# Acervo: obras com os números que a Escala usa e as grafias para o formato Alvo.
acervo = json.load(open(os.path.join(RAIZ, "ferramentas/acervo/acervo.json"), encoding="utf-8"))
obras = []
for a in acervo:
    grafias = set()
    sem_parenteses = re.sub(r"\s*\([^)]*\)", "", a["nome"]).strip()
    if sem_parenteses != a["nome"]: grafias.add(sem_parenteses)
    for m in re.findall(r"\(([^)]*)\)", a["nome"]): grafias.add(m)
    titulo = a["fonte"].rsplit("/wiki/", 1)[1].replace("_", " ")
    from urllib.parse import unquote
    titulo = unquote(titulo)
    if titulo != a["nome"]: grafias.add(re.sub(r"\s*\([^)]*\)", "", titulo))
    obras.append({"id": a["id"], "nome": a["nome"], "g": sorted(grafias), "cidade": a["cidade"], "pais": a["pais"],
                  "arq": a["arquitetos"], "ano": a["ano"], "altura": a["altura"], "fonte": a["fonte"]})
json.dump(obras, open(os.path.join(RAIZ, "dados/acervo.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(perguntas), "perguntas do Achado;", len(obras), "obras no acervo")
