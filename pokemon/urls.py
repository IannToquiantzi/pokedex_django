from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),   # página principal
    path('add/', views.add_pokemon, name='add_pokemon'),  # agregar pokemon
]
