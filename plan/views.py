from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class PlanView(TemplateView):
    template_name = 'plan/list.html'