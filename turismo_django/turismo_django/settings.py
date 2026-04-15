"""
TurismoDjango - Settings Configuration
Configuracion del proyecto Django para desarrollo y AWS Elastic Beanstalk.
"""

import os
from pathlib import Path

from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent


def get_bool_env(name, default=False):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_list_env(name, default=None):
    raw_value = os.environ.get(name, "")
    values = [item.strip() for item in raw_value.split(",") if item.strip()]
    return values if values else (default or [])


def get_int_env(name, default=0):
    value = os.environ.get(name)
    if value is None or value.strip() == "":
        return default
    return int(value)


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-turismo-dev-only")

DEBUG = get_bool_env("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = get_list_env("DJANGO_ALLOWED_HOSTS", ["localhost", "127.0.0.1"])

CSRF_TRUSTED_ORIGINS = get_list_env(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    [
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "turismo_django",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "turismo_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "turismo_django" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "turismo_django.wsgi.application"


DB_ENGINE = os.environ.get("DB_ENGINE", "").strip().lower()

if DB_ENGINE == "mssql":
    DATABASES = {
        "default": {
            "ENGINE": "mssql",
            "NAME": os.environ.get("DB_NAME", ""),
            "USER": os.environ.get("DB_USER", ""),
            "PASSWORD": os.environ.get("DB_PASSWORD", ""),
            "HOST": os.environ.get("DB_HOST", ""),
            "PORT": os.environ.get("DB_PORT", "1433"),
            "OPTIONS": {
                "driver": os.environ.get("DB_DRIVER", "ODBC Driver 18 for SQL Server"),
                "extra_params": os.environ.get(
                    "DB_EXTRA_PARAMS",
                    "Encrypt=yes;TrustServerCertificate=yes",
                ),
                "connection_timeout": get_int_env("DB_CONNECTION_TIMEOUT", 30),
                "connection_retries": get_int_env("DB_CONNECTION_RETRIES", 5),
                "connection_retry_backoff_time": get_int_env(
                    "DB_CONNECTION_RETRY_BACKOFF_TIME",
                    5,
                ),
                "query_timeout": get_int_env("DB_QUERY_TIMEOUT", 30),
            },
        }
    }
elif os.environ.get("RDS_DB_NAME"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("RDS_DB_NAME"),
            "USER": os.environ.get("RDS_USERNAME"),
            "PASSWORD": os.environ.get("RDS_PASSWORD"),
            "HOST": os.environ.get("RDS_HOSTNAME"),
            "PORT": os.environ.get("RDS_PORT", "5432"),
            "OPTIONS": {
                "sslmode": "require",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


DATABASE_CONNECTION_POOLING = get_bool_env(
    "DATABASE_CONNECTION_POOLING",
    default=True,
)


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "es-co"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = get_bool_env("DJANGO_SECURE_SSL_REDIRECT", default=True)
    SESSION_COOKIE_SECURE = get_bool_env(
        "DJANGO_SESSION_COOKIE_SECURE",
        default=SECURE_SSL_REDIRECT,
    )
    CSRF_COOKIE_SECURE = get_bool_env(
        "DJANGO_CSRF_COOKIE_SECURE",
        default=SECURE_SSL_REDIRECT,
    )
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_SECONDS = int(
        os.environ.get(
            "DJANGO_SECURE_HSTS_SECONDS",
            "3600" if SECURE_SSL_REDIRECT else "0",
        )
    )
    SECURE_HSTS_INCLUDE_SUBDOMAINS = SECURE_HSTS_SECONDS > 0
    SECURE_HSTS_PRELOAD = SECURE_HSTS_SECONDS > 0


MESSAGE_TAGS = {
    messages.SUCCESS: "success",
    messages.ERROR: "error",
    messages.WARNING: "warning",
    messages.INFO: "info",
}
