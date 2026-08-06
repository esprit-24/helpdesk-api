from rest_framework.routers import DefaultRouter

from apps.tickets.views import (
    AssignmentViewSet,
    CategoryViewSet,
    PriorityViewSet,
    StatusViewSet,
    TicketViewSet,
)


router = DefaultRouter()

router.register(
    "statuses",
    StatusViewSet,
    basename="status",
)

router.register(
    "priorities",
    PriorityViewSet,
    basename="priority",
)

router.register(
    "categories",
    CategoryViewSet,
    basename="category",
)

router.register(
    "tickets",
    TicketViewSet,
    basename="ticket",
)

router.register(
    "assignments",
    AssignmentViewSet,
    basename="assignment",
)


urlpatterns = router.urls