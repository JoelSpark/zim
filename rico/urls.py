from django.conf.urls import url

from . import views

urlpatterns = [
    # /rico/
    url(r'^$', views.index, name='index'),
    # Faults
    url(r'^faults/$', views.FaultIndex.as_view(), name='fault_index'),
    url(r'^faults/new$', views.add_fault, name='add_fault'),
    url(r'^faults/(?P<pk>[0-9]+)/$', views.FaultDetail.as_view(), name='fault_detail'),
    # Issues
    url(r'^issues/$', views.IssueIndex.as_view(), name='issue_index'),
    url(r'^issues/new$', views.add_issue, name='add_issue'),
    url(r'^issues/(?P<pk>[0-9]+)/$', views.IssueDetail.as_view(), name='issue_detail'),
    # Assets
    url(r'^assets/$', views.AssetIndex.as_view(), name='asset_index'),
    url(r'^assets/new$', views.add_asset, name='add_asset'),
    url(r'^assets/(?P<pk>[0-9]+)/$', views.AssetDetail.as_view(), name='asset_detail'),
    # Comments
    url(r'^(?P<object_name>\w+)s/(?P<pk>[0-9]+)/comment/$', views.add_comment, name='add_comment'),
]
