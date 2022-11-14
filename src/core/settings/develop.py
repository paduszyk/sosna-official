import dj_database_url

from .common import *  # noqa
from .common import BASE_DIR, INSTALLED_APPS, MIDDLEWARE, PROJECT_DIR

# Secret key

SECRET_KEY = "sosna-development-secret-key"


# Debugging

DEBUG = True


# Allowed hosts and internal IPs

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]


# Apps

INSTALLED_APPS += [
    "debug_toolbar",
]


# Middleware

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


# URLconf

ROOT_URLCONF = "core.urls.develop"


# Databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:@localhost:5432/postgres"
    ),
}


# Static files

STATIC_URL = "static/"

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "static"


# Media files

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"
