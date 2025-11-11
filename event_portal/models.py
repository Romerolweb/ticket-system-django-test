from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import uuid
# Create your models here.


class BaseTrackingModel(models.Model):
    """
    An abstract base model providing common tracking fields.

    This model includes a UUID primary key, a creation timestamp, and a last
    updated timestamp. It is intended to be inherited by other models.

    Attributes:
        id (UUIDField): The primary key for the model, a UUID.
        date_created (DateTimeField): The timestamp when the instance was created.
        last_updated (DateTimeField): The timestamp of the last update.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the BaseTrackingModel.
        """
        abstract = True


class Category(BaseTrackingModel):
    """
    A model representing event categories.

    Each category has a unique name and a slug for URL generation.

    Attributes:
        EVENT_CATEGORIES (tuple): A tuple of choices for the category name.
        name (CharField): The name of the category.
        slug (SlugField): The URL-friendly version of the name.
    """
    EVENT_CATEGORIES = (
        ("Conferences", "Conferences"),
        ("Trade Shows", "Trade Shows"),
        ("Networking", "Networking"),
        ("WorkShops", "WorkShops"),
        ("Product Launch", "Product Launch"),
        ("Charity", "Charity"),
        ("Music", "Music"),
        ("Concert", "Concert"),
        ("Performing & Visual Arts", "Performing & Visual Arts"),
        ("Food & Drink", "Food & Drink"),
        ("Party", "Party"),
        ("Sports & Fitness", "Sports & Fitness"),
        ("Technology", "Technology"),
        ("Digital", "Digital")
    )
    name = models.CharField(max_length=40, choices=EVENT_CATEGORIES, unique=True)
    slug = models.SlugField(db_index=True, editable=False)

    class Meta(BaseTrackingModel.Meta):
        """
        Meta options for the Category model.
        """
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically generate the slug.
        """
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name


class Event(BaseTrackingModel):
    """
    The main model for storing event details.

    Attributes:
        title (CharField): The title of the event.
        event_start_date (DateField): The start date of the event.
        event_end_date (DateField): The end date of the event.
        event_start_time (TimeField): The start time of the event.
        event_end_time (TimeField): The end time of the event.
        location (CharField): The general location or venue of the event.
        address (CharField): The specific address of the event.
        host (ForeignKey): The user who is hosting the event.
        slug (SlugField): The URL-friendly version of the title.
        category (ManyToManyField): The categories the event belongs to.
        about (TextField): A detailed description of the event.
        expired (BooleanField): A flag indicating if the event has passed.
    """
    title = models.CharField(max_length=250, unique=True)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=100, null=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(db_index=True, editable=False)
    category = models.ManyToManyField(Category)
    about = models.TextField(null=True)
    expired = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically generate the slug.
        """
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the event.

        Returns:
            str: The title of the event.
        """
        return self.title


class Ticket(BaseTrackingModel):
    """
    A model for different types of tickets available for an event.

    Attributes:
        ticket_type (CharField): The type of the ticket (e.g., VIP, General).
        ticket_price (FloatField): The price of the ticket.
        event (ForeignKey): The event this ticket is associated with.
    """
    ticket_type = models.CharField(max_length=25)
    ticket_price = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the ticket.

        Returns:
            str: The ID of the ticket.
        """
        return self.ticket_id


class SocialMedia(BaseTrackingModel):
    """
    A model to store social media links for an event.

    Attributes:
        facebook (URLField): The Facebook URL for the event.
        instagram (URLField): The Instagram URL for the event.
        twitter (URLField): The Twitter URL for the event.
        linkedIn (URLField): The LinkedIn URL for the event.
        event (ForeignKey): The event these social media links belong to.
    """
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the social media links.

        Returns:
            str: The title of the associated event.
        """
        return f"{self.event.title}"
        
