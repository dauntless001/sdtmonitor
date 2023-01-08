from django.urls import path
from base import views


app_name = 'base'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("about-us/", views.AboutUsView.as_view(), name='about'),
    path("contact-us/", views.ContactView.as_view(), name='contact'),
    path("profile/", views.EditUser.as_view(), name='profile'),
]