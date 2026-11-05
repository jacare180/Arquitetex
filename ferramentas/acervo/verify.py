import re, sys, os, unicodedata
sys.path.insert(0, '.')
from overrides import ARQ, MOV, STEM, ANO
def txt(oid):
    t = ""
    for l in ("pt", "en"):
        p = f"cache/{oid}.{l}.raw"
        if os.path.exists(p): t += open(p, encoding="utf-8").read()
    return unicodedata.normalize("NFC", t).lower()
def fold(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
bad = 0
for oid, v in ARQ.items():
    if not v: continue
    T = fold(txt(oid))
    names = re.split(r";|,| e |\(|\)", v)
    for n in names:
        n = n.strip()
        if not n or n in ("reforma de 1999", "escultura", "atribuído", "conversão", "usina", "reforma"): continue
        last = fold(n.split()[-1])
        if last in ("architects", "architecture", "partners", "merrill", "harmon", "workshop"): last = fold(n.split()[0])
        if last not in T: print("ARQ?", oid, "|", n); bad += 1
for oid, v in MOV.items():
    if v and not re.search(STEM[v], txt(oid)): print("MOV?", oid, v); bad += 1
print("pendentes:", bad)
