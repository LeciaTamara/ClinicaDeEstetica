from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="indexProfissional"),
    path("criarProfissional/", views.add_profissional, name="criarProfissional"),
<<<<<<< HEAD
    path('deletarContaProfissional/<str:username>/', views.deletarContaProfissional, name='deletarContaProfissional'),
=======
    path('alterarSenha/<str:username>/', views.editSenha, name="alterarSenha"),
    path("deletarContaProfissional/", views.deletarContaProfissional, name="deletarContaProfissional"),
>>>>>>> 063b0a25733742030d958f917ce817d37c3aa46e
    path("editarDadosProfissional/", views.editarDadosProfissional, name="editarDadosProfissional"),
    path("verProfissional/", views.verProfissional, name="verProfissional"),
    path("redirecionaParaIndexClinica/", views.redirecionaParaIndexClinica, name = "redirecionaParaIndexClinica"),
    path("logout/", views.realizarLogout, name="lougout"),
]