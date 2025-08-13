from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        # Import signals so receivers are registered when the app loads
        import properties.signals  # noqa: F401
