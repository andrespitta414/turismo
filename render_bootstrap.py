import os
import sys
from pathlib import Path


def bootstrap_django_settings() -> None:
    root = Path(__file__).resolve().parent

    candidates = [
        (root, "turismo_django.settings"),
        (root / "turismo_django", "turismo_django.settings"),
    ]

    for path_to_add, settings_module in candidates:
        if (path_to_add / "turismo_django" / "settings.py").exists():
            sys.path.insert(0, str(path_to_add))
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
            return

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turismo_django.settings")
