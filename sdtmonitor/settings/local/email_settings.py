import os

# Sending email configuration
EMAIL_HOST_USER = os.getenv(
    "EMAIL_HOST_USER", "contact@sdtmonitor.com"
)

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

EMAIL_PORT = os.getenv("EMAIL_PORT", 587)

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")

EMAIL_USE_TLS = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

