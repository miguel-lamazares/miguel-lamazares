import os
import random

# Diretório onde estão os GIFs
gif_directory = "gif"

# Nome do arquivo README.md
readme_file = "README.md"

# Identificador do container no README
container_id = "gif-conteiner"

# Lista todos os arquivos GIF no diretório
gif_files = [f for f in os.listdir(gif_directory) if f.endswith(".gif")]

if not gif_files:
    print("Nenhum GIF encontrado no diretório de GIFs.")
    exit(1)

# Escolhe um GIF aleatório
random_gif = random.choice(gif_files)

# Atualiza o conteúdo do README
with open(readme_file, "r") as file:
    content = file.readlines()

# Substituir a linha contendo o GIF pelo novo
with open(readme_file, "w") as file:
    for line in content:
        if f'id="{container_id}"' in line:
            start = line.find('src="') + len('src="')
            end = line.find('"', start)
            updated_line = line[:start] + f"{gif_directory}/{random_gif}" + line[end:]
            file.write(updated_line)
        else:
            file.write(line)

print(f"README atualizado com o GIF: {random_gif}")import os
import random
import shutil

# Diretório onde estão os GIFs
gif_directory = "gif"

# Nome do GIF principal
principal_gif = "gif/principal.gif"

# Lista todos os arquivos GIF no diretório, exceto o principal.gif
gif_files = [f for f in os.listdir(gif_directory) if f.endswith(".gif") and f != "principal.gif"]

if not gif_files:
    print("Nenhum GIF disponível para seleção.")
    exit(1)

# Escolhe um GIF aleatório
random_gif = random.choice(gif_files)

# Copia o GIF selecionado para substituir o principal.gif
shutil.copy(os.path.join(gif_directory, random_gif), principal_gif)

print(f"principal.gif atualizado para: {random_gif}")