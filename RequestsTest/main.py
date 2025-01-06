import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '27ac718002e9d23712dfc31021f49c1a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

# Создание покемона
body_create_pokemon = {
    "name": "Цветочек",
    "photo_id": 1
}
response_create_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(response_create_pokemon.text)

# Получение ID созданного покемона
PO_ID = response_create_pokemon.json()['id']

# Изменение имени покемона
body_change_pokemon = {
    "pokemon_id": PO_ID,
    "name": "Ромашка",
    "photo_id": 1
}
response_change_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change_pokemon)
print(response_change_pokemon.text)

# Помещение покемона в покеболл
body_pokemon_in_pokeball = {
    "pokemon_id": PO_ID
}
response_pokemon_in_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokemon_in_pokeball)
print(response_pokemon_in_pokeball.text)



