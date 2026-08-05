from rest_framework import serializers

from apps.tickets.models import (
    Category,
    Priority,
    Status,
    Ticket,
)
from apps.users.models import User
from apps.users.serializers import UserSummarySerializer


####################################################
# Status serializers
####################################################

class StatusSummarySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying basic status information.
    """

    class Meta:
        model = Status
        fields = (
            "id",
            "name",
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


####################################################
# Priority serializers
####################################################

class PrioritySummarySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying basic priority information.
    """

    class Meta:
        model = Priority
        fields = (
            "id",
            "name",
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


####################################################
# Category serializers
####################################################

class CategorySummarySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying basic category information.
    """

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
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


####################################################
# Ticket serializers
####################################################

class TicketReadSerializer(serializers.ModelSerializer):
    """
    Serializer for reading ticket information.
    """

    requester = UserSummarySerializer(read_only=True)
    owner = UserSummarySerializer(read_only=True)

    status = StatusSummarySerializer(read_only=True)
    priority = PrioritySummarySerializer(read_only=True)
    category = CategorySummarySerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "title",
            "description",
            "requester",
            "owner",
            "status",
            "priority",
            "category",
            "created_at",
            "updated_at",
            "closed_at",
        )


class TicketWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for writing ticket information.
    """

    requester = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )

    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
    )

    priority = serializers.PrimaryKeyRelatedField(
        queryset=Priority.objects.all(),
    )

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Ticket
        fields = (
            "title",
            "description",
            "requester",
            "owner",
            "status",
            "priority",
            "category",
        )