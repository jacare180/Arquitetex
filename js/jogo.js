// Arquitetex: protótipo jogável. Regras em REGRAS.md, visual em design.md.
(function () {
  "use strict";

  var P = window.Pontuacao, R = window.Respostas, D = window.Desenhos;
  var TEMPO = 25;               // segundos por pergunta no diário
  var CHAVE = "arquitetex:v1";  // localStorage
  var REPO = "https://github.com/jacare180/Arquitetex";
  var app = document.getElementById("app");
  var dados = { achado: [], acervo: [] };
  var relogio = null;

  /* ---------- utilidades ---------- */

  function el(tag, attrs, filhos) {
    var n = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === "texto") { n.textContent = attrs[k]; }
      else if (k.indexOf("on") === 0) { n.addEventListener(k.slice(2), attrs[k]); }
      else if (attrs[k] !== false && attrs[k] != null) { n.setAttribute(k, attrs[k] === true ? "" : attrs[k]); }
    });
    (filhos || []).forEach(function (f) { if (f) { n.appendChild(typeof f === "string" ? document.createTextNode(f) : f); } });
    return n;
  }

  function hoje() {
    try {
      return new Intl.DateTimeFormat("en-CA", { timeZone: "America/Sao_Paulo" }).format(new Date());
    } catch (e) { return new Date().toISOString().slice(0, 10); }
  }
  function dataBr(iso) { var p = iso.split("-"); return p[2] + "/" + p[1] + "/" + p[0]; }

  function sementeDe(texto) {
    var h = 1779033703 ^ texto.length;
    for (var i = 0; i < texto.length; i++) { h = Math.imul(h ^ texto.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
    return h >>> 0;
  }
  function gerador(semente) {
    var a = semente;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function embaralhar(lista, rnd) {
    var l = lista.slice();
    for (var i = l.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)); var t = l[i]; l[i] = l[j]; l[j] = t; }
    return l;
  }
  function escolher(lista, rnd) { return lista[Math.floor(rnd() * lista.length)]; }

  function ler() { try { return JSON.parse(localStorage.getItem(CHAVE)) || { dias: {} }; } catch (e) { return { dias: {} }; } }
  function gravar(estado) { try { localStorage.setItem(CHAVE, JSON.stringify(estado)); } catch (e) { /* sem armazenamento: o jogo segue */ } }

  function numero(texto) {
    var t = String(texto).replace(/\s|m²|m|anos?/gi, "");
    if (!t) { return NaN; }
    if (t.indexOf(",") >= 0) { t = t.replace(/\./g, "").replace(",", "."); }
    else if (/^\d{1,3}(\.\d{3})+$/.test(t)) { t = t.replace(/\./g, ""); }
    return parseFloat(t);
  }
  function fmt(n) { return Number(n).toLocaleString("pt-BR", { maximumFractionDigits: 1 }); }
  function fmtAno(n) { return n < 0 ? (-n) + " a.C." : String(n); }

  /* ---------- o jacaré ---------- */

  var FALAS = {
    "Cartão-postal": ["Resposta de cartão-postal. O papel quase não sentiu.", "Até o porteiro do prédio pensou nessa."],
    "Clássico": ["Clássico. De quem prestou atenção na aula.", "Correto, bem passado a nanquim."],
    "Repertório": ["Agora sim, repertório de quem lê planta baixa.", "Escolha de quem já passou uma tarde lá."],
    "Arquivo": ["Isso saiu de alguma gaveta de mapoteca. Gostei.", "Pouca gente lembraria dessa."],
    "Achado": ["Um achado. Vou emoldurar essa resposta.", "Nem eu tinha pensado nessa, e eu sou um jacaré arquiteto."],
    "No prumo": ["No prumo. Nem o nível de bolha discorda."],
    "Na régua": ["Na régua. Um traço a mais e era perfeito."],
    "Aproximado": ["Aproximado. Dá para aprovar na prefeitura."],
    "Esboço": ["Esboço. A ideia estava lá, a escala não."],
    "Fora de escala": ["Fora de escala. Confere essa trena."],
    "tempo": ["O tempo acabou. Essa prancheta ficou em branco."],
    "desistiu": ["Passou. Às vezes o melhor traço é o que não se faz."]
  };
  function fala(chave) { var l = FALAS[chave] || [""]; return l[Math.floor(Math.random() * l.length)]; }

  var TITULOS = [[1, "Obra entregue"], [0.75, "Projeto executivo"], [0.5, "Anteprojeto"], [0.25, "Croqui"], [0, "Esboço"]];
  function titulo(fracao) { for (var i = 0; i < TITULOS.length; i++) { if (fracao >= TITULOS[i][0]) { return TITULOS[i][1]; } } return "Esboço"; }

  /* ---------- montagem das partidas ---------- */

  function rodadasAchado(rnd) {
    return embaralhar(dados.achado, rnd).slice(0, P.PERGUNTAS_POR_PARTIDA).map(function (q) {
      return { tipo: "achado", pergunta: q.pergunta, respostas: q.respostas.map(function (r) { return { resposta: r.r, grafias: r.g, faixa: r.f }; }) };
    });
  }

  function rodadasEscala(rnd) {
    var comAno = dados.acervo.filter(function (o) { return o.ano !== null && o.ano >= 1850; });
    var comAltura = dados.acervo.filter(function (o) { return o.altura !== null && o.altura >= 40; });
    var usadas = {};
    function nova(lista) {
      var o, tentativas = 0;
      do { o = escolher(lista, rnd); tentativas++; } while (usadas[o.id] && tentativas < 50);
      usadas[o.id] = true; return o;
    }
    var tipos = embaralhar(["ano", "ano", "ano", "altura", "altura", "alvo-altura", "alvo-ano"], rnd);
    return tipos.map(function (t) {
      if (t === "ano") {
        var a = nova(comAno);
        return { tipo: "numero", pontuacao: "Ano", obra: a, valor: a.ano, unidade: "", titulo: a.nome, pergunta: "Em que ano esta obra ficou pronta?" };
      }
      if (t === "altura") {
        var b = nova(comAltura);
        return { tipo: "numero", pontuacao: "Medida", obra: b, valor: b.altura, unidade: "m", titulo: b.nome, pergunta: "Quantos metros de altura tem esta obra?" };
      }
      if (t === "alvo-altura") {
        var alvo = Math.round(escolher(comAltura.filter(function (o) { return o.altura >= 60; }), rnd).altura / 10) * 10;
        return { tipo: "alvo", pontuacao: "Medida", atributo: "altura", valor: alvo, unidade: "m", titulo: alvo + " m",
                 pergunta: "Diga um edifício ou torre famosa com cerca de " + alvo + " m de altura", candidatas: dados.acervo.filter(function (o) { return o.altura !== null; }) };
      }
      var ano = Math.round(escolher(comAno.filter(function (o) { return o.ano >= 1900; }), rnd).ano / 5) * 5;
      return { tipo: "alvo", pontuacao: "Ano", atributo: "ano", valor: ano, unidade: "", titulo: String(ano),
               pergunta: "Diga uma obra de arquitetura famosa que ficou pronta perto de " + ano, candidatas: dados.acervo.filter(function (o) { return o.ano !== null; }) };
    });
  }

  function novaPartida(modo, livre) {
    var dia = hoje();
    var semente = livre ? Math.floor(Math.random() * 1e9) : sementeDe(dia + ":" + modo);
    var rnd = livre ? Math.random : gerador(semente);
    return {
      modo: modo, livre: livre, dia: dia, i: 0, total: 0, resultados: [],
      rodadas: modo === "achado" ? rodadasAchado(rnd) : rodadasEscala(rnd),
      semente: semente,
      desenho: modo === "achado" ? D.DO_ACHADO[semente % D.DO_ACHADO.length] : "torre"
    };
  }

  /* ---------- telas ---------- */

  function limpar() { pararRelogio(); app.innerHTML = ""; window.scrollTo(0, 0); }

  function marca(pequena) {
    return el("h1", { "class": "marca relevo" + (pequena ? " marca-pequena" : "") }, [
      pequena ? el("button", { type: "button", "class": "marca-botao", onclick: inicio, "aria-label": "Voltar ao início" }, ["Arquitetex"]) : "Arquitetex"
    ]);
  }

  function inicio() {
    limpar();
    var estado = ler(), dia = hoje(), feito = (estado.dias[dia] || {});
    function cartao(modo, nome, descricao) {
      var r = feito[modo];
      return el("li", { "class": "modo" }, [
        el("h2", { texto: nome }),
        el("p", { "class": "modo-descricao", texto: descricao }),
        r ? el("p", { "class": "modo-feito" }, [el("span", { "class": "num", texto: r.total }), " de 700 hoje, " + titulo(r.total / 700).toLowerCase()]) : null,
        el("div", { "class": "acoes" }, [
          r ? el("button", { type: "button", "class": "botao", onclick: function () { jogar(modo, true); } }, ["Jogar no modo livre"])
            : el("button", { type: "button", "class": "botao botao-cheio", onclick: function () { jogar(modo, false); } }, ["Jogar o desafio de hoje"]),
          r ? el("button", { type: "button", "class": "botao-texto", onclick: function () { verFim(r, modo); } }, ["Ver o resultado de hoje"]) : null
        ])
      ]);
    }
    app.appendChild(el("section", { "class": "inicio" }, [
      ornamento(),
      marca(false),
      el("p", { "class": "subtitulo", texto: "Um jogo diário para quem lê cidades e desenha com a cabeça." }),
      el("p", { "class": "data", texto: "Desafios de " + dataBr(dia) }),
      el("ul", { "class": "modos" }, [
        cartao("achado", "Achado", "Uma categoria, uma resposta. Quanto mais rara, mais pontos."),
        cartao("escala", "Escala", "Um número, um chute. Quanto mais perto, mais pontos.")
      ]),
      el("p", { "class": "rodape-nota", texto: "Protótipo. As perguntas da Escala ainda são provisórias, geradas a partir do acervo de obras." })
    ]));
  }

  function ornamento() {
    var d = el("div", { "class": "ornamento", "aria-hidden": "true" });
    d.innerHTML = '<svg viewBox="0 0 72 20"><path class="orn-luz" d="M4 10c6-8 12 8 18 0s12-8 14 0 8 8 14 0 12 8 18 0" transform="translate(-0.6 -0.6)"/>' +
      '<path class="orn-sombra" d="M4 10c6-8 12 8 18 0s12-8 14 0 8 8 14 0 12 8 18 0" transform="translate(0.6 0.6)"/></svg>';
    return d;
  }

  var partida = null;

  function jogar(modo, livre) { partida = novaPartida(modo, livre); rodada(); }

  function rodada() {
    limpar();
    var q = partida.rodadas[partida.i];
    var obra = el("figure", { "class": "obra" });
    partida.obra = D.montar(obra, partida.desenho, partida.semente, partida.total / 700);
    obra.appendChild(el("figcaption", { "class": "obra-legenda", texto: partida.total === 0 ? "A obra de hoje, ainda só em pistas de relevo" : Math.round(partida.total / 7) + "% da obra com tinta" }));

    var espiral = partida.livre ? null : relogioSvg();
    var cabecalho = el("header", { "class": "barra" }, [
      marca(true),
      el("p", { "class": "passo" }, [
        espiral ? espiral.svg : null,
        el("span", { texto: (partida.modo === "achado" ? "Achado" : "Escala") + ", pergunta " + (partida.i + 1) + " de 7" }),
        espiral ? el("span", { "class": "segundos num", "aria-live": "off", texto: TEMPO + " s" }) : el("span", { "class": "livre", texto: "modo livre" })
      ]),
      el("p", { "class": "placar-mini num", texto: partida.total + " de 700" })
    ]);

    var area = el("div", { "class": "rodada" });
    var retorno = el("div", { "class": "retorno", "aria-live": "polite" });
    var campo = el("input", { id: "resposta", type: "text", autocomplete: "off", autocapitalize: "sentences", spellcheck: "false",
      inputmode: q.tipo === "numero" ? "decimal" : null, placeholder: q.tipo === "numero" ? (q.pontuacao === "Ano" ? "Ano" : "Metros") : "Sua resposta",
      "aria-label": "Sua resposta" });
    var form = el("form", { "class": "resposta", novalidate: true }, [
      campo,
      el("div", { "class": "acoes" }, [
        el("button", { type: "submit", "class": "botao botao-cheio" }, ["Responder"]),
        el("button", { type: "button", "class": "botao-texto", onclick: function () { encerrar({ pontos: 0, motivo: "desistiu" }); } }, ["Passar"])
      ])
    ]);

    var enunciado = q.tipo === "achado"
      ? [el("h2", { "class": "pergunta", texto: q.pergunta })]
      : [el("p", { "class": "pergunta-sobre", texto: q.tipo === "alvo" ? "Alvo" : "" }), el("h2", { "class": "pergunta", texto: q.titulo }), el("p", { "class": "pergunta-detalhe", texto: q.pergunta })];

    form.addEventListener("submit", function (e) { e.preventDefault(); responder(q, campo.value, retorno, form); });
    enunciado.forEach(function (n) { if (n.textContent) { area.appendChild(n); } });
    area.appendChild(form);
    area.appendChild(retorno);
    app.appendChild(el("section", { "class": "tela-rodada" }, [cabecalho, obra, area]));
    campo.focus({ preventScroll: true });
    if (espiral) { iniciarRelogio(espiral, cabecalho.querySelector(".segundos")); }
  }

  /* ---------- relógio em espiral ---------- */

  function relogioSvg() {
    var NS = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", "0 0 24 24"); svg.setAttribute("class", "espiral"); svg.setAttribute("aria-hidden", "true");
    var d = "M12 12c0-1 1-1.6 1.8-1 .9.7.6 2.2-.5 2.7-1.6.7-3.3-.6-3.2-2.3.1-2.4 2.6-3.8 4.7-3 2.8 1 3.6 4.6 1.8 6.9-2.3 3-7 2.9-8.9-.3-2.3-3.7.1-8.6 4.3-9.2 4.8-.7 8.7 3.5 7.9 8.2";
    var base = document.createElementNS(NS, "path"); base.setAttribute("d", d); base.setAttribute("class", "espiral-base");
    var tinta = document.createElementNS(NS, "path"); tinta.setAttribute("d", d); tinta.setAttribute("class", "espiral-tinta"); tinta.setAttribute("pathLength", "1");
    svg.appendChild(base); svg.appendChild(tinta);
    return { svg: svg, tinta: tinta };
  }
  function iniciarRelogio(espiral, rotulo) {
    var inicio = Date.now() + 600;  // começa quando a pergunta termina de aparecer
    relogio = setInterval(function () {
      var passado = Math.max(0, (Date.now() - inicio) / 1000);
      var resta = Math.max(0, TEMPO - passado);
      espiral.tinta.style.strokeDashoffset = String(resta / TEMPO);
      rotulo.textContent = Math.ceil(resta) + " s";
      if (resta <= 0) { encerrar({ pontos: 0, motivo: "tempo" }); }
    }, 200);
  }
  function pararRelogio() { if (relogio) { clearInterval(relogio); relogio = null; } }

  /* ---------- respostas ---------- */

  function responder(q, texto, retorno, form) {
    retorno.innerHTML = "";
    if (!texto.trim()) { return; }
    if (q.tipo === "numero") {
      var n = numero(texto);
      if (isNaN(n)) { retorno.appendChild(el("p", { "class": "aviso", texto: "Escreva só o número, por exemplo " + (q.pontuacao === "Ano" ? "1968" : "120") + "." })); return; }
      var r = P.pontosEscala(q.pontuacao, n, q.valor);
      encerrar({ pontos: r.pontos, noPrumo: r.noPrumo, faixa: P.faixaEscala(r.pontos), chute: n });
      return;
    }
    var lista = q.tipo === "achado" ? q.respostas : q.candidatas.map(function (o) { return { resposta: o.nome, grafias: o.g, obra: o }; });
    var achou = R.reconhecer(texto, lista);
    if (achou.tipo === "exata") { aceitar(q, achou.item); return; }
    if (achou.tipo === "parecida") {
      retorno.appendChild(el("div", { "class": "confirma" }, [
        el("p", {}, ["Você quis dizer ", el("strong", { texto: achou.escrita }), "?"]),
        el("div", { "class": "acoes" }, [
          el("button", { type: "button", "class": "botao botao-cheio", onclick: function () { aceitar(q, achou.item); } }, ["Sim"]),
          el("button", { type: "button", "class": "botao-texto", onclick: function () { retorno.innerHTML = ""; form.querySelector("input").focus(); } }, ["Não, vou corrigir"])
        ])
      ]));
      return;
    }
    var pergunta = q.tipo === "achado" ? q.pergunta : q.pergunta;
    var url = REPO + "/issues/new?title=" + encodeURIComponent("Sugestão para o acervo: " + texto.trim()) +
      "&body=" + encodeURIComponent("Pergunta: " + pergunta + "\nResposta sugerida: " + texto.trim() + "\nFonte (link):\n");
    retorno.appendChild(el("div", { "class": "aviso" }, [
      el("p", { texto: q.tipo === "achado" ? "“" + texto.trim() + "” não está entre as respostas desta pergunta. Tente outra." : "Não conheço essa obra, ou não tenho esse dado dela. Tente outra." }),
      el("a", { href: url, target: "_blank", rel: "noopener", "class": "link" }, ["Sugerir para o acervo"])
    ]));
    form.querySelector("input").select();
  }

  function aceitar(q, item) {
    if (q.tipo === "achado") {
      encerrar({ pontos: P.pontosAchado(item.faixa), faixa: item.faixa, escolha: item.resposta });
      return;
    }
    var valor = item.obra[q.atributo];
    var r = P.pontosEscala(q.pontuacao, valor, q.valor);
    encerrar({ pontos: r.pontos, noPrumo: r.noPrumo, faixa: P.faixaEscala(r.pontos), escolha: item.obra.nome, valorEscolha: valor, obraEscolha: item.obra });
  }

  function encerrar(res) {
    pararRelogio();
    var q = partida.rodadas[partida.i];
    res.motivo = res.motivo || null;
    partida.total += res.pontos;
    partida.resultados.push({ pergunta: q.tipo === "achado" ? q.pergunta : q.titulo, faixa: res.faixa || (res.motivo === "tempo" ? "Tempo esgotado" : "Passou"), pontos: res.pontos, escolha: res.escolha || (res.chute != null ? String(res.chute) : "") });

    var tela = app.querySelector(".tela-rodada");
    var area = tela.querySelector(".rodada");
    area.querySelector("form").remove();
    var ret = area.querySelector(".retorno"); ret.innerHTML = "";
    var novos = partida.obra.entintar(partida.total / 700);
    tela.querySelector(".obra-legenda").textContent = (novos > 0 ? "+" + novos + (novos === 1 ? " traço" : " traços") + ". " : "Nenhum traço novo. ") + Math.round(partida.total / 7) + "% da obra com tinta";
    tela.querySelector(".placar-mini").textContent = partida.total + " de 700";
    var seg = tela.querySelector(".segundos"); if (seg) { seg.textContent = ""; }

    var blocos = [];
    if (res.motivo) {
      blocos.push(el("p", { "class": "faixa", texto: res.motivo === "tempo" ? "Tempo esgotado, 0 ponto" : "Pergunta passada, 0 ponto" }));
    } else {
      blocos.push(el("p", { "class": "escolha", texto: res.escolha || (fmt(res.chute) + (q.unidade ? " " + q.unidade : "")) }));
      blocos.push(el("p", { "class": "faixa" }, [res.faixa + ", ", el("span", { "class": "num", texto: "+" + res.pontos }), res.pontos === 1 ? " ponto" : " pontos"]));
    }
    blocos.push(el("p", { "class": "fala" }, [el("span", { "class": "selo", "aria-hidden": "true" }), fala(res.motivo || res.faixa)]));
    if (q.tipo !== "achado" && !res.motivo) {
      blocos.push(escalimetro(q, q.tipo === "numero" ? res.chute : res.valorEscolha, q.tipo === "numero" ? "Seu chute" : res.escolha));
    }
    blocos.push(contexto(q, res));
    blocos.push(el("button", { type: "button", "class": "botao botao-cheio", onclick: proxima }, [partida.i < 6 ? "Próxima pergunta" : "Ver o resultado"]));
    var resultado = el("div", { "class": "resultado" }, blocos);
    ret.appendChild(resultado);
    resultado.querySelector("button").focus({ preventScroll: true });
  }

  function contexto(q, res) {
    if (q.tipo === "achado") {
      var comum = q.respostas.filter(function (r) { return r.faixa === "Cartão-postal"; })[0];
      var raras = q.respostas.filter(function (r) { return r.faixa === "Achado"; });
      var rara = raras[Math.floor(Math.random() * raras.length)];
      return el("p", { "class": "contexto" }, ["Mais comum: " + (comum ? comum.resposta : "") + ". Uma rara: " + (rara ? rara.resposta : "") + ". " + q.respostas.length + " respostas no acervo."]);
    }
    if (q.tipo === "numero") {
      var certo = q.pontuacao === "Ano" ? fmtAno(q.valor) : fmt(q.valor) + " m";
      return el("p", { "class": "contexto" }, [q.obra.nome + ", " + certo + ". ", el("a", { href: q.obra.fonte, target: "_blank", rel: "noopener", "class": "link" }, ["Fonte"])]);
    }
    var melhor = q.candidatas.slice().sort(function (a, b) { return Math.abs(a[q.atributo] - q.valor) - Math.abs(b[q.atributo] - q.valor); })[0];
    var fmtV = function (v) { return q.atributo === "ano" ? fmtAno(v) : fmt(v) + " m"; };
    var partes = [];
    partes.push("Melhor resposta: " + melhor.nome + ", " + fmtV(melhor[q.atributo]) + ".");
    return el("p", { "class": "contexto", texto: partes.join("") });
  }

  // Escalímetro: régua com a resposta certa no meio e o chute marcado; a tinta cobre a distância entre os dois.
  // Em unidades da régua, a pontuação p fica a (100 - p) / 120 do centro, tanto para anos quanto para medidas.
  function posicao(q, v) {
    var u = q.pontuacao === "Ano" ? (v - q.valor) / 30 : Math.log(v / q.valor) / (Math.log(3) * 1.2);
    return Math.max(-1, Math.min(1, u));
  }
  function escalimetro(q, v, rotuloChute) {
    var fmtV = function (x) { return q.pontuacao === "Ano" ? fmtAno(x) : fmt(x) + " m"; };
    var u = posicao(q, v), pct = function (x) { return (50 + x * 46) + "%"; };
    var regua = el("div", { "class": "regua", role: "img", "aria-label": "Seu chute " + fmtV(v) + ", resposta " + fmtV(q.valor) });
    var esq = Math.min(0, u), larg = Math.abs(u);
    regua.appendChild(el("span", { "class": "regua-corpo" }));
    [-0.833, -0.667, -0.417, -0.167, 0.167, 0.417, 0.667, 0.833].forEach(function (b) {
      var pts = Math.round(100 - Math.abs(b) * 120);
      regua.appendChild(el("span", { "class": "regua-marca", style: "left:" + pct(b) }));
      regua.appendChild(el("span", { "class": "regua-numero num", style: "left:" + pct(b), texto: String(pts) }));
    });
    for (var i = -20; i <= 20; i++) { if (i % 5) { regua.appendChild(el("span", { "class": "regua-miuda", style: "left:" + pct(i / 24) })); } }
    var barra = el("span", { "class": "regua-tinta" + (u < 0 ? " para-esquerda" : ""), style: "left:" + pct(esq) + ";width:" + (larg * 46) + "%" });
    regua.appendChild(barra);
    regua.appendChild(el("span", { "class": "regua-certo", style: "left:50%" }));
    regua.appendChild(el("span", { "class": "regua-chute", style: "left:" + pct(u) }));
    return el("figure", { "class": "escalimetro" }, [
      el("figcaption", { "class": "escalimetro-legenda" }, [
        el("span", {}, [rotuloChute + ": ", el("strong", { "class": "num", texto: fmtV(v) })]),
        el("span", {}, [q.tipo === "alvo" ? "Alvo: " : "Resposta: ", el("strong", { "class": "num", texto: fmtV(q.valor) })])
      ]),
      regua,
      el("p", { "class": "escalimetro-nota", texto: "Os números na régua são os pontos de cada distância." })
    ]);
  }

  function proxima() {
    if (partida.i < 6) { partida.i++; rodada(); return; }
    var resumo = { total: partida.total, resultados: partida.resultados, dia: partida.dia, livre: partida.livre, desenho: partida.desenho, semente: partida.semente };
    if (!partida.livre) {
      var estado = ler();
      estado.dias[partida.dia] = estado.dias[partida.dia] || {};
      estado.dias[partida.dia][partida.modo] = resumo;
      gravar(estado);
    }
    verFim(resumo, partida.modo);
  }

  function verFim(resumo, modo) {
    limpar();
    var fracao = resumo.total / 700;
    var obra = el("figure", { "class": "obra obra-grande" });
    var chave = resumo.desenho || (modo === "achado" ? "masp" : "torre");
    var desenho = D.montar(obra, chave, resumo.semente || 1, 0);
    requestAnimationFrame(function () { requestAnimationFrame(function () { desenho.entintar(fracao); }); });
    obra.appendChild(el("figcaption", { "class": "obra-legenda" }, [
      el("span", { texto: Math.round(fracao * 100) + "% da obra com tinta. A obra de hoje era" }),
      el("strong", { texto: desenho.nome }),
      el("span", { texto: desenho.legenda })
    ]));
    var texto = "Arquitetex, " + (modo === "achado" ? "Achado" : "Escala") + " de " + dataBr(resumo.dia) + (resumo.livre ? " (livre)" : "") + "\n" +
      resumo.total + " de 700, " + Math.round(fracao * 100) + "% da obra\n" +
      resumo.resultados.map(function (r, i) { return (i + 1) + ". " + r.faixa + ", " + r.pontos; }).join("\n");
    var aviso = el("p", { "class": "copiado", "aria-live": "polite" });
    app.appendChild(el("section", { "class": "fim" }, [
      marca(true),
      el("p", { "class": "fim-titulo", texto: titulo(fracao) }),
      el("p", { "class": "fim-placar" }, [el("span", { "class": "num", texto: resumo.total }), el("small", { texto: " de 700" })]),
      obra,
      el("ol", { "class": "lista-rodadas" }, resumo.resultados.map(function (r) {
        return el("li", {}, [el("span", { "class": "lr-pergunta", texto: r.pergunta }), el("span", { "class": "lr-escolha", texto: r.escolha || "sem resposta" }), el("span", { "class": "lr-pontos num", texto: r.faixa + ", " + r.pontos })]);
      })),
      el("div", { "class": "acoes" }, [
        el("button", { type: "button", "class": "botao botao-cheio", onclick: function () {
          var ok = function () { aviso.textContent = "Resultado copiado."; };
          try { navigator.clipboard.writeText(texto).then(ok, function () { aviso.textContent = texto; }); } catch (e) { aviso.textContent = texto; }
        } }, ["Copiar resultado"]),
        el("button", { type: "button", "class": "botao", onclick: function () { jogar(modo, true); } }, ["Jogar no modo livre"]),
        el("button", { type: "button", "class": "botao-texto", onclick: inicio }, ["Início"])
      ]),
      aviso
    ]));
  }

  /* ---------- partida ---------- */

  function carregar(caminho) { return fetch(caminho).then(function (r) { if (!r.ok) { throw new Error(caminho); } return r.json(); }); }
  Promise.all([carregar("dados/achado.json"), carregar("dados/acervo.json")]).then(function (res) {
    dados.achado = res[0]; dados.acervo = res[1];
    inicio();
  }).catch(function () {
    app.innerHTML = "";
    app.appendChild(el("p", { "class": "aviso", texto: "Não consegui carregar as perguntas. Recarregue a página." }));
  });
})();
