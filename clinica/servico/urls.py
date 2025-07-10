from django.urls import path 
from .import views

urlpatterns = [
    path("index/", views.index, name="indexServico"),
    path("addServico/", views.addServico, name="addServico"),
    path("alterarServico/<int:id>/", views.alterarServico, name="alterarServico"),
    path("deletarServico/<int:id>/", views.deletarServico, name="deletarServico"),

]
