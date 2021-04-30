from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/edit', views.profile_edit, name='editprofile'),
    path('profile', views.profile,name='profile'),
    path('gigs/', include('gigs.urls'))
]