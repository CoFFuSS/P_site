from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *

menu = ["о сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):  # HttpRequest
    posts = Main.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'menu' : menu, 'title' : 'Главная страница'})

def about(request):  # HttpRequest
    return render(request, 'main/about.html', {'menu' : menu, 'title' : 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    
    return HttpResponse(f"<h1>Архив по годам<h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')