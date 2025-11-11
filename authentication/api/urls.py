"""
URL patterns for the authentication API.

This module defines the API endpoints for user authentication, including
user registration, token-based login, and host profile creation.
"""
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Endpoint for user registration
    path("sign-up/", views.CreateAccountView.as_view(), name="create-account"),

    # Endpoints for JWT token authentication
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/refresh/", TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint for creating a host profile
    path("event-profile/create/", views.HostProfileCreateView.as_view(), name="create-event-host-profile")
]
