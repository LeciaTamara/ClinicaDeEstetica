from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="indexProfissional"),
    path("criarProfissional/", views.add_profissional, name="criarProfissional"),
    path('deletarContaProfissional/', views.deletarContaProfissional, name='deletarContaProfissional'),
    path('alterarSenha/<str:username>/', views.editSenha, name='alterarSenha'),
    path("editarDadosProfissional/", views.editarDadosProfissional, name="editarDadosProfissional"),
    path("verProfissional/", views.verProfissional, name="verProfissional"),
    path("redirecionaParaIndexClinica/", views.redirecionaParaIndexClinica, name = "redirecionaParaIndexClinica"),
    path("logout/", views.realizarLogout, name="lougout"),
    path('excluirConta/<str:username>/', views.deletarContaProfissional, name='excluirConta'),
]