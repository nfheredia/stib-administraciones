# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import DashboardIndexView

urlpatterns = patterns('',
    url(
       regex = r'^$',
       view = DashboardIndexView.as_view(),
       name = 'index'
    ),
)