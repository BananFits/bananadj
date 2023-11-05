from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect, \
    HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'humster/index.html')

def animals(request):
    return render(request, 'humster/animals.html')
def about(request):
    return render(request, 'humster/about.html')

def kub(request):
    return render(request, 'humster/3D_cub.html')

def category(request, cat_id):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p> Хомячок номер -<b>{cat_id}</b> </p>' )

def category_slug(request, cat_slug):
    return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p>  категория -<b>{cat_slug}</b> </p>' )

def archive(request, year,):
    if year > 2023:
        3/0
        uri = reverse('cat', args=('sport', ))
        return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def SFASFGAS(request):
    3/0
    return HttpResponse(f"<h1>asqsdhdsfh1<h1><p>slug: {3 / 0}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def page(request):
    return HttpResponseServerError("<h1>ПРОСТИ, ДУРАК!<h1>")



