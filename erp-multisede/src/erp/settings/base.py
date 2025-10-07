import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parents[2]

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR.parent, ".env"))

SECRET_KEY = env("DJANGO_SECRET_KEY", default="change_me")
DEBUG = env.bool("DJANGO_DEBUG", True)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "django_filters",
    "axes",
    "guardian",
    "simple_history",
    "apps.core.apps.CoreConfig",
    "apps.accounts.apps.AccountsConfig",
    "apps.logistics.apps.LogisticsConfig",
    "apps.adminflow.apps.AdminFlowConfig",
    "apps.hr.apps.HRConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "erp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "erp.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="erp"),
        "USER": env("POSTGRES_USER", default="erp"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="erp"),
        "HOST": env("POSTGRES_HOST", default="db"),
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}

AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
)

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ERP API",
    "VERSION": "0.1.0",
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True

AXES_ENABLED = True
AXES_FAILURE_LIMIT = 5

CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
