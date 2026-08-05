from rest_framework import serializers

from apps.tickets.models import (
    Status,
    Priority,
    Category,
)


class StatusSerializer(serializers.ModelSerializer):
    """
    Serializer for the Status model.
    """

    class Meta:
        model = Status
        fields = (
            "id",
            "name",
            "description",
            "is_final",
            "is_active",
        )


class PrioritySerializer(serializers.ModelSerializer):
    """
    Serializer for the Priority model.
    """

    class Meta:
        model = Priority
        fields = (
            "id",
            "name",
            "description",
            "level",
        )


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
        )