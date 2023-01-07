from django import forms
from sdtmonitor.utils.forms import CssForm
from base.models import User

class UserForm(forms.ModelForm, CssForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]