from django.db.models.fields import DateTimeField
from django.forms import widgets
from orders.models import Deliver, Message, Order
from django import forms


class OrderForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Order
        fields = ["price_offer", "deadline", "file_example", "order_message"]
        exclude = ["plan_id", "gig", "customer"]


class DeliverForm(forms.ModelForm):
    message = forms.CharField(max_length=20, required=True)
    file = forms.FileField(required=True)

    class Meta:
        model = Deliver
        fields = ["message", "file"]
        exclude = ["order", "is_accepted", "is_paid"]
