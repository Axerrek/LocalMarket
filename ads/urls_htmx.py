from django.urls import path
from .views import ads_htmx

urlpatterns = [
    path('', ads_htmx, name='ads-htmx'),
]
