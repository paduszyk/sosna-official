import os

from core.settings.develop import *  # noqa
from core.settings.develop import BASE_DIR

# Databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
