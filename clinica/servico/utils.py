from servico.models import Servico, TipoServico

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

# mostrar serviço
def mostrarServico():
    verServicos = Servico.objects.values_list('servico', flat=True)
    armazenaServico = {}
    
    for servico in verServicos:
        servicoPrestado = Servico.objects.filter(servico=servico).first()
        if servicoPrestado:
            armazenaServico[servico] = servicoPrestado
    return {'armazenaServico': armazenaServico}