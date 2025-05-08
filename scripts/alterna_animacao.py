# Caminho do README.md
readme_path = "README.md"

# Leitura do conteúdo do arquivo README.md
with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

# Blocos de código para Pacman e Snake
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

# Alternar entre os blocos
if pacman_block in content:
    content = content.replace(pacman_block, snake_block)
elif snake_block in content:
    content = content.replace(snake_block, pacman_block)

# Atualizando o README.md com o novo conteúdo
with open(readme_path, "w", encoding="utf-8") as file:
    file.write(content)

print("Conteúdo do README.md alterado com sucesso!")
