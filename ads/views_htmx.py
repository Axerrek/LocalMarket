from django.shortcuts import render
from .models import Ad, Category

def ads_list_fragment(request):
    """
    Zwraca fragment HTML listy ogłoszeń.
    HTMX wywoła to przy ładowaniu strony.
    """
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, "ads/partials/ad_item_list.html", {"ads": ads})


def ad_form(request):
    """
    Renderuje formularz dodawania ogłoszenia.
    Nie tworzy obiektów bezpośrednio – obsługuje tylko HTML.
    """
    categories = Category.objects.all()
    return render(request, "ads/partials/ad_form.html", {"categories": categories})


def ad_item_fragment(request, ad_id):
    """
    Zwraca fragment HTML dla pojedynczego ogłoszenia.
    Można go użyć przy dodawaniu nowego ogłoszenia przez HTMX.
    """
    ad = Ad.objects.get(id=ad_id)
    return render(request, "ads/partials/ad_item.html", {"ad": ad})
from decimal import Decimal
def ads_filtered(request):
    qs = Ad.objects.all()
    print("Oto Twoje zapytanie SQL:")
    print(qs.query)
    # Kategorie
    category = request.GET.get("category")
    if category:
        qs = qs.filter(category_id=category)

    # Region
    region_id = request.GET.get('region')
    if region_id:
        qs = qs.filter(region=region_id)

    # Wyszukiwanie po tytule
    q = request.GET.get("q")
    if q:
        qs = qs.filter(title__icontains=q)

    # Cena min/max
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    try:
        if price_min:
            qs = qs.filter(price__gte=Decimal(price_min))
        if price_max:
            qs = qs.filter(price__lte=Decimal(price_max))
    except Exception:
        pass  # w razie złego formatu liczby

    return render(
        request,
        "ads/partials/ad_item_list.html",
        {"ads": qs}
    )