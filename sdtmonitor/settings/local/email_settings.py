import os
from decouple import config
# Sending email configuration

EMAIL_HOST_USER = config(
    "EMAIL_HOST_USER"
)

EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

EMAIL_PORT = config("EMAIL_PORT")

EMAIL_HOST = config("EMAIL_HOST")

EMAIL_USE_TLS = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

