from django.core.exceptions import ValidationError
import pytest

from apps.users.models import User


@pytest.mark.django_db
def test_user_has_requester_role_by_default():
    # Arrange
    user = User.objects.create_user(
        username="testuser",
        password="testpassword",
    )

    # Act
    role = user.role

    # Assert
    assert role == User.Role.REQUESTER


@pytest.mark.django_db
def test_user_full_name():
    # Arrange
    user = User.objects.create_user(
        username="john",
        password="testpassword",
        first_name="John",
        last_name="Doe",
    )

    # Act
    full_name = user.full_name

    # Assert
    assert full_name == "John Doe"


@pytest.mark.django_db
def test_user_role_must_be_valid():
    # Arrange
    user = User(
        username="invalid-role",
        role="INVALID",
    )

    # Act + Assert
    with pytest.raises(ValidationError):
        user.full_clean()
