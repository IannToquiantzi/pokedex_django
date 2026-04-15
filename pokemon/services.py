import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name):
    response = requests.get(URL + name.lower())
    
    if response.status_code == 200:
        return response.json()
        
    return None

