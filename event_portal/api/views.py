from datetime import datetime 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import viewsets
from django_auto_prefetching import AutoPrefetchViewSetMixin

 

from ..models import *
from .serializers import *
from .renderers import CustomRenderer
from .permissions import *
from .pagination import CustomPagination
from .filters import EventFilter


class CategoryListView(ListAPIView):
    """
    API endpoint to list all available event categories.

    This view provides a paginated list of all categories in the system.

    Attributes:
        serializer_class (Serializer): The serializer for Category objects.
        renderer_classes (list): The renderers for the response.
        pagination_class (Pagination): The pagination style for the list.
        queryset (QuerySet): The queryset of all Category objects.
    """
    serializer_class = CategorySerializer
    renderer_classes = [CustomRenderer]
    pagination_class = CustomPagination
    queryset = Category.objects.all()


class CategoryCreateView(CreateAPIView):
    """
    API endpoint to create a new category.

    This view is restricted to admin users only. It allows for the creation
    of new event categories.

    Attributes:
        authentication_classes (list): The authentication methods for this view.
        permission_classes (list): The permissions required for this view.
        renderer_classes (list): The renderers for the response.
        serializer_class (Serializer): The serializer for creating a Category.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    renderer_classes = [CustomRenderer]
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a category.

    This view allows anyone to view a category, but only admin users can
    update or delete it. The category is looked up by its slug.

    Attributes:
        serializer_class (Serializer): The serializer for Category objects.
        permission_classes (list): The permissions required for this view.
        renderer_classes (list): The renderers for the response.
    """
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    renderer_classes = [CustomRenderer]

    def get_object(self):
        """
        Retrieves the category object based on the slug in the URL.

        Returns:
            Category: The category instance.
        """
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Category, slug=slug)
        return obj


class EventAPIViewset(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    """
    A ViewSet for handling CRUD operations for Events.

    This ViewSet provides 'list', 'create', 'retrieve', 'update',
    and 'destroy' actions for events. It also includes filtering, searching,
    and ordering capabilities.

    Attributes:
        serializer_class (Serializer): The serializer for Event objects.
        pagination_class (Pagination): The pagination style for the list.
        renderer_classes (list): The renderers for the response.
        filter_backends (list): The filter backends to use.
        filterset_class (FilterSet): The filter set for filtering events.
        search_fields (list): The fields to search against.
        ordering_fields (list): The fields to order by.
    """
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    renderer_classes = [CustomRenderer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EventFilter
    search_fields = ["location", "category__name", "title"]
    ordering_fields = ["event_start_date", "date_posted", "last_updated"]

    def perform_create(self, serializer):
        """
        Sets the host of the event to the current user upon creation.

        Args:
            serializer (EventSerializer): The serializer instance.
        """
        user = self.request.user
        serializer.save(host=user)

    def get_queryset(self):
        """
        Returns a queryset of upcoming events.

        Filters events to include only those with a start date from today
        onwards, ordered by the most recently updated.

        Returns:
            QuerySet: A queryset of future Event objects.
        """
        return Event.objects.filter(
            event_start_date__gte=datetime.today().date().strftime('%Y-%m-%d')
        ).order_by("-last_updated")

    def get_object(self):
        """
        Retrieves an event object by its slug from the URL.

        Returns:
            Event: The event instance.
        """
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Event, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        """
        Sets the permissions required for each action.

        - 'create': User must be authenticated.
        - 'update', 'partial_update', 'destroy': User must be the event host.
        - Other actions ('list', 'retrieve'): Allow any user.

        Returns:
            list: A list of permission classes.
        """
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [EventHostOrReadOnly]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()


class CategoryEventView(ListAPIView):
    """
    API endpoint to list all events belonging to a specific category.

    This view retrieves a list of events filtered by the category slug
    provided in the URL.

    Attributes:
        serializer_class (Serializer): The serializer for Event objects.
        pagination_class (Pagination): The pagination style for the list.
        renderer_classes (list): The renderers for the response.
        filter_backends (list): The filter backends to use.
        ordering_fields (list): The fields to order by.
        search_fields (list): The fields to search against.
    """
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    renderer_classes = [CustomRenderer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ["event_start_date", "date_posted", "last_updated"]
    search_fields = ["location", "title"]

    def get_queryset(self):
        """
        Returns a queryset of events filtered by category slug.

        The slug is extracted from the URL kwargs.

        Returns:
            QuerySet: A queryset of Event objects in the specified category.
        """
        slug = self.kwargs["slug"]
        queryset = Event.objects.filter(category__slug=slug)
        return queryset
    
    
    
    
    
    


         

        
        

    
    
    
    
        
    

