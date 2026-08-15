import pytest
from rest_framework.test import APIRequestFactory

from apps.users.models import User
from apps.users.permissions import (
    IsManagerOrAdmin,
    IsSelfOrManagerOrAdmin,
)


@pytest.mark.django_db
def test_manager_or_admin_allows_manager(manager):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get("/api/users/")
    request.user = manager

    permission = IsManagerOrAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is True


@pytest.mark.django_db
def test_manager_or_admin_allows_admin(admin):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get("/api/users/")
    request.user = admin

    permission = IsManagerOrAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is True


@pytest.mark.django_db
def test_manager_or_admin_denies_requester(requester):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get("/api/users/")
    request.user = requester

    permission = IsManagerOrAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is False


@pytest.mark.django_db
def test_manager_or_admin_denies_technician(technician):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get("/api/users/")
    request.user = technician

    permission = IsManagerOrAdmin()

    # Act
    result = permission.has_permission(request, None)

    # Assert
    assert result is False


@pytest.mark.django_db
def test_self_or_manager_or_admin_allows_own_profile(requester):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get(f"/api/users/{requester.id}/")
    request.user = requester

    permission = IsSelfOrManagerOrAdmin()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        requester,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_self_or_manager_or_admin_allows_manager(
    manager,
    requester,
):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get(f"/api/users/{requester.id}/")
    request.user = manager

    permission = IsSelfOrManagerOrAdmin()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        requester,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_self_or_manager_or_admin_allows_admin(
    admin,
    requester,
):
    # Arrange
    factory = APIRequestFactory()
    request = factory.get(f"/api/users/{requester.id}/")
    request.user = admin

    permission = IsSelfOrManagerOrAdmin()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        requester,
    )

    # Assert
    assert result is True


@pytest.mark.django_db
def test_self_or_manager_or_admin_denies_other_requester(
    requester,
):
    # Arrange
    other_user = User.objects.create_user(
        username="other",
        password="testpassword",
        role=User.Role.REQUESTER,
    )

    factory = APIRequestFactory()
    request = factory.get(f"/api/users/{other_user.id}/")
    request.user = requester

    permission = IsSelfOrManagerOrAdmin()

    # Act
    result = permission.has_object_permission(
        request,
        None,
        other_user,
    )

    # Assert
    assert result is False
