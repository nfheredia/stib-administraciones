# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import (NotasTecnicasCreateView,
                    NotasTecnicasListView,
                    NotasTecnicasDeleteView,
                    reenviar_email,
                    NotasTecnicasDetailView,
                    enviar_cambio_estado,
                    NotasTecnicasEdificioListView,
                    NotasTecnicasTrabajoRealizadoView)

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

    # -- reenviar email
    url(
        r'^reenviar/mail/(?P<pk>\d+)$',
        reenviar_email,
        name='reenviar-mail'
    ),

    # -- detalle de una nota técnica
    url(
        r'^(?P<pk>\d+)$',
        NotasTecnicasDetailView.as_view(),
        name='detail'
    ),

    # -- enviar cambio de estado
    url(
        r'^cambio/estado$',
        enviar_cambio_estado,
        name='cambio-estado'
    ),

    # -- listado notas técnicas de un edificio en particular
    url(
        r'^edificio/(?P<edificio>\d+)$',
        NotasTecnicasEdificioListView.as_view(),
        name='notas-tecnicas-edificio'
    ),

    # -- marcar la nota tecnica como trabajo realizado
    url(
        r'^(?P<pk>\d+)/trabajo/realizado$',
        NotasTecnicasTrabajoRealizadoView.as_view(),
        name='trabajo-realizado'
    ),

)
