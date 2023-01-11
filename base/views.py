from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from plan.models import Plan
from django.contrib.auth.mixins import LoginRequiredMixin
from base.forms import UserForm
from wsite.models import Website
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def greeting(self):
        '''Function Goes Here'''
        return 'Good Morning'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['websites'] = Website.objects.filter(user=self.request.user)[:5]
        context['greeting'] = self.greeting()
        return context

class EditUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'profile.html'
        context = {
            'form' : UserForm(instance=self.request.user)
        }
        return render(request, template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, instance=self.request.user)
        form.save()
        messages.success(request, 'Profile Updated Successfully')
        return redirect("base:profile")

'''
Update Profile
Subscription Page
'''