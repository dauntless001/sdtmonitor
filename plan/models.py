from django.db import models
from sdtmonitor.utils.models import NameTimeBasedModel, TimeBasedModel, StatusModel
# Create your models here.
class Plan(NameTimeBasedModel):
    description = models.TextField()
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
