import django_filters
from ..models import Event

class EventFilter(django_filters.FilterSet):
    """
    A filter set for querying Event instances.

    This filter set allows for filtering events by a date range for the
    event start date, as well as by location, host's email, and category name.

    Attributes:
        event_start_date (DateFromToRangeFilter): A filter for a date range.
        Meta (class): A class to configure the filter set's behavior.
    """
    event_start_date = django_filters.DateFromToRangeFilter()

    class Meta:
        """
        Meta options for the EventFilter.

        Attributes:
            model (Model): The model to be filtered (Event).
            fields (list): The fields to include in the filter.
        """
        model = Event
        fields = ["event_start_date", "location", "host__email", "category__name"]