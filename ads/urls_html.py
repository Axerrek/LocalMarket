from django.urls import path
from .views_html import ads_list

urlpatterns = [
    path('', ads_list, name='ads_list'),
]
