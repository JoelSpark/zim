# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse

from .models import Fault, Asset


def index(request):
    return HttpResponse("Hello, world. This is the rico index.")


def fault_list(request):
    fault_list = get_list_or_404(Fault.objects.order_by('id'))
    return render(request, 'faults/index.html', {'fault_list': fault_list})


def fault_detail(request, fault_id):
    fault = get_object_or_404(Fault, pk=fault_id)
    return render(request, 'faults/detail.html', {'fault': fault})


def asset_list(request):
    asset_list = get_list_or_404(Asset.objects.order_by('name'))
    return render(request, 'assets/index.html', {'asset_list': asset_list})


def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'assets/detail.html', {'asset': asset})
