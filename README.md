Arquitetex
==========

Jogo diário para arquitetos e amantes de arte. Dois modos: **Achado** (quanto mais rara a resposta, mais pontos) e **Escala** (quanto mais perto, mais pontos). A obra do dia começa em relevo seco e ganha tinta a cada ponto.

* Regras: `REGRAS.md`
* Sistema visual: `design.md`
* Banco de perguntas: planilha "Arquitetex: banco de perguntas" no Google Drive

Rodar
-----

Abra com um servidor local (o jogo lê os arquivos de `dados/`):

```
python3 -m http.server
```

e visite http://localhost:8000. Testes da pontuação e do reconhecimento de respostas: `npm test`.

Arquivos
--------

* `index.html`: página do jogo (GitHub Pages). `prototipo.html` é a mesma página sem cabeçalho, para a visualização no Claude
* `js/jogo.js`: telas e fluxo da partida
* `js/pontuacao.js` e `js/respostas.js`: contas e reconhecimento de respostas
* `js/desenhos.js`: as obras que crescem (croqui e torre, provisórios)
* `dados/`: gerado por `python3 ferramentas/gerar_dados.py` a partir das ferramentas
* `ferramentas/acervo/` e `ferramentas/achado/`: coleta na Wikipedia
