# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import NotasTecnicasCreateView

urlpatterns = patterns('',

    # -- creacion de una nueva nota técnica
    url(
        r'^create$',
        NotasTecnicasCreateView.as_view(),
        name='create'
    ),
)
