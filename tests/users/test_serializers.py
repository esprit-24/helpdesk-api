import pytest

from apps.users.serializers import (
    UserReadSerializer,
    UserSummarySerializer,
)


@pytest.mark.django_db
def test_user_summary_serializer(requester):
    # Arrange
    serializer = UserSummarySerializer(requester)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": requester.id,
        "full_name": "",
        "is_active": True,
    }


@pytest.mark.django_db
def test_user_summary_serializer_with_full_name(requester):
    # Arrange
    requester.first_name = "John"
    requester.last_name = "Doe"
    requester.save()

    serializer = UserSummarySerializer(requester)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": requester.id,
        "full_name": "John Doe",
        "is_active": True,
    }


@pytest.mark.django_db
def test_user_read_serializer(requester):
    # Arrange
    serializer = UserReadSerializer(requester)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": requester.id,
        "username": "requester",
        "full_name": "",
        "email": "",
        "role": "REQUESTER",
        "is_active": True,
    }


@pytest.mark.django_db
def test_user_read_serializer_with_full_data(manager):
    # Arrange
    manager.first_name = "John"
    manager.last_name = "Doe"
    manager.email = "john@example.com"
    manager.is_active = True
    manager.save()

    serializer = UserReadSerializer(manager)

    # Act
    data = serializer.data

    # Assert
    assert data == {
        "id": manager.id,
        "username": "manager",
        "full_name": "John Doe",
        "email": "john@example.com",
        "role": "MANAGER",
        "is_active": True,
    }