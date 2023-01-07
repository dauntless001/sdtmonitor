from django.shortcuts import render
from django.views.generic import TemplateView
from plan.models import Plan
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context




'''
Update Profile
Subscription Page
'''