from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, HostUserProfile


class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the CustomUser model.

    This class defines how the CustomUser model is displayed and managed in the
    Django admin interface. It specifies the forms for adding and changing
    users, the fields to display in the list view, and the fields for filtering
    and searching.

    Attributes:
        add_form (Form): The form used for creating a new user.
        form (Form): The form used for changing an existing user.
        model (Model): The model this admin class is for (CustomUser).
        list_display (tuple): The fields to display in the admin list view.
        list_filter (tuple): The fields to use for filtering in the admin sidebar.
        fieldsets (tuple): The layout of fields on the user edit page.
        add_fieldsets (tuple): The layout of fields on the user creation page.
        search_fields (tuple): The fields to search by in the admin list view.
        ordering (tuple): The default ordering for the admin list view.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'event_hoster')
    list_filter = ('email', 'is_staff', 'is_active', 'event_hoster')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'event_hoster')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(HostUserProfile)
class HostUserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the HostUserProfile model.

    This class defines how the HostUserProfile model is displayed in the
    Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
    """
    list_display = ("user", "company_name")

admin.site.register(CustomUser, CustomUserAdmin)



