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