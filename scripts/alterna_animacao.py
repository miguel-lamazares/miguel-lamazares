import datetime

readme_path = "README.md"

pacman_block = '''<div id="pacman">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/miguel-lamazares/miguel-lamazares/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/miguel-lamazares/miguel-lamazares/output/pacman-contribution-graph.svg">
  <img alt="pacman contribution graph" src="https://raw.githubusercontent.com/miguel-lamazares/miguel-lamazares/output/pacman-contribution-graph.svg">
</picture>
</div>'''

snake_block = '''<div id="snake" align="center">
<img src="https://raw.githubusercontent.com/miguel-lamazares/miguel-lamazares/output/snake.svg" alt="Snake animation" />
</div>'''

with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

# Hora UTC
hora = datetime.datetime.utcnow().hour

# Decide qual bloco mostrar
if hora % 4 == 0:
    bloco = snake_block
elif hora % 2 == 0:
    bloco = pacman_block
else:
    bloco = ""

# Atualiza a seção entre os marcadores
inicio = content.find("<!--animacoes-->") + len("<!--animacoes-->")
fim = content.find("<!--fim-animacoes-->")

novo_conteudo = content[:inicio] + "\n" + bloco + "\n" + content[fim:]

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(novo_conteudo)
