
from django.urls import path

from . import views


urlpatterns = [
    path("index/", views.index, name="indexClinica"),
    path("addClinica/", views.addClinica, name="adicionaClinica"),
    path("mostrarSobre/", views.mostrarSobre, name="mostrarSobre"),
    path("atualizarClinica/", views.atualizarClinica, name="atualizarClinica"),
    path("login/", views.login_usuario, name="login"), 
    path('redirecionarParaAdministrador/', views.redirecionarParaAdministrador, name='redirecionarParaAdministrador'), 
    path('redirecionarParaCliente/', views.redirecionarParaCliente, name='redirecionarParaCliente'),
    path('redirecionaParaProfissional/', views.redirecionaParaProfissional, name="redirecionaParaProfissional")
]