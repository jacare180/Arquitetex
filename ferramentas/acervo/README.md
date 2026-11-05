Coleta do acervo de obras
=========================

Scripts que montaram a aba "Acervo de obras" da planilha a partir da Wikipedia.

1. `obras.py`: a lista de obras (id, nome, cidade, país, tipo e títulos das páginas em português e inglês).
2. `fetch_raw.py`: baixa o texto de cada página para `cache/` (segue redirecionamentos).
3. `fetch_views.py`: baixa as visualizações dos últimos 12 meses (lento, o servidor limita).
4. `parse.py`: lê a ficha técnica de cada página.
5. `overrides.py`: correções feitas à mão (anos, arquitetos, estilos).
6. `verify.py`: confere se cada correção aparece no texto da página de origem.
7. `build.py`: padroniza unidades e gera `acervo.json`.

Rodar de dentro desta pasta: `python3 fetch_raw.py && python3 parse.py && python3 verify.py && python3 build.py`.
O `cache/` não vai para o repositório.
