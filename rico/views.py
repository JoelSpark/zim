# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the rico index.")


def detail(request, fault_id):
    return HttpResponse("You're looking at fault_id %s" % fault_id)
