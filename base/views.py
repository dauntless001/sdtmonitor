from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from plan.models import Plan
from django.contrib.auth.mixins import LoginRequiredMixin
from base.forms import UserForm
from base.models import About
# Create your views here.
class IndexView(TemplateView):
    template_name = 'partials/homepage.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class EditUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'profile.html'
        context = {
            'form' : UserForm()
        }
        return render(request, template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        form.save()
        return redirect("base:profile")

'''
Update Profile
Subscription Page
'''