import pytest
from rest_framework.test import APIRequestFactory

from apps.tickets.models import Assignment, Category, Priority, Status, Ticket
from apps.users.models import User


@pytest.fixture
def requester():
    return User.objects.create_user(
        username="requester",
        password="testpassword",
        role=User.Role.REQUESTER,
    )


@pytest.fixture
def other_requester():
    return User.objects.create_user(
        username="other-requester",
        password="testpassword",
        role=User.Role.REQUESTER,
    )


@pytest.fixture
def technician():
    return User.objects.create_user(
        username="technician",
        password="testpassword",
        role=User.Role.TECHNICIAN,
    )


@pytest.fixture
def manager():
    return User.objects.create_user(
        username="manager",
        password="testpassword",
        role=User.Role.MANAGER,
    )


@pytest.fixture
def admin():
    return User.objects.create_user(
        username="admin",
        password="testpassword",
        role=User.Role.ADMIN,
    )


@pytest.fixture
def status():
    return Status.objects.create(
        name="Open",
    )


@pytest.fixture
def priority():
    return Priority.objects.create(
        name="High",
        level=1,
    )


@pytest.fixture
def category():
    return Category.objects.create(
        name="Hardware",
    )


@pytest.fixture
def ticket(requester, status, priority, category):
    return Ticket.objects.create(
        title="Computer does not start",
        requester=requester,
        status=status,
        priority=priority,
        category=category,
    )


@pytest.fixture
def other_ticket(other_requester, status, priority, category):
    return Ticket.objects.create(
        title="Other computer does not start",
        requester=other_requester,
        status=status,
        priority=priority,
        category=category,
    )


@pytest.fixture
def assignment(ticket, technician, manager):
    return Assignment.objects.create(
        ticket=ticket,
        technician=technician,
        assigned_by=manager,
    )


@pytest.fixture
def request_factory():
    return APIRequestFactory()