from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from clinicaEstetica.forms import AdicionarUsuarioForm, EditUsuarioForm
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

#alterar informações
@login_required
def editarDadosProfissional(request):
    user = request.user
    profissional = get_object_or_404(Profissional, user=user)
    
    if request.method == 'POST':
        editarUserForm = EditUsuarioForm(request.POST, instance=user)
        editarProfissionalForm = EditProfissionalForm(request.POST, instance=profissional)

        if editarUserForm.is_valid() and editarProfissionalForm.is_valid():
            editarUserForm.save()
            editarProfissionalForm.save()
            return redirect('indexProfissional')
    else:
        editarUserForm = EditUsuarioForm(request.POST, instance=user)
        editarProfissionalForm = EditProfissionalForm(request.POST, instance=profissional)

        return render(request, 'profissional/profissionalForm.html', {'editarUserForm' : editarUserForm, 'editarProfissionalForm' : editarProfissionalForm, 'profissional' : profissional} )


#Ver Profissionais detalhes de profissionais
@login_required()
def verProfissional (request):
    #pega o profissional pelo o username
    user = request.user
    profissional= Profissional.objects.get(user=user)
    userProfissional = profissional.user

    return render(request, 'profissional/verPerfil.html', {'user' : userProfissional, 'profissional' : profissional})

# Apagar profissional
def deletarContaCliente(request, username):
    apagarCliente = get_object_or_404(Cliente, user__username=username)

    clienteUser = apagarCliente.user
    apagarCliente.delete()
    clienteUser.delete()
    return redirect('indexClinica')

@login_required()
def deletarContaProfissional(request):
    #pega o profissional pelo o username
    user = request.user
    profissional= get_object_or_404(Profissional, user = user)
  
    profissionalUser = profissional.user
    profissional.delete()
    profissionalUser.delete()
    return redirect('indexProfissional')