import requests

pokemon_id = 0
def get_gif(pokemon_id: int):
    x = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{pokemon_id}.gif"
    response = requests.get(x)
    if response.status_code == 200:
        with open(f"{pokemon_id}.gif", "wb") as f:
            f.write(response.content)
        print(f"GIF for Pokemon ID {pokemon_id} saved successfully.")
    else:
        print(f"Failed to retrieve GIF for Pokemon ID {pokemon_id}. Status code: {response.status_code}")



for pokemon_id in range(1,651): 
    get_gif(pokemon_id)

# why is there too many pokemons? 