from .import views
from django.urls import path


urlpatterns = [
    path("index/", views.index, name="indexAdm"),
    path("add/", views.add_administrador, name="add"),
    path('verAdministrador/', views.verAdministrador, name='verAdministrador'),
    path('verServico/', views.mostrarServicos, name='verServico'),
    path('verProfissional/', views.verProfissional, name='verProfissional'),
    path('verCliente/', views.verCliente, name='verCliente'),
    path("deletarServico/<int:id>/", views.deletarServico, name="deletarServico"),
    path("alterarServico/<int:id>/", views.alterarServico, name="alterarServico"),
    path("redirecionaServico/", views.redirecionarParaServico, name="redirecionaServico"),
    path("alterarCategoria/<int:id>/", views.alterarCategoria, name="alterarCategoria"),
    path("deletarCategoria/<int:id>/", views.deletarCategoria, name="deletarCategoria"),
    
]