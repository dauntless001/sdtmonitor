import os
from decouple import config


CELERY_RESULT_BACKEND = config(
    "REDIS_URL")

BROKER_URL = CELERY_RESULT_BACKEND

CELERY_BROKER_URL = CELERY_RESULT_BACKEND

CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_TASK_SERIALIZER = "json"
