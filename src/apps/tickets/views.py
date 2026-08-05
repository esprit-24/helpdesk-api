from rest_framework import viewsets

from apps.tickets.models import (
    Status,
    Priority,
    Category,
    Ticket,
)
from apps.tickets.serializers import (
    StatusSerializer,
    PrioritySerializer,
    CategorySerializer,
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