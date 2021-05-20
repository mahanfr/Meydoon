import os
from core.settings import MEDIA_ROOT
from django.db.models.signals import post_save ,post_delete ,pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from users.models import Profile
from wallets.models import Wallet

User = get_user_model()

# AUTO CREATE PROFILE AFTER USER CREATED
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# AUTO CREATE WALLET AFTER USER CREATED
@receiver(post_save, sender=User)
def create_wallet(sender,instance,created,**kwargs):
    if created:
        Wallet.objects.create(user=instance)
    instance.wallet.save()

# TODO: change hardcoded default to a settings property
# AUTO DELETE PROFILE PICS AFTER MODEL DELETE
@receiver(post_delete,sender=Profile)
def auto_delete_profile_pic_on_delete(sender,instance,**kwargs):
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path)and not 'default.jpg' in str(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)

# AUTO DELETE PROFILE PICS AFTER MODEL MODIFIED
@receiver(pre_save, sender=Profile)
def auto_delete_profile_pic_on_change(sender, instance, **kwargs):
    if not instance.id:
        return False
    
    try:
        old_file = Profile.objects.get(id=instance.id).profile_pic
    except Profile.DoesNotExist:
        return False

    new_file = instance.profile_pic
    if old_file and not old_file == new_file and not 'default.jpg' in str(old_file.path):
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
