# coding: utf-8
from django.contrib import admin
import models
from django import forms

from arqueomonitor.apps.products.models import Product, Publication, Staff


# Register your models here.
class AuditModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'created_by', 'updated_on', 'updated_by')

    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)

class CustomProductChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.product_name)

class CustomPublicationChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.publication_name)

class CustomStaffChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.staff_email)

## Admin forms
# class ProductAdminForm(forms.ModelForm):
#     sample_station = CustomProductChoiceField(queryset=Product.objects.all())
#
#     class Meta:
#         model = Product
#         fields = '__all__'

# class TankTrialAdminForm(forms.ModelForm):
#     #tank_trial_name = CustomTankTrialChoiceField(queryset=TankTrial.objects.all())
#     tank_trial_station = CustomStationChoiceField(queryset=Station.objects.all())
#     class Meta:
#         model = TankTrial
#         fields = '__all__'

## Admin Models
class ProductAdmin(AuditModelAdmin):
    list_display = ('product_name',)

class PublicationAdmin(AuditModelAdmin):
    list_display = ('publication_name',)

class StaffAdmin(AuditModelAdmin):
    list_display = ('staff_email',)
# class ProductAdmin(AuditModelAdmin):
#     list_display = ('product_name',)
#     form = ProductAdminForm
#     def get_product(self, obj):
#         if obj.sample_station:
#             return obj.sample_station.station_name
#         else:
#             return
#     get_station.short_description = 'Station'
#     get_station.admin_order_field = 'station.station_name'
#
# class TankTrialAdmin(AuditModelAdmin):
#     list_display = ('tank_trial_name',)
#     form = TankTrialAdminForm
#     def get_station(self, obj):
#         if obj.tank_trial_station:
#             return obj.tank_trial_station.station_name
#         else:
#             return
#     get_station.short_description = 'Station'
#     get_station.admin_order_field = 'station.station_name'
#
#
admin.site.register(Product, ProductAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Staff, StaffAdmin)
