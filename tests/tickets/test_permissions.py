import pytest

from apps.tickets.models import Assignment
from apps.tickets.permissions import (
    CanViewAssignment,
    CanViewTicket,
    IsAdmin,
    IsManagerOrAdmin,
)
from apps.users.models import User


# Role-based permissions
@pytest.mark.django_db
def test_admin_is_allowed(admin, request_factory):
    # Arrange
    request = request_factory.get("/")
    request.user = admin
    permission = IsAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is True


@pytest.mark.django_db
def test_manager_is_not_admin(manager, request_factory):
    # Arrange
    request = request_factory.get("/")
    request.user = manager
    permission = IsAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is False


@pytest.mark.django_db
def test_manager_is_allowed(manager, request_factory):
    # Arrange
    request = request_factory.get("/")
    request.user = manager
    permission = IsManagerOrAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is True


@pytest.mark.django_db
def test_requester_is_not_allowed_as_manager_or_admin(
    requester,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = requester
    permission = IsManagerOrAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is False


# Ticket permissions
@pytest.mark.django_db
def test_manager_can_view_any_ticket(
    manager,
    other_ticket,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = manager
    permission = CanViewTicket()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        other_ticket,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_requester_can_view_own_ticket(
    requester,
    ticket,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = requester
    permission = CanViewTicket()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        ticket,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_requester_cannot_view_other_ticket(
    requester,
    other_ticket,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = requester
    permission = CanViewTicket()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        other_ticket,
    )

    # Assert
    assert result is False


@pytest.mark.django_db
def test_technician_can_view_assigned_ticket(
    technician,
    ticket,
    assignment,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = technician
    permission = CanViewTicket()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        ticket,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_technician_cannot_view_unassigned_ticket(
    technician,
    ticket,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = technician
    permission = CanViewTicket()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        ticket,
    )

    # Assert
    assert result is False


# Assignment permissions
@pytest.mark.django_db
def test_manager_can_view_any_assignment(
    manager,
    assignment,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = manager
    permission = CanViewAssignment()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        assignment,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_technician_can_view_own_assignment(
    technician,
    assignment,
    request_factory,
):
    # Arrange
    request = request_factory.get("/")
    request.user = technician
    permission = CanViewAssignment()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        assignment,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_technician_cannot_view_other_assignment(
    technician,
    manager,
    ticket,
    request_factory,
):
    # Arrange
    other_technician = User.objects.create_user(
        username="other-technician",
        password="testpassword",
        role=User.Role.TECHNICIAN,
    )

    assignment = Assignment.objects.create(
        ticket=ticket,
        technician=other_technician,
        assigned_by=manager,
    )

    request = request_factory.get("/")
    request.user = technician
    permission = CanViewAssignment()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        assignment,
    )

    # Assert
    assert result is False
