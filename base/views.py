from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from plan.models import Plan
from django.contrib.auth.mixins import LoginRequiredMixin
from base.forms import UserForm
from base.models import About, Contact
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context


class AboutUsView(View):

    def get(self, request):
        about_data = About.objects.first()
        template_name = 'about.html'
        context = {
            'about_data': about_data
        }
        return render(request, template_name, context)
    # create post data to populate data storage with the admin



class ContactView(View):

    def get(self, request):
        contact_data = Contact.objects.first()
        template_name = 'contact.html'
        context = {
            'contact_data' : contact_data
        }
        return render(request, template_name, context)
    # create post data to populate data storage with the admin


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

Profile Settings Pages-->
change password
edit profile

home pages -->
Homepage
About us
Pricing

wsite pages ->
create, retreive website
add emails to website


'''