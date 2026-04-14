from django.shortcuts import render, redirect
from .utils import save_pokemon
from.models import Pokemon
from .stats import get_stats


# Create your views here.


def dashboard(request):
    pokemons = Pokemon.objects.all()
    stats = get_stats()
    
    return render(request, "dashboard.html",{
        "pokemons": pokemons,
        "stats": stats
    })
    

def add_pokemon(request):
    if request.method == "POST":
        name = request.POST.get("name")
        save_pokemon(name)
    
    return redirect("/")

