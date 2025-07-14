from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="indexProfissional"),
    path("criarProfissional/", views.add_profissional, name="criarProfissional"),
    path('alterarSenha/<str:username>/', views.editSenha, name="alterarSenha"),
    path("deletarContaProfissional/", views.deletarContaProfissional, name="deletarContaProfissional"),
    path("editarDadosProfissional/", views.editarDadosProfissional, name="editarDadosProfissional"),
    path("verProfissional/", views.verProfissional, name="verProfissional"),
    path("redirecionaParaIndexClinica/", views.redirecionaParaIndexClinica, name = "redirecionaParaIndexClinica"),
]