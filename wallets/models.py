import uuid
from django.db import models

# Create your models here.
class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)

    def __str__(self):
        return f'#{self.id}'