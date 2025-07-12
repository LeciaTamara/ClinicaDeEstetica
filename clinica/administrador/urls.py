from .import views
from django.urls import path


urlpatterns = [
    path("index/", views.index, name="indexAdm"),
    path("add/", views.add_administrador, name="add")
    
]