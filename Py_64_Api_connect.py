#let's get pokemon info?
#pokimon api
import requests #need to install it
base_link = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f'{base_link}/pokemon/{pokimon_name}'
    response = requests.get(url)
    #print(response) prints repsonse cod n stuff

    if response.status_code == 200:
        pokemon_data =response.json()
        print("Data retrived!")
        return  pokemon_data
    else:
        print(f"Data retrival failed {response.status_code}")

pokimon_name = "pikachu"
pokemon_info = get_pokemon_info(pokimon_name)

if pokemon_info:
    print(f'Name: {pokemon_info["name"].capitalize()}')
    print(f'Id: {pokemon_info["id"]}')
    print(f'Height: {pokemon_info["height"]}')
    print(f'Weight: {pokemon_info["weight"]}')
