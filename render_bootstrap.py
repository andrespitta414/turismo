import os
import sys
from pathlib import Path


def bootstrap_django_settings() -> None:
    root = Path(__file__).resolve().parent
    search_roots = [root, root / "turismo_django"]

    for base in search_roots:
        if not base.exists():
            continue
        for settings_file in base.rglob("settings.py"):
            if settings_file.parent.name != "turismo_django":
                continue

            project_root = settings_file.parent.parent
            if str(project_root) not in sys.path:
                sys.path.insert(0, str(project_root))
            if str(root) not in sys.path:
                sys.path.insert(0, str(root))

            os.environ["DJANGO_SETTINGS_MODULE"] = "turismo_django.settings"
            return

    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    os.environ["DJANGO_SETTINGS_MODULE"] = "turismo_django.settings"
