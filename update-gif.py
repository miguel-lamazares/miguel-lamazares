import os
import random
import shutil
from datetime import datetime

# Diretório onde estão os GIFs
gif_directory = "gif"

# Nome do GIF principal (fixo)
principal_gif = os.path.join(gif_directory, "principal.gif")

# Verifica se o diretório de GIFs existe
if not os.path.exists(gif_directory):
    print(f"❌ Diretório '{gif_directory}' não encontrado.")
    exit(1)

# Lista todos os arquivos GIF no diretório, exceto o principal.gif
gif_files = [
    f for f in os.listdir(gif_directory)
    if f.endswith(".gif") and f != "principal.gif"
]

if not gif_files:
    print("❌ Nenhum GIF disponível para seleção.")
    exit(1)

# Escolhe um GIF aleatório
random_gif = random.choice(gif_files)
source_path = os.path.join(gif_directory, random_gif)

# Verifica se o arquivo de origem existe e não está vazio
if not os.path.isfile(source_path):
    print(f"❌ Arquivo de origem não encontrado: {source_path}")
    exit(1)

if os.path.getsize(source_path) == 0:
    print(f"❌ Arquivo de origem está vazio: {source_path}")
    exit(1)

# Substitui o principal.gif
try:
    # Remove o anterior (boa prática para garantir substituição limpa)
    if os.path.exists(principal_gif):
        os.remove(principal_gif)

    shutil.copy(source_path, principal_gif)

    # Verifica se o novo arquivo não está vazio
    if os.path.getsize(principal_gif) == 0:
        print("❌ Erro: principal.gif foi criado, mas está vazio.")
        exit(1)

    print(f"✅ principal.gif atualizado para: {random_gif}")

    # (Opcional) Registrar log de atualização
    with open("gif_update_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] principal.gif atualizado para: {random_gif}\n")

except Exception as e:
    print(f"❌ Erro ao copiar de {source_path} para {principal_gif}: {e}")
    exit(1)
