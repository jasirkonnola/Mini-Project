from django.apps import AppConfig


class EduusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eduUsers'

    def ready(self):
        import eduUsers.signals