import string

from django.utils.crypto import get_random_string

def get_slug_text(amount=15):
    """generates random characters `amount` number of times"""
    return f"{get_random_string(amount, string.ascii_lowercase)}"