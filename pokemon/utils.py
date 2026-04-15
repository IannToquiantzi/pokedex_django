from .models import Pokemon
from .services import get_pokemon

def save_pokemon(name):
    data = get_pokemon(name)
    
    if not data:
        print("No se encontró el Pokémon")
        return None

    try:
        tipo = data['types'][0]['type']['name']
        imagen = data['sprites']['front_default']
        nombre = data['name']
        height = data.get('height')
        weight = data.get('weight')
        base_experience = data.get('base_experience')
        
    except (KeyError, IndexError):
        print("Error en estructura de API")
        return None

    pokemon, created = Pokemon.objects.get_or_create(
        nombre=nombre,
        defaults={
            "tipo": tipo,
            "imagen": imagen,
            "height": height,
            "weight": weight,
            "base_experience": base_experience
            
        }
    )
    
    return pokemon