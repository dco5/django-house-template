from __future__ import annotations

from django.conf import settings
from django.http import HttpRequest


def login_redirect_url(request: HttpRequest) -> str:
    return f"{settings.PORTAL_LOGIN_URL}?next={request.get_full_path()}"
