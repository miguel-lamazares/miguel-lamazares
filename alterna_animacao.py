import os

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

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

# Alternar
if pacman_block in content:
    content = content.replace(pacman_block, snake_block)
elif snake_block in content:
    content = content.replace(snake_block, pacman_block)

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(content)
