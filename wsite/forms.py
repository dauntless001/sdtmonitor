from django import forms
from sdtmonitor.utils.forms import CssForm
from wsite.models import Website

class WebsiteForm(forms.ModelForm, CssForm):
    class Meta:
        model = Website
        exclude = ['user', 'status', 'slug']