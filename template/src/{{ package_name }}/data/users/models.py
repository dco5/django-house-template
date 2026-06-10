from __future__ import annotations

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model — extend here, never migrate away from stock auth.User later."""
