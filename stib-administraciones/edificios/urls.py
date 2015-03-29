# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from .views import (
    EdificiosListView,
    EdificiosCreateView,
    EdificiosUpdateView,
    EdificiosDeleteView,
    EdificiosAdministracionesView
)

urlpatterns = patterns('',
    url(
        r'^$',
        EdificiosListView.as_view(),
        name='list'
    ),
    url(
        r'^create/$',
        EdificiosCreateView.as_view(),
        name='create'
    ),
    url(
        r'^update/(?P<pk>\d+)$',
        EdificiosUpdateView.as_view(),
        name='update'
    ),
    url(
        r'^delete/(?P<pk>\d+)$',
        EdificiosDeleteView.as_view(),
        name='delete'
    ),
    url(
        r'^administracion/(?P<pk>\d+)$',
        EdificiosAdministracionesView.as_view(),
        name='administraciones'
    ),

)