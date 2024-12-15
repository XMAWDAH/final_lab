from django.shortcuts import render
from django.http import HttpResponse
from .models import Developer,Game

def home(request):
    return render(request, 'app1/home.html')

def list_game(request):
    games = Game.objects.all()
    return render(request, 'app1/list_games.html', {'games': games})
