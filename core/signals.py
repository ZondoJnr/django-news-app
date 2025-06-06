from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import JournalistProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        JournalistProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_journalistprofile(sender, instance, **kwargs):
    instance.journalistprofile.save()
