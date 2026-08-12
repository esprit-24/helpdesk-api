from rest_framework import serializers

from apps.users.models import User


class UserSummarySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying basic user information.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "is_active",
        )


class UserReadSerializer(serializers.ModelSerializer):
    """
    Serializer for reading user information.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "full_name",
            "email",
            "role",
            "is_active",
        )
