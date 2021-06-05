from orders.models import Order
from gigs.models import Gig, Plan
from django.shortcuts import redirect, render
from .forms import DeliverForm, OrderForm

# Create your views here.
def order(request):
    plan_id = request.GET.get("plan", "/")
    gig_id = request.GET.get("gig", "/")
    gig = Gig.objects.get(id=gig_id)
    if request.method == "POST":
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save(commit=False).plan_id = plan_id
            order_form.save(commit=False).customer = request.user
            order_form.save(commit=False).gig = gig
            # How git works
            order_form.save()
            return redirect("index")
    else:
        order_form = OrderForm()
    return render(request, "orders/create_order.html", context={"order_form": order_form})


def deliver(request):
    order_id = request.GET.get("order", "/")
    if request.method == "POST":
        order = Order.objects.get(id=order_id)
        deliver_form = DeliverForm(request.POST, request.FILES)
        if deliver_form.is_valid():
            deliver_form.save(commit=False).order = order
            deliver_form.save()
            return redirect("profile")
        else:
            redirect("deliver")
    else:
        deliver_form = DeliverForm()
    return render(request, "orders/deliver.html", context={"deliver_form": deliver_form})
