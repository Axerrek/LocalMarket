from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.conf.urls.static import static
def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def test_api(request):
    return Response({"message": "LocalMarket API działa poprawnie!"})


urlpatterns = [
    path('', home, name='home'),                 # Strona główna HTML
    path('admin/', admin.site.urls),             # Admin
    path('ads/', include('ads.urls_html')),      # HTML widoki
    path('htmx/', include('ads.urls_htmx')),     # HTMX widoki
    path('api/', include('ads.urls')),           # REST API
    path('api/test/', test_api),                 # Testowy endpoint JSON
    path('accounts/', include('allauth.urls')),  # Allauth  
    path('chat/', include('chat.urls')),         # Chat app
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)