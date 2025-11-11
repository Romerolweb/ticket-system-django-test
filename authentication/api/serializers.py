from ..models import CustomUser, HostUserProfile
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating user accounts.

    This serializer handles the creation of new users, including password
    validation. It also ensures that the email provided is unique.

    Attributes:
        password2 (CharField): A write-only field for password confirmation.
        event_hoster (StringRelatedField): A read-only field showing if the user
                                          is an event host.
    """
    password2 = serializers.CharField(write_only=True)
    event_hoster = serializers.StringRelatedField()

    class Meta:
        """
        Meta options for the AccountSerializer.

        Attributes:
            model (Model): The model to be serialized (CustomUser).
            fields (list): The fields to include in the serialization.
            extra_kwargs (dict): Additional keyword arguments for fields.
        """
        model = CustomUser
        fields = ["id", "email", "password", "password2", "event_hoster"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, data):
        """
        Validates the password and password2 fields to ensure they match.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data.

        Raises:
            ValidationError: If the passwords do not match.
        """
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("The two passwords do not match !")
        return data

    def create(self, validated_data):
        """
        Creates a new user instance.

        Args:
            validated_data (dict): The validated data for creating the user.

        Returns:
            CustomUser: The newly created user instance.

        Raises:
            ValidationError: If an account with the given email already exists.
        """
        email = validated_data["email"]
        password = validated_data["password"]
        confirm_account = CustomUser.objects.filter(email=email)
        if confirm_account.exists():
            raise serializers.ValidationError("An account already exists with this email")
        new_account = CustomUser.objects.create_user(email=email, password=password)
        return new_account


class HostUserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the HostUserProfile model.

    This serializer handles the creation and representation of host profiles.
    The 'user' field is read-only and displays the string representation of
    the related user.

    Attributes:
        user (StringRelatedField): A read-only field for the associated user.
    """
    user = serializers.StringRelatedField()

    class Meta:
        """
        Meta options for the HostUserProfileSerializer.

        Attributes:
            model (Model): The model to be serialized (HostUserProfile).
            fields (str): Specifies that all fields in the model should be used.
        """
        model = HostUserProfile
        fields = "__all__"
        