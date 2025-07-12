from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from administrador.forms import AdministradorForm
from django.contrib import messages

# Create your views here.


#Index de administrador

def index (request):
    return render(request, 'administrador/indexAdministrador.html')


# Adicionar administrador
def add (request):
    form = AdministradorForm(request.POST)
    print(form.errors)
    if form.is_valid():
        administrador = form.save(commit=False)
        administrador.save()

        tornarAdmin(request, administrador.username)
        return redirect('indexAdm')
    return render(request, 'administrador/cadastrarAdminForm.html', {'form' :form})

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