from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.

    Defines the display and filtering options for categories in the admin panel.

    Attributes:
        list_display (tuple): Fields to display in the category list view.
        list_filter (tuple): Fields to use for filtering categories.
    """
    list_display = ("name",)
    list_filter = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Event model.

    Defines the display and filtering options for events in the admin panel.

    Attributes:
        list_display (tuple): Fields to display in the event list view.
        list_filter (tuple): Fields to use for filtering events.
    """
    list_display = ("title", "event_start_date", "location", "host")
    list_filter = ("event_start_date", "location", "host")


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SocialMedia model.

    Defines the display and filtering options for social media links
    in the admin panel.

    Attributes:
        list_display (tuple): Fields to display in the social media list view.
        list_filter (tuple): Fields to use for filtering social media links.
    """
    list_display = ("facebook", "instagram", "linkedIn", "twitter")
    list_filter = ("facebook", "instagram", "linkedIn", "twitter")
