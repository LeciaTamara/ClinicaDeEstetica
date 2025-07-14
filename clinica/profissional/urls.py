from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="indexProfissional"),
    path("criarProfissional/", views.add_profissional, name="criarProfissional"),
   # path("mostrardetalhes/<str:username>/", views.mostrardetalhes, name="mostrardetalhes")
    path("editarDadosProfissional/<str:username>/", views.alterarInformacao, name="alterarInformacao"),
]