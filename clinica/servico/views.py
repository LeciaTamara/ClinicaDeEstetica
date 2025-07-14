from queue import Full
from django.shortcuts import redirect, render
from servico.models import Servico, TipoServico
from servico.forms import EditCategoriaForm, EditServicoForm, ServicoCategoriaForm, ServicoForm
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

def index(request):
    servicos = Servico.objects.all()

    # categorias = Servico.objects.values_list('categoria', flat=True).distinct()
    # servicoPorCategoria = {}

    # for categoria in categorias:
    #     servico = Servico.objects.filter(categoria=categoria).first()
    #     if servico:
    #         servicoPorCategoria[categoria] = servico
    return render(request, 'servico/indexServico.html', {'servicos': servicos})

#Adicionar Categoria de serviço
@permission_required('servico.add_servico', raise_exception=True)
def addCategoria(request):
    formServico = ServicoCategoriaForm(request.POST, request.FILES)
    print(formServico.errors)

    if formServico.is_valid():
        categoriaServico = formServico.save(commit=False)
        categoriaServico.save()
        return redirect('indexServico')
    return render(request, 'servico/servicoForm.html', {'formServico' :formServico})

# mostra as categorias de cada servico
# Ela tem como argumento o request, o template = '', que permite que
# a ela ser chamada em outros apps e exibir essas informações.
# def mostrarCategoria():
#     # Essa linha retorna para a variavél categorias os valores do atrbuto
#     # categoria, onde flat=True tranforma os valores retornados pela a lista
#     # em uma lista simples, e o distinc não permite que valores iguais entre
#     # na lista.
#     categorias = TipoServico.objects.values_list('categoria', flat=True).distinct()
#     # Essa linha cria um dicionário vázio
#     servicoPorCategoria = {}

#     for categoria in categorias:
#         servico = TipoServico.objects.filter(categoria=categoria).first()
#         if servico:
#             servicoPorCategoria[categoria] = servico
#     return {'servicoPorCategoria': servicoPorCategoria}

# Editar Categoria
@permission_required('servico.change_servico', raise_exception=True)
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
@permission_required('servico.delete_servico', raise_exception=True)
def deletarCategoria(request, id):
    categoria = TipoServico.objects.get(pk=id)
    categoria.delete()


# Adicionar Serviço
@permission_required('servio.add_servico', raise_exception=True)
def addServico(request):
    formServico = ServicoForm(request.POST, request.FILES)

    print(formServico.errors)
    if formServico.is_valid():
        servico = formServico.save(commit=False)
        servico.save()
        return redirect('indexServico')
    return render(request, 'servico/servicoForm.html',{'formServico': formServico})      

#Editar servico
@permission_required('servico.change_servico', raise_exception=True)
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
            return render(request, 'servico/servicoForm.html')


#Deletar Servico
@permission_required('servico.delete_sevico', raise_exception=True)
def deletarServico(request, id):
    servico = Servico.objects.get(pk=id)

    servico.delete()
    return redirect('indexServico')

#Redireciona para o painel de administrador
def redirecionarParaAdministrador(request):
    return redirect(reverse('indexAdm'))