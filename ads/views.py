from rest_framework import viewsets, permissions
from .models import Ad, Category
from .serializers import AdSerializer, CategorySerializer
from .permissions import IsOwner  # stwórz plik permissions.py

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            return [IsOwner()]
        return super().get_permissions()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
