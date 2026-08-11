from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_authenticated = bool(request.user and request.user.is_authenticated)

        if not is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True

        if request.method == "POST" and getattr(
                view,
                "basename",
                None) == "order":
            return True

        return bool(request.user.is_staff)
