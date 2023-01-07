from sdtmonitor.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#p^%q3)9rnxmlu(bhd!yn$7p=1g$o#3=xzy5&##tjp+um+b!gl"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES["default"]= {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "sdtmonitor.db",
}


# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


STATIC_ROOT = BASE_DIR / "assets"