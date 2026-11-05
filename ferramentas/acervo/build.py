import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from obras import O
from parse import read, clean
import overrides as OV
P = {r["id"]: r for r in json.load(open("parsed.json", encoding="utf-8"))}
titles = json.load(open("titles.json", encoding="utf-8"))

# Correções verificadas no texto das páginas (ver conversa).
ANO = {"museu-republica":2006,"mon":2002,"opera-arame":1992,"sesc-pompeia":1982,"teatro-oficina":1994,"museu-amanha":2015,
 "mar-rio":2013,"pedregulho":1952,"real-gabinete":1887,"maracana":1950,"vasconcelos":2006,"biblioteca-unam":1956,"twa":1962,
 "unite":1952,"batllo":1906,"mila":1912,"guggenheim-bilbao":1997,"alhambra":1354,"bauhaus":1926,"torre-einstein":1921,"vals":1996,
 "rotonda":1605,"tate-modern":2000,"barbican":1976,"mairea":1939,"skogskyrkogarden":1920,"opera-sydney":1973,"igreja-luz":1989,
 "angkor":1150,"masp":1968,"partenon":-432,"giza":-2560,"coliseu":80,"fallingwater":1937,"one-wtc":2014,"santa-sofia":537,
 "cidade-proibida":1420,"djenne":1907,"taipei-101":2004,"valencia":2009,"grundtvig":1940,"catedral-rio":1979,"marina-bay":2010,
 "petronas":1999,"merdeka-118":2023,"skytree":2012,"lotus":1986,"ponte-jk":2002,"ponte-estaiada":2008,"museu-ipiranga":1895,
 "pinacoteca":1905,"chartres":1252,"notre-dame":1345,"versalhes":None,"chandigarh":None,"sagrada-familia":None,"colonia":1880}
NAO_ANO = {"versalhes","chandigarh","sagrada-familia"}
ALTURA = {"giza":146.6,"cristo":38,"bosco-verticale":116,"ponte-jk":60,"kavanagh":120,"teatro-amazonas":None,"partenon":13.72}
AREA_FORA = {"mube","teatro-amazonas","twa","robie","rotonda","skogskyrkogarden","chandigarh","taj-mahal","cidade-proibida","partenon","abraj-al-bait","shanghai-tower"}
AREA = {"abraj-al-bait":310638,"shanghai-tower":380000,"batllo":3100,"lotus":None}
ANDARES_FORA = {"cn-tower","eiffel","congresso","skytree"}

def ano(oid, r):
    if oid in ANO: return ANO[oid]
    v = r.get("ano", "")
    bc = re.search(r"(\d{3,4})\s*(BC|a\.?C)", v)
    if bc: return -int(bc.group(1))
    ys = [int(y) for y in re.findall(r"(?<!\d)(\d{4})(?!\d)", v) if 1000 <= int(y) <= 2026]
    if ys: return max(ys) if re.search(r"[–-]|período|1951", v) else ys[0]
    return None

def num(s):
    s = s.replace("&nbsp;", " ")
    m = re.search(r"(\d[\d.,\s]*\d|\d)", s)
    if not m: return None
    t = m.group(1).replace(" ", "")
    if re.match(r"^\d{1,3}([.,]\d{3})+$", t): t = re.sub(r"[.,]", "", t)
    else: t = t.replace(",", ".")
    try: return float(t)
    except: return None

def altura(oid, r):
    if oid in ALTURA: return ALTURA[oid]
    v = r.get("altura", "")
    n = num(v)
    if n is None: return None
    if re.search(r"\bft\b|feet|pés", v): n = n * 0.3048
    return round(n, 1)

def area(oid, r):
    if oid in AREA: return AREA[oid]
    if oid in AREA_FORA: return None
    v = r.get("area", "")
    if not v or re.search(r"\b(ha|hectare|acre)", v): return None
    n = num(v)
    if n is None: return None
    if re.search(r"sq\s*ft|sqft|ft2|ft²", v): n = n * 0.092903
    elif not re.search(r"m2|m²|sqm|metros", v): return None
    return int(round(n))

