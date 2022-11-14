from pathlib import Path

# Paths

PROJECT_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = PROJECT_DIR.parent


# Apps

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


# Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Template configuration

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT_DIR / "templates",
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


# Users & authentication

AUTH_USER_MODEL = "auth.User"


# Internationalization

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    PROJECT_DIR / "locale",
]


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
