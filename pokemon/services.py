import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name):
    response = requests.get(URL + name.lower())
    
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'base_experience': data['base_experience']
        }
        
    return None

