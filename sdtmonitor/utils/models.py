import auto_prefetch
from django.db import models
from sdtmonitor.utils.choices import SiteStatus

class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class NameTimeBasedModel(TimeBasedModel):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    status = models.CharField(max_length=30, choices=SiteStatus.choices, default=SiteStatus.up)


    class Meta:
        abstract = True