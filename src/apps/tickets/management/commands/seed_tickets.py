from django.core.management.base import BaseCommand

from apps.tickets.models import Category, Priority, Status

STATUSES = [
    {
        "name": "Open",
        "description": "Ticket has been created and is waiting to be processed.",
        "is_final": False,
        "is_active": True,
    },
    {
        "name": "In Progress",
        "description": "Ticket is currently being worked on.",
        "is_final": False,
        "is_active": True,
    },
    {
        "name": "Pending",
        "description": "Ticket is waiting for additional information or action.",
        "is_final": False,
        "is_active": True,
    },
    {
        "name": "Resolved",
        "description": "A solution has been provided and is awaiting confirmation.",
        "is_final": False,
        "is_active": True,
    },
    {
        "name": "Closed",
        "description": "Ticket has been closed.",
        "is_final": True,
        "is_active": True,
    },
]


PRIORITIES = [
    {
        "name": "Low",
        "description": "Low priority issue.",
        "level": 1,
    },
    {
        "name": "Medium",
        "description": "Medium priority issue.",
        "level": 2,
    },
    {
        "name": "High",
        "description": "High priority issue.",
        "level": 3,
    },
    {
        "name": "Critical",
        "description": "Critical priority issue.",
        "level": 4,
    },
]


CATEGORIES = [
    {
        "name": "Hardware",
        "description": "Hardware related issues.",
    },
    {
        "name": "Software",
        "description": "Software related issues.",
    },
    {
        "name": "Network",
        "description": "Network related issues.",
    },
    {
        "name": "Account",
        "description": "Account and authentication issues.",
    },
    {
        "name": "Other",
        "description": "Other issues.",
    },
]


class Command(BaseCommand):
    """
    Populate the database with reference data.
    """

    help = "Populate the database with default statuses, priorities and categories."

    def handle(self, *args, **options):
        self.seed_statuses()
        self.seed_priorities()
        self.seed_categories()

        self.stdout.write(self.style.SUCCESS("Reference data seeded successfully."))

    def seed_statuses(self):
        for status_data in STATUSES:
            _, created = Status.objects.get_or_create(
                name=status_data["name"],
                defaults={
                    "description": status_data["description"],
                    "is_final": status_data["is_final"],
                    "is_active": status_data["is_active"],
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Status '{status_data['name']}' created.")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Status '{status_data['name']}' already exists."
                    )
                )

    def seed_priorities(self):
        for priority_data in PRIORITIES:
            _, created = Priority.objects.get_or_create(
                name=priority_data["name"],
                defaults={
                    "description": priority_data["description"],
                    "level": priority_data["level"],
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Priority '{priority_data['name']}' created.")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Priority '{priority_data['name']}' already exists."
                    )
                )

    def seed_categories(self):
        for category_data in CATEGORIES:
            _, created = Category.objects.get_or_create(
                name=category_data["name"],
                defaults={
                    "description": category_data["description"],
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Category '{category_data['name']}' created.")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Category '{category_data['name']}' already exists."
                    )
                )
