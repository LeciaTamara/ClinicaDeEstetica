
from django.urls import path

from . import views


urlpatterns = [
    path("index/", views.index, name="indexClinica"),
    path("addClinica/", views.addClinica, name="adicionaClinica"),
    path("mostrarSobre/", views.mostrarSobre, name="mostrarSobre"),
    path("atualizarClinica/", views.atualizarClinica, name="atualizarClinica"),
]