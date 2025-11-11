from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users.

    This form extends Django's UserCreationForm to work with the CustomUser
    model, which uses email as the username field.

    Attributes:
        Meta (class): A class to configure the form's behavior.
    """

    class Meta:
        """
        Meta options for the CustomUserCreationForm.

        Attributes:
            model (Model): The model to use for the form (CustomUser).
            fields (tuple): The fields to include in the form.
        """
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating existing users.

    This form extends Django's UserChangeForm to work with the CustomUser
    model.

    Attributes:
        Meta (class): A class to configure the form's behavior.
    """

    class Meta:
        """
        Meta options for the CustomUserChangeForm.

        Attributes:
            model (Model): The model to use for the form (CustomUser).
            fields (tuple): The fields to include in the form.
        """
        model = CustomUser
        fields = ('email',)
