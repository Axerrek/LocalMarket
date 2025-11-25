from django.shortcuts import render
from .models import Ad, Category
from django.contrib.auth.models import User

def ad_form(request):
    # Formularz HTMX
    categories = Category.objects.all()
    return render(request, "ads/partials/ad_form.html", {"categories": categories})

def ad_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")  # <--- tutaj plik

        ad = Ad.objects.create(
            title=title,
            description=description,
            price=price,
            owner=request.user if request.user.is_authenticated else User.objects.first(),
            category=Category.objects.get(id=category_id) if category_id else None,
            image=image  # <--- przypisanie obrazu
        )

        # Zwracamy fragment <li> dla HTMX
        return render(request, "ads/partials/ad_item.html", {"ad": ad})
