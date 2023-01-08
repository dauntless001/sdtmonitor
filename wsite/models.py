import auto_prefetch
from django.db import models
from sdtmonitor.utils.models import NameTimeBasedModel, TimeBasedModel, StatusModel
from sdtmonitor.utils.strings import get_slug_text
# Create your models here.


class Website(NameTimeBasedModel, StatusModel):
    user = auto_prefetch.ForeignKey('base.User', on_delete=models.CASCADE)
    url = models.URLField()
    slug = models.SlugField(default=get_slug_text)
    is_up = models.BooleanField(default=True)
    downtime = models.PositiveIntegerField(default=0)
    notification_sent = models.BooleanField(default=False)
    response_time = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.name} site by {self.user}'


class WebsiteLog(TimeBasedModel, StatusModel):
    site = auto_prefetch.ForeignKey('wsite.Website', on_delete=models.CASCADE)

    def __str__(self):
        return ''


class WebsiteEmail(TimeBasedModel):
    site = auto_prefetch.ForeignKey('wsite.Website', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.email} is watching {self.site}'
