# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import importlib

from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from .models import Fault, Asset, Comment
from .forms import CommentForm


def index(request):
    return HttpResponse("Hello, world. This is the rico index.")


def fault_list(request):
    fault_list = get_list_or_404(Fault.objects.order_by('id'))
    return render(request, 'faults/index.html', {'fault_list': fault_list})


def fault_detail(request, pk):
    fault = get_object_or_404(Fault, pk=pk)
    return render(request, 'faults/detail.html', {'fault': fault})


def asset_list(request):
    asset_list = get_list_or_404(Asset.objects.order_by('name'))
    return render(request, 'assets/index.html', {'asset_list': asset_list})


def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'assets/detail.html', {'asset': asset})


def add_comment(request, object_name, pk):
    print object_name
    rico_models = importlib.import_module('rico.models')
    _object = get_object_or_404(
        getattr(rico_models, object_name.title()), pk=pk)
    if not hasattr(_object, 'comments'):
        return HttpResponseBadRequest(
            "%s does not have comments field" % _object.__name__)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            _object.comments.add(comment)
            return redirect('%s_detail' % object_name, pk=pk)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})
