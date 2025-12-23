from django.urls import path
from .views_htmx import ads_list_fragment, ad_item_fragment, ad_form

urlpatterns = [
    path('form/', ad_form, name='ad_form'),
    path('ads/list-fragment/', ads_list_fragment, name='ads_list_fragment'),
    path('ads/item-fragment/<int:ad_id>/', ad_item_fragment, name='ad_item_fragment'),
]