from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import MongoUser

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = MongoUser(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password1"])
            user.save()
            messages.success(request, "Account created!")

            # explicitly tell Django which BE to use
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login_id = form.cleaned_data["login"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=login_id, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome back!")
                return redirect("profile")
            messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You've been logged out")
    return redirect("login")

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")