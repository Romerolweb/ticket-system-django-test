from django.apps import AppConfig


class EventPortalConfig(AppConfig):
    """
    Configuration for the 'event_portal' Django app.

    This class sets up the configuration for the event_portal app, such as
    the default auto field for models and the app name.

    Attributes:
        default_auto_field (str): The default primary key type for models.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_portal'
