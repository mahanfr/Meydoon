from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_dashboard_mygigs, name="dashboard"),
    path("orders/", views.get_dashboard_orders, name="dashboard-orders"),
    # path("comments/", views.register, name="dashboard-comments"),
    # path("messages/", views.register, name="dashboard-messages"),
    # path("myorders/", views.register, name="dashboard-myorders"),
    # path("wallet/", views.register, name="dashboard-wallet"),
    # path("settings/", views.register, name="dashboard-settings"),
]
