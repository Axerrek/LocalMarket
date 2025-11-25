from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Użytkownik o tej nazwie już istnieje.")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("ads_list")

    return render(request, "auth/register.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Niepoprawne dane logowania.")
            return redirect("login")

        login(request, user)
        return redirect("ads_list")

    return render(request, "auth/login.html")


def logout_user(request):
    logout(request)
    return redirect("ads_list")