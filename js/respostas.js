// Reconhecimento das respostas digitadas no Achado e no Alvo da Escala.
(function (raiz) {
  "use strict";

  var ARTIGOS = /^(o|a|os|as|the|el|la|le|les|il|lo)\s+/;

  // "Edifício  Itália!" -> "edificio italia"
  function normalizar(texto) {
    return String(texto)
      .normalize("NFD").replace(/[̀-ͯ]/g, "")
      .toLowerCase()
      .replace(/&/g, " e ")
      .replace(/[^a-z0-9]+/g, " ")
      .trim()
      .replace(ARTIGOS, "");
  }

  function distancia(a, b) {
    if (a === b) { return 0; }
    var anterior = [], atual, i, j;
    for (j = 0; j <= b.length; j++) { anterior[j] = j; }
    for (i = 1; i <= a.length; i++) {
      atual = [i];
      for (j = 1; j <= b.length; j++) {
        var troca = anterior[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1);
        atual[j] = Math.min(anterior[j] + 1, atual[j - 1] + 1, troca);
      }
      anterior = atual;
    }
    return anterior[b.length];
  }

  // Erros tolerados: nenhum em palavras curtas, 1 até 8 letras, 2 acima disso.
  function tolerancia(tamanho) {
    if (tamanho <= 4) { return 0; }
    if (tamanho <= 8) { return 1; }
    return 2;
  }

  // respostas: [{ resposta: "Lina Bo Bardi", grafias: ["Lina", "Achillina Bo"], ... }]
  // Devolve { tipo: "exata" | "parecida" | "nenhuma", item, escrita }.
  // "parecida" pede confirmação ao jogador ("Você quis dizer ...?").
  function reconhecer(digitado, respostas) {
    var alvo = normalizar(digitado);
    if (!alvo) { return { tipo: "nenhuma" }; }
    var melhor = null;
    for (var i = 0; i < respostas.length; i++) {
      var item = respostas[i];
      var formas = [item.resposta].concat(item.grafias || []);
      for (var k = 0; k < formas.length; k++) {
        var forma = normalizar(formas[k]);
        if (forma === alvo) { return { tipo: "exata", item: item, escrita: item.resposta }; }
        var d = distancia(alvo, forma);
        if (d <= tolerancia(forma.length) && (!melhor || d < melhor.d)) { melhor = { d: d, item: item }; }
      }
    }
    if (melhor) { return { tipo: "parecida", item: melhor.item, escrita: melhor.item.resposta }; }
    return { tipo: "nenhuma" };
  }

  var api = { normalizar: normalizar, distancia: distancia, reconhecer: reconhecer };
  if (typeof module === "object" && module.exports) { module.exports = api; } else { raiz.Respostas = api; }
})(this);
