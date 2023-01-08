import os

from celery import Celery

from sdtmonitor.settings.packages.celery import CELERY_BROKER_URL
from sdtmonitor.utils.settings import get_app_settings
# from reportr.helpers.tasks import send_daily_overview

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_app_settings())

CELERY_RESULT_BACKEND = CELERY_BROKER_URL

# set the default Django settings module for the 'celery' program.
app = Celery(
    "sdtmonitor",
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_RESULT_BACKEND)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace="CELERY")

# Load task modules from all registered Django app configs.

app.autodiscover_tasks()


@app.task()
def debug_task(self):
    """debug information for tasks"""
    print(f"Request: {self.request!r}")

# celery -A reportr worker -l info -E
# celery -A reportr beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
# pip install eventlet
# celery -A reportr worker -l info
# celery -A reportr beat -l info -S django
# celery -A reportr worker --loglevel=info --pool=solo for windows
