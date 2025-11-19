from django.urls import path
from . import views_html

urlpatterns = [
    path('form/', views_html.ad_form, name='ad_form'),
]