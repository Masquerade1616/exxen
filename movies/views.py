from multiprocessing import context
from django.shortcuts import render
from .models import *     #  modelsi import ediyoruz * eklıyerek hepsini alıyoruz
# Create your views here.

    #   oluşturdugumuz clasa admın panelınden ekledıklerımızı viewste göstermemiz gerekiyor bunun için gereklı kodlar

def index(request):
    filmler = Movie.objects.all()
    context = {
        'filmler':filmler
    }
    return render(request, 'exxen.html', context)
