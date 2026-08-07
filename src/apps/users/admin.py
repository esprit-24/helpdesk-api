from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Administration du modèle utilisateur personnalisé.
    """

    list_display = (
        "username",
        "full_name",
        "email",
        "role",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )

    ordering = (
        "username",
    )

    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Helpdesk",
            {
                "fields": (
                    "role",
                ),
            },
        ),
    )