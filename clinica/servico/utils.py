from servico.models import Servico, TipoServico
# Arquivo util.py utilizado para criar funçoes que são utilizadas em outros apps
# com no app clinicaEstetica.

# Essas funçõe são todas utilizadas no app clinica Estetica

# mostra as categorias de cada servico
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

# mostrar os dados do serviço
def mostrarServico():
    armazenaServico = Servico.objects.all()
    return {'armazenaServico': armazenaServico}

# mostrar os serviços exibidos depois de clicar no botão mostrar mais 
def mostrarMaisServicos():
    servico = Servico.objects.all()[8:]
    #retorna um dicionário
    return {'armazenaServico': servico}
