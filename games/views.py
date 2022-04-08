from django.shortcuts import render
from django.views.generic import ListView
from games.models import Game

def home(request):
    return render(request,'home.html')

class GameListView(ListView):
    model=Game
    template_name='games/home.html'
    context_object_name='game_list'
