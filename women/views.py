from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('Страница нового приложения')


def categories(request, cat_id):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1> Статьи по категориям </h1><p>{cat_id}<p>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')