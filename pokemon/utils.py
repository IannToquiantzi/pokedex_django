from .models import Pokemon
from .services import get_pokemon

def save_pokemon(name):
    data = get_pokemon(name)
    
    if not data:
        return None
    
    pokemon, created = Pokemon.objects.get_or_create(
        name=data['name'],
        defaults=data
    )
    
    return pokemon