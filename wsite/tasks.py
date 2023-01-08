import os
from celery import shared_task

from django.utils.timezone import now, timedelta, datetime

from sdtmonitor.celery import app
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from wsite.models import Website, WebsiteEmail


def send_email(context, website, to):
    from_email = settings.EMAIL_HOST_USER
    subject = f'Website Update for {website}'
    html_message = render_to_string('base/daily_overview.html',context)
    plain_message = strip_tags(html_message)
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)    

@app.task()
def send_report_overview():
    environment = os.getenv("ENVIRONMENT", "DEV")
    url = None

    # if environment == 'DEV':
    #     url = "http://127.0.0.1:8000"
    url = "http://127.0.0.1:8000"
    websites = Website.objects.all()
    # for website in websites:
    #     context = {
    #     'url' : url
    #     }
    #     send_email(context=context, to=[], website=website)
                    
    return True
