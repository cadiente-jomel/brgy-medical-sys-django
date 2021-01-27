from .models import CitizenPersonalInfo, CitizenProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CitizenPersonalInfo)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CitizenProfile.objects.create(citizen=instance)


@receiver(post_save, sender=CitizenPersonalInfo)
def save_profile(sender, instance, **kwargs):
    instace.profile_pic.save()
