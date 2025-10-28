import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon():
    inputpokemon = input("enter pokemon: ")
    url = base_url + inputpokemon
    print(url)
    response = requests.get(url)
    structured_data = response.json()
    print(structured_data['id'])
get_pokemon()
