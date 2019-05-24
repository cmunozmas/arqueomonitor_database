# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from arqueomonitor.apps.base.models import AuditBaseModel

class Product(AuditBaseModel):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(_('Product Name'), max_length=30, unique=True, blank=False, null=False)
    product_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products\".\"product'

class Publication(AuditBaseModel):
    publication_id = models.AutoField(primary_key=True)
    publication_name = models.CharField(_('Publication Name'), max_length=30, unique=True, blank=False, null=False)
    publication_date = models.DateTimeField(_('Publication Date'), blank=True, null=True)
    publication_citation = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products\".\"publication'

class Staff(AuditBaseModel):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(_('Staff Name'), max_length=30, blank=False, null=False)
    staff_surname = models.CharField(_('Staff Surname'), max_length=30, blank=False, null=False)
    staff_position = models.CharField(_('Staff Position'), max_length=30, blank=True, null=True)
    staff_email = models.CharField(_('Staff email'), max_length=30, unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products\".\"staff'
