from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model de Administrador

class Administrador(User):
    nome = models.CharField(max_length=100)