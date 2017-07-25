# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import importlib
from datetime import datetime

from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from .models import Fault, Asset, Issue
from .forms import FaultForm, IssueForm, AssetForm, CommentForm


def index(request):
    return HttpResponse("Hello, world. This is the rico index.")


def fault_index(request):
    fault_list = get_list_or_404(Fault.objects.order_by('id'))
    return render(request, 'faults/index.html', {'fault_list': fault_list})


def fault_detail(request, pk):
    fault = get_object_or_404(Fault, pk=pk)
    return render(request, 'faults/detail.html', {'fault': fault})


def add_fault(request):
    if request.method == "POST":
        form = FaultForm(request.POST)
        if form.is_valid():
            fault = form.save(commit=False)
            if fault.start_time is None:
                fault.start_time = datetime.now()
            fault.save()
            return redirect('fault_detail', pk=fault.id)
    else:
        form = FaultForm()
    return render(request, 'faults/add_fault.html', {'form': form})


def issue_index(request):
    issue_list = get_list_or_404(Issue.objects.order_by('id'))
    return render(request, 'issues/index.html', {'issue_list': issue_list})


def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'issues/detail.html', {'issue': issue})


def add_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.save()
            return redirect('issue_detail', pk=issue.id)
    else:
        form = IssueForm()
    return render(request, 'issues/add_issue.html', {'form': form})


def asset_list(request):
    asset_list = get_list_or_404(Asset.objects.order_by('name'))
    return render(request, 'assets/index.html', {'asset_list': asset_list})


def asset_detail(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    return render(request, 'assets/detail.html', {'asset': asset})


def add_asset(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('asset_detail', pk=asset.id)
    else:
        form = AssetForm()
    return render(request, 'assets/add_asset.html', {'form': form})


def add_comment(request, object_name, pk):
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
