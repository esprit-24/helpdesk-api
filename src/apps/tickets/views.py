from rest_framework import viewsets

from apps.tickets.models import (
    Status,
    Priority,
    Category,
)
from apps.tickets.serializers import (
    StatusSerializer,
    PrioritySerializer,
    CategorySerializer,
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