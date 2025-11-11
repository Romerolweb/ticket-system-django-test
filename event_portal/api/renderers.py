from rest_framework import renderers 
import json
from django.core.serializers.json import DjangoJSONEncoder

class CustomRenderer(renderers.JSONRenderer):
    """
    A custom JSON renderer that wraps the response data in a standard format.

    This renderer formats all API responses to have a consistent structure,
    with a 'status' field ('Successful' or 'Error') and a 'data' field
    containing the actual response data or error details.

    Attributes:
        charset (str): The character set for the response.
    """
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders the data into a custom JSON format.

        If the data contains an error detail, the status is set to 'Error'.
        Otherwise, the status is 'Successful'.

        Args:
            data (dict): The response data.
            accepted_media_type (str, optional): The accepted media type.
            renderer_context (dict, optional): Context for the renderer.

        Returns:
            str: The JSON-formatted response string.
        """
        response = ""

        if "ErrorDetail" in str(data):
            response = json.dumps(
                {
                    "status": "Error",
                    "data": data,
                }
            )
        else:
            response = json.dumps(
                {
                    "status": "Successful",
                    "data": data,
                },
                cls=DjangoJSONEncoder
            )
        return response