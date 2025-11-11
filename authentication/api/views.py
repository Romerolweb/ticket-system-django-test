from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.validators import ValidationError
from django.db import IntegrityError

from .serializers import AccountSerializer, HostUserProfileSerializer
from event_portal.api.renderers import CustomRenderer
from django.contrib.auth import get_user_model
from ..models import HostUserProfile

class CreateAccountView(CreateAPIView):
    """
    API endpoint for creating a new user account.

    This view handles user registration. It expects an email and a password.
    Upon successful creation, it returns the user's data.

    Attributes:
        serializer_class (Serializer): The serializer for account creation.
        permission_classes (list): The permissions required for this view.
        renderer_classes (list): The renderers for the response.
    """
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]
    renderer_classes = [CustomRenderer]


class HostProfileCreateView(CreateAPIView):
    """
    API endpoint for creating a host profile for a user.

    This view allows an authenticated user to create an event host profile.
    A user must have a host profile to be able to create events.

    Attributes:
        serializer_class (Serializer): The serializer for host profile creation.
        authentication_classes (list): The authentication methods for this view.
        permission_classes (list): The permissions required for this view.
        renderer_classes (list): The renderers for the response.
    """
    serializer_class = HostUserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [CustomRenderer]

    def perform_create(self, serializer):
        """
        Saves the host profile, associating it with the current user.

        Args:
            serializer (HostUserProfileSerializer): The serializer instance.

        Raises:
            ValidationError: If the user already has a host profile.
        """
        instance = self.request.user
        try:
            serializer.save(user=instance)
        except IntegrityError:
            raise ValidationError(
                {
                    "detail": "This user already has an event host profile"
                }
            )
      
        

