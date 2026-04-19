import os
import sys
import importlib
from pathlib import Path


def bootstrap_django_settings() -> None:
    root = Path(__file__).resolve().parent
    ignored_parts = {
        ".venv",
        "venv",
        ".git",
        "__pycache__",
        "site-packages",
    }

    candidates = []
    for settings_file in root.rglob("settings.py"):
        if any(part in ignored_parts for part in settings_file.parts):
            continue
        candidates.append(settings_file)

    if candidates:
        candidates = sorted(candidates, key=lambda path: len(path.parts))
        settings_file = candidates[0]
        package_dir = settings_file.parent
        project_root = package_dir.parent
        package_name = package_dir.name

        if str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))

        discovered_pkg = importlib.import_module(package_name)
        if package_name != "turismo_django":
            sys.modules["turismo_django"] = discovered_pkg
            try:
                settings_mod = importlib.import_module(f"{package_name}.settings")
                sys.modules["turismo_django.settings"] = settings_mod
            except Exception:
                pass
            try:
                urls_mod = importlib.import_module(f"{package_name}.urls")
                sys.modules["turismo_django.urls"] = urls_mod
            except Exception:
                pass
            try:
                wsgi_mod = importlib.import_module(f"{package_name}.wsgi")
                sys.modules["turismo_django.wsgi"] = wsgi_mod
            except Exception:
                pass

        os.environ["DJANGO_SETTINGS_MODULE"] = "turismo_django.settings"
        return

    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turismo_django.settings")
