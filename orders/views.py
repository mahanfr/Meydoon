from gigs.models import Gig, Plan
from django.shortcuts import redirect, render
from .forms import OrderForm

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
            order_form.save()
            return redirect("index")
    else:
        order_form = OrderForm()
    return render(request, "orders/create_order.html", context={"order_form": order_form})
