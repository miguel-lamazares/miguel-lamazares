import os

# Caminho do README.md
readme_path = 'README.md'

# Função para alternar entre as animações
def toggle_animation():
    with open(readme_path, 'r') as file:
        content = file.read()

    # Verifica se a animação do Pac-Man está visível
    if "<!-- Animação Pac-Man -->" in content:
        # Se o Pac-Man estiver comentado, descomente e comente a Snake
        new_content = content.replace("<!-- Animação Pac-Man -->", "")
        new_content = new_content.replace("<!-- Animação Snake -->", "<!-- Animação Snake -->\n")

    elif "<!-- Animação Snake -->" in content:
        # Se a Snake estiver comentada, descomente e comente o Pac-Man
        new_content = content.replace("<!-- Animação Pac-Man -->", "<!-- Animação Pac-Man -->\n")
        new_content = new_content.replace("<!-- Animação Snake -->", "")

    # Salva as mudanças
    with open(readme_path, 'w') as file:
        file.write(new_content)

    print("Alternando animações!")

# Chama a função para alternar as animações
toggle_animation()