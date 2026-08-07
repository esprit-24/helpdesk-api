from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model.
    """

    class Role(models.TextChoices):
        """
        Available user roles.
        """
        
        REQUESTER = "REQUESTER", "Requester"
        TECHNICIAN = "TECHNICIAN", "Technician"
        MANAGER = "MANAGER", "Manager"
        ADMIN = "ADMIN", "Administrator"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.REQUESTER,
    )

    @property
    def full_name(self):
        """
        Return the user's full name.
        """
        return self.get_full_name()