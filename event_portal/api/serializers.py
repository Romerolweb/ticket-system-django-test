from ..models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    This serializer handles the representation of Category objects, including
    all fields.

    Attributes:
        Meta (class): A class to configure the serializer's behavior.
    """

    class Meta:
        """
        Meta options for the CategorySerializer.

        Attributes:
            model (Model): The model to be serialized (Category).
            fields (str): Specifies that all fields in the model should be used.
        """
        model = Category
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.

    This serializer handles the representation of Event objects. It includes
    validation to ensure that the event's end date is not before its start date.

    Attributes:
        host (StringRelatedField): A read-only field for the event host.
        slug (StringRelatedField): A read-only field for the event slug.
        Meta (class): A class to configure the serializer's behavior.
    """
    host = serializers.StringRelatedField()
    slug = serializers.StringRelatedField()

    class Meta:
        """
        Meta options for the EventSerializer.

        Attributes:
            model (Model): The model to be serialized (Event).
            fields (list): The fields to include in the serialization.
        """
        model = Event
        fields = [
            "title", "event_start_date",
            "event_start_time", "event_end_date",
            "event_end_time", "location",
            "address", "date_created", "category",
            "last_updated", "about", "expired", "host",
            "slug"
        ]

    def validate(self, data):
        """
        Validates that the event end date is not earlier than the start date.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data.

        Raises:
            ValidationError: If the event_end_date is before the
                             event_start_date.
        """
        try:
            if data["event_end_date"] < data["event_start_date"]:
                raise serializers.ValidationError("event_end_date cannot be less than event_start_date")
        except KeyError:
            pass
        return data
        
    