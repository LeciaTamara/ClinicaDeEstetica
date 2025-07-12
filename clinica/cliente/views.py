from django.shortcuts import redirect, render

from cliente.forms import ClienteForm
from clinicaEstetica.forms import AdicionarUsuarioForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def indexCliente(request):
    return render(request,'cliente/indexCliente.html')

# O cliente criar a conta dele 
# def addCliente(request):
#     form = CadastrarClienteForm(request.POST)
#     print(form.errors)
#     if form.is_valid():
#         cliente = form.save(commit=False)
#         cliente.save()
#         return redirect('indexCliente')
#     return render(request, 'cliente/addClienteForm.html', {'form' :form})

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