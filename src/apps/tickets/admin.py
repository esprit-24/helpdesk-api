from django.contrib import admin

from .models import Category, Priority, Status, Ticket, Assignment


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name", "is_final", "is_active")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    search_fields = ("name",)
    ordering = ("level",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "requester",
        "owner",
        "status",
        "priority",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "status",
        "priority",
        "category",
    )

    ordering = ("-created_at",)

    list_select_related = (
        "requester",
        "owner",
        "status",
        "priority",
        "category",
    )

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "ticket",
        "technician",
        "assigned_by",
        "assigned_at",
        "is_primary",
    )

    search_fields = (
        "ticket__title",
        "technician__username",
        "assigned_by__username",
    )

    list_filter = (
        "technician",
        "is_primary",
    )

    ordering = ("-assigned_at",)

    list_select_related = (
        "ticket",
        "technician",
        "assigned_by",
    )