from django.conf.urls import url

from . import views

urlpatterns = [
    # /rico/
    url(r'^$', views.index, name='index'),
    # /rico/id
    url(r'^faults/$', views.fault_list, name='fault_index'),
    url(r'^faults/(?P<fault_id>[0-9]+)/$', views.fault_detail, name='fault_detail'),
    url(r'^assets/$', views.asset_list, name='asset_index'),
    url(r'^assets/(?P<asset_id>[0-9]+)/$', views.asset_detail, name='asset_detail'),
]
