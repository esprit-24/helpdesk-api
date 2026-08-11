import pytest

from apps.users.models import User


@pytest.fixture
def requester():
    return User.objects.create_user(
        username="requester",
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