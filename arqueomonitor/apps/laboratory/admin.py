# coding: utf-8
from django.contrib import admin
import models
from django import forms

from models import TankTrial, Sample
from arqueomonitor.apps.campaign.models import Station


# Register your models here.
class AuditModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'created_by', 'updated_on', 'updated_by')

    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)

class CustomSampleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.sample_name)

class CustomTankTrialChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.tank_trial_name)

class CustomStationChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.station_name)

## Admin forms
class SampleAdminForm(forms.ModelForm):
    sample_station = CustomStationChoiceField(queryset=Station.objects.all())

    class Meta:
        model = Sample
        fields = '__all__'

class TankTrialAdminForm(forms.ModelForm):
    #tank_trial_name = CustomTankTrialChoiceField(queryset=TankTrial.objects.all())
    tank_trial_station = CustomStationChoiceField(queryset=Station.objects.all())
    class Meta:
        model = TankTrial
        fields = '__all__'

## Admin Models
# class StationAdmin(AuditModelAdmin):
#     list_display = ('station_name',)

class SampleAdmin(AuditModelAdmin):
    list_display = ('sample_name',)
    form = SampleAdminForm
    def get_station(self, obj):
        if obj.sample_station:
            return obj.sample_station.station_name
        else:
            return
    get_station.short_description = 'Station'
    get_station.admin_order_field = 'station.station_name'

class TankTrialAdmin(AuditModelAdmin):
    list_display = ('tank_trial_name',)
    form = TankTrialAdminForm
    def get_station(self, obj):
        if obj.tank_trial_station:
            return obj.tank_trial_station.station_name
        else:
            return
    get_station.short_description = 'Station'
    get_station.admin_order_field = 'station.station_name'


admin.site.register(Sample, SampleAdmin)
admin.site.register(TankTrial, TankTrialAdmin)
