import requests
import time

token = '11cbe5b64b79d3a50f0d1767de46de51'
host = 'https://api.pokemonbattle.me:9104'

answer = requests.post(f'{host}/pokemons', json =
                       {
        "name": "Zolly",
        "photo": "https://dolnikov.ru/pokemons/albums/060.png"
                       }, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(answer.text)

time.sleep(5)  # Задержка в 5 секунд

answer_name = requests.put(f'{host}/pokemons', json =
                        {
    "pokemon_id": "12679",
    "name": "Heimer",
    "photo": "https://dolnikov.ru/pokemons/albums/080.png"
                        },headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(answer_name.text)

time.sleep(9)  # Задержка в 5 секунд

answer_catch = requests.post(f'{host}/trainers/add_pokeball', json =
                        {
    "pokemon_id": "9779"
                        }, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(answer_catch.text)

