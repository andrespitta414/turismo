"""
turismo_django - App Configuration
"""

from django.apps import AppConfig


class TurismoDjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'turismo_django'
    verbose_name = 'Sistema de Turismo'
    
    def ready(self):
        pass