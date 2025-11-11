from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 
import uuid
from django.conf import settings
# Create your models here.

from .manager import CustomUserManager

class CustomUser(AbstractUser):
    """
    Custom user model for the application.

    This model extends the default Django AbstractUser, using email as the
    unique identifier (USERNAME_FIELD) instead of a username.

    Attributes:
        id (UUIDField): The primary key for the user, a UUID.
        email (EmailField): The user's unique email address.
        event_hoster (BooleanField): Flag indicating if the user is an event host.
    """
    username = None
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(_('email address'), unique=True)
    event_hoster = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """
        Returns the string representation of the user.

        Returns:
            str: The user's email address.
        """
        return self.email


class HostUserProfile(models.Model):
    """
    Profile for users who are event hosters.

    This model stores additional information about users who have the
    `event_hoster` flag set to True in their CustomUser model.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the CustomUser model.
        company_name (CharField): The name of the host's company.
        company_description (TextField): A description of the company.
        website_url (URLField): The company's website.
        phone_number (CharField): The company's phone number.
        address (CharField): The company's physical address.
        city (CharField): The city where the company is located.
        state (CharField): The state or province.
        country (CharField): The country.
        zip_code (CharField): The postal or zip code.
        twitter (URLField): The company's Twitter profile URL.
        facebook (URLField): The company's Facebook page URL.
        instagram (URLField): The company's Instagram profile URL.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    company_name = models.CharField(max_length=50, unique=True)
    company_description = models.TextField(max_length=500, blank=True)
    website_url = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    facebook = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)

    def __str__(self):
        """
        Returns the string representation of the host profile.

        Returns:
            str: The email of the user associated with the profile.
        """
        return self.user.email
  
    
    
    

