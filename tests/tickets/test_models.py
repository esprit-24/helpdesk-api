from django.core.exceptions import ValidationError

import pytest

from apps.tickets.models import Assignment, Category, Priority, Status, Ticket


@pytest.mark.django_db
def test_status_string_representation(status):
    # Arrange
    # status est fourni par la fixture.

    # Act
    result = str(status)

    # Assert
    assert result == "Open"


@pytest.mark.django_db
def test_status_name_must_be_unique(status):
    # Arrange
    duplicate_status = Status(name="Open")

    # Act + Assert
    with pytest.raises(ValidationError):
        duplicate_status.full_clean()


@pytest.mark.django_db
def test_priorities_are_ordered_by_level():
    # Arrange
    high = Priority.objects.create(
        name="High",
        level=3,
    )
    low = Priority.objects.create(
        name="Low",
        level=1,
    )
    medium = Priority.objects.create(
        name="Medium",
        level=2,
    )

    # Act
    priorities = list(Priority.objects.all())

    # Assert
    assert priorities == [low, medium, high]


@pytest.mark.django_db
def test_priority_level_must_be_unique(priority):
    # Arrange
    duplicate_priority = Priority(
        name="Critical",
        level=1,
    )

    # Act + Assert
    with pytest.raises(ValidationError):
        duplicate_priority.full_clean()


@pytest.mark.django_db
def test_priority_string_representation(priority):
    # Arrange
    # priority est fourni par la fixture.

    # Act
    result = str(priority)

    # Assert
    assert result == "High"


@pytest.mark.django_db
def test_category_string_representation(category):
    # Arrange
    # category est fourni par la fixture.

    # Act
    result = str(category)

    # Assert
    assert result == "Hardware"


@pytest.mark.django_db
def test_category_name_must_be_unique(category):
    # Arrange
    duplicate_category = Category(name="Hardware")

    # Act + Assert
    with pytest.raises(ValidationError):
        duplicate_category.full_clean()


@pytest.mark.django_db
def test_ticket_string_representation(ticket):
    # Arrange
    # ticket est fourni par la fixture.

    # Act
    result = str(ticket)

    # Assert
    assert result == "Computer does not start"


@pytest.mark.django_db
def test_ticket_owner_is_optional(ticket):
    # Arrange
    # ticket est fourni sans owner.

    # Act
    owner = ticket.owner

    # Assert
    assert owner is None


@pytest.mark.django_db
def test_ticket_closed_at_is_optional(ticket):
    # Arrange
    # ticket est fourni sans closed_at.

    # Act
    closed_at = ticket.closed_at

    # Assert
    assert closed_at is None


@pytest.mark.django_db
def test_tickets_are_ordered_by_creation_date(
    requester,
    status,
    priority,
    category,
):
    # Arrange
    first_ticket = Ticket.objects.create(
        title="First ticket",
        requester=requester,
        status=status,
        priority=priority,
        category=category,
    )
    second_ticket = Ticket.objects.create(
        title="Second ticket",
        requester=requester,
        status=status,
        priority=priority,
        category=category,
    )

    # Act
    tickets = list(Ticket.objects.all())

    # Assert
    assert tickets == [second_ticket, first_ticket]


@pytest.mark.django_db
def test_assignment_string_representation(
    ticket,
    technician,
    manager,
):
    # Arrange
    assignment = Assignment.objects.create(
        ticket=ticket,
        technician=technician,
        assigned_by=manager,
    )

    # Act
    result = str(assignment)

    # Assert
    assert result == "Computer does not start → technician"


@pytest.mark.django_db
def test_assignment_is_not_primary_by_default(
    ticket,
    technician,
    manager,
):
    # Arrange
    assignment = Assignment.objects.create(
        ticket=ticket,
        technician=technician,
        assigned_by=manager,
    )

    # Act
    is_primary = assignment.is_primary

    # Assert
    assert is_primary is False
