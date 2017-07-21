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
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        try:
            return str(self.id)
        except NameError:
            return "None"
