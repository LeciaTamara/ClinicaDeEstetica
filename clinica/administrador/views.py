from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from administrador.forms import AdministradorForm, EditAdmForm, SenhaForm
from administrador.models import Administrador
from profissional.models import Profissional
from cliente.models import Cliente
from servico.models import Servico, TipoServico
from servico.forms import EditCategoriaForm, EditServicoForm
from servico.forms import EditServicoForm
from clinicaEstetica.forms import AdicionarUsuarioForm, EditUsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from servico.utils import mostrarCategoria, mostrarMaisServicos, mostrarServico
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your views here.

#Index de administrador
@login_required()
def index (request):
    return render(request, 'administrador/indexAdministrador.html',)

#Ver todos os administradores
@login_required()
def verAdministrador (request):
    administradores = Administrador.objects.select_related('user').all()
    return render(request, 'administrador/verAdministrador.html', {'administradores' : administradores})

#Ver todos os profissionais
@login_required()
def verProfissional (request):
    profissionais = Profissional.objects.select_related('user').all()
    return render(request, 'administrador/verProfissional.html', {'profissionais' : profissionais})

#Ver todos os clientes
@login_required()
def verCliente (request):
    clientes = Cliente.objects.select_related('user').all()
    return render(request, 'administrador/verClientes.html', {'clientes' : clientes})

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

#Update Adm
@login_required
def editarDadosAdmin(request, username):
    administrador = get_object_or_404(Administrador, user__username=username)
    user = administrador.user
    
    editarUserForm = EditUsuarioForm(request.POST, instance=user)
    editarAdministradorForm = EditAdmForm(request.POST, instance=administrador)

    if request.method == 'POST':
        if editarUserForm.is_valid() and editarAdministradorForm.is_valid():
            editarUserForm.save()
            editarAdministradorForm.save()
            return redirect('indexAdm')

    return render(request, 'administrador/cadastrarAdminForm.html', {'editarUserForm' : editarUserForm, 'editarAdministradorForm' : editarAdministradorForm, 'Administrador' : administrador} )


#Delete Adm
def deletarContaAdmin(request, username):
    apagarAdministrador = get_object_or_404(Administrador, user__username=username)

    administradorUser = apagarAdministrador.user
    apagarAdministrador.delete()
    administradorUser.delete()
    return redirect('indexClinica')

#Editar senha
def editSenha(request, username):
    User = get_user_model()
    if request.user.is_authenticated:
        verificarUsuario = Administrador.objects.filter(user__username=username).first()
        if verificarUsuario and request.user.username == verificarUsuario.user.username:
            if request.method == 'GET':
                administradores = User.objects.all()
                administrador= Cliente.objects.filter(user__username=username).first()
                formSenha = SenhaForm(instance=administrador)

                return render(request, 'administrador/senhaForm.html', {'formSenha' : formSenha ,'administradores': administradores})
                
            elif request.method == 'POST':
                administradores = User.objects.all()
                administrador = Administrador.objects.get(user__username=username)
                formSenha = SenhaForm(request.POST, instance=administrador)

                if formSenha.is_valid():
                    formSenha.save()
                        
                    return redirect('indexAdm')
                else:
                    pessoas = User.objects.all()
        
                    return render(request, 'cliente/senhaForm.html')
        else:
            messages.error(request, "Não é possivél alterar a senha de outro usuário")
            return redirect('indexAdm')

#Todos os serviços
def mostrarServicos(request):
    servicos = {}
    servicos.update(mostrarServico())
    return render(request, 'administrador/todosServicos.html', servicos)

#Deletar serviço
def deletarServico(request, id):
    servico = Servico.objects.get(pk=id)

    servico.delete()
    return redirect('verServico')

def alterarServico(request, id):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        servico = Servico.objects.filter(pk=id).first()
        formServico = EditServicoForm(instance=servico)

        return render(request, 'servico/servicoForm.html',{'formServico': formServico, 'servicos': servicos})
    
    elif request.method == 'POST':
        servicos = Servico.objects.all()
        servico = Servico.objects.get(pk=id)
        formServico = EditServicoForm(request.POST, request.FILES, instance=servico)


        if formServico.is_valid():
            formServico.save()
            return redirect('indexServico')
        else:
            servicos = Servico.objects.all()
            return render(request, 'administrador/servicoForm.html')

#Redireciona para o painel de serviços
def redirecionarParaServico(request):
    return redirect(reverse('indexServico'))

#alterar categoria
def alterarCategoria(request, id):
    if request.method == 'GET':
        categorias = TipoServico.objects.all()
        categoria = TipoServico.objects.filter(pk=id).first()
        formServico = EditCategoriaForm(instance=categoria)
        return render(request, 'servico/servicoForm.html', {'formServico': formServico, 'categorias': categorias})
    elif request.method == 'POST':
        categorias = TipoServico.objects.all()
        categoria = TipoServico.objects.get(pk=id)
        formServico = EditCategoriaForm(request.POST, request.FILES, instance=categoria)

        if formServico.is_valid():
            formServico.save()
            return redirect('indexServico')
        else:
            categorias = TipoServico.objects.all()
            return render(request, 'servico/servicoForm.html')
        

# Deletar Categoria
def deletarCategoria(request, id):
    categoria = TipoServico.objects.get(pk=id)
    categoria.delete()

    return ("indexAdm")

