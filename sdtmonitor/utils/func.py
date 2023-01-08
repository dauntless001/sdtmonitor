import requests
from wsite.models import Website
from celery import task
from .views import send_email_notification, send_sms_notification

@task
def check_website_status():
    websites = Website.objects.all()
    for website in websites:
        try:
            response = requests.get(website.url)
            website.response_time = response.elapsed.microseconds / 1000
            website.status_code = response.status_code
            if response.status_code == 200:
                if not website.is_up:

                    # website was down but is now up
                    website.notification_sent = False
                    website.downtime = 0
                website.is_up = True
            else:
                if website.is_up:
                    
                    # website was up but is now down
                    if not website.notification_sent:
                        recipients = ['your-email@example.com', 'your-phone-number@sms.gateway.com']
                        subject = 'Website Down: {}'.format(website.url)
                        message = 'The website {} is down.'.format(website.url)
                        send_email_notification(subject, message, recipients)
                        send_sms_notification(subject, message, recipients)
                        website.notification_sent = True
                website.is_up = False
        except requests.ConnectionError:
            if website.is_up:
                # website was up but is now down
                if not website.notification_sent:
                    recipients = ['your-email@example.com', 'your-phone-number@sms.gateway.com']
                    subject = 'Website Down: {}'.format(website.url)
                    message = 'The website {} is down.'.format(website.url)
                    send_email_notification(subject, message, recipients)
                    send_sms_notification(subject, message, recipients)
                    website.notification_sent = True
            website.is_up = False
            website.response_time = 0
            website.status_code = 0
        website.save()

