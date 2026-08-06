from rest_framework import serializers

from apps.tickets.models import (
    Assignment,
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


class TicketSummarySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying basic ticket information.
    """

    requester = UserSummarySerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "title",
            "requester",
        )


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


####################################################
# Assignment serializers
####################################################


class AssignmentReadSerializer(serializers.ModelSerializer):
    """
    Serializer for reading assignment information.
    """

    ticket = TicketSummarySerializer(read_only=True)

    technician = UserSummarySerializer(read_only=True)

    assigned_by = UserSummarySerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = (
            "id",
            "ticket",
            "technician",
            "assigned_by",
            "assigned_at",
            "ended_at",
            "is_primary",
        )


class AssignmentWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for writing assignment information.
    """

    ticket = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(),
    )

    technician = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    assigned_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    ended_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Assignment
        fields = (
            "ticket",
            "technician",
            "assigned_by",
            "ended_at",
            "is_primary",
        )