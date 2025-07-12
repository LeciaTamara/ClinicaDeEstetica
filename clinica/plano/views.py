from django.shortcuts import redirect, render
from plano.models import Plano
from plano.forms import EditPlanoForm, PlanoForm

def addPlano(request):
    formPlano = PlanoForm(request.POST)

    if formPlano.is_valid():
        plano = formPlano.save(commit=False)
        plano.save()
        return redirect('indexPlano')
    return render(request, 'plano/planoForm.html',{'formPlano': formPlano})

def index(request):
    return render(request, 'plano/indexPlano.html')

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
       return redirect('indexPlano')
    else:
       planos = Plano.objects.all()
       return render(request, 'plano/planoForm.html')

def deletarPlano(request, id):
    form = Plano.objects.get(pk=id)

    form.delete()
    return redirect('indexPlano')