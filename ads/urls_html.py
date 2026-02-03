from django.urls import path

from ads.views_htmx import ads_filtered
from .views_html import ads_list
from . import views_html
urlpatterns = [
    path('', ads_list, name='ads_list'),
    path('new/', views_html.ad_create_page, name='ad_create'),
    path("<int:ad_id>/", views_html.ad_detail, name="ad_detail"),
    path('filtered/', ads_filtered, name='ads_filtered'),
]
