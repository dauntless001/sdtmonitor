from django.urls import path
from base import views


app_name = 'base'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("profile", views.EditUser.as_view(), name='profile'),
]