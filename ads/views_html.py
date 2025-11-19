from django.shortcuts import render, redirect
from .models import Ad, Category
from django.contrib.auth.models import User
def ad_form(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")

        print("POST data:", title, description, price, category_id)

        ad = Ad.objects.create(
            title=title,
            description=description,
            price=price,
            owner=User.objects.first(),
            category=Category.objects.get(id=category_id) if category_id else None
        )

        # Zwracamy tylko LI do listy
        return render(request, "ads/partials/ad_item.html", {"ad": ad})

    # GET → formularz do modala
    return render(request, "ads/partials/ad_form.html", {"categories": categories})

def ads_list(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, 'ads/ads_list.html', {'ads': ads})
