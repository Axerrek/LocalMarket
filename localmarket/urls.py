from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def test_api(request):
    return Response({"message": "LocalMarket API działa poprawnie!"})

urlpatterns = [
    path('', home, name='home'),                # Strona główna HTML
    path('admin/', admin.site.urls),            # Panel admina
    path('htmx/', include('ads.urls_htmx')),   # HTMX (fragmenty HTML)
    path('api/', include('ads.urls')),          # REST API z prefiksem /api/
    path('api/test/', test_api),                # Testowy endpoint JSON
]

