from django.conf.urls import patterns, url

from .views import (EstableverTipoComunicacion,
                    NotificarUsuariosProductos,
					NotificarUsuariosServicios,
                    search_productos_autocomplete)

urlpatterns = patterns('stib-administraciones.productos.views',
    url(
        regex=r'^$',
        view=EstableverTipoComunicacion.as_view(),
        name='definir'
    ),
    url(
        regex=r'^productos-administraciones$',
        view=NotificarUsuariosProductos.as_view(),
        name='productos-administraciones'
    ),
    url(
        regex=r'^search_productos_autocomplete/$',
        view=search_productos_autocomplete,
        name='search_productos_autocomplete'
    ),
	,
    url(
        regex=r'^serivicios-administraciones$',
        view=NotificarUsuariosServicios.as_view(),
        name='serivicios-administraciones'
    ),
)



