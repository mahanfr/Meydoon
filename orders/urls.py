from django.urls import path, include
from orders import views

urlpatterns = [path("", views.order, name="order"), path("/deliver", views.deliver, name="deliver")]
