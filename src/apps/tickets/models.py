from django.db import models


class Status(models.Model):
    """
    Represents the lifecycle state of a ticket.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique name of the ticket status.",
    )

    description = models.TextField(
        blank=True,
        help_text="Optional description of the ticket status.",
    )

    is_final = models.BooleanField(
        default=False,
        help_text="Whether this status represents the end of a ticket lifecycle.",
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Whether this status can be used for new tickets.",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Priority(models.Model):
    """
    Represents the priority level of a ticket.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique name of the priority.",
    )

    description = models.TextField(
        blank=True,
        help_text="Optional description of the priority.",
    )

    level = models.PositiveSmallIntegerField(
        unique=True,
        help_text="Numeric level used to sort priorities.",
    )

    class Meta:
        ordering = ["level"]
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Represents the category assigned to a ticket.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Unique name of the category.",
    )

    description = models.TextField(
        blank=True,
        help_text="Optional description of the category.",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """
    Represents a support ticket.
    """

    title = models.CharField(
        max_length=255,
        help_text="Short summary of the issue.",
    )

    description = models.TextField(
        blank=True,
        help_text="Detailed description of the issue.",
    )

    requester = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="requested_tickets",
        help_text="User who created the ticket.",
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_tickets",
        help_text="User responsible for the ticket.",
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="tickets",
        help_text="Current status of the ticket.",
    )

    priority = models.ForeignKey(
        Priority,
        on_delete=models.PROTECT,
        related_name="tickets",
        help_text="Priority assigned to the ticket.",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="tickets",
        help_text="Category assigned to the ticket.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the ticket was created.",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time of the last update.",
    )

    closed_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time when the ticket was closed.",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.title


class Assignment(models.Model):
    """
    Represents the assignment of a technician to a ticket.
    """

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="assignments",
        help_text="Ticket associated with this assignment.",
    )

    technician = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="assignments",
        help_text="Technician assigned to the ticket.",
    )

    assigned_by = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="created_assignments",
        help_text="User who assigned the technician.",
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the assignment was created.",
    )

    ended_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time when the assignment ended.",
    )

    is_primary = models.BooleanField(
        default=False,
        help_text="Whether this is the primary assignment.",
    )

    class Meta:
        ordering = ["-assigned_at"]
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

        constraints = [
            models.UniqueConstraint(
                fields=["ticket"],
                condition=models.Q(is_primary=True),
                name="unique_primary_assignment_per_ticket",
            ),
        ]

    def __str__(self):
        return f"{self.ticket} → {self.technician}"
