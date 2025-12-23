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