def andares(oid, r):
    if oid in ANDARES_FORA: return None
    n = re.match(r"\s*(\d+)", r.get("andares", ""))
    return int(n.group(1)) if n else None

ESTILOS = [("modernisme","Modernismo catalão"),("brutal","Brutalismo"),("metabol","Metabolismo"),("deconstruc","Desconstrutivismo"),("desconstru","Desconstrutivismo"),
 ("high-tech","High-tech"),("hi-tech","High-tech"),("neo-futur","Neofuturismo"),("neofutur","Neofuturismo"),("blob","Arquitetura blob"),
 ("art déco","Art déco"),("art deco","Art déco"),("art nouveau","Art nouveau"),("modernisme","Modernismo catalão"),("secession","Secessão vienense"),
 ("de stijl","De Stijl"),("prairie","Prairie School"),("organic","Arquitetura orgânica"),("orgânic","Arquitetura orgânica"),
 ("expressionis","Expressionismo"),("structural expressionism","Expressionismo estrutural"),("postmodern","Pós-modernismo"),("pós-modern","Pós-modernismo"),("pós moderno","Pós-modernismo"),
 ("rationalis","Racionalismo"),("racionalis","Racionalismo"),("international","Estilo internacional"),("internacional","Estilo internacional"),
 ("mid-century","Modernismo"),("modern","Modernismo"),("eclé","Ecletismo"),("eclec","Ecletismo"),("neogót","Neogótico"),("gothic revival","Neogótico"),
 ("gótic","Gótico"),("gothic","Gótico"),("renaissance revival","Neorrenascimento"),("renaissance","Renascimento"),("renascen","Renascimento"),
 ("baroque","Barroco"),("barroc","Barroco"),("rococ","Rococó"),("neoclass","Neoclassicismo"),("neocláss","Neoclassicismo"),("classicism","Classicismo"),
 ("classical","Clássico grego"),("bizant","Bizantino"),("byzantine","Bizantino"),("mughal","Arquitetura mogol"),("colonial","Colonial"),("romanesque","Românico"),("românic","Românico"),
 ("futurist","Futurismo"),("minimal","Minimalismo"),("contemporar","Contemporâneo")]
def estilo(oid, r):
    v = (r.get("estilo", "") or "").lower()
    if "structural expressionism" in v: return "Expressionismo estrutural"
    for k, nome in ESTILOS:
        if k in v: return nome
    return None

def arquitetos(oid, r):
    v = r.get("arquiteto", "")
    v = re.sub(r"\{\{\s*ublist\s*\|", "", v).replace("}}", "").replace("|", " ")
    v = re.sub(r"\s+(and|&)\s+", ", ", v)
    v = re.sub(r"\s*,\s*", ", ", v).strip(" ,")
    return v

out = []
for o in O:
    oid, nome, cidade, pais, tipo, tpt, ten, prim = o
    r = P[oid]
    key = f"{oid}.{prim}" if f"{oid}.{prim}" in titles else (f"{oid}.pt" if f"{oid}.pt" in titles else f"{oid}.en")
    lang = key.rsplit(".", 1)[1]
    url = f"https://{lang}.wikipedia.org/wiki/" + titles[key].replace(" ", "_")
    out.append({"id": oid, "nome": nome, "arquitetos": OV.ARQ[oid] if oid in OV.ARQ else arquitetos(oid, r), "cidade": cidade, "pais": pais,
        "ano": None if oid in NAO_ANO else OV.ANO.get(oid, ano(oid, r)), "altura": altura(oid, r), "area": area(oid, r), "andares": andares(oid, r),
        "movimento": OV.MOV[oid] if oid in OV.MOV else estilo(oid, r), "tipo": tipo, "fonte": url, "views_key": [k for k in (f"{oid}.pt", f"{oid}.en") if k in titles]})
json.dump(out, open("acervo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for x in out:
    print(x["id"], "|", x["ano"], "|", x["altura"], "|", x["andares"], "|", x["area"], "|", x["movimento"], "|", x["arquitetos"][:70])
