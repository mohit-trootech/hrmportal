from os.path import join
from pathlib import Path
from dj_database_url import config
from dotenv import dotenv_values
from utils.constants import Settings, EmailConfig
from django.utils.timezone import timedelta

env = dotenv_values(".env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPEND_SLASH = True
ROOT_URLCONF = Settings.ROOT_URLCONF
AUTH_USER_MODEL = "user_management.User"

admins = (("Mohit Prajapat", """mohit.prajapat@trootech.com"""),)
CORS_ORIGIN_ALLOW_ALL = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get("SECRET_KEY", None)

# Installed Apps Configuration
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Project Apps Configuration
PROJECT_APPS = [
    "access_management",
    "account_management",
    "attendence_management",
    "broadcast_management",
    "device_management",
    "document_management",
    "holiday_management",
    "hrmportal",
    "interview_management",
    "leave_management",
    "organization_management",
    "project_management",
    "remotework_management",
    "resignation_management",
    "review_management",
    "salary_management",
    "tax_management",
    "user_management",
]

# Third Party Apps Configuration
THIRD_PARTY_APPS = [
    "django_extensions",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "django_crontab",
    "cities_light",
    "widget_tweaks",
    "django_cleanup.apps.CleanupConfig",
    "phonenumber_field",
]


INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS


# Middleware Configuration
THIRD_PARTY_MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]
DJANGO_MIDDLEWARES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
MIDDLEWARE = THIRD_PARTY_MIDDLEWARE + DJANGO_MIDDLEWARES

# Root Urls Configuration
ROOT_URLCONF = Settings.ROOT_URLCONF

# Templates + Context Processors Configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(BASE_DIR, Settings.TEMPLATES)],
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

# WSGI - Web Server Gateway Interface Server
WSGI_APPLICATION = Settings.WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {"default": config(default=env.get("DATABASE_URL", None))}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = Settings.LANGUAGE_CODE

TIME_ZONE = Settings.TIME_ZONE

USE_I18N = Settings.USE_I18N

USE_TZ = Settings.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = Settings.STATIC_URL
STATICFILES_DIRS = [join(BASE_DIR, Settings.STATIC_FILES_DIRS)]
STATIC_ROOT = join(BASE_DIR, Settings.STATIC_ROOT)

# Media files (Models File)
MEDIA_URL = Settings.MEDIA_URL
MEDIA_ROOT = join(BASE_DIR, Settings.MEDIA_ROOT)


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
# -------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email Configuration
EMAIL_BACKEND = EmailConfig.EMAIL_BACKEND
EMAIL_HOST = EmailConfig.EMAIL_HOST
EMAIL_USE_SSL = True  # use port 465
EMAIL_USE_TLS = False  # use port 587
EMAIL_PORT = EmailConfig.PORT_465 if EMAIL_USE_SSL else EmailConfig.PORT_587
EMAIL_HOST_USER = env.get("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = env.get("EMAIL_HOST_PASSWORD", None)

# Celery Configuration
CELERY_BROKER_URL = env.get("CELERY_BROKER_URL", None)
CELERY_TIMEZONE = Settings.TIME_ZONE
CELERY_RESULT_BACKEND = "redis"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_EXTENDED = True

# Logging Configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {name} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

# Cities Light Configuration
CITIES_LIGHT_INCLUDE_COUNTRIES = ["IN"]
CITIES_LIGHT_TRANSLATION_LANGUAGES = ["en"]


# Cache Configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique_snowflake",
    }
}
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 15,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
