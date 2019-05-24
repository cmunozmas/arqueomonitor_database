# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from arqueomonitor.apps.base.models import AuditBaseModel
#from scb_mng_models.models.instrumentation import Deployment, Instrument, Sensor

# queryset = Deployment.objects.all()
# DEPLOYMENT_CHOICES = ()
# for i in range(0,len(queryset)):
#     deployment_i = (queryset[i].deployment_id, queryset[i].deployment_id)
#     DEPLOYMENT_CHOICES = DEPLOYMENT_CHOICES + (deployment_i,)

# queryset = instrumentation.Cruise.objects.all()
# CRUISE_CHOICES = ()
# for i in range(0,len(queryset)):
#     cruise_name_i = (queryset[i].cruise_name, queryset[i].cruise_name)
#     CRUISE_CHOICES = CRUISE_CHOICES + (cruise_name_i,)
#
# queryset = instrumentation.Deployment.objects.all()
# DEPLOYMENT_CHOICES = ()
# for i in range(0,len(queryset)):
#     deployment_name_i = (queryset[i].deployment_name, queryset[i].deployment_name)
#     DEPLOYMENT_CHOICES = DEPLOYMENT_CHOICES + (deployment_name_i,)
#
INSTRUMENT_TYPE_CHOICES = (
    ('ctd', 'CTD'),
    ('turbidimeter', 'TURBIDIMETER'),
    ('currentmeter', 'CURRENTMETER'),
)

class Station(AuditBaseModel):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    station_description = models.TextField(blank=True, null=True)
    station_geospatial_lat = models.FloatField(blank=True, null=True)
    station_geospatial_lon = models.FloatField(blank=True, null=True)
    station_geospatial_lat_units = models.CharField(max_length=10, blank=True, null=True)
    station_geospatial_lon_units = models.CharField(max_length=10, blank=True, null=True)
    station_geospatial_datum = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'campaign\".\"station'

class Cruise(AuditBaseModel):
    cruise_id = models.AutoField(primary_key=True)
    cruise_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    cruise_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'campaign\".\"cruise'


class Deployment(AuditBaseModel):
    deployment_id = models.AutoField(primary_key=True)
    deployment_description = models.TextField(blank=True, null=True)
    deployment_cruise = models.ForeignKey('Cruise', null=True)
    deployment_instrument = models.ForeignKey('Instrument', null=True)
    deployment_station = models.ForeignKey('Station', null=True)
    deployment_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    deployment_initial_date = models.DateTimeField(blank=True, null=True)
    deployment_end_date = models.DateTimeField(blank=True, null=True)
    deployment_filename = models.CharField(max_length=50, blank=True, null=True)
    deployment_geospatial_lon_max = models.TextField(blank=True, null=True)
    deployment_geospatial_lon_min = models.TextField(blank=True, null=True)
    deployment_principal_investigator = models.TextField(default='Prof Manuel Bethencourt, Prof Alfredo Izquierdo', blank=True, null=True)
    deployment_project = models.TextField(default='Arqueomonitor - Study of the influence of physical, chemical and biological conditions in the damage and protection of Underwater Historical Heritage CTM2009-08668 and CTM2010-1636', blank=True, null=True)
    deployment_principal_investigator_email = models.TextField(default='manuel.bethencourt@uca.es, alfredo.izquierdo@uca.es', blank=True, null=True)
    deployment_geospatial_lat_resolution = models.TextField(blank=True, null=True)
    deployment_geospatial_lat_units = models.TextField(blank=True, null=True)
    deployment_geospatial_lon_units = models.TextField(blank=True, null=True)
    deployment_data_center = models.TextField(default='Balearic Islands Coastal Observing and Forecsting System, SOCIB-ICTS', blank=True, null=True)
    deployment_author_url = models.TextField(blank=True, null=True)
    deployment_distribution_statement = models.TextField(blank=True, null=True)
    deployment_geospatial_lon_resolution = models.TextField(blank=True, null=True)
    deployment_acknowledgement = models.TextField(default='This work was supported by the Spanish Ministry of Economy and Competitiveness and FEDER, Project CTM2010-16363 (ARQUEOMONITOR). Data management efforts were conducted from the Balearic Islands Coastal Observing and Forecasting System (SOCIB-ICTS). The coordinates of the Fougueux and Bucentaure sites were supplied by The Underwater Archaeology Centre of Andalusia. Their studies are needed to understand the history of these ships', blank=True, null=True)
    deployment_code = models.TextField(blank=True, null=True)
    deployment_publisher_name = models.TextField(default= 'University de Cadiz', blank=True, null=True)
    deployment_geospatial_vertical_max = models.TextField(blank=True, null=True)
    deployment_author_email = models.TextField(default='cmunoz@socib.es', blank=True, null=True)
    deployment_geospatial_vertical_units = models.TextField(blank=True, null=True)
    deployment_geospatial_vertical_min = models.TextField(blank=True, null=True)
    deployment_institution = models.TextField(default= 'University de Cadiz', blank=True, null=True)
    deployment_local_time_zone = models.TextField(blank=True, null=True)
    deployment_geospatial_vertical_resolution = models.TextField(blank=True, null=True)
    deployment_license = models.TextField(default= 'CC-BY 4.0', blank=True, null=True)
    deployment_geospatial_lat_min = models.TextField(blank=True, null=True)
    deployment_geospatial_lat_max = models.TextField(blank=True, null=True)
    deployment_contributor_name = models.TextField(default='Cristian Munoz, Tomas Fernandez, Manuel Gonzalez, Alejandro Caballero', blank=True, null=True)
    deployment_contributor_role = models.TextField(default= 'Research Technician, Researcher, Researcher, Research Technician', blank=True, null=True)
    deployment_publisher_url = models.TextField(blank=True, null=True)
    deployment_citation = models.TextField(default= 'University de Cadiz', blank=True, null=True)
    deployment_publisher_email = models.TextField(default= 'cmunoz@socib.es',blank=True, null=True)
    deployment_author = models.TextField(default='Cristian Munoz', blank=True, null=True)
    deployment_area = models.TextField(default='Cadiz Gulf, Spain',blank=True, null=True)
    deployment_data_center_email = models.TextField(default='cmunoz@socib.es', blank=True, null=True)
    geospatialverticalpositive = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'campaign\".\"deployment'

class Instrument(AuditBaseModel):
    instrument_id = models.AutoField(primary_key=True)
    #instrument_instrument_type = models.ForeignKey('InstrumentType', blank=True, null=True)
    instrument_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    instrument_model = models.TextField(blank=True)
    instrument_manufacturer = models.TextField(blank=True)
    instrument_serial = models.TextField(blank=True)
    instrument_description = models.TextField(blank=True)
    instrument_type =  models.CharField(_('instrument_type'), max_length=15, choices=INSTRUMENT_TYPE_CHOICES, null=True, blank=True)
    #instrument_department = models.ForeignKey(Department, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'campaign\".\"instrument'
