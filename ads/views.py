from rest_framework import viewsets
from .models import Ad, Category
from .serializers import AdSerializer, CategorySerializer

from django.shortcuts import render
from .models import Ad

def ads_htmx(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, "ads_list.html", {"ads": ads})

# Widok dla ogłoszeń
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

# Widok dla kategorii
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
