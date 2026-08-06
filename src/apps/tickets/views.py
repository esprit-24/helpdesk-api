from rest_framework import viewsets

from apps.tickets.models import (
    Assignment,
    Category,
    Priority,
    Status,
    Ticket,
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


class StatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Status model.
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class PriorityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Priority model.
    """

    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Category model.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Ticket model.
    """

    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action in (
            "list",
            "retrieve",
        ):
            return TicketReadSerializer

        return TicketWriteSerializer
    

class AssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Assignment model.
    """

    queryset = Assignment.objects.all()

    def get_serializer_class(self):
        if self.action in (
            "list",
            "retrieve",
        ):
            return AssignmentReadSerializer

        return AssignmentWriteSerializer