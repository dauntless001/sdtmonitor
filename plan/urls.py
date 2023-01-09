from django.urls import path
from plan import views


app_name = 'plan'

urlpatterns = [
    path("", views.PricingView.as_view(), name='plans'),
]