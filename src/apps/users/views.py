from rest_framework import viewsets

from apps.users.models import User
from apps.users.serializers import UserReadSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for the User model.
    """

    queryset = User.objects.order_by("username")
    serializer_class = UserReadSerializer