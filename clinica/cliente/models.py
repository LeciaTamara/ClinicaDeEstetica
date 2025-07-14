from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    telefone = models.IntegerField()
    identificador = models.CharField(max_length=20, default='cliente')

    class Meta:
        permissions = (
            ("detail_cliente","Pode ver detalhe do perfil"),
            ("AgendarServico_cliente", "Pode agendar um servico"),
        )

class AgendarServico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeCliente = models.CharField(max_length=100)
    servico = models.ManyToManyField('servico.Servico', null=True)
    data = models.DateField(null=True, blank=True)
    horario = models.TimeField()
