from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(User):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    telefone = models.IntegerField()