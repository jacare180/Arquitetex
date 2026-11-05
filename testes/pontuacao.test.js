const test = require("node:test");
const assert = require("node:assert");
const P = require("../js/pontuacao.js");
const R = require("../js/respostas.js");

test("Achado: faixas e zero", () => {
  assert.strictEqual(P.pontosAchado("Cartão-postal"), 10);
  assert.strictEqual(P.pontosAchado("Achado"), 100);
  assert.strictEqual(P.pontosAchado(null), 0);
  assert.throws(() => P.pontosAchado("Raro"));
});

test("Escala por ano", () => {
  assert.deepStrictEqual(P.pontosEscala("Ano", 1968, 1968), { pontos: 100, noPrumo: true });
  assert.strictEqual(P.pontosEscala("Ano", 1963, 1968).pontos, 80);
  assert.strictEqual(P.pontosEscala("Ano", 1943, 1968).pontos, 0);
  assert.strictEqual(P.pontosEscala("Ano", 1900, 1968).pontos, 0);
  assert.strictEqual(P.pontosEscala("Ano", 1969, 1968).pontos, 96);
});

test("Escala por medida", () => {
  assert.strictEqual(P.pontosEscala("Medida", 828, 828).noPrumo, true);
  assert.strictEqual(P.pontosEscala("Medida", 840, 828).noPrumo, true);   // 1,4% de erro
  assert.strictEqual(P.pontosEscala("Medida", 1656, 828).pontos, 37);     // o dobro
  assert.strictEqual(P.pontosEscala("Medida", 414, 828).pontos, 37);      // a metade
  assert.strictEqual(P.pontosEscala("Medida", 2484, 828).pontos, 0);      // o triplo
  assert.strictEqual(P.pontosEscala("Medida", 900, 828).pontos < 100, true);
});

test("Tempo esgotado vale 0", () => {
  assert.strictEqual(P.pontosEscala("Ano", null, 1968).pontos, 0);
  assert.strictEqual(P.pontosEscala("Medida", undefined, 100).pontos, 0);
});

test("Fração da obra", () => {
  assert.strictEqual(P.fracaoDaObra(700), 1);
  assert.strictEqual(P.fracaoDaObra(420), 0.6);
  assert.strictEqual(P.fracaoDaObra(0), 0);
});

test("Faixas da Escala", () => {
  assert.strictEqual(P.faixaEscala(100), "No prumo");
  assert.strictEqual(P.faixaEscala(99), "Na régua");
  assert.strictEqual(P.faixaEscala(37), "Esboço");
});

const lina = [
  { resposta: "Lina Bo Bardi", grafias: ["Lina", "Achillina Bo"] },
  { resposta: "Oscar Niemeyer", grafias: ["Niemeyer"] },
  { resposta: "Affonso Eduardo Reidy", grafias: ["Reidy", "Affonso Reidy"] }
];

test("Reconhecimento: acentos, maiúsculas e grafias", () => {
  assert.strictEqual(R.normalizar("  Edifício Itália! "), "edificio italia");
  assert.strictEqual(R.reconhecer("lina bo bardi", lina).tipo, "exata");
  assert.strictEqual(R.reconhecer("NIEMEYER", lina).escrita, "Oscar Niemeyer");
  assert.strictEqual(R.reconhecer("Affonso Reidy", lina).tipo, "exata");
});

test("Reconhecimento: erro pequeno pede confirmação", () => {
  const r = R.reconhecer("Niemayer", lina);
  assert.strictEqual(r.tipo, "parecida");
  assert.strictEqual(r.escrita, "Oscar Niemeyer");
});

test("Reconhecimento: palavra curta não aceita erro e resposta errada não passa", () => {
  assert.strictEqual(R.reconhecer("Lima", lina).tipo, "nenhuma");
  assert.strictEqual(R.reconhecer("Le Corbusier", lina).tipo, "nenhuma");
  assert.strictEqual(R.reconhecer("", lina).tipo, "nenhuma");
});
