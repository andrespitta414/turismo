import os
import sys
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
        parent_dir = settings_file.parent
        package_init = parent_dir / "__init__.py"
        wsgi_file = parent_dir / "wsgi.py"
        if package_init.exists() and wsgi_file.exists():
            candidates.append(settings_file)

    if candidates:
        settings_file = candidates[0]
        package_dir = settings_file.parent
        project_root = package_dir.parent
        settings_module = f"{package_dir.name}.settings"

        if str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))

        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
        return

    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turismo_django.settings")
