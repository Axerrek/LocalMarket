from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Endpointy będą: /api/ads/, /api/categories/
]
