from django.db import models

class Plano(models.Model):
    tipo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='preco')
    servico = models.ForeignKey('servico.Servico', on_delete=models.CASCADE)