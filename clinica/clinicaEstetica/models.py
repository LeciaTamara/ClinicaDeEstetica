from django.db import models

# Create your models here.
class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    sobre = models.CharField(max_length=500)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return f'{self.nome}'