from django.conf.urls import patterns, url
from .views import (HorariosEdificiosListView,
                    HorariosEdificiosCreateView,
                    HorariosEdificiosUpdateView,
                    HorariosEdificiosDeleteView)

urlpatterns = patterns('',

    # lista de horarios de un edificio
    url(
        r'^edificio/(?P<edificio>\d+)$',
        HorariosEdificiosListView.as_view(),
        name='edificio_horario_list'
    ),

    # creacion de un horarios para un edificio
    url(
        r'^edificio/(?P<edificio>\d+)/create$',
        HorariosEdificiosCreateView.as_view(),
        name='edificio_horario_create'
    ),

    # modificacion de un horarios para un edificio
    url(
        r'^edificio/(?P<edificio>\d+)/update/(?P<pk>\d+)$',
        HorariosEdificiosUpdateView.as_view(),
        name='edificio_horario_update'
    ),

    # borrar de un horario de un edificio
    url(
        r'^edificio/(?P<edificio>\d+)/delete/(?P<pk>\d+)$',
        HorariosEdificiosDeleteView.as_view(),
        name='edificio_horario_delete'
    ),
)
