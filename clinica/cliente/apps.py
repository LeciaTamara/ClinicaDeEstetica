from django.apps import AppConfig


class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cliente'

    def ready(self):
        from .setup import configurar_grupos_e_permissoes
        configurar_grupos_e_permissoes()
