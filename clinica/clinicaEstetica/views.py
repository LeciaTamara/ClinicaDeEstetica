from django.shortcuts import redirect, render

from servico.utils import mostrarCategoria, mostrarServico
from clinicaEstetica.models import Clinica
from clinicaEstetica.forms import ClinicaForm, EditClinicaForm

# Create your views here.
# Essa view chama e retorna a view mostrarCategoria de servico
def index(request):
    # Essa linha retorna os dados da view mostrarCategoria para o indexClinica
    # Onde está a palavra templateDestino tem que ser o mesmo none definido na
    # view de mostrarCategoria em servio, mudando só o caminho para onde vai os dados
    servicos = {}
    servicos.update(mostrarCategoria())
    servicos.update(mostrarServico())
    return render(request,'clinicaEstetica/indexClinica.html', servicos)

# Adicionar Irformações sobre a clínica

def addClinica(request):
    formClinica = ClinicaForm(request.POST)

    if formClinica.is_valid():
        clinica = formClinica.save(commit=False)
        clinica.save()
        return redirect('indexClinica')
    return render(request, 'clinicaEstetica/clinicaForm.html', {'formClinica' : formClinica})

# Mostrar sobre

def mostrarSobre(request):
    clinicaInformacao = Clinica.objects.first()
    return render(request, 'clinicaEstetica/about.html', {'clinicaInformacao' : clinicaInformacao})

# Atualizar dados da clinica

def atualizarClinica(request):

    if request.method == 'GET':
        clinica = Clinica.objects.all()
        clinica = Clinica.objects.first()
        formClinica = EditClinicaForm(instance=clinica)
        return render(request, 'clinicaEstetica/clinicaForm.html', {'formClinica': formClinica})

    #pega os dados que foi capturado e atualiza
    elif request.method == 'POST':
        clinica = Clinica.objects.first()
        formClinica = EditClinicaForm(request.POST, instance=clinica)

        if formClinica.is_valid():
            formClinica.save()
            return redirect('indexClinica')
        else:
            clinica = clinica.objects.all()
            return render(request, 'clinicaEstetica/clinicaForm.html')