from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.indexCliente, name='indexCliente'),
    path('adicionarCliente/', views.addCliente, name='adicionarCliente'),
]