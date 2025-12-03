from django.shortcuts import render, redirect
from .models import Ad, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def ad_form(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")  # <-- NOWOŚĆ

        ad = Ad.objects.create(
            title=title,
            description=description,
            price=price,
            owner=request.user if request.user.is_authenticated else User.objects.first(),
            category=Category.objects.get(id=category_id) if category_id else None,
            image=image  # <-- ZAPIS OBRAZU
        )

        return render(request, "ads/partials/ad_item.html", {"ad": ad})

    return render(request, "ads/partials/ad_form.html", {"categories": categories})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, "ads/ad_detail.html", {"ad": ad})

@login_required
def ad_create_page(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")  # <-- NOWOŚĆ

        ad = Ad.objects.create(
            title=title,
            description=description,
            price=price,
            owner=request.user,
            category=Category.objects.get(id=category_id) if category_id else None,
            image=image  # <-- ZAPIS OBRAZU
        )

        return redirect("ads_list")

    return render(request, "ads/ad_create.html", {"categories": categories})


def ads_list(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, 'ads/ads_list.html', {'ads': ads})


def login_page(request):
    return render(request, "auth/login.html")
