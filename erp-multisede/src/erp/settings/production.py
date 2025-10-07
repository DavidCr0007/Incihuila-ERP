from .base import *  # noqa

DEBUG = False
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["erp.local"])  # noqa: F405

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)  # noqa: F405

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

CELERY_BROKER_URL = env("REDIS_URL", default="redis://redis:6379/0")  # noqa: F405
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
