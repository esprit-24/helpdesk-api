from rest_framework.permissions import BasePermission

from apps.users.models import User


class IsManagerOrAdmin(BasePermission):
    """
    Permission allowing access only to managers and administrators.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in (
                User.Role.MANAGER,
                User.Role.ADMIN,
            )
        )
    

class IsSelfOrManagerOrAdmin(BasePermission):
    """
    Permission allowing users to access their own profile,
    or allowing managers and administrators to access any profile.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj
            or request.user.role in (
                User.Role.MANAGER,
                User.Role.ADMIN,
            )
        )