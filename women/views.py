from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forns import AddPostForm
from .models import *


def index(request):
    posts = Women.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404
    context = {
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
