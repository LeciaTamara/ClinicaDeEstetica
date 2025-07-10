from django.db import models

class Servico(models.Model):
    tipo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='preco')
    profissional = models.ForeignKey('profissional.Profissional', on_delete=models.CASCADE)