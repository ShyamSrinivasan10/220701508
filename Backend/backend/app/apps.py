from django.apps import AppConfig


class AppConfiguration(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.app'
