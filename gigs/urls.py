from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.gig_index, name="gig_index"),
    path("<int:gig_id>", views.gig_view, name="gig_info"),
    path("create_gig", views.create_gig, name="create_gig"),
    path("category/<int:category_id>", views.show_category, name="category"),
    path("orders/", include("orders.urls")),
    path("approve/", views.comment_aprove, name="approve"),
    path("<int:gigid>/edit", views.edit_gig, name="edit_gig"),
    path("plan/<int:planid>/edit", views.edit_plan, name="edit_plan"),
]
