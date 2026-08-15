import pytest
from rest_framework.test import APIClient

from apps.tickets.models import Assignment, Ticket


# Status
@pytest.mark.django_db
def test_unauthenticated_user_cannot_list_statuses():
    # Arrange
    client = APIClient()

    # Act
    response = client.get("/api/statuses/")

    # Assert
    assert response.status_code == 401


@pytest.mark.django_db
def test_requester_can_list_statuses(requester, status):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get("/api/statuses/")

    # Assert
    assert response.status_code == 200
    assert response.data == [
        {
            "id": status.id,
            "name": "Open",
            "description": "",
            "is_final": False,
            "is_active": True,
        }
    ]


@pytest.mark.django_db
def test_manager_can_create_status(manager):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    payload = {
        "name": "Closed",
        "description": "Ticket is closed.",
        "is_final": True,
        "is_active": True,
    }

    # Act
    response = client.post(
        "/api/statuses/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 201
    assert response.data["name"] == "Closed"


@pytest.mark.django_db
def test_requester_cannot_create_status(requester):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "name": "Closed",
        "description": "Ticket is closed.",
        "is_final": True,
        "is_active": True,
    }

    # Act
    response = client.post(
        "/api/statuses/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_manager_can_update_status(manager, status):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    payload = {
        "name": "In Progress",
        "description": "Ticket is being handled.",
        "is_final": False,
        "is_active": True,
    }

    # Act
    response = client.patch(
        f"/api/statuses/{status.id}/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 200
    assert response.data["name"] == "In Progress"


@pytest.mark.django_db
def test_requester_cannot_update_status(requester, status):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "name": "In Progress",
    }

    # Act
    response = client.patch(
        f"/api/statuses/{status.id}/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_delete_status(admin, status):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=admin)

    # Act
    response = client.delete(f"/api/statuses/{status.id}/")

    # Assert
    assert response.status_code == 204


@pytest.mark.django_db
def test_manager_cannot_delete_status(manager, status):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.delete(f"/api/statuses/{status.id}/")

    # Assert
    assert response.status_code == 403


# Priority
@pytest.mark.django_db
def test_unauthenticated_user_cannot_list_priorities():
    # Arrange
    client = APIClient()

    # Act
    response = client.get("/api/priorities/")

    # Assert
    assert response.status_code == 401


@pytest.mark.django_db
def test_requester_can_list_priorities(requester, priority):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get("/api/priorities/")

    # Assert
    assert response.status_code == 200
    assert response.data == [
        {
            "id": priority.id,
            "name": "High",
            "description": "",
            "level": 1,
        }
    ]


@pytest.mark.django_db
def test_manager_can_create_priority(manager):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    payload = {
        "name": "Critical",
        "description": "Highest priority.",
        "level": 2,
    }

    # Act
    response = client.post(
        "/api/priorities/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 201
    assert response.data["name"] == "Critical"


@pytest.mark.django_db
def test_requester_cannot_create_priority(requester):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "name": "Critical",
        "description": "Highest priority.",
        "level": 2,
    }

    # Act
    response = client.post(
        "/api/priorities/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_delete_priority(admin, priority):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=admin)

    # Act
    response = client.delete(f"/api/priorities/{priority.id}/")

    # Assert
    assert response.status_code == 204


@pytest.mark.django_db
def test_manager_cannot_delete_priority(manager, priority):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.delete(f"/api/priorities/{priority.id}/")

    # Assert
    assert response.status_code == 403


# Category
@pytest.mark.django_db
def test_unauthenticated_user_cannot_list_categories():
    # Arrange
    client = APIClient()

    # Act
    response = client.get("/api/categories/")

    # Assert
    assert response.status_code == 401


@pytest.mark.django_db
def test_requester_can_list_categories(requester, category):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get("/api/categories/")

    # Assert
    assert response.status_code == 200
    assert response.data == [
        {
            "id": category.id,
            "name": "Hardware",
            "description": "",
        }
    ]


@pytest.mark.django_db
def test_manager_can_create_category(manager):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    payload = {
        "name": "Software",
        "description": "Software-related issues.",
    }

    # Act
    response = client.post(
        "/api/categories/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 201
    assert response.data["name"] == "Software"


@pytest.mark.django_db
def test_requester_cannot_create_category(requester):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "name": "Software",
        "description": "Software-related issues.",
    }

    # Act
    response = client.post(
        "/api/categories/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_delete_category(admin, category):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=admin)

    # Act
    response = client.delete(f"/api/categories/{category.id}/")

    # Assert
    assert response.status_code == 204


@pytest.mark.django_db
def test_manager_cannot_delete_category(manager, category):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.delete(f"/api/categories/{category.id}/")

    # Assert
    assert response.status_code == 403


# Ticket
@pytest.mark.django_db
def test_unauthenticated_user_cannot_list_tickets():
    # Arrange
    client = APIClient()

    # Act
    response = client.get("/api/tickets/")

    # Assert
    assert response.status_code == 401


@pytest.mark.django_db
def test_requester_can_only_list_own_tickets(
    requester,
    ticket,
    other_ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get("/api/tickets/")

    # Assert
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == ticket.id
    assert response.data[0]["title"] == "Computer does not start"


@pytest.mark.django_db
def test_technician_can_only_list_assigned_tickets(
    technician,
    ticket,
    other_ticket,
    assignment,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=technician)

    # Act
    response = client.get("/api/tickets/")

    # Assert
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == ticket.id


@pytest.mark.django_db
def test_manager_can_list_all_tickets(
    manager,
    ticket,
    other_ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.get("/api/tickets/")

    # Assert
    assert response.status_code == 200
    assert {item["id"] for item in response.data} == {
        ticket.id,
        other_ticket.id,
    }


@pytest.mark.django_db
def test_requester_is_automatically_set_on_ticket_creation(
    requester,
    status,
    priority,
    category,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "title": "New computer issue",
        "description": "The computer does not start.",
        "status": status.id,
        "priority": priority.id,
        "category": category.id,
    }

    # Act
    response = client.post(
        "/api/tickets/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 201

    created_ticket = Ticket.objects.get(title="New computer issue")

    assert created_ticket.requester == requester


@pytest.mark.django_db
def test_requester_can_retrieve_own_ticket(
    requester,
    ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get(f"/api/tickets/{ticket.id}/")

    # Assert
    assert response.status_code == 200
    assert response.data["id"] == ticket.id


@pytest.mark.django_db
def test_requester_cannot_retrieve_other_ticket(
    requester,
    other_ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get(f"/api/tickets/{other_ticket.id}/")

    # Assert
    assert response.status_code == 404


@pytest.mark.django_db
def test_technician_can_retrieve_assigned_ticket(
    technician,
    ticket,
    assignment,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=technician)

    # Act
    response = client.get(f"/api/tickets/{ticket.id}/")

    # Assert
    assert response.status_code == 200
    assert response.data["id"] == ticket.id


@pytest.mark.django_db
def test_manager_can_update_ticket(
    manager,
    ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    payload = {
        "title": "Updated ticket",
    }

    # Act
    response = client.patch(
        f"/api/tickets/{ticket.id}/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 200
    assert response.data["title"] == "Updated ticket"


@pytest.mark.django_db
def test_requester_cannot_update_ticket(
    requester,
    ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "title": "Updated ticket",
    }

    # Act
    response = client.patch(
        f"/api/tickets/{ticket.id}/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_delete_ticket(
    admin,
    ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=admin)

    # Act
    response = client.delete(f"/api/tickets/{ticket.id}/")

    # Assert
    assert response.status_code == 204


@pytest.mark.django_db
def test_manager_cannot_delete_ticket(
    manager,
    ticket,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.delete(f"/api/tickets/{ticket.id}/")

    # Assert
    assert response.status_code == 403


# Assignment
@pytest.mark.django_db
def test_unauthenticated_user_cannot_list_assignments():
    # Arrange
    client = APIClient()

    # Act
    response = client.get("/api/assignments/")

    # Assert
    assert response.status_code == 401


@pytest.mark.django_db
def test_manager_can_list_all_assignments(
    manager,
    assignment,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.get("/api/assignments/")

    # Assert
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == assignment.id


@pytest.mark.django_db
def test_technician_can_list_own_assignments(
    technician,
    assignment,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=technician)

    # Act
    response = client.get("/api/assignments/")

    # Assert
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == assignment.id


@pytest.mark.django_db
def test_requester_cannot_list_assignments(requester):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get("/api/assignments/")

    # Assert
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_manager_can_create_assignment(
    manager,
    ticket,
    technician,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    payload = {
        "ticket": ticket.id,
        "technician": technician.id,
        "is_primary": True,
    }

    # Act
    response = client.post(
        "/api/assignments/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 201

    assignment = Assignment.objects.get(
        ticket=ticket,
        technician=technician,
    )

    assert assignment.assigned_by == manager
    assert assignment.is_primary is True


@pytest.mark.django_db
def test_requester_cannot_create_assignment(
    requester,
    ticket,
    technician,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    payload = {
        "ticket": ticket.id,
        "technician": technician.id,
        "is_primary": True,
    }

    # Act
    response = client.post(
        "/api/assignments/",
        payload,
        format="json",
    )

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_manager_can_delete_assignment(
    manager,
    assignment,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.delete(f"/api/assignments/{assignment.id}/")

    # Assert
    assert response.status_code == 204


@pytest.mark.django_db
def test_technician_cannot_delete_assignment(
    technician,
    assignment,
):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=technician)

    # Act
    response = client.delete(f"/api/assignments/{assignment.id}/")

    # Assert
    assert response.status_code == 403
