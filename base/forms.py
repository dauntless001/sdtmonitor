from django import forms
from sdtmonitor.utils.forms import CssForm
from base.models import User, About

class UserForm(forms.ModelForm, CssForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class AboutForm(forms.Form):
    class Meta:
        model = About
        field = __all__
