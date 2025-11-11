from django.contrib.auth.base_user import BaseUserManager 
from django.utils.translation import gettext_lazy as _ 


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.

    This manager provides methods to create users and superusers, using email
    as the unique identifier for authentication instead of a username.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            **extra_fields: Additional fields to be saved with the user.

        Returns:
            CustomUser: The created user object.

        Raises:
            ValueError: If the email is not provided.
        """
        if not email:
            raise ValueError(_("The Email must be set !"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a SuperUser with the given email and password.

        Args:
            email (str): The superuser's email address.
            password (str): The superuser's password.
            **extra_fields: Additional fields for the superuser.

        Returns:
            CustomUser: The created superuser object.

        Raises:
            ValueError: If is_staff or is_superuser is not set to True.
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(email, password, **extra_fields)
