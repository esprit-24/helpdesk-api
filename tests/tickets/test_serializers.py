from datetime import timedelta

import pytest
from django.utils import timezone

from apps.tickets.models import Assignment, Ticket
from apps.tickets.serializers import (
    AssignmentReadSerializer,
    AssignmentWriteSerializer,
    CategorySerializer,
    CategorySummarySerializer,
    PrioritySerializer,
    PrioritySummarySerializer,
    StatusSerializer,
    StatusSummarySerializer,
    TicketReadSerializer,
    TicketSummarySerializer,
    TicketWriteSerializer,
)

# ============================================================
# Status serializers
# ============================================================


@pytest.mark.django_db
def test_status_summary_serializer(status):
    # Arrange
    serializer = StatusSummarySerializer(status)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": status.id,
        "name": "Open",
    }


@pytest.mark.django_db
def test_status_serializer(status):
    # Arrange
    status.description = "Ticket is currently open."
    status.is_final = False
    status.is_active = True
    status.save()

    serializer = StatusSerializer(status)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": status.id,
        "name": "Open",
        "description": "Ticket is currently open.",
        "is_final": False,
        "is_active": True,
    }


@pytest.mark.django_db
def test_status_serializer_accepts_valid_data():
    # Arrange
    data = {
        "name": "Closed",
        "description": "Ticket is closed.",
        "is_final": True,
        "is_active": True,
    }

    serializer = StatusSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["name"] == "Closed"
    assert serializer.validated_data["is_final"] is True


# ============================================================
# Priority serializers
# ============================================================


@pytest.mark.django_db
def test_priority_summary_serializer(priority):
    # Arrange
    serializer = PrioritySummarySerializer(priority)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": priority.id,
        "name": "High",
    }


@pytest.mark.django_db
def test_priority_serializer(priority):
    # Arrange
    priority.description = "High priority ticket."
    priority.save()

    serializer = PrioritySerializer(priority)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": priority.id,
        "name": "High",
        "description": "High priority ticket.",
        "level": 1,
    }


@pytest.mark.django_db
def test_priority_serializer_accepts_valid_data():
    # Arrange
    data = {
        "name": "Critical",
        "description": "Critical priority.",
        "level": 2,
    }

    serializer = PrioritySerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["name"] == "Critical"
    assert serializer.validated_data["level"] == 2


# ============================================================
# Category serializers
# ============================================================


@pytest.mark.django_db
def test_category_summary_serializer(category):
    # Arrange
    serializer = CategorySummarySerializer(category)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": category.id,
        "name": "Hardware",
    }


@pytest.mark.django_db
def test_category_serializer(category):
    # Arrange
    category.description = "Hardware-related issues."
    category.save()

    serializer = CategorySerializer(category)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": category.id,
        "name": "Hardware",
        "description": "Hardware-related issues.",
    }


@pytest.mark.django_db
def test_category_serializer_accepts_valid_data():
    # Arrange
    data = {
        "name": "Software",
        "description": "Software-related issues.",
    }

    serializer = CategorySerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["name"] == "Software"


# ============================================================
# Ticket summary serializer
# ============================================================


@pytest.mark.django_db
def test_ticket_summary_serializer(ticket):
    # Arrange
    serializer = TicketSummarySerializer(ticket)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": ticket.id,
        "title": "Computer does not start",
        "requester": {
            "id": ticket.requester.id,
            "full_name": "",
            "is_active": True,
        },
    }


# ============================================================
# Ticket read serializer
# ============================================================


@pytest.mark.django_db
def test_ticket_read_serializer_without_owner(ticket):
    # Arrange
    serializer = TicketReadSerializer(ticket)

    # Act
    data = serializer.data

    # Assert
    assert data["id"] == ticket.id
    assert data["title"] == "Computer does not start"
    assert data["description"] == ""
    assert data["owner"] is None

    assert data["requester"] == {
        "id": ticket.requester.id,
        "full_name": "",
        "is_active": True,
    }

    assert data["status"] == {
        "id": ticket.status.id,
        "name": "Open",
    }

    assert data["priority"] == {
        "id": ticket.priority.id,
        "name": "High",
    }

    assert data["category"] == {
        "id": ticket.category.id,
        "name": "Hardware",
    }

    assert data["closed_at"] is None


@pytest.mark.django_db
def test_ticket_read_serializer_with_owner(
    ticket,
    manager,
):
    # Arrange
    ticket.owner = manager
    ticket.save()

    serializer = TicketReadSerializer(ticket)

    # Act
    data = serializer.data

    # Assert
    assert data["owner"] == {
        "id": manager.id,
        "full_name": "",
        "is_active": True,
    }


