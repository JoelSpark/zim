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


def fault_detail(request, fault_id):
    fault = get_object_or_404(Fault, pk=fault_id)
    return render(request, 'faults/detail.html', {'fault': fault})


def asset_list(request):
    asset_list = get_list_or_404(Asset.objects.order_by('name'))
    return render(request, 'assets/index.html', {'asset_list': asset_list})


def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'assets/detail.html', {'asset': asset})


def add_comment_to_fault(request, fault_id):
    fault = get_object_or_404(Fault, pk=fault_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            fault.comments.add(comment)
            return redirect('fault_detail', fault_id=fault_id)
    else:
        form = CommentForm()
    return render(request, 'faults/add_comment_to_fault.html', {'form': form})


def comments(request):
    # POST methods allow you to create a new comment
    # Request should include:
    if request.REQUEST_METHOD == 'POST':
        # Unpack POST request
        try:
            user = request.REMOTE_USER
            content = request.POST.get('content')
            object_list = request.POST.getlist('object_list')
        except KeyError as e:
            return HttpResponseBadRequest(
                "'%s' not provided in POST request" % e)
        # Determine what sort of object(s) to attach the comment to
        try:
            rico_models = importlib.import_module('rico.models')
            object_list = []
            for (model, pk) in object_list:
                _object = get_object_or_404(getattr(rico_models, model),
                                            pk=pk)
        except AttributeError as e:
            return HttpResponseBadRequest("'%s' not a valid rico model")
        # Check all object(s) have a comments field before creating any comment
        for _object in object_list:
            if not hasattr(_object, 'comments'):
                return HttpResponseBadRequest(
                    "'%s' does have 'comments' field" % _object.__name__)
        comment = Comment(user=user,
                          content=content)
        comment.save()
        for _object in object_list:
            _object.comments.add(comment)
        return HttpResponse("done!")
