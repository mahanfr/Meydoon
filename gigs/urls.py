from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.gig_index, name="gig_index"),
    # path("<int:gig_id>", views.gig_view, name="gig_info"),
    path("create_gig", views.create_gig, name="create_gig"),
    path("category/<int:category_id>", views.show_category, name="category"),
    path("orders/", include("orders.urls")),
    path("approve/", views.comment_aprove, name="approve"),
    path("<int:gigid>/edit", views.edit_gig, name="edit_gig"),
    path("plan/edit/<int:planid>/", views.edit_plan, name="edit_plan"),
    path("<int:pk>", views.GigDetail.as_view(), name="gig_detail"),
    path("add_comment", views.AddComment.as_view(), name="add_comment"),
    path("add_plan", views.AddPlan.as_view(), name="add_plan"),
    # path("add_image", views.add_image, name="add_image"),
]
