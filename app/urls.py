# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^zipcode/', include('zipcode.urls', namespace='zipcode')),
)
