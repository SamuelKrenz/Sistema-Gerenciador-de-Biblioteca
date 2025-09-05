from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros),
    path('salva_livros', views.salva_livros)
]