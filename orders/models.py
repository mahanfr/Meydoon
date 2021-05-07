from django.db import models
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _

class Order(models.Model):
    STATE_CHOICES=(
        (1,_('accept')),
        (2,_('decline')),
    )
    gig = models.ForeignKey('gigs.gig', on_delete=models.SET_NULL,null=True)
    plan_id = models.IntegerField(default=0) # might get plan from web quary other than make it required
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    order_message = models.CharField(max_length=400)
    price_offer = models.IntegerField(null=True,blank=True)
    deadline = models.DateField(null=True,blank=True)
    file_example = models.FileField(upload_to='example_files',null=True,blank=True)
    state = models.SmallIntegerField(choices=STATE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    

class Message(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)


class Deliver(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.SET_NULL,null=True)
    message = models.CharField(max_length=400)
    file = models.FileField(upload_to='files')
    is_accepted = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
