from rest_framework.permissions import BasePermission

from apps.users.models import User


####################################################
# Role-based permissions
####################################################

class IsAdmin(BasePermission):
    """
    Permission allowing only administrators.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(
            request,
            view,
        )


class IsManagerOrAdmin(BasePermission):
    """
    Permission allowing managers and administrators.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in (
                User.Role.ADMIN,
                User.Role.MANAGER,
            )
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(
            request,
            view,
        )


####################################################
# Ticket permissions
####################################################

class CanViewTicket(BasePermission):
    """
    Permission allowing a user to view a ticket.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return whether the authenticated user can view the ticket.
        """
        user = request.user

        if user.role in (
            User.Role.ADMIN,
            User.Role.MANAGER,
        ):
            return True

        if obj.requester == user:
            return True

        return obj.assignments.filter(
            technician=user,
        ).exists()


####################################################
# Assignment permissions
####################################################

class CanViewAssignment(BasePermission):
    """
    Permission allowing a user to view an assignment.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return whether the authenticated user can view the assignment.
        """
        user = request.user

        if user.role in (
            User.Role.ADMIN,
            User.Role.MANAGER,
        ):
            return True

        return obj.technician == user