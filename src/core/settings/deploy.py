import dj_database_url
from decouple import config

from .common import *  # noqa

# Secret key

SECRET_KEY = config("SECRET_KEY")


# Debugging

DEBUG = False


# Allowed hosts

ALLOWED_HOSTS = []


# URLconf

ROOT_URLCONF = "core.urls.deploy"


# WSGI application

WSGI_APPLICATION = "core.wsgi.application"


# Databases

DATABASES = {
    "default": dj_database_url.config(default=config("DATABASE_URL")),
}
