from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, View, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from wsite.models import Website
from wsite.forms import WebsiteForm
from sdtmonitor.settings.local.email_settings import SERVER_EMAIL
# Create your views here.


class ListWebsiteView(LoginRequiredMixin, ListView):
    template_name = 'wsite/list.html'
    paginate_by = 15
    context_object_name = 'websites'
    
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)


class CreateWebsiteView(LoginRequiredMixin, CreateView):
    template_name = 'wsite/create.html'
    form_class = WebsiteForm
    model = Website

    def form_valid(self, form):
        request = self.request
        website = form.save(commit=False)
        website.user = request.user
        website.save()
        messages.success(
            request,
            f"Website {website.name} successfully added for monitor",
        )
        msg_to_user = (
            f"Hi {request.user}\n\n" +
            f"Site {website.name} has been added to your watch list" +
            f"You can proceed with your day to day activity while we help you watch it")

        send_mail(
            subject="New Site Added to Watch List",
            message=msg_to_user,
            fail_silently=True,
            from_email=SERVER_EMAIL,
            recipient_list=[request.user.email],
        )

        return redirect("wsite:wsites")


class RetrieveWebsiteView(LoginRequiredMixin, DetailView):
    template_name = 'wsite/detail.html'
    slug_url_kwarg = 'slug'
    model = Website



class DeleteWebsiteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        sites = get_object_or_404(Website, slug=self.kwargs['slug'])
        sites.delete()
        messages.success(
            request,
            f"Website removed from watchlist",
        )
        return redirect("wsite:wsites")
