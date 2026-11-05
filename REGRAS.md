Arquitetex: regras do jogo
==========================

Jogo diário para arquitetos e amantes de arte, com dois modos: **Achado**
(quanto mais rara a resposta, mais pontos) e **Escala** (quanto mais perto da
resposta, mais pontos). Um jacaré arquiteto comenta cada jogada.

Este documento guarda tudo o que já foi decidido. Itens marcados como
**proposta** ainda esperam aprovação.


Estrutura geral
---------------

* **Dois desafios diários**, um para cada modo, com 7 perguntas cada.
* As perguntas do dia são iguais para todo mundo e o dia vira à meia-noite
  no horário de Brasília.
* **Cronômetro só no diário:** 25 segundos por pergunta. O relógio começa
  quando a pergunta termina de aparecer na tela.
* **Tempo esgotado vale 0** nos dois modos.
* **Modo livre:** depois de terminar o diário de um modo, o jogador pode
  jogar esse modo quantas vezes quiser, sem cronômetro, com perguntas
  sorteadas do banco.
* **Nenhuma rodada de bônus.** Cada pergunta vale no máximo 100 pontos, e
  uma partida vale no máximo **700 pontos**.
* Não há comparação com outros jogadores ("melhor que X%"), porque o jogo
  não tem servidor.


Modo Achado
-----------

Aparece uma categoria (por exemplo, "Um arquiteto brasileiro modernista") e o
jogador escreve uma resposta que pertence a ela.

### Faixas

| Faixa         | Pontos |
|---------------|-------:|
| Cartão-postal |     10 |
| Clássico      |     30 |
| Repertório    |     60 |
| Arquivo       |     85 |
| Achado        |    100 |

### Como responde

* O jogador **digita** a resposta. Não há autocompletar, para não revelar a
  lista.
* Pode **errar quantas vezes quiser**. A **primeira resposta válida conta**
  e encerra a pergunta.
* Se não acertar nenhuma, a pergunta vale **0**.
* O jogo aceita grafias alternativas (Lina, Lina Bo Bardi, Achillina Bo) e
  tolera erros pequenos. Quando corrige uma grafia, ele pergunta antes:
  "Você quis dizer Lina Bo Bardi?". O jogador confirma ou edita.
* Cada pergunta tem de 40 a 150 respostas aceitas, cada uma com a sua faixa.

### Sugerir para o acervo

Quando uma resposta certa não está na lista, o jogador pode tocar em
"sugerir para o acervo". Isso abre uma issue no GitHub já preenchida. Depois
de aprovada, a sugestão vira resposta aceita.


Modo Escala
-----------

### Dois formatos, misturados no mesmo desafio

1. **Pergunta:** o jogo pergunta e a resposta é um número.
   Exemplo: "Em que ano o MASP foi inaugurado?"
2. **Alvo:** o jogo dá um número e o jogador diz uma obra que chega perto
   dele. Exemplo: "Diga um edifício com cerca de 300 m de altura". A obra
   precisa estar no acervo e ter esse dado preenchido. Se não estiver, o
   jogador tenta de novo e pode sugerir a obra para o acervo. Depois da
   resposta, o jogo mostra a melhor resposta possível e outras próximas.

### Um chute por pergunta

A pontuação depende da distância entre o chute e a resposta, e a conta muda
conforme o tipo de número:

| Tipo                                     | Conta                                          | Exemplos                                    |
|------------------------------------------|------------------------------------------------|---------------------------------------------|
| Ano                                      | `100 - 4 x anos de erro`, mínimo 0             | 5 anos de erro: 80. 25 anos ou mais: 0      |
| Medida ou quantidade (m, m², andares...) | `100 x (1 - ln(maior/menor) / ln 3)`, mínimo 0 | o dobro ou a metade: cerca de 37. O triplo: 0 |

* Erro de até 2% (ou ano exato) vale **100** e ganha o selo **No prumo**.
* Os pontos são arredondados para o inteiro mais próximo.

### Faixas de resultado (proposta)

| Pontos  | Nome            |
|---------|-----------------|
| 100     | No prumo        |
| 80 a 99 | Na régua        |
| 50 a 79 | Aproximado      |
| 20 a 49 | Esboço          |
| 0 a 19  | Fora de escala  |


O elemento que cresce
---------------------

* **Achado:** um **croqui**. Cada dia tem uma obra escondida que vai sendo
  desenhada em camadas (linha do chão, linhas de construção, contorno,
  aberturas, hachura e sombra, aguada de cor e, por fim, o nome da obra com
  a assinatura do jacaré).
* **Escala:** uma **torre** de edifício famoso que sobe pavimento por
  pavimento, com marcos de altura reais pelo caminho.
* **700 pontos são 100% da obra.** Quem faz menos vê só a parte
  proporcional: com 420 pontos, vê 60% da obra.
* Começamos com umas 10 obras para cada modo, em rodízio.
* **Em aberto:** de onde vêm os desenhos dos croquis.


O jacaré arquiteto
------------------

* Comenta cada resposta, no mesmo tom do jacaré do Flagx.
* Depois de cada resposta, conta uma curiosidade curta sobre a obra ou o
  assunto.


Banco de perguntas
------------------

* Tudo nasce numa planilha com cinco abas: Acervo de obras, Achado, Escala,
  Obras que crescem e Sugestões. Um script transforma a planilha nos
  arquivos JSON que o jogo lê.
* Toda linha tem **fonte**.
* O **acervo de obras** alimenta os dois modos: a mesma obra pode ser
  resposta no Achado e gerar perguntas na Escala (ano, altura, área).
* Lançamento com **50 perguntas por modo**. O banco cresce de três jeitos:
  1. novas perguntas sempre que der;
  2. a mesma categoria volta com outro recorte ("Um museu" e depois "Um
     museu da América Latina");
  3. depois de alguns meses, perguntas antigas podem voltar ao diário.


Fora do escopo por enquanto
---------------------------

* Estética, que será feita com a skill Hallmark quando a direção visual for
  definida.
* Origem dos desenhos dos croquis.
