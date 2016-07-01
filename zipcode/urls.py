# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .resources import ZipcodeResource

urlpatterns = patterns('',
    url(r'^$', ZipcodeResource.as_list(), name='zipcode_list'),
    url(r'(?P<zipcode>\d+)/$', ZipcodeResource.as_detail(), name='zipcode_detail'),
)