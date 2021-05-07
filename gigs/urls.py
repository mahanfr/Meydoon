from django.urls import path
from . import views

urlpatterns = [
    path('',views.gig_index,name='gig_index'),
    path('<int:gig_id>',views.gig_view,name='gig_info'),
    path('create_gig', views.create_gig, name='create_gig'),
    path('category/<int:category_id>', views.show_category, name='category')
]