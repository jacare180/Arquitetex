// Contas de pontuação do Arquitetex. As regras estão em REGRAS.md.
(function (raiz) {
  "use strict";

  var FAIXAS_ACHADO = {
    "Cartão-postal": 10,
    "Clássico": 30,
    "Repertório": 60,
    "Arquivo": 85,
    "Achado": 100
  };

  var MAXIMO_POR_PERGUNTA = 100;
  var PERGUNTAS_POR_PARTIDA = 7;
  var MAXIMO_POR_PARTIDA = MAXIMO_POR_PERGUNTA * PERGUNTAS_POR_PARTIDA;
  var MARGEM_NO_PRUMO = 0.02;
  var PONTOS_POR_ANO = 4;
  var PROPORCAO_ZERO = 3;

  // Achado: pontos da primeira resposta válida; nenhuma válida (ou tempo esgotado) vale 0.
  function pontosAchado(faixa) {
    if (!faixa) { return 0; }
    if (!(faixa in FAIXAS_ACHADO)) { throw new Error("Faixa desconhecida: " + faixa); }
    return FAIXAS_ACHADO[faixa];
  }

  // Escala: um chute por pergunta. tipo é "Ano" ou "Medida".
  // Devolve { pontos, noPrumo }. Chute ausente (tempo esgotado) vale 0.
  function pontosEscala(tipo, chute, valor) {
    if (chute === null || chute === undefined || isNaN(chute)) { return { pontos: 0, noPrumo: false }; }
    var pontos;
    if (tipo === "Ano") {
      var erro = Math.abs(chute - valor);
      if (erro === 0) { return { pontos: 100, noPrumo: true }; }
      pontos = 100 - PONTOS_POR_ANO * erro;
    } else if (tipo === "Medida") {
      if (chute <= 0 || valor <= 0) { return { pontos: 0, noPrumo: false }; }
      if (Math.abs(chute - valor) / valor <= MARGEM_NO_PRUMO) { return { pontos: 100, noPrumo: true }; }
      var razao = Math.max(chute, valor) / Math.min(chute, valor);
      pontos = 100 * (1 - Math.log(razao) / Math.log(PROPORCAO_ZERO));
    } else {
      throw new Error("Tipo de pontuação desconhecido: " + tipo);
    }
    return { pontos: Math.max(0, Math.min(99, Math.round(pontos))), noPrumo: false };
  }

  // Faixa de resultado da Escala (nomes ainda em proposta).
  function faixaEscala(pontos) {
    if (pontos >= 100) { return "No prumo"; }
    if (pontos >= 80) { return "Na régua"; }
    if (pontos >= 50) { return "Aproximado"; }
    if (pontos >= 20) { return "Esboço"; }
    return "Fora de escala";
  }

  // Quanto da obra (croqui ou torre) aparece: 700 pontos = 100%.
  function fracaoDaObra(total) {
    return Math.max(0, Math.min(1, total / MAXIMO_POR_PARTIDA));
  }

  var api = {
    FAIXAS_ACHADO: FAIXAS_ACHADO,
    MAXIMO_POR_PARTIDA: MAXIMO_POR_PARTIDA,
    PERGUNTAS_POR_PARTIDA: PERGUNTAS_POR_PARTIDA,
    pontosAchado: pontosAchado,
    pontosEscala: pontosEscala,
    faixaEscala: faixaEscala,
    fracaoDaObra: fracaoDaObra
  };
  if (typeof module === "object" && module.exports) { module.exports = api; } else { raiz.Pontuacao = api; }
})(this);
