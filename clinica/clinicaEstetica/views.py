from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from plano.utils import visualizarPlano
from servico.utils import mostrarCategoria, mostrarMaisServicos, mostrarServico
from clinicaEstetica.models import Clinica
from clinicaEstetica.forms import ClinicaForm, EditClinicaForm

# Create your views here.
# Essa view chama e retorna a view Categoria e servico
def index(request):
    # Essa linha retorna os dados da view mostrarCategoria para o indexClinica
    # Onde está a palavra templateDestino tem que ser o mesmo none definido na
    # view de mostrarCategoria em servio, mudando só o caminho para onde vai os dados
    servicos = {}
    servicos.update(mostrarCategoria())
    servicos.update(mostrarServico())
    return render(request,'clinicaEstetica/indexClinica.html', servicos)

# mostrar os serviços restantes ao clicar no botão mostrar mais serviços no
# índice de clinicaEstetica
def mostrarServicos(request):
    servicos = {}
    servicos.update(mostrarMaisServicos())
    return render(request, 'clinicaEstetica/__todosServicos.html', servicos)

# mostrar planos
def mostrarPlano(request):
    planos = {}
    planos.update(visualizarPlano())
    return render(request, 'clinicaEstetica/__pricingStart.html', planos)

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
        

def login_usuario(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        usuario = form.get_user()
        login(request, usuario)

        # Redireciona conforme o perfil
        if hasattr(usuario, 'administrador') and usuario.administrador.identificador == 'administrador':
            return redirect('redirecionarParaAdministrador')
        elif hasattr(usuario, 'cliente') and usuario.cliente.identificador == 'cliente':
            return redirect('redirecionarParaCliente')
        elif hasattr(usuario, 'profissional') and usuario.profissional.identificador == 'profissional':
            return redirect('redirecionaParaProfissional')
        else:
            return redirect('login')  # fallback

    return render(request, 'registration/login.html', {'form': form})

#  #Login de acordo com o perfil do usuário       
# @login_required 
# def login_usuario(request): 
#     if request.method == 'POST': 
#         loginForm = AuthenticationForm(request, data=request.POST) 
#         if loginForm.is_valid(): 
#             usuario = loginForm.get_user() 
#             login(request, usuario) 
#             if hasattr(usuario, 'administrador') and getattr(usuario.administrador, 'identificador', '') == 'administrador': 
#                 return redirect('redirecionarParaAdministrador') 
#             elif hasattr(usuario, 'profissional') and getattr(usuario.profissional, 'identificador', '') == 'profissional': 
#                 return redirect('redirecionarParaProfissional') 
#             elif hasattr(usuario, 'cliente') and getattr(usuario.cliente, 'identificador', '') == 'cliente': 
#                 return redirect('redirecionarParaCliente') 
#             return redirect('index') 
#         else: 
#             loginForm = AuthenticationForm() 
#     return render(request, 'registration/login.html', {'loginForm': loginForm}) 
        
#Redireciona para a pagina de Administrador 
def redirecionarParaAdministrador(request):
    return redirect(reverse('indexAdm')) 
        
#Redireciona para a pagina de Cliente 
def redirecionarParaCliente(request): 
    return redirect(reverse('indexCliente'))

#Redireciona para a pagina de Profissional
def redirecionaParaProfissional(request):
    return redirect(reverse('indexProfissional'))
