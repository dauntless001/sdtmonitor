from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass


class About(models.Model):
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    company_history = models.TextField()
    company_mission = models.TextField()
    company_values = models.TextField()
    company_goals = models.TextField()

    def __str__(self):
        return self.company_name