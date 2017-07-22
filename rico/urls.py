from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # /fault/id
    url(r'^(?P<fault_id>[0-9]+)/$', views.detail, name='detail'),
]
