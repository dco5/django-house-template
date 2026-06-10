from __future__ import annotations

from django.db import models


class ActionSource(models.TextChoices):
    """How a write was triggered. Required by every domain operation."""

    ADMIN = "ADMIN", "Admin"
    PORTAL = "PORTAL", "Portal"
    API = "API", "API"
    SYSTEM = "SYSTEM", "Sistema"
    CELERY = "CELERY", "Celery"
