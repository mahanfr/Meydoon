import uuid
from django.db import models
from django.utils import timezone


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)
    last_withdraw_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'#{self.id}'


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey('wallets.Wallet', on_delete=models.PROTECT)
    amount = models.BigIntegerField()
    state = models.SmallIntegerField(default=1) # ckeck if transaction was seccessful
    source = models.SmallIntegerField(default=0)
    is_withdrawn = models.BooleanField(default=False) # check if the transaction is still dangerous to be removed
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'#{self.id}'

