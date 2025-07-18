from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model de Administrador

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=20, default='administrador')
    nome = models.CharField(max_length=100) 

    class Meta:
        permissions = (
            ("detailhes_administrador","Pode ver detalhe do da view administrador"),
        )