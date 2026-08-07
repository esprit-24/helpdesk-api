from django.conf import settings
from django.core.management.base import BaseCommand

from apps.users.models import User

USERS = [
    {
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "System",
        "last_name": "Administrator",
        "role": User.Role.ADMIN,
        "is_staff": True,
        "is_superuser": True,
    },
    {
        "username": "manager",
        "email": "manager@example.com",
        "first_name": "Help",
        "last_name": "Manager",
        "role": User.Role.MANAGER,
        "is_staff": True,
        "is_superuser": False,
    },
    {
        "username": "tech1",
        "email": "tech1@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": User.Role.TECHNICIAN,
        "is_staff": False,
        "is_superuser": False,
    },
    {
        "username": "tech2",
        "email": "tech2@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "role": User.Role.TECHNICIAN,
        "is_staff": False,
        "is_superuser": False,
    },
    {
        "username": "requester1",
        "email": "requester1@example.com",
        "first_name": "Alice",
        "last_name": "Requester",
        "role": User.Role.REQUESTER,
        "is_staff": False,
        "is_superuser": False,
    },
    {
        "username": "requester2",
        "email": "requester2@example.com",
        "first_name": "Bob",
        "last_name": "Requester",
        "role": User.Role.REQUESTER,
        "is_staff": False,
        "is_superuser": False,
    },
]


class Command(BaseCommand):
    """
    Populate the database with default users.
    """

    help = "Populate the database with default users."

    def handle(self, *args, **options):
        self.seed_users()

        self.stdout.write(
            self.style.SUCCESS(
                "Users seeded successfully."
            )
        )

    def seed_users(self):
        for user_data in USERS:
            username = user_data["username"]

            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(
                        f"User '{username}' already exists."
                    )
                )
                continue

            User.objects.create_user(
                **user_data,
                password=settings.DEFAULT_USER_PASSWORD,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"User '{username}' created."
                )
            )
            