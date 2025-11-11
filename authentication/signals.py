from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from authentication.models import HostUserProfile

@receiver(post_save, sender=HostUserProfile)
def update_user_instance(sender, instance, created, **kwargs) -> None:
    """
    Updates the user's 'event_hoster' status when a host profile is created.

    This signal receiver is triggered after a HostUserProfile instance is saved.
    If a new profile was created, it sets the 'event_hoster' field of the
    associated user to True.

    Args:
        sender (Model): The model class that sent the signal (HostUserProfile).
        instance (HostUserProfile): The actual instance being saved.
        created (bool): A boolean indicating whether a new record was created.
        **kwargs: Wildcard keyword arguments.
    """
    if created:
        user = instance.user
        user.event_hoster = True
        user.save()