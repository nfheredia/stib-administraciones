from django.conf.urls import patterns, url

from .views import (FotosAdministracionListView,
                    FotosAdministracionCreateView,
                    FotosAdministracionUpdateView,
                    FotosAdministracionDeleteView)

urlpatterns = patterns('stib_administraciones.perfiles.views',
    url(
        regex=r'^administracion/(?P<edificio>\d+)$',
        view=FotosAdministracionListView.as_view(),
        name='administracion_list'
    ),
    url(
        regex=r'^administracion/create/(?P<edificio>\d+)$',
        view=FotosAdministracionCreateView.as_view(),
        name='administracion_create'
    ),
    url(
        regex=r'^administracion/update/(?P<pk>\d+)/(?P<edificio>\d+)$',
        view=FotosAdministracionUpdateView.as_view(),
        name='administracion_update'
    ),
    url(
        regex=r'^administracion/delete/(?P<pk>\d+)/(?P<edificio>\d+)$',
        view=FotosAdministracionDeleteView.as_view(),
        name='administracion_delete'
    ),
)
