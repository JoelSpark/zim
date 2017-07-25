# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import importlib
from datetime import datetime

from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import generic

from .models import Fault, Asset, Issue
from .forms import FaultForm, IssueForm, AssetForm, CommentForm


def index(request):
    return render(request, 'rico/index.html')


class FaultIndex(generic.ListView):
    template_name = 'faults/index.html'

    def get_queryset(self):
        return Fault.objects.order_by('-id')


class FaultDetail(generic.DetailView):
    model = Fault
    template_name = 'faults/detail.html'


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


class IssueIndex(generic.ListView):
    template_name = 'issues/index.html'

    def get_queryset(self):
        return Issue.objects.order_by('-id')


class IssueDetail(generic.DetailView):
    model = Issue
    template_name = 'issues/detail.html'


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


class AssetIndex(generic.ListView):
    template_name = 'assets/index.html'

    def get_queryset(self):
        return Asset.objects.order_by('-id')


class AssetDetail(generic.DetailView):
    model = Asset
    template_name = 'assets/detail.html'


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
