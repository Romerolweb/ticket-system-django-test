from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuration for the 'authentication' Django app.

    This class sets up the configuration for the authentication app, such as
    the default auto field for models and the app name. It also imports the
    app's signals when the app is ready.

    Attributes:
        default_auto_field (str): The default primary key type for models.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self) -> None:
        """
        Imports the signals for the authentication app.

        This method is called by Django when the application is ready. It
        imports the signals module to ensure that the signal handlers are

        connected.
        """
        import authentication.signals