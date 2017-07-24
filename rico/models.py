# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.content


class Asset(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fault(models.Model):
    # Attributes
    body = models.TextField()
    start_time = models.DateTimeField('start time')
    resolved_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=2, default='AC',
        choices=[('AC', 'Active'),
                 ('IN', 'Inactive'),
                 ('FP', 'False Positive'),
                 ('OB', 'OBE')])
    # Foreign Keys
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,
                              null=True, blank=True)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        try:
            return str(self.id)
        except NameError:
            return "None"


class Issue(models.Model):
    # Attributes
    title = models.CharField(max_length=140)
    created_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    resolution = models.CharField(
        max_length=2, default='NO',
        choices=[('NO', 'None'),
                 ('MA', 'Manual'),
                 ('GF', 'Ground FDIR'),
                 ('SF', 'Space FDIR'),
                 ('SO', 'Solved'),
                 ('CR', 'Cannot Reproduce'),
                 ('CF', 'Cannot Fix'),
                 ('OB', 'OBE')])
    # Foreign Keys
    faults = models.ManyToManyField(Fault)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title
