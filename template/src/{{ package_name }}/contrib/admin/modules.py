"""Admin autodiscovery: imports admin.py from each bounded context under interfaces/backoffice/.

Admin classes never live in data apps — they belong to the backoffice interface.
"""

from __future__ import annotations

import glob
import sys
from importlib import import_module, util

from django.conf import settings


def get_admin_modules_in_backoffice(module_to_search: str) -> list:
    admin_modules = []
    admin_config = settings.ADMIN_INTERFACES
    admin_module = sys.modules[admin_config]
    admin_path = admin_module.__path__[0]

    for file in glob.glob(admin_path + "/**/__init__.py", recursive=True):
        spec = util.spec_from_file_location(module_to_search, file)
        if spec is None or spec.loader is None:
            continue
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        admin_modules.append(module)

    return admin_modules


def autodiscover_backoffice_admin_files(*args: str) -> None:
    from django.utils.module_loading import import_string

    module_names = args or ("admin",)
    admin_modules = get_admin_modules_in_backoffice(module_names[0])

    for context in admin_modules:
        for module_name in module_names:
            try:
                if not hasattr(context, "default_app_config"):
                    continue
                app_config = import_string(context.default_app_config)
                import_module(f"{app_config.name}.{module_name}")
            except (ImportError, AttributeError):
                pass
