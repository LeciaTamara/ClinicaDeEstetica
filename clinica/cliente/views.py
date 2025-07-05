from django.shortcuts import redirect, render

from cliente.forms import CadastrarClienteForm


# Create your views here.

def indexCliente(request):
    return render(request,'cliente/indexCliente.html')

# O cliente criar a conta dele 
def addCliente(request):
    form = CadastrarClienteForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.save()
        return redirect('indexCliente')
    return render(request, 'cliente/addClienteForm.html', {'form' :form})
    