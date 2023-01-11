from sdtmonitor.settings.local.email_settings import *
from sdtmonitor.settings.base import *
import os
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')


MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES["default"]= {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "sdtmonitor.db",
}


STATIC_ROOT = BASE_DIR / "assets"
CSRF_TRUSTED_ORIGINS = [config("CSRF_TRUSTED_ORIGINS"),]