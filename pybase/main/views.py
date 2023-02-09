from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):  # HttpRequest
    posts = Main.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'main/index.html', context=context)


def about(request):  # HttpRequest
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Main, slug=post_slug)
    
    context = {
        'post' : post,
        'menu' : menu,
        'title' : post.title,
        'cat_selected' : post.cat_id,
    }
    
    return render(request, 'main/post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Main.objects.filter(cat_id = cat[0].id)

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat[0].id,
    }
    return render(request, 'main/index.html', context=context)
