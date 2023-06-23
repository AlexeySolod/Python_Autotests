import requests
import pytest 

host = 'https://api.pokemonbattle.me:9104'
token = '11cbe5b64b79d3a50f0d1767de46de51'

def test_status_code():
    trainers_info = requests.get(f'{host}/trainers', params = {'trainer_id':4242})
    assert trainers_info.status_code == 200

def test_trainer_name():
    trainer_body = requests.get(f'{host}/trainers', params = {'trainer_id' :4242})
    assert trainer_body.json()['trainer_name'] == 'Solid Snake'