from orders.models import Message, Order
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from .forms import UserEditForm, UserRegisterForm, ProfileEditForm
from gigs.models import Gig


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {"u_form": user_form, "p_form": profile_form}

    return render(request, "users/profile_edit.html", context)


@login_required
@csrf_exempt
def profile(request):
    user_gig = Gig.objects.filter(user=request.user)
    orders = []
    message = ""
    for gig in user_gig:
        try:
            orders.append(Order.objects.get(gig=gig))
        except Order.DoesNotExist:
            continue
    if request.method == "POST":
        if request.is_ajax:
            order_id = request.POST["id"]
            x = Order.objects.get(id=order_id)
            if request.POST["act"] == "accept":
                x.state = 1
                x.save()
            else:
                x.state = 3
                x.save()
            return redirect("profile")
        return redirect("profile")
    else:
        context = {"user_gig": user_gig, "orders": orders, "message": message}
        return render(request, "users/profile.html", context=context)
