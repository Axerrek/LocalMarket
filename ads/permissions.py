from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Pozwala edytować/usuwać obiekty tylko ich właścicielowi.
    """

    def has_object_permission(self, request, view, obj):
        # Zawsze pozwala na GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Właściciel ogłoszenia może edytować/usunąć
        return obj.owner == request.user
