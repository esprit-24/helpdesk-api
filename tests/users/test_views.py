import pytest
from rest_framework.test import APIClient

from apps.users.models import User


@pytest.fixture
def requester():
    return User.objects.create_user(
        username="requester",
        password="testpassword",
        role=User.Role.REQUESTER,
    )


@pytest.fixture
def manager():
    return User.objects.create_user(
        username="manager",
        password="testpassword",
        role=User.Role.MANAGER,
    )


@pytest.mark.django_db
def test_requester_cannot_list_users(requester):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get("/api/users/")

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_manager_can_list_users(manager):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.get("/api/users/")

    # Assert
    assert response.status_code == 200
    assert response.data == [
        {
            "id": manager.id,
            "username": "manager",
            "full_name": "",
            "email": "",
            "role": "MANAGER",
            "is_active": True,
        }
    ]


@pytest.mark.django_db
def test_user_can_retrieve_own_profile(requester):
    # Arrange
    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get(f"/api/users/{requester.id}/")

    # Assert
    assert response.status_code == 200
    assert response.data == {
        "id": requester.id,
        "username": "requester",
        "full_name": "",
        "email": "",
        "role": "REQUESTER",
        "is_active": True,
    }


@pytest.mark.django_db
def test_user_cannot_retrieve_other_profile(requester):
    # Arrange
    other_user = User.objects.create_user(
        username="other",
        password="testpassword",
        role=User.Role.REQUESTER,
    )

    client = APIClient()
    client.force_authenticate(user=requester)

    # Act
    response = client.get(f"/api/users/{other_user.id}/")

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
def test_manager_can_retrieve_other_profile(manager):
    # Arrange
    other_user = User.objects.create_user(
        username="other",
        password="testpassword",
        role=User.Role.REQUESTER,
    )

    client = APIClient()
    client.force_authenticate(user=manager)

    # Act
    response = client.get(f"/api/users/{other_user.id}/")

    # Assert
    assert response.status_code == 200
    assert response.data == {
        "id": other_user.id,
        "username": "other",
        "full_name": "",
        "email": "",
        "role": "REQUESTER",
        "is_active": True,
    }


@pytest.mark.django_db
def test_unauthenticated_user_cannot_list_users():
    # Arrange
    client = APIClient()

    # Act
    response = client.get("/api/users/")

    # Assert
    assert response.status_code == 401
