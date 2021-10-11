from django.apps import AppConfig


class RarityToolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rarity_tool'

    def ready(self):
        from . import scheduler
        scheduler.start()