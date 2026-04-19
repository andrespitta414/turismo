import importlib.util
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
IGNORED_PARTS = {".venv", "venv", ".git", "__pycache__", "site-packages"}


def _find_project_settings() -> Path:
    candidates: list[Path] = []
    for settings_file in ROOT_DIR.rglob("settings.py"):
        if settings_file == Path(__file__).resolve():
            continue
        if any(part in IGNORED_PARTS for part in settings_file.parts):
            continue
        if (settings_file.parent / "wsgi.py").exists():
            candidates.append(settings_file)

    if not candidates:
        raise RuntimeError("Could not locate Django project settings.py")

    candidates.sort(key=lambda path: len(path.parts))
    return candidates[0]


PROJECT_SETTINGS_PATH = _find_project_settings()
PROJECT_ROOT = PROJECT_SETTINGS_PATH.parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

spec = importlib.util.spec_from_file_location("_project_settings", PROJECT_SETTINGS_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load settings spec from {PROJECT_SETTINGS_PATH}")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if name.isupper():
        globals()[name] = getattr(module, name)
