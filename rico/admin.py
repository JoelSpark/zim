# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Asset, Fault, Comment, Issue

admin.site.register(Asset)
admin.site.register(Fault)
admin.site.register(Comment)
admin.site.register(Issue)
