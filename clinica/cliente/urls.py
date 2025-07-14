from django.urls import path
from .import views
from clinicaEstetica.views import login_usuario

urlpatterns = [
    path("login/", login_usuario, name="login"), 
    path('index/', views.indexCliente, name='indexCliente'),
    path('adicionarCliente/', views.add_cliente, name='adicionarCliente'),
    path('editar/<str:username>/', views.editarDadosCliente, name='editar'),
<<<<<<< HEAD
    path('verPerfil/', views.verPerfil, name='verPerfil'),
=======
    path('alterarSenha/<str:username>/', views.editSenha, name="alterarSenha"),
    path("logout/", views.realizarLogout, name="logout"),
    path('verPerfil/<str:username>/', views.verPrfil, name='verPerfil'),
>>>>>>> 063b0a25733742030d958f917ce817d37c3aa46e
    path('excluirConta/<str:username>/', views.deletarContaCliente, name='excluirConta'),
    path('marcarServico/', views.marcarServico, name='marcarServico'),
    path('mostrarCategoria/', views.mostrarCategoria, name='mostrarCategoria'),
]