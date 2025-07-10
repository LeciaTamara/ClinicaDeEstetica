from django.shortcuts import redirect, render
from servico.models import Servico
from servico.forms import EditServicoForm, ServicoForm

def addServico(request):
    formServico = ServicoForm(request.POST)

    if formServico.is_valid():
        servico = formServico.save(commit=False)
        servico.save()
        return redirect('indexServico')
    return render(request, 'servico/servicoForm.html',{'formServico': formServico})

def index(request):
    return render(request, 'servico/indexServico.html')

def alterarServico(request, id):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        servico = Servico.objects.filter(pk=id).first()
        formServico = EditServicoForm(instance=servico)

        return render(request, 'servico/servicoForm.html',{'formServico': formServico, 'servicos': servicos})
    
    elif request.method == 'POST':
        servicos = Servico.objects.all()
        servico = Servico.objects.get(pk=id)
        formServico = EditServicoForm(request.POST,instance=servico)

    if formServico.is_valid():
       formServico.save()
       return redirect('indexServico')
    else:
       servicos = Servico.objects.all()
       return render(request, 'servico/servicoForm.html')

def deletarServico(request, id):
    form = Servico.objects.get(pk=id)

    form.delete()
    return redirect('indexServico')