from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.tickets.models import (
    Assignment,
    Category,
    Priority,
    Status,
    Ticket,
)
from apps.tickets.permissions import (
    CanViewAssignment,
    CanViewTicket,
    IsAdmin,
    IsManagerOrAdmin,
)
from apps.tickets.serializers import (
    AssignmentReadSerializer,
    AssignmentWriteSerializer,
    CategorySerializer,
    PrioritySerializer,
    StatusSerializer,
    TicketReadSerializer,
    TicketWriteSerializer,
)
from apps.users.models import User


####################################################
# Status ViewSet
####################################################

class StatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Status model.
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_permissions(self):
        """
        Return the permissions required for the current action.
        """
        if self.action in (
            "create",
            "update",
            "partial_update",
        ):
            permission_classes = [
                IsAuthenticated,
                IsManagerOrAdmin,
            ]

        elif self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                IsAdmin,
            ]

        else:
            permission_classes = [
                IsAuthenticated,
            ]

        return [
            permission()
            for permission in permission_classes
        ]


####################################################
# Priority ViewSet
####################################################

class PriorityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Priority model.
    """

    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer

    def get_permissions(self):
        """
        Return the permissions required for the current action.
        """
        if self.action in (
            "create",
            "update",
            "partial_update",
        ):
            permission_classes = [
                IsAuthenticated,
                IsManagerOrAdmin,
            ]

        elif self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                IsAdmin,
            ]

        else:
            permission_classes = [
                IsAuthenticated,
            ]

        return [
            permission()
            for permission in permission_classes
        ]


####################################################
# Category ViewSet
####################################################

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Category model.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """
        Return the permissions required for the current action.
        """
        if self.action in (
            "create",
            "update",
            "partial_update",
        ):
            permission_classes = [
                IsAuthenticated,
                IsManagerOrAdmin,
            ]

        elif self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                IsAdmin,
            ]

        else:
            permission_classes = [
                IsAuthenticated,
            ]

        return [
            permission()
            for permission in permission_classes
        ]


####################################################
# Ticket ViewSet
####################################################

class TicketViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Ticket model.
    """

    queryset = Ticket.objects.all()

    def get_queryset(self):
        """
        Return the tickets visible to the authenticated user.
        """
        user = self.request.user

        if user.role in (
            User.Role.ADMIN,
            User.Role.MANAGER,
        ):
            return Ticket.objects.all()

        if user.role == User.Role.REQUESTER:
            return Ticket.objects.filter(
                requester=user,
            )

        if user.role == User.Role.TECHNICIAN:
            return Ticket.objects.filter(
                assignments__technician=user,
            ).distinct()

        return Ticket.objects.none()

    def get_serializer_class(self):
        """
        Return the serializer corresponding to the current action.
        """
        if self.action in (
            "list",
            "retrieve",
        ):
            return TicketReadSerializer

        return TicketWriteSerializer

    def get_permissions(self):
        """
        Return the permissions required for the current action.
        """
        if self.action == "retrieve":
            permission_classes = [
                IsAuthenticated,
                CanViewTicket,
            ]

        elif self.action in (
            "update",
            "partial_update",
        ):
            permission_classes = [
                IsAuthenticated,
                IsManagerOrAdmin,
            ]

        elif self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                IsAdmin,
            ]

        else:
            permission_classes = [
                IsAuthenticated,
            ]

        return [
            permission()
            for permission in permission_classes
        ]

    def perform_create(self, serializer):
        """
        Automatically set the requester to the authenticated user.
        """
        serializer.save(
            requester=self.request.user,
        )


####################################################
# Assignment ViewSet
####################################################

class AssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Assignment model.
    """

    queryset = Assignment.objects.all()

    def get_queryset(self):
        """
        Return the assignments visible to the authenticated user.
        """
        user = self.request.user

        if user.role in (
            User.Role.ADMIN,
            User.Role.MANAGER,
        ):
            return Assignment.objects.all()

        if user.role == User.Role.TECHNICIAN:
            return Assignment.objects.filter(
                technician=user,
            )

        return Assignment.objects.none()

    def get_serializer_class(self):
        """
        Return the serializer corresponding to the current action.
        """
        if self.action in (
            "list",
            "retrieve",
        ):
            return AssignmentReadSerializer

        return AssignmentWriteSerializer

    def get_permissions(self):
        """
        Return the permissions required for the current action.
        """
        if self.action == "retrieve":
            permission_classes = [
                IsAuthenticated,
                CanViewAssignment,
            ]

        elif self.action in (
            "create",
            "update",
            "partial_update",
            "destroy",
        ):
            permission_classes = [
                IsAuthenticated,
                IsManagerOrAdmin,
            ]

        else:
            permission_classes = [
                IsAuthenticated,
            ]

        return [
            permission()
            for permission in permission_classes
        ]

    def perform_create(self, serializer):
        """
        Automatically set the assigner to the authenticated user.
        """
        serializer.save(
            assigned_by=self.request.user,
        )