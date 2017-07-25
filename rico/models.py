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


class Fault(models.Model):
    # Attributes
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    resolved_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=2, default='AC',
        choices=[('AC', 'Active'),
                 ('IN', 'Inactive'),
                 ('FP', 'False Positive'),
                 ('OB', 'OBE')])
    # Foreign Keys
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        try:
            return str(self.title)
        except NameError:
            return "None"


class Asset(models.Model):
    name = models.CharField(max_length=140)
    faults = models.ManyToManyField(Fault)

    def __str__(self):
        return self.name


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
