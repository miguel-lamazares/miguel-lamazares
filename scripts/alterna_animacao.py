import datetime
import os

# Caminho do arquivo README
readme_path = "README.md"

# Ler o conteúdo do README
with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

# Definir os blocos de HTML das animações
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

# Obter a hora atual
now = datetime.datetime.now()
current_hour = now.hour

# Alternar entre as animações com base nas faixas de horário
if current_hour >= 0 and current_hour < 2:
    new_block = snake_block  # De 00:00 a 01:59, a animação é a da cobra
elif current_hour >= 2 and current_hour < 4:
    new_block = pacman_block  # De 02:00 a 03:59, a animação é o pacman
elif current_hour >= 4 and current_hour < 6:
    new_block = snake_block  # De 04:00 a 05:59, a animação é a da cobra
elif current_hour >= 6 and current_hour < 8:
    new_block = pacman_block  # De 06:00 a 07:59, a animação é o pacman
else:
    new_block = snake_block  # Caso contrário, vamos alternando com a cobra (ajustar conforme necessário)

# Substituir o bloco dentro da seção <!--animacoes-->
start_index = content.find("<!--animacoes-->") + len("<!--animacoes-->")
end_index = content.find("<!--/animacoes-->")

if start_index != -1 and end_index != -1:
    content = content[:start_index] + "\n" + new_block + "\n" + content[end_index:]
else:
    print("A seção <!--animacoes--> não foi encontrada no README.")

# Escrever o conteúdo de volta no README
with open(readme_path, "w", encoding="utf-8") as file:
    file.write(content)
