from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from .Regform import Regforms

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login")
    return render(request, "user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {
                "message": "User Not Found"
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Logged out."
    })


def signup(request):
    if request.method == "POST":
        form = Regforms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            user = authenticate(request,email=email,username=username, password=password_raw)
            login(request, user)
            return redirect("index")
    else:
        form = Regforms()
    return render(request, "signup.html", {"form": form})