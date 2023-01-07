from django.db import models

class SiteStatus(models.TextChoices):
        down = 'down', 'Down'
        up = 'up', 'Up'
