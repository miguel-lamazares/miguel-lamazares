import os
import random
import shutil

# Diretório onde estão os GIFs
gif_directory = "gif"

# Nome do GIF principal (fixo)
principal_gif = os.path.join(gif_directory, "principal.gif")

# Verifica se o diretório de GIFs existe
if not os.path.exists(gif_directory):
    print(f"Diretório '{gif_directory}' não encontrado.")
    exit(1)

# Lista todos os arquivos GIF no diretório, exceto o principal.gif
gif_files = [f for f in os.listdir(gif_directory) if f.endswith(".gif") and f != "principal.gif"]

if not gif_files:
    print("Nenhum GIF disponível para seleção.")
    exit(1)

# Escolhe um GIF aleatório
random_gif = random.choice(gif_files)

# Copia o GIF selecionado para substituir o principal.gif
try:
    shutil.copy(os.path.join(gif_directory, random_gif), principal_gif)
    print(f"principal.gif atualizado para: {random_gif}")
except Exception as e:
    print(f"Erro ao atualizar principal.gif: {e}")
    exit(1)