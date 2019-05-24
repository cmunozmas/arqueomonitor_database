from django import forms
from models import Cruise, Deployment, Instrument


# class CruiseForm(forms.Form):
#   cruise_name = forms.CharField(max_length=30)
#   cruise_description = forms.CharField(widget=forms.Textarea)

class CruiseForm(forms.Form):
    class Meta:
        model = Cruise
        fields = "__all__"
