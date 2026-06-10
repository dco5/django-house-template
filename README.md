# django-house-template

Copier template encoding the house Django architecture distilled from three production projects
(byla_platform, por-ti-web, wms_iq) plus the best of
[cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) and 2026 community practice.

## What you get

- **Django 6.0 / Python 3.13**, managed with **uv** (`uv.lock`, PEP 735 dependency groups)
- **Layered architecture, mechanically enforced by ruff** (TID251 banned imports):
  `data/` (thin models) → `domain/` (operations / queries / processes) → `interfaces/` (portal / api / backoffice / tasks)
- **Audit-first writes**: every domain operation takes `performed_by` + `action_source`; ready-made immutable `AuditLog`
- **Custom User model** from day one, argon2 password hashing (cookiecutter-django lineage)
- **Portal pattern**: session auth with `@portal_login_required`, HTMX + Alpine (vendored, no CDN), Django 6.0 template partials
- Optional: **django-ninja** API, **Celery + Redis + beat**, **Tailwind + DaisyUI** (django-tailwind-cli), **Sentry**
- **Admin autodiscovery** into `interfaces/backoffice/` — admin never lives in data apps
- **pytest + factory-boy** (unit / integration markers), pre-commit (ruff check + format), mypy + django-stubs
- **CI**: GitHub Actions — ruff, mypy, `makemigrations --check`, `check --deploy`, pytest (with Postgres service)
- **Deploy tiers**: Docker compose + fabfile (default) or VPS systemd + gunicorn + nginx (`deploy.sh`)
- **CLAUDE.md / AGENTS.md** agent-workflow conventions baked in

## Usage

```bash
uvx copier copy gh:dco5/django-house-template myproject
cd myproject
uv sync
cp .env.example .env   # then fill SECRET_KEY
cd src && uv run python manage.py migrate && uv run python manage.py runserver
```

## Updating an existing project

The reason this template uses Copier: projects can pull template improvements later.

```bash
cd myproject
uvx copier update --trust
```

Answers are stored in `.copier-answers.yml`; the template is versioned with git tags.

## Architecture rules (the short version)

| Layer | May import | Contains |
|---|---|---|
| `data/` | nothing above | models (BaseModel: UUID pk + timestamps), TextChoices constants, custom fields |
| `domain/` | `data/` | `operations.py` (writes, `@transaction.atomic`, `performed_by` + `action_source`), `queries.py` (reads, never raise), `processes.py` (workflows) |
| `interfaces/` | everything | portal views (never write ORM directly), ninja API, backoffice admin, Celery task wrappers |

Violations fail `ruff check` — not code review.

See the full handbook for the reasoning behind every decision.

## License

MIT
