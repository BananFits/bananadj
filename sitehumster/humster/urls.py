

from django.urls import path, re_path, register_converter
from . import views
from. import converters

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about),
    path('kub/', views.kub, name='kub'),
    path('animals/', views.animals),
    path('cats/<int:cat_id>/', views.category,name='cat_id'),
    path('cats/<slug:cat_slug>/', views.category_slug, name='cat'),
    path("archive/<year4:year>/", views.archive, name='archive')

]
