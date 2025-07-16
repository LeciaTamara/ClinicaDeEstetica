from django.contrib.auth.models import Group, Permission
from django.db.utils import OperationalError

def configurar_grupos_e_permissoes():
    try:
        grupo, _ = Group.objects.get_or_create(name='Administradores')

        permissoes_desejadas = [
            'add_administrador',
            'change_administrador',
            'delete_administrador',
            'detail_administrador',
            'view_administrador',
            'add_clinica',
            'change_clinica',
            'delete_clinica',
            'view_clinica',
            'change_clinica',
            'add_plano',
            'change_plano',
            'delete_plano',
            'view_plano',
            'add_servico',
            'change_servico',
            'delete_servico',
            'view_servico',
            'add_tiposervico',
            'change_tiposervico',
            'delete_tiposervico',
            'view_tiposervico',
            
        ]

        permissoes = Permission.objects.filter(codename__in=permissoes_desejadas)
        grupo.permissions.set(permissoes)

    except OperationalError:
        pass
