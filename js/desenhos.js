// Obras que crescem. Cada desenho é uma lista de traços na ordem em que recebem tinta.
// Provisório: os croquis definitivos ainda vão ser desenhados.
(function (raiz) {
  "use strict";

  var NS = "http://www.w3.org/2000/svg";

  var DESENHOS = {
    masp: {
      nome: "Museu de Arte de São Paulo",
      legenda: "Lina Bo Bardi, 1968, vão livre de 74 m",
      viewBox: "0 0 640 300",
      tracos: [
        "M30 252 H610",
        "M118 236 H522", "M118 230 V242", "M522 230 V242",
        "M118 96 V252", "M146 96 V252", "M494 96 V252", "M522 96 V252",
        "M104 96 H536", "M104 112 H536",
        "M104 152 H536", "M104 166 H536",
        "M118 112 V200 H522 V112",
        "M118 200 L130 214 H510 L522 200",
        "M150 124 H490", "M150 138 H490", "M150 180 H490", "M150 190 H490",
        "M190 124 V190", "M250 124 V190", "M310 124 V190", "M370 124 V190", "M430 124 V190",
        "M70 252 V230 Q76 214 82 230 V252",
        "M300 252 V236 M300 236 a3 3 0 1 0 0.1 0 M296 244 L304 244",
        "M352 252 V238 M352 238 a3 3 0 1 0 0.1 0",
        "M580 252 V200 M560 210 Q580 160 600 210 Q580 222 560 210"
      ]
    },
    torre: {
      nome: "Torre",
      legenda: "Torre provisória, um pavimento a cada 35 pontos",
      viewBox: "0 0 300 460",
      tracos: (function () {
        var t = ["M40 440 H260", "M110 440 V80", "M190 440 V80"];
        for (var i = 0; i < 18; i++) {
          var y = 420 - i * 19;
          t.push("M110 " + y + " H190");
          t.push("M124 " + (y + 4) + " V" + (y + 14) + " M150 " + (y + 4) + " V" + (y + 14) + " M176 " + (y + 4) + " V" + (y + 14));
        }
        t.push("M110 80 L150 36 L190 80", "M150 36 V12");
        return t;
      })()
    }
  };

  // Monta o SVG em três camadas: luz e sombra (o relevo) e a tinta por cima.
  function montar(alvo, chave) {
    var d = DESENHOS[chave];
    alvo.innerHTML = "";
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", d.viewBox);
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", d.nome);
    svg.setAttribute("class", "obra-svg");
    var camadas = {};
    [["luz", "-0.8 -0.8"], ["sombra", "0.8 0.8"], ["tinta", "0 0"]].forEach(function (c) {
      var g = document.createElementNS(NS, "g");
      g.setAttribute("class", "camada-" + c[0]);
      g.setAttribute("transform", "translate(" + c[1] + ")");
      svg.appendChild(g);
      camadas[c[0]] = g;
    });
    var tinta = [];
    d.tracos.forEach(function (tr) {
      ["luz", "sombra", "tinta"].forEach(function (c) {
        var p = document.createElementNS(NS, "path");
        p.setAttribute("d", tr);
        p.setAttribute("pathLength", "1");
        camadas[c].appendChild(p);
        if (c === "tinta") { tinta.push(p); }
      });
    });
    alvo.appendChild(svg);
    return {
      nome: d.nome,
      legenda: d.legenda,
      // fracao de 0 a 1: quanto da obra já tem tinta
      entintar: function (fracao) {
        var n = tinta.length;
        tinta.forEach(function (p, i) {
          var local = Math.max(0, Math.min(1, fracao * n - i));
          p.style.strokeDashoffset = String(1 - local);
        });
      }
    };
  }

  raiz.Desenhos = { montar: montar, DESENHOS: DESENHOS };
})(this);
