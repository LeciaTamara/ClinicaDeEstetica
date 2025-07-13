from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from administrador.forms import AdministradorForm
from clinicaEstetica.forms import AdicionarUsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

#Index de administrador
login_required()
def index (request):
    return render(request, 'administrador/indexAdministrador.html')


# Adicionar administrador
def add_administrador(request):
    form_user = AdicionarUsuarioForm(request.POST or None)
    form = AdministradorForm(request.POST or None)
    if form_user.is_valid() and form.is_valid():
        user_administrador = form_user.save()
        administrador = form.save(commit=False)
        administrador.user = user_administrador
        administrador.identificador = 'administrador'
        administrador.save()
        print("Administrador criado:", administrador.id)

        tornarAdmin(request, user_administrador.username)
        print("Administrador salvo:", administrador.id)

        return redirect('indexAdm')
    return render(request, 'administrador/cadastrarAdminForm.html', {'form_user': form_user, 'form': form})

#tornar o usuário um administrador
def tornarAdmin(request, userName): 
    administrador = get_object_or_404(User, username = userName) 
    if administrador.is_superuser: 
        messages.error(request, "Você já é um Administrador") 
        
    else: 
        administrador.is_superuser = True #Transforma o administrador em superUsuário 
        administrador.is_staff = True #Permite que o usuário acesse o painel de administração do django 
        administrador.save() 
        messages.success(request, "Usuário promovido a administrador") 
    
    return redirect('indexAdm')