from plano.models import Plano

#Mostrar todos os planos
def visualizarPlano():
    verPlano = Plano.objects.all()
    return{'verPlano': verPlano}