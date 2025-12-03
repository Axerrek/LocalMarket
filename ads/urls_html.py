from django.urls import path
from .views_html import ads_list
from . import views_html
from . import views_auth
urlpatterns = [
    path('', ads_list, name='ads_list'),
    path('new/', views_html.ad_create_page, name='ad_create'),
    # LOGOWANIE / REJESTRACJA
    path('login/', views_auth.login_page, name='login'),
    path('register/', views_auth.register_page, name='register'),
    path('logout/', views_auth.logout_user, name='logout'),
    path("<int:ad_id>/", views_html.ad_detail, name="ad_detail"),
]
