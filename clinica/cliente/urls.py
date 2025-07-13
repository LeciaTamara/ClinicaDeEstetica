from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.indexCliente, name='indexCliente'),
    path('adicionarCliente/', views.add_cliente, name='adicionarCliente'),
    path('editar/<str:username>/', views.editarDadosCliente, name='editar'),
    path('verPerfil/<str:username>/', views.verPrfil, name='verPerfil'),
    path('excluirConta/<str:username>/', views.deletarContaCliente, name='excluirConta')
]