# ============================================================
# Ticket write serializer
# ============================================================


@pytest.mark.django_db
def test_ticket_write_serializer_accepts_valid_data(
    status,
    priority,
    category,
):
    # Arrange
    data = {
        "title": "New ticket",
        "description": "New ticket description.",
        "status": status.id,
        "priority": priority.id,
        "category": category.id,
    }

    serializer = TicketWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["title"] == "New ticket"
    assert serializer.validated_data["status"] == status
    assert serializer.validated_data["priority"] == priority
    assert serializer.validated_data["category"] == category


@pytest.mark.django_db
def test_ticket_write_serializer_accepts_null_owner(
    status,
    priority,
    category,
):
    # Arrange
    data = {
        "title": "New ticket",
        "description": "",
        "owner": None,
        "status": status.id,
        "priority": priority.id,
        "category": category.id,
    }

    serializer = TicketWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["owner"] is None


@pytest.mark.django_db
def test_ticket_write_serializer_rejects_missing_status(
    priority,
    category,
):
    # Arrange
    data = {
        "title": "New ticket",
        "description": "",
        "priority": priority.id,
        "category": category.id,
    }

    serializer = TicketWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is False
    assert "status" in serializer.errors


@pytest.mark.django_db
def test_ticket_write_serializer_rejects_missing_priority(
    status,
    category,
):
    # Arrange
    data = {
        "title": "New ticket",
        "description": "",
        "status": status.id,
        "category": category.id,
    }

    serializer = TicketWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is False
    assert "priority" in serializer.errors


@pytest.mark.django_db
def test_ticket_write_serializer_rejects_missing_category(
    status,
    priority,
):
    # Arrange
    data = {
        "title": "New ticket",
        "description": "",
        "status": status.id,
        "priority": priority.id,
    }

    serializer = TicketWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is False
    assert "category" in serializer.errors


# ============================================================
# Assignment read serializer
# ============================================================


@pytest.mark.django_db
def test_assignment_read_serializer(assignment):
    # Arrange
    serializer = AssignmentReadSerializer(assignment)

    # Act
    data = serializer.data

    # Assert
    assert data["id"] == assignment.id

    assert data["ticket"] == {
        "id": assignment.ticket.id,
        "title": "Computer does not start",
        "requester": {
            "id": assignment.ticket.requester.id,
            "full_name": "",
            "is_active": True,
        },
    }

    assert data["technician"] == {
        "id": assignment.technician.id,
        "full_name": "",
        "is_active": True,
    }

    assert data["assigned_by"] == {
        "id": assignment.assigned_by.id,
        "full_name": "",
        "is_active": True,
    }

    assert data["ended_at"] is None
    assert data["is_primary"] is False


# ============================================================
# Assignment write serializer
# ============================================================


@pytest.mark.django_db
def test_assignment_write_serializer_accepts_valid_data(
    ticket,
    technician,
):
    # Arrange
    data = {
        "ticket": ticket.id,
        "technician": technician.id,
        "is_primary": True,
    }

    serializer = AssignmentWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["ticket"] == ticket
    assert serializer.validated_data["technician"] == technician
    assert serializer.validated_data["is_primary"] is True


@pytest.mark.django_db
def test_assignment_write_serializer_accepts_null_ended_at(
    ticket,
    technician,
):
    # Arrange
    data = {
        "ticket": ticket.id,
        "technician": technician.id,
        "ended_at": None,
        "is_primary": False,
    }

    serializer = AssignmentWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["ended_at"] is None


@pytest.mark.django_db
def test_assignment_write_serializer_accepts_ended_at(
    ticket,
    technician,
):
    # Arrange
    ended_at = timezone.now() + timedelta(hours=1)

    data = {
        "ticket": ticket.id,
        "technician": technician.id,
        "ended_at": ended_at,
        "is_primary": False,
    }

    serializer = AssignmentWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is True
    assert serializer.validated_data["ended_at"] == ended_at


@pytest.mark.django_db
def test_assignment_write_serializer_rejects_missing_ticket(
    technician,
):
    # Arrange
    data = {
        "technician": technician.id,
        "is_primary": False,
    }

    serializer = AssignmentWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is False
    assert "ticket" in serializer.errors


@pytest.mark.django_db
def test_assignment_write_serializer_rejects_missing_technician(
    ticket,
):
    # Arrange
    data = {
        "ticket": ticket.id,
        "is_primary": False,
    }

    serializer = AssignmentWriteSerializer(data=data)

    # Act
    is_valid = serializer.is_valid()

    # Assert
    assert is_valid is False
    assert "technician" in serializer.errors
