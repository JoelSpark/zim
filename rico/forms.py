# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Fault, Issue, Asset, Comment


class FaultForm(ModelForm):
    class Meta:
        model = Fault
        fields = ('title',
                  'description',
                  'start_time',
                  'resolved_time',
                  'status',
                  )
        exclude = ('comments',)


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ('title',
                  'description',
                  'resolution',
                  'faults',
                  )
        exclude = ('created_time',
                   'comments',
                   )


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ('name',)
        exclude = ('faults',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        exclude = ('user',)
