from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .decorators import portal_login_required


@portal_login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "portal/dashboard.html")


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("portal:dashboard")

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username", ""),
            password=request.POST.get("password", ""),
        )
        if user is not None:
            login(request, user)
            next_url = request.POST.get("next") or "portal:dashboard"
            return redirect(next_url)
        messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "portal/auth/login.html", {"next": request.GET.get("next", "")})


@require_POST
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("portal:login")
