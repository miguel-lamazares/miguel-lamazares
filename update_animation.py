import os

# Caminho do README.md
readme_path = 'README.md'

def toggle_animation():
    """
    Alterna entre as animações do Pac-Man e Snake no README.md.
    Se o Pac-Man estiver visível, ele será comentado, e a Snake será descomentada, e vice-versa.
    """
    try:
        # Verifica se o arquivo README.md existe
        if not os.path.exists(readme_path):
            raise FileNotFoundError(f"Arquivo '{readme_path}' não encontrado.")

        # Lê o conteúdo do README.md
        with open(readme_path, 'r') as file:
            content = file.read()

        # Verifica e alterna entre as animações
        if "<!-- Animação Pac-Man -->" in content:
            # Alterna para Snake
            print("Descomentando Snake e comentando Pac-Man.")
            new_content = content.replace("<!-- Animação Pac-Man -->", "")
            new_content = new_content.replace("<!-- Animação Snake -->", "<!-- Animação Snake -->\n")
        elif "<!-- Animação Snake -->" in content:
            # Alterna para Pac-Man
            print("Descomentando Pac-Man e comentando Snake.")
            new_content = content.replace("<!-- Animação Pac-Man -->", "<!-- Animação Pac-Man -->\n")
            new_content = new_content.replace("<!-- Animação Snake -->", "")
        else:
            raise ValueError("Nenhuma das animações foi encontrada no README.md.")

        # Salva as alterações no README.md
        with open(readme_path, 'w') as file:
            file.write(new_content)

        print("Animação alternada com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao alternar animações: {e}")

# Executa a função
if __name__ == "__main__":
    toggle_animation()
