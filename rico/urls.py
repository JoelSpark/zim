from django.conf.urls import url

from . import views

urlpatterns = [
    # /rico/
    url(r'^$', views.index, name='index'),
    # /rico/id
    url(r'^faults/$', views.fault_list, name='fault list'),
    url(r'^faults/(?P<fault_id>[0-9]+)/$', views.fault_detail, name='fault detail'),
]
