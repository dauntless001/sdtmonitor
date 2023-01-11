from celery import shared_task
from django.utils.timezone import now, timedelta, datetime
from sdtmonitor.celery import app
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from wsite.models import Website
from sdtmonitor.utils.func import get_website_status


def send_email(context, website, to):
    from_email = settings.EMAIL_HOST_USER
    subject = f'Website Update for {website}'
    html_message = render_to_string('report_notification.html',context)
    plain_message = strip_tags(html_message)
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)    

@app.task()
def send_report_notification():
    websites = Website.objects.all()
    for website in websites:
        status = get_website_status(website.url)
        print(status)
        if status != website.status:
            last_time = website.modified_at
            website.status = status
            website.save()
            duration = website.modified_at - last_time 
            msg = 'Your site is down'
            if status == 'up':
                msg = f'Your site is now up and running. Downtime duration is {duration}'
            context = {
                'message' : msg,
            }
            send_email(context=context, to=[email.email for email in website.websiteemail_set.all()], website=website)             
    return True
