import requests


def get_website_status(url):
    try:
        response = requests.get(url)
        return 'up' if response.status_code == 200 else 'down'
    except:
        return 'down'

