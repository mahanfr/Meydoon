from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from gigs.models import Gig
from django.contrib.auth import get_user_model


@login_required
def get_dashboard_mygigs(request):
    user_gig = request.user.gig_set.all()
    context = {"user_gig": user_gig}
    return render(request, "dashboard/mygigs.html", context=context)

@login_required
def get_dashboard_orders(request):
    gigs = request.user.gig_set.all()
    orders = []
    for gig in gigs:
        if gig.order_set.count() > 0:
            orders.append(gig.order_set.all())
    context = {"orders": orders}
    return render(request, "dashboard/orders.html", context=context)

@login_required
def get_dashboard_comments(request):
    gigs = request.user.gig_set.all()
    comments = []
    for gig in gigs:
        if gig.comment_set.count() > 0:
            comments.append(gig.order_set.all())
    context = {"comments": comments}
    return render(request, "dashboard/comments.html", context=context)