from django.contrib.auth.models import Group, Permission
from django.db.utils import OperationalError

def configurar_grupos_e_permissoes():
    try:
        grupo, _ = Group.objects.get_or_create(name='Clientes')

        permissoes_desejadas = [
            'change_cliente',
            'delete_cliente',
            'view_cliente',
            'detail_cliente',
            'add_cliente',
            'AgendarServico_cliente',
            'change_agendarservico',
            'delete_agendarservico',
            'view_agendarservico',
        ]

        permissoes = Permission.objects.filter(codename__in=permissoes_desejadas)
        grupo.permissions.set(permissoes)

    except OperationalError:
        pass
