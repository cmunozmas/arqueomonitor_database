# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from arqueomonitor.apps.base.models import AuditBaseModel

HEIGHT_CHOICES = (
    ('h1', 'H1'),
    ('h2', 'H2'),
    ('h3', 'H3'),
)
MATERIAL_CHOICES = (
    ('copper', 'COPPER'),
    ('brass', 'BRASS'),
    ('forged_steel', 'FORGED STEEL'),
    ('steel', 'STEEL'),
)
REPLICA_CHOICES = (
    ('r1', 'R1'),
    ('r2', 'R2'),
    ('r3', 'R3'),
    ('r4', 'R4'),
    ('r5', 'R5'),
    ('r6', 'R6'),
)
PUMP_LEVEL_CHOICES = (
    ('ca', 'CA'),
    ('ra', 'RA'),
    ('sa', 'SA'),
)
class TankTrial(AuditBaseModel):
    tank_trial_id = models.AutoField(primary_key=True)
    tank_trial_name = models.CharField(_('Trial Name'), max_length=30, unique=True, blank=False, null=False)
    tank_trial_station = models.ForeignKey('campaign.Station', null=True)
    tank_trial_height =  models.CharField(_('Trial Height'), max_length=15, choices=HEIGHT_CHOICES, blank=False, null=False)
    tank_trial_material =  models.CharField(_('Material Type'), max_length=15, choices=MATERIAL_CHOICES, blank=False, null=False)
    tank_trial_replica =  models.CharField(_('Replica'), max_length=15, choices=REPLICA_CHOICES, blank=False, null=False)
    tank_trial_pump_level =  models.CharField(_('Pump Level'), max_length=15, choices=PUMP_LEVEL_CHOICES, blank=False, null=False)
    tank_trial_date = models.DateTimeField(_('Trial Date'), blank=False, null=False)
    tank_trial_file_name = models.CharField(_('File Name'), max_length=30, unique=True, blank=False, null=False)
    tank_trial_temp = models.FloatField(_('Temperature'), blank=True, null=True)
    tank_trial_salt  = models.FloatField(_('Salinity'), blank=True, null=True)
    tank_trial_cond  = models.FloatField(_('Conductivity'), blank=True, null=True)
    tank_trial_dox  = models.FloatField(_('Dissolved Oxygen'), blank=True, null=True)
    tank_trial_orp  = models.FloatField(_('ORP'), blank=True, null=True)
    tank_trial_comments = models.TextField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'laboratory\".\"tank_trial'

class Sample(AuditBaseModel):
    sample_id = models.AutoField(primary_key=True)
    sample_name = models.CharField(_('Sample Name'), max_length=30, unique=True, blank=False, null=False)
    sample_station = models.ForeignKey('campaign.Station', null=True)
    sample_deployment_date = models.DateTimeField(_('Sample Deployment Date'), blank=True, null=True)
    sample_recovery_date = models.DateTimeField(_('Sample Recovery Date'), blank=True, null=True)
    sample_impairment_date = models.DateTimeField(_('Sample Impairment Date'), blank=True, null=True)
    sample_height =  models.CharField(_('Sample Height'), max_length=15, choices=HEIGHT_CHOICES, blank=False, null=False)
    sample_material =  models.CharField(_('Material Type'), max_length=15, choices=MATERIAL_CHOICES, blank=False, null=False)
    sample_replica =  models.CharField(_('Replica'), max_length=15, choices=REPLICA_CHOICES, blank=False, null=False)
    sample_file_name = models.CharField(_('File Name'), max_length=30, unique=True, blank=True, null=True)
    sample_weight_pre_deployment = models.FloatField(_('Sample weight pre-deployment'), blank=True, null=True)
    sample_weight_post_recovery = models.FloatField(_('Sample weight post recovery'), blank=True, null=True)
    sample_comments = models.TextField(blank=True, null=True)
    sample_image_deployment = models.ImageField(upload_to='sample_image_deployment', blank=True, null=True)
    sample_image_recovery = models.ImageField(upload_to='sample_image_recovery', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'laboratory\".\"sample'
