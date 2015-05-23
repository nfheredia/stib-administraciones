from django.conf.urls import patterns, url
from .views import (ContactosEdificiosListView,
                    ContactosEdificiosCreateView,
                    ContactosEdificiosUpdateView,
                    ContactosEdificiosDeleteView)

urlpatterns = patterns('',

    # lista de contactos de un edificio
    url(
        r'^edificio/(?P<edificio>\d+)$',
        ContactosEdificiosListView.as_view(),
        name='edificio_contactos_list'
    ),

    # creacion de un contacto para un edificio
    url(
        r'^edificio/(?P<edificio>\d+)/create$',
        ContactosEdificiosCreateView.as_view(),
        name='edificio_contactos_create'
    ),

    # modificacion de un contacto para un edificio
    url(
        r'^edificio/(?P<edificio>\d+)/update/(?P<pk>\d+)$',
        ContactosEdificiosUpdateView.as_view(),
        name='edificio_contactos_update'
    ),

    # borrar de un contacto de un edificio
    url(
        r'^edificio/(?P<edificio>\d+)/delete/(?P<pk>\d+)$',
        ContactosEdificiosDeleteView.as_view(),
        name='edificio_contactos_delete'
    ),
)
