from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model.
    """

    @property
    def full_name(self):
        """
        Return the user's full name.
        """
        return self.get_full_name()