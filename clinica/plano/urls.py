from django.urls import path 
from .import views

urlpatterns = [
    path("index/", views.index, name="indexPlano"),
    path("addPlano/", views.addPlano, name="addPlano"),
    path("alterarPlano/<int:id>/", views.alterarPlano, name="alterarPlano"),
    path("deletarPlano/<int:id>/", views.deletarPlano, name="deletarPlano"),
    path("redirecionaParaAdministrador/", views.redirecionarParaAdministrador, name="redirecionarParaAdministrador"),
    path("mostrarPlano/", views.mostrarPlano, name="mostrarPlano")
]