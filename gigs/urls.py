from django.urls import path
from . import views

urlpatterns = [
    path('',views.gig_index,name='gig_index'),
    path('<int:gig_id>',views.gig_view,name='gig_info')
]