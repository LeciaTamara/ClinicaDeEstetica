from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="indexProfissional"),
    path("criarProfissional/", views.criarProfissional, name="criarProfissional"),
   # path("mostrardetalhes/<str:username>/", views.mostrardetalhes, name="mostrardetalhes")
    path("alterarInformacao/<int:id>/", views.alterarInformacao, name="alterarInformacao"),
]