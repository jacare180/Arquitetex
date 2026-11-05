// Obras que crescem. Cada obra é uma lista de traços; a tinta chega a eles numa ordem sorteada pelo dia,
// e o relevo mostra só algumas pistas. Provisório: os croquis definitivos ainda vão ser desenhados.
(function (raiz) {
  "use strict";

  var NS = "http://www.w3.org/2000/svg";

  function masp() {
    var t = ["M20 262 H620", "M118 96 V262", "M146 96 V262", "M494 96 V262", "M522 96 V262",
      "M104 96 H536", "M104 112 H536", "M104 152 H536", "M104 166 H536", "M118 112 V200 H522 V112"];
    for (var x = 160; x <= 480; x += 16) { t.push("M" + x + " 116 V196"); }                 // caixilhos
    [126, 140, 182, 192].forEach(function (y) { t.push("M150 " + y + " H490"); });
    for (var h = 0; h < 18; h++) { var hx = 160 + h * 19; t.push("M" + hx + " 206 L" + (hx + 14) + " 218"); } // sombra no vão
    for (var p = 0; p < 9; p++) { var px = 40 + p * 70; t.push("M" + px + " 270 H" + (px + 40)); }            // calçada da Paulista
    [[230, 262], [262, 262], [300, 262], [360, 262], [410, 262], [446, 262]].forEach(function (g) {          // gente no belvedere
      t.push("M" + g[0] + " " + g[1] + " V" + (g[1] - 16) + " M" + (g[0] - 4) + " " + (g[1] - 10) + " H" + (g[0] + 4));
      t.push("M" + (g[0] - 2.5) + " " + (g[1] - 19) + " a2.5 2.5 0 1 0 5 0 a2.5 2.5 0 1 0 -5 0");
    });
    [[50, 262], [580, 262], [608, 262]].forEach(function (a) {                                   // árvores
      t.push("M" + a[0] + " " + a[1] + " V" + (a[1] - 46));
      t.push("M" + (a[0] - 20) + " " + (a[1] - 40) + " Q" + a[0] + " " + (a[1] - 96) + " " + (a[0] + 20) + " " + (a[1] - 40) + " Q" + a[0] + " " + (a[1] - 28) + " " + (a[0] - 20) + " " + (a[1] - 40));
      t.push("M" + (a[0] - 10) + " " + (a[1] - 52) + " Q" + a[0] + " " + (a[1] - 64) + " " + (a[0] + 10) + " " + (a[1] - 52));
    });
    for (var v = 0; v < 6; v++) { t.push("M" + (130 + v * 2) + " " + (100 + v * 10) + " H" + (134 + v * 2)); } // textura do concreto
    for (var c = 0; c < 6; c++) { t.push("M" + (500 + c * 2) + " " + (100 + c * 10) + " H" + (504 + c * 2)); }
    t.push("M90 262 L104 246 L118 262", "M560 238 H600 M560 238 V262 M600 238 V262");
    return t;
  }

  function catedral() {
    var t = ["M20 262 H620", "M206 262 Q320 252 434 262"];
    var n = 16;
    for (var i = 0; i < n; i++) {                                     // colunas: abrem na base, estreitam no anel e se abrem no topo
      var th = Math.PI * (i + 0.5) / n, c = Math.cos(th), sn = Math.sin(th);
      var bx = 320 + 112 * c, wx = 320 + 26 * Math.cos(th + 0.5), tx = 320 + 64 * Math.cos(th + 0.9);
      var ty = 64 - 10 * sn;
      t.push("M" + bx.toFixed(1) + " 262 Q" + wx.toFixed(1) + " 150 " + tx.toFixed(1) + " " + ty.toFixed(1));
      t.push("M" + tx.toFixed(1) + " " + ty.toFixed(1) + " l" + (8 * c).toFixed(1) + " -14");
    }
    t.push("M282 148 Q320 156 358 148", "M286 132 Q320 138 354 132");  // o anel que une as colunas
    for (var k = 0; k < 12; k++) {                                     // vitrais entre as colunas
      var x = 236 + k * 15;
      t.push("M" + x + " 240 Q" + (320 + (x - 320) * 0.25) + " 160 " + (320 + (x - 320) * 0.5) + " 96");
    }
    for (var e = 0; e < 10; e++) { t.push("M" + (60 + e * 12) + " 272 H" + (70 + e * 12)); t.push("M" + (470 + e * 12) + " 272 H" + (480 + e * 12)); } // espelho d'água
    t.push("M540 262 V150", "M528 262 V150", "M528 150 H540", "M522 170 H546", "M534 150 V138");                // campanário
    for (var s = 0; s < 8; s++) { t.push("M528 " + (180 + s * 10) + " H540"); }
    [[110, 262], [150, 262], [470, 262], [600, 262]].forEach(function (g) {
      t.push("M" + g[0] + " " + g[1] + " V" + (g[1] - 16) + " M" + (g[0] - 4) + " " + (g[1] - 10) + " H" + (g[0] + 4));
      t.push("M" + (g[0] - 2.5) + " " + (g[1] - 19) + " a2.5 2.5 0 1 0 5 0 a2.5 2.5 0 1 0 -5 0");
    });
    for (var a = 0; a < 6; a++) { t.push("M" + (250 + a * 25) + " 262 L" + (260 + a * 25) + " 250"); }          // rampa de entrada
    return t;
  }

  function copan() {
    var t = ["M20 262 H620"];
    var andares = 34;
    for (var i = 0; i <= andares; i++) {                               // os brises em onda, um por andar
      var y = 250 - i * 6;
      t.push("M90 " + y + " C210 " + (y - 14) + " 300 " + (y + 16) + " 400 " + y + " S530 " + (y - 12) + " 560 " + y);
    }
    t.push("M90 250 V46", "M560 250 V46", "M90 46 C210 32 300 62 400 46 S530 34 560 46");
    for (var v = 0; v < 12; v++) { var x = 110 + v * 38; t.push("M" + x + " 252 V262"); }                       // galeria no térreo
    for (var c = 0; c < 8; c++) { t.push("M" + (40 + c * 72) + " 272 H" + (70 + c * 72)); }                    // calçada
    [[40, 262], [600, 262]].forEach(function (a) {
      t.push("M" + a[0] + " " + a[1] + " V" + (a[1] - 46));
      t.push("M" + (a[0] - 18) + " " + (a[1] - 40) + " Q" + a[0] + " " + (a[1] - 92) + " " + (a[0] + 18) + " " + (a[1] - 40) + " Q" + a[0] + " " + (a[1] - 28) + " " + (a[0] - 18) + " " + (a[1] - 40));
    });
    [[200, 262], [240, 262], [470, 262]].forEach(function (g) {
      t.push("M" + g[0] + " " + g[1] + " V" + (g[1] - 16) + " M" + (g[0] - 4) + " " + (g[1] - 10) + " H" + (g[0] + 4));
    });
    for (var w = 0; w < 30; w++) { var wx = 104 + (w % 15) * 30, wy = (w < 15 ? 70 : 150); t.push("M" + wx + " " + wy + " V" + (wy + 8)); } // vãos de janela
    return t;
  }

  function torre() {
    var t = ["M40 440 H260", "M110 440 V80", "M190 440 V80"];
    for (var i = 0; i < 18; i++) {
      var y = 420 - i * 19;
      t.push("M110 " + y + " H190");
      t.push("M124 " + (y + 4) + " V" + (y + 14) + " M150 " + (y + 4) + " V" + (y + 14) + " M176 " + (y + 4) + " V" + (y + 14));
    }
    t.push("M110 80 L150 36 L190 80", "M150 36 V12");
    return t;
  }

  var DESENHOS = {
    masp: { nome: "Museu de Arte de São Paulo", legenda: "Lina Bo Bardi, 1968, vão livre de 74 m", viewBox: "0 0 640 300", tracos: masp(), ordem: "sorteada" },
    catedral: { nome: "Catedral de Brasília", legenda: "Oscar Niemeyer, 1970, dezesseis colunas de concreto", viewBox: "0 0 640 300", tracos: catedral(), ordem: "sorteada" },
    copan: { nome: "Edifício Copan", legenda: "Oscar Niemeyer, 1966, 115 m de altura", viewBox: "0 0 640 300", tracos: copan(), ordem: "sorteada" },
    torre: { nome: "Torre", legenda: "Torre provisória, um pavimento a cada 35 pontos", viewBox: "0 0 300 460", tracos: torre(), ordem: "em-ordem" }
  };
  var DO_ACHADO = ["masp", "catedral", "copan"];

  function embaralhar(lista, semente) {
    var a = semente >>> 0, l = lista.slice();
    function rnd() { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }
    for (var i = l.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)); var x = l[i]; l[i] = l[j]; l[j] = x; }
    return l;
  }

  // Monta o SVG: pistas em relevo (algumas) e a tinta por cima.
  // fracaoInicial já sai entintada sem animação; entintar(f) anima até a nova fração, traço por traço.
  function montar(alvo, chave, semente, fracaoInicial) {
    var d = DESENHOS[chave];
    alvo.innerHTML = "";
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", d.viewBox);
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", "Desenho da obra do dia");
    svg.setAttribute("class", "obra-svg");
    var camadas = {};
    [["luz", "-0.8 -0.8"], ["sombra", "0.8 0.8"], ["tinta", "0 0"]].forEach(function (c) {
      var g = document.createElementNS(NS, "g");
      g.setAttribute("class", "camada-" + c[0]);
      g.setAttribute("transform", "translate(" + c[1] + ")");
      svg.appendChild(g);
      camadas[c[0]] = g;
    });
    var ordem = d.ordem === "sorteada" ? embaralhar(d.tracos, semente || 1) : d.tracos.slice();
    var pistas = {};
    if (d.ordem === "sorteada") {
      embaralhar(d.tracos.map(function (_, i) { return i; }), (semente || 1) + 7).slice(0, Math.round(d.tracos.length * 0.12)).forEach(function (i) { pistas[d.tracos[i]] = true; });
      pistas[d.tracos[0]] = true; // a linha do chão
    }
    var tinta = [];
    ordem.forEach(function (tr) {
      if (pistas[tr] || (d.ordem !== "sorteada" && d.tracos.indexOf(tr) < 3)) {
        ["luz", "sombra"].forEach(function (c) {
          var p = document.createElementNS(NS, "path"); p.setAttribute("d", tr); camadas[c].appendChild(p);
        });
      }
      var pt = document.createElementNS(NS, "path");
      pt.setAttribute("d", tr); pt.setAttribute("pathLength", "1");
      camadas.tinta.appendChild(pt); tinta.push(pt);
    });
    alvo.appendChild(svg);

    var feitos = 0;
    function quantos(f) { return Math.round(Math.max(0, Math.min(1, f)) * tinta.length); }
    feitos = quantos(fracaoInicial || 0);
    tinta.forEach(function (p, i) { p.style.transition = "none"; p.style.strokeDashoffset = i < feitos ? "0" : "1"; });

    return {
      nome: d.nome,
      legenda: d.legenda,
      total: tinta.length,
      // devolve quantos traços novos ganharam tinta
      entintar: function (fracao) {
        var alvoN = quantos(fracao), novos = alvoN - feitos;
        var reduz = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        for (var i = feitos; i < alvoN; i++) {
          var p = tinta[i];
          p.style.transition = reduz ? "none" : "stroke-dashoffset 520ms cubic-bezier(.2,.7,.2,1) " + ((i - feitos) * 140) + "ms";
          p.getBoundingClientRect();
          p.style.strokeDashoffset = "0";
        }
        feitos = Math.max(feitos, alvoN);
        return Math.max(0, novos);
      }
    };
  }

  raiz.Desenhos = { montar: montar, DESENHOS: DESENHOS, DO_ACHADO: DO_ACHADO };
})(this);
