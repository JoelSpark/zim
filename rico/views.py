# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse

from .models import Fault


def index(request):
    return HttpResponse("Hello, world. This is the rico index.")


def fault_list(request):
    fault_list = Fault.objects.order_by('id')
    context = {
        'fault_list': fault_list
    }
    return render(request, 'faults/index.html', context)


def fault_detail(request, fault_id):
    return HttpResponse("You're looking at fault_id %s" % fault_id)
