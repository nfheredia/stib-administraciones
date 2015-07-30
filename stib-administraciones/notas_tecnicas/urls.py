# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import NotasTecnicasCreateView, NotasTecnicasListView, NotasTecnicasDeleteView

urlpatterns = patterns('',

    # -- creacion de una nueva nota técnica
    url(
        r'^create$',
        NotasTecnicasCreateView.as_view(),
        name='create'
    ),

    # -- listadp notas técnicas
    url(
        r'^$',
        NotasTecnicasListView.as_view(),
        name='list'
    ),

    # -- borrar nota técnica
    url(
        r'^delete/(?P<pk>\d+)$',
        NotasTecnicasDeleteView.as_view(),
        name='delete'
    ),

)
