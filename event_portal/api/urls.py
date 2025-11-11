"""
URL patterns for the event portal API.

This module defines the API endpoints for managing events and categories,
including creating, listing, and detailing events and categories.
"""
from django.urls import path
from . import views


urlpatterns = [
    # Category endpoints
    path("category-list/", views.CategoryListView.as_view(), name="category-list"),
    path("create-category/", views.CategoryCreateView.as_view(), name="create-category"),
    path("category-detail/<slug:slug>/", views.CategoryDetailView.as_view(), name="category-detail"),

    # Event endpoints (using a ViewSet)
    path('create-event/', views.EventAPIViewset.as_view({'post': 'create'}), name='create-event'),
    path('event-list/', views.EventAPIViewset.as_view({'get': 'list'}), name='events-list'),
    path('event-detail/<slug:slug>/',
         views.EventAPIViewset.as_view(
             {
                 'get': 'retrieve', 'put': 'update',
                 'patch': 'partial_update',
                 'delete': 'destroy'
             }),
         name='event-detail'
         ),

    # Endpoint to get events by category
    path("events-by-category/<slug:slug>/", views.CategoryEventView.as_view(), name="events-by-category")
]
