from django.urls import path
from plan import views


app_name = 'plan'

urlpatterns = [
    path("", views.PlanView.as_view(), name='plans'),
]