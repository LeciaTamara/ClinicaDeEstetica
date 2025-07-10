from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profissional(User):
   nome = models.TextField(max_length=100)
   endereco = models.CharField(max_length=150)
   especializacao = models.CharField(max_length=100)
   numTelefone =  models.IntegerField()
   salario = models.IntegerField()