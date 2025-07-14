

from cliente.models import Cliente
from cliente.forms import AgendarServicoForm, ClienteForm, EditClienteForm
from servico.utils import mostrarCategoria
from clinicaEstetica.forms import AdicionarUsuarioForm, EditUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from servico.models import TipoServico

# Create your views here.

#Read
@login_required()
def indexCliente(request):
    return render(request,'cliente/verPerfil.html')

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
        return redirect('verPerfil')
    return render(request, 'cliente/addClienteForm.html', {'form_user': form_user, 'form': form})

#Read com condição
@login_required
def verPerfil(request):
    cliente = get_object_or_404(Cliente, user=request.user)
    return render(request, 'cliente/verPerfil.html', {'cliente': cliente})


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
            return redirect('verPerfil')

    return render(request, 'cliente/addClienteForm.html', {'editarUserForm' : editarUserForm, 'editarClienteForm' : editarClienteForm, 'cliente' : cliente} )


#Delete
def deletarContaCliente(request, username):
    apagarCliente = get_object_or_404(Cliente, user__username=username)

    clienteUser = apagarCliente.user
    apagarCliente.delete()
    clienteUser.delete()
    return redirect('indexClinica')

# Agendar Servico
# EditUsuarioForm
@login_required
def marcarServico(request):
    formCliente = EditUsuarioForm(request.POST or None)
    formAgendaServico = AgendarServicoForm(request.POST or None)
    if formCliente.is_valid() and formAgendaServico.is_valid():
        clienteForm = formCliente.save()
        agendaServicoForm = formAgendaServico.save(commit=False)
        agendaServicoForm.user = clienteForm
        agendaServicoForm.save()
        formAgendaServico.save_m2m()
        return redirect('indexClinica')
    else:
        return render(request, 'cliente/agendarForm.html', {'formCliente': formCliente, 'formAgendaServico': formAgendaServico})
    

# Mostrar fotos de categoria
def mostrarFotosCategoria(request):
    servicos = {}
    servicos.update(mostrarCategoria())
    return render(request,'clinicaEstetica/indexClinica.html', servicos)


from collections import defaultdict

# def mostrarCategoria():
#     categorias = TipoServico.objects.values_list('categoria', flat=True).distinct()
#     servicoPorCategoria = defaultdict(list)

#     for categoria in categorias:
#         servicos = TipoServico.objects.filter(categoria=categoria)
#         servicoPorCategoria[categoria].extend(servicos)

#     return {'servicoPorCategoria': dict(servicoPorCategoria)}


# def mostrarTodasImagens(request):
#     imagens = TipoServico.objects.all()
#     return render(request, 'cliente/indexCliente.html', {
#         'imagens': imagens
#     })


def mostrarCategoria():
    # Essa linha retorna para a variavél categorias os valores do atrbuto
    # categoria, onde flat=True tranforma os valores retornados pela a lista
    # em uma lista simples, e o distinc não permite que valores iguais entre
    # na lista.
    categorias = TipoServico.objects.values_list('categoria', flat=True).distinct()
    # Essa linha cria um dicionário vázio
    servicoPorCategoria = {}

    for categoria in categorias:
        servico = TipoServico.objects.filter(categoria=categoria).first()
        if servico:
            servicoPorCategoria[categoria] = servico
    return {'servicoPorCategoria': servicoPorCategoria}