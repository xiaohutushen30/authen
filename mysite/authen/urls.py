from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^index/$','authen.views.index'),
    url(r'^api/cr_status/$','authen.views.comput_room_status'),
)
