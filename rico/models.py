# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fault(models.Model):
    body = models.TextField()
    start_time = models.DateTimeField('start time')
    resolved_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=2, default='AC',
        choices=[('AC', 'Active'),
                 ('IN', 'Inactive'),
                 ('FP', 'False Positive'),
                 ('OB', 'OBE')])
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        try:
            return str(self.id)
        except NameError:
            return "None"
