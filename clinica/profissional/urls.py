from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="indexProfissional"),
    path("criarProfissional/", views.add_profissional, name="criarProfissional"),
   # path("mostrardetalhes/<str:username>/", views.mostrardetalhes, name="mostrardetalhes")
    path("alterarInformacao/<int:id>/", views.alterarInformacao, name="alterarInformacao"),
    path('alterarSenha/<str:username>/', views.editSenha, name="alterarSenha"),
]