from django.shortcuts import redirect, render
from django.urls import reverse
from plano.models import Plano
from plano.forms import EditPlanoForm, PlanoForm
from django.contrib.auth.decorators import permission_required

#Criar plano
@permission_required('plano.add_plano', raise_exception=True)
def addPlano(request):
    formPlano = PlanoForm(request.POST)

    if formPlano.is_valid():
        plano = formPlano.save(commit=False)
        plano.save()
        formPlano.save_m2m()
        return redirect('indexPlano')
    return render(request, 'plano/planoForm.html',{'formPlano': formPlano})


#Ver planos
def index(request):
    return render(request, 'plano/indexPlano.html')


#Editar planos
@permission_required('plano.change_plano', raise_exception=True)
def alterarPlano(request, id):
    if request.method == 'GET':
        planos = Plano.objects.all()
        plano = Plano.objects.filter(pk=id).first()
        formPlano = EditPlanoForm(instance=plano)

        return render(request, 'plano/planoForm.html',{'formPlano': formPlano, 'planos': planos})
    
    elif request.method == 'POST':
        planos = Plano.objects.all()
        plano = Plano.objects.get(pk=id)
        formPlano = EditPlanoForm(request.POST,instance=plano)

        if formPlano.is_valid():
            formPlano.save()
            return redirect('indexAdm')
        else:
            planos = Plano.objects.all()
            return render(request, 'plano/planoForm.html')

#Deletar palanos
@permission_required('plano.delete_plano', raise_exception=True)
def deletarPlano(request, id):
    form = Plano.objects.get(pk=id)

    form.delete()
    return redirect('indexAdm')

#Redireciona para o painel de administrador
def redirecionarParaAdministrador(request):
    return redirect(reverse('indexAdm'))

#Mostrar planos para cliente
def mostrarPlano(request):
    planos = Plano.objects.all()  # ou com filtro
    return render(request, 'plano/__pricingStart.html', {'verPlano': planos})
