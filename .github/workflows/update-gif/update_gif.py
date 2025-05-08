import os
import random

# Caminho para a pasta com os GIFs
gif_folder = 'gif'
gif_files = [f for f in os.listdir(gif_folder) if f.endswith('.gif')]

# Escolher um GIF aleatório
random_gif = random.choice(gif_files)

# Caminho para o README.md
readme_path = 'README.md'

# Substituir a imagem no README
with open(readme_path, 'r') as file:
    content = file.read()

# Substituir o link do GIF no README
new_content = content.replace("gif/1.gif", f"gif/{random_gif}")

# Salvar a alteração no README
with open(readme_path, 'w') as file:
    file.write(new_content)

print(f"Atualizado para o GIF {random_gif}")
