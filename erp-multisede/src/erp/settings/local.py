from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ["debug_toolbar"]  # type: ignore # noqa: F405

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # type: ignore # noqa: F405

INTERNAL_IPS = ["127.0.0.1", "0.0.0.0"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CELERY_BROKER_URL = env("REDIS_URL", default="redis://redis:6379/0")  # noqa: F405
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
