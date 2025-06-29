from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedAndNotGuest(BasePermission):
    """
    Erlaubt nur authentifizierten Benutzern Änderungen,
    Gäste (username = 'Gast') dürfen nur lesen.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        return user.is_authenticated and user.username != 'Gast'
