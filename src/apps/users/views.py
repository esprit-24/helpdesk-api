from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.permissions import (
    IsManagerOrAdmin,
    IsSelfOrManagerOrAdmin,
)   
from apps.users.serializers import UserReadSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for the User model.
    """

    queryset = User.objects.order_by("username")
    serializer_class = UserReadSerializer

    def get_permissions(self):
        """
        Return the permissions required for the current action.
        """
        if self.action == "list":
            permission_classes = [IsManagerOrAdmin]

        elif self.action == "retrieve":
            permission_classes = [
                IsAuthenticated,
                IsSelfOrManagerOrAdmin,
            ]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]