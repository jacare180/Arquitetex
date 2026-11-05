Arquitetex: sistema visual
==========================

Direção custom da skill Hallmark, decidida em 5 de novembro de 2026.

Ideia
-----

Relevo seco em papel de algodão. A obra do dia (croqui no Achado, torre na Escala) está na tela desde o começo, só em relevo, tom sobre tom. Cada ponto põe tinta num traço; 700 pontos deixam a obra inteira entintada. Nada fica colorido: ganhar é pôr tinta no papel.

Extremo: austero, puxando para o luxo silencioso (do material e do acabamento, não de brilho).
Clima: silencioso, tátil, artesanal, contemplativo, leve, rarefeito, poético, sereno.
Referência: capa de "Il peso dell'universo", Jorge Luis Borges, impressa em relevo seco.

Cores
-----

| Token | Cor | Contraste com o papel | Uso |
|---|---|---|---|
| `--papel` | #ECEAE5 | | fundo, liso, sem textura |
| `--luz` | #F8F7F3 | | lado iluminado do relevo |
| `--relevo` | #C8C4BC | 1,45 | ornamentos, divisórias, obra ainda não revelada, selo do jacaré |
| `--sombra` | #B7B2A8 | | lado em sombra do relevo |
| `--linha` | #77726A | 3,97 | bordas de campos e botões |
| `--tinta` | #5E5A53 | 5,7 | tudo o que se lê |

Visual único e claro, como um livro (modo escuro ainda não decidido).

Tipografia
----------

Piazzolla (Google Fonts), uma família só, romano e itálico. Itálico só em linhas inteiras, nunca numa palavra solta dentro de um título. Placares com algarismos tabulares e alinhados.

Relevo
------

O relevo é um par de luz e sombra de 1 px sobre a cor do papel. Só aparece onde tem função: a obra não revelada, o nome Arquitetex e o selo do jacaré. Exceção registrada ao gate 47c da Hallmark (relevo imitando material), porque aqui ele é a mecânica do jogo.

Movimento
---------

Lento e suave. A tinta corre pelo traço (`stroke-dashoffset`); a resposta afunda no papel como uma prensa. Com `prefers-reduced-motion`, tudo aparece sem movimento.

Outros elementos
----------------

- Cronômetro do diário: uma espiral, como a da capa.
- Jacaré arquiteto: selo redondo em relevo; falas em itálico.
- Composição: eixo central, margens largas, uma pergunta por tela.
