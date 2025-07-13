from django.shortcuts import redirect, render

from cliente.models import Cliente
from cliente.forms import ClienteForm, EditClienteForm
from clinicaEstetica.forms import AdicionarUsuarioForm, EditUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

#Read
@login_required()
def indexCliente(request):
    return render(request,'cliente/indexCliente.html')

#Adicionar Cliente
def add_cliente(request):
    form_user = AdicionarUsuarioForm(request.POST or None)
    form = ClienteForm(request.POST or None)
    if form_user.is_valid() and form.is_valid():
        user_cliente = form_user.save()
        cliente = form.save(commit=False)
        cliente.user = user_cliente
        cliente.identificador = 'cliente'
        cliente.save()
        return redirect('indexCliente')
    return render(request, 'cliente/addClienteForm.html', {'form_user': form_user, 'form': form})

#Read com condição
@login_required
def verPrfil(request, username):
    cliente = Cliente.objects.get(user__username=username)
    userCliente = cliente.user

    return render(request, 'cliente/verPerfil.html', {'user' : userCliente, 'cliente' : cliente})


#Update
@login_required
def editarDadosCliente(request, username):
    cliente = get_object_or_404(Cliente, user__username=username)
    user = cliente.user
    
    editarUserForm = EditUsuarioForm(request.POST, instance=user)
    editarClienteForm = EditClienteForm(request.POST, instance=cliente)

    if request.method == 'POST':
        if editarUserForm.is_valid() and editarClienteForm.is_valid():
            editarUserForm.save()
            editarClienteForm.save()
            return redirect('indexCliente')

    return render(request, 'cliente/addClienteForm.html', {'editarUserForm' : editarUserForm, 'editarClienteForm' : editarClienteForm, 'cliente' : cliente} )


#Delete
def deletarContaCliente(request, username):
    apagarCliente = get_object_or_404(Cliente, user__username=username)

    clienteUser = apagarCliente.user
    apagarCliente.delete()
    clienteUser.delete()
    return redirect('indexClinica')