from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from wsite.models import Website, WebsiteEmail


class AddEmailView(LoginRequiredMixin, UserPassesTestMixin ,View):
    '''
    This view add emails to website monitor list
    '''

    def get_website(self):
        return get_object_or_404(Website, slug=self.kwargs['slug'])

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        _, created = WebsiteEmail.objects.get_or_create(site=self.get_website(), email=email)
        data = {
            'msg' : 'Emails Added Successfully'
        }
        return JsonResponse(data, safe=False)

    def test_func(self):
        if self.get_website().user == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        data = {
            'msg' : 'You are not Authorized to Perform this Action'
        }
        return JsonResponse(data,safe=False)


class RemoveEmailView(LoginRequiredMixin, UserPassesTestMixin ,View):
    '''
    This view add emails to website monitor list
    '''

    def get_website(self):
        return get_object_or_404(Website, slug=self.kwargs['slug'])

    def post(self, request, *args, **kwargs):
        email = get_object_or_404(WebsiteEmail, site=self.get_website(), email=request.POST['email'])
        email.delete()
        data = {
            'msg' : 'Emails Removed Successfully'
        }
        return JsonResponse(data, safe=False)

    def test_func(self):
        if self.get_website().user == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        data = {
            'msg' : 'You are not Authorized to Perform this Action'
        }
        return JsonResponse(data,safe=False)