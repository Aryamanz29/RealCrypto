from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Position
from .tasks import get_crypto_data


@receiver(post_save, sender=Position)
def set_codes(sender, instance, created, *args, **kwargs):
    if created:
        get_crypto_data.delay()
