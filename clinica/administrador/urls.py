from .import views
from django.urls import path


urlpatterns = [
    path("index/", views.index, name="indexAdm"),
    path("add/", views.add_administrador, name="add"),
    path("editarAdministrador/<str:username>/", views.editarDadosAdmin, name="editarAdministrador"),
    path("deletarAdministrador/<str:username>/", views.deletarContaAdmin, name="deletarAdministrador"),
    path('verAdministrador/', views.verAdministrador, name='verAdministrador'),
    path('alterarSenha/<str:username>/', views.editSenha, name="alterarSenha"),
    path("logout/", views.realizarLogout, name="logout"),
    path('verServico/', views.mostrarServicos, name='verServico'),
    path('verProfissional/', views.verProfissional, name='verProfissional'),
    path('verCliente/', views.verCliente, name='verCliente'),
    path("deletarServico/<int:id>/", views.deletarServico, name="deletarServico"),
    path("alterarServico/<int:id>/", views.alterarServico, name="alterarServico"),
    path("redirecionaServico/", views.redirecionarParaServico, name="redirecionaServico"),
    path("redirecionaPlano/", views.redirecionaPlano, name="redirecionaPlano"),
    path("alterarCategoria/<int:id>/", views.alterarCategoria, name="alterarCategoria"),
    path("deletarCategoria/<int:id>/", views.deletarCategoria, name="deletarCategoria"),
    path("verPlano/", views.verPlano, name="verPlano"),
    path("deletarProfissional/<str:username>/", views.deletarProfissional, name="deletarProfissional"),
    
]