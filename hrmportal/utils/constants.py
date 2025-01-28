from django.utils.translation import gettext_lazy as _  # noqa # TODO: Remove this Later


class Settings:
    """Settings for the project."""

    ROOT_URLCONF = "hrmportal.urls"
    TEMPLATES = "templates"
    WSGI_APPLICATION = "hrmportal.wsgi.application"
    ASGI_APPLICATION = "hrmportal.asgi.application"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_TZ = True
    STATIC_URL = "/static/"
    STATIC_FILES_DIRS = "static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"


class EmailConfig:
    """Email Configuration."""

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_587 = 587
    PORT_465 = 465
    EMAIL_USE_TLS = True
