from rest_framework.pagination import PageNumberPagination 

class CustomPagination(PageNumberPagination):
    """
    Custom pagination class for the API.

    This class sets a default page size and allows clients to override it
    using the 'max-size' query parameter, up to a maximum limit.

    Attributes:
        page_size (int): The default number of items to include on a page.
        page_size_query_param (str): The name of the query parameter for
                                     requesting a specific page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size = 8
    page_size_query_param = "max-size"
    max_page_size = 15