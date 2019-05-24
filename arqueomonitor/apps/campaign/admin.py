# coding: utf-8
from django.contrib import admin
import models
from django import forms
from models import Cruise, Deployment, Instrument, Station
# Register your models here.


class AuditModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'created_by', 'updated_on', 'updated_by')

    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)

class CustomCruiseChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.cruise_name)

class CustomDeploymentChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.deployment_name)

class CustomInstrumentChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.instrument_name)

class CustomStationChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.station_name)

## Admin forms
class StationAdminForm(forms.ModelForm):
    station_name = CustomStationChoiceField(queryset=Station.objects.all())

    class Meta:
        model = Station
        fields = '__all__'

class CruiseAdminForm(forms.ModelForm):
    cruise_name = CustomCruiseChoiceField(queryset=Cruise.objects.all())

    class Meta:
        model = Cruise
        fields = '__all__'

class DeploymentAdminForm(forms.ModelForm):
    deployment_cruise = CustomCruiseChoiceField(queryset=Cruise.objects.all())
    #campaign_deployment_name = CustomDeploymentChoiceField(queryset=Deployment.objects.all())
    deployment_instrument = CustomInstrumentChoiceField(queryset=Instrument.objects.all())
    deployment_station = CustomStationChoiceField(queryset=Station.objects.all())
    class Meta:
        model = Deployment
        fields = '__all__'

class InstrumentAdminForm(forms.ModelForm):
    instrument_name = CustomInstrumentChoiceField(queryset=Instrument.objects.all())

    class Meta:
        model = Instrument
        fields = '__all__'

## Admin Models
class StationAdmin(AuditModelAdmin):
    list_display = ('station_name',)

class CruiseAdmin(AuditModelAdmin):
    list_display = ('cruise_name',)

class DeploymentAdmin(AuditModelAdmin):
    #search_fields = ['campaign_deployment_id']
    list_display = ('deployment_name', 'get_cruise', 'get_instrument')
    form = DeploymentAdminForm

    def get_cruise(self, obj):
        if obj.deployment_cruise:
            return obj.deployment_cruise.cruise_name
        else:
            return
    get_cruise.short_description = 'Cruise'
    get_cruise.admin_order_field = 'cruise.cruise_name'

    def get_instrument(self, obj):
        if obj.deployment_instrument:
            return obj.deployment_instrument.instrument_name
        else:
            return
    get_instrument.short_description = 'Instrument'
    get_instrument.admin_order_field = 'instrument.instrument_name'

    def get_station(self, obj):
        if obj.deployment_station:
            return obj.deployment_station.station_name
        else:
            return
    get_station.short_description = 'Station'
    get_station.admin_order_field = 'station.station_name'

class InstrumentAdmin(AuditModelAdmin):
    list_display = ('instrument_name',)


admin.site.register(Cruise, CruiseAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Station, StationAdmin)
