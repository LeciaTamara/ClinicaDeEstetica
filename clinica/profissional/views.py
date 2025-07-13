from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from clinicaEstetica.forms import AdicionarUsuarioForm
from profissional.models import Profissional
from profissional.forms import EditProfissionalForm, ProfissionalForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
     profissionais = Profissional.objects.all()
     usuario = User.objects.all()

     contexto = {
         'profissionais' :profissionais,
         'title' :'Listas de profissionais',
         'usuario' : usuario
     }
     return render(request, 'profissional/indexProfissional.html', contexto)

#criar profissional
def add_profissional(request):
    form_user = AdicionarUsuarioForm(request.POST or None)
    form = ProfissionalForm(request.POST or None)
    if form_user.is_valid() and form.is_valid():
        user_profissional = form_user.save()
        profissional = form.save(commit=False)
        profissional.user = user_profissional
        profissional.identificador = 'profissional'
        profissional.save()
        return redirect('indexProfissional')
    return render(request, 'profissional/profissionalForm.html', {'form_user': form_user, 'form': form})


# def criarProfissional(request):
#     formProfissional = ProfissionalForm(request.POST)

#     if formProfissional.is_valid():
#         profissional = formProfissional.save(commit=False)
#         profissional.save()

#         #redireciona para a página inicial do Admin
#         return redirect(reverse('indexAdm'))

#     return render(request, 'profissional/profissionalForm.html', {'formProfissional': formProfissional})


# Mostrar detalhes
# def mostrardetalhes(request, username):
#     # Captura o username do usuário e exibe as suas informações no formulário
#     #pega todos os dados do modelo da classe User

#     User = get_user_model()

#     #if request.user.is_authenticated:
#     verificaUsername = User.objects.filter(username=username).first()

#         #if verificaUsername and request.user.username == verificaUsername.username:
#     profissionais = User.objects.all()
#     profissional = User.objects.filter(username=username).first()

#     profissional = Profissional.objects.all()

#     return render(request, 'profissional/detalhes.html', {'profissional' : profissional})

#     # else:
#     #     messages.error(request, "Você não está longado")
#     #     return redirect('indexProfissional')


#alterar informações

def alterarInformacao(request, id):
    #pega o id do usuário
    if request.method == 'GET':
        print('dados do usuário')
        profissionais = Profissional.objects.all()
        profissional = Profissional.objects.filter(pk=id).first()
        formProfissional = EditProfissionalForm(instance=profissional)

        return render(request, 'profissional/profissionalForm.html', {'formProfissional' :formProfissional, 'profissionais' :profissionais})
    #pega o usuário que foi capturado e atualiza os dados
    elif request.method == 'POST':
        print('método POST')
        profissionais = Profissional.objects.all()
        profissional = Profissional.objects.get(pk=id)
        formProfissional = EditProfissionalForm(request.POST, instance=profissional)

        #verifica o id do usuário
        if formProfissional.is_valid():
            formProfissional.save()
            return redirect('indexProfissional')
        else:
            profissionais = Profissional.objects.all()
            return render(request, 'profissional/profissionalForm.html')