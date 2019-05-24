from django import forms
from models import Cruise, Deployment, Instrument, Station


# class CruiseForm(forms.Form):
#   cruise_name = forms.CharField(max_length=30)
#   cruise_description = forms.CharField(widget=forms.Textarea)

class CruiseForm(forms.Form):
    cruise_name = forms.CharField(max_length=30)
    cruise_description = forms.CharField(widget=forms.Textarea)
    # class Meta:
    #     model = Cruise
    #     fields = "__all__"
class StationForm(forms.Form):
    station_name = forms.CharField(max_length=30)
    station_description = forms.CharField(widget=forms.Textarea)
    station_lat = forms.FloatField()
