from django.shortcuts import render
from django.views.generic import TemplateView
from plan.models import Pricing
# Create your views here.


class PricingView(View):

    def get(self, request):
        pricing_data = Pricing.objects.first()
        template_name = 'plan/list.html'
        context = {
            'pricing_data': pricing_data
        }
        return render(request, template_name, context)
    # create post data to populate data storage with the admin