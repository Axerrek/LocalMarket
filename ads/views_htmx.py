from django.shortcuts import render, redirect
from .models import Ad
from django.contrib.auth.models import User

def ad_form(request):
    return render(request, "ads/partials/ad_form.html")

def ad_create(request):
    if request.method == "POST":
        Ad.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            price=request.POST["price"],
            owner=User.objects.first(),  # tymczasowe
        )
        return redirect("ads_list")
