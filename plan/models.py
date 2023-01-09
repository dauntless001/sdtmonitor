from django.db import models
from sdtmonitor.utils.models import NameTimeBasedModel, TimeBasedModel, StatusModel
# Create your models here.


# Plan changed to Pricing and the fields modified
class Pricing(NameTimeBasedModel):
    plan_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return self.plan_name
