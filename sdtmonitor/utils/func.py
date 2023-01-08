import requests
<<<<<<< HEAD
from wsite.models import Website
from celery import task
from django.core.mail import send_mail, send_mass_mail, BadHeaderError



# opens a connection to the mail server each time it’s executed
def send_email_notification(subject, message, from_email, recipients):

    send_mail(subject, message, from_email, 
    recipients, fail_silently=False)


def send_mass_email_notification(subject, message, from_email, recipient_list):
    
    send_mass_mail(subject, message, from_email, recipient_list)


# uses a single connection for all of its message
def send_sms_notification(subject, message, from_email, recipients):
    sms_message = (subject, message, from_email, recipients)
    send_mass_mail((sms_message,), fail_silently=False)


=======
>>>>>>> master


def get_website_status(url):
    try:
        response = requests.get(url)
        return 'up' if response.status_code == 200 else 'down'
    except:
        return 'down'

