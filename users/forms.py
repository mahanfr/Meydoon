from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['email', 'user_name','phone_number', 'password1', 'password2']
