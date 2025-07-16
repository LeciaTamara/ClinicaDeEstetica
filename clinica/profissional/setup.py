from django.contrib.auth.models import Group, Permission
from django.db.utils import OperationalError

def configurar_grupos_e_permissoes():
    try:
        grupo, _ = Group.objects.get_or_create(name='Profissionais')

        permissoes_desejadas = [
            'change_profissional',
            'delete_profissional',
            'view_profissional',
            'detail_profissional'
        ]

        permissoes = Permission.objects.filter(codename__in=permissoes_desejadas)
        grupo.permissions.set(permissoes)

    except OperationalError:
        pass
