from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from users.models import Profile
from wallets.models import Wallet

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def create_wallet(sender,instance,created,**kwargs):
    if created:
        Wallet.objects.create(user=instance)
    instance.wallet.save()