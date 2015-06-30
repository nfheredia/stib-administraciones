from django.conf.urls import patterns, url

from .views import (EstableverTipoComunicacion,
                    NotificarProductosUsuarios,
                    NotificarServiciosUsuarios,
                    get_autocomplete_result,
                    NotificarProductosEdificios,
                    get_autocomplete_edificios_result,
                    NotificarServiciosEdificios,
                    NotificacionesEdificiosView)

urlpatterns = patterns('stib-administraciones.productos.views',
    url(
       regex=r'^$',
       view=EstableverTipoComunicacion.as_view(),
       name='definir'
    ),
    url(
       regex=r'^productos-administraciones$',
       view=NotificarProductosUsuarios.as_view(),
       name='productos-administraciones'
    ),
    url(
       regex=r'^search-autocomplete/$',
       view=get_autocomplete_result,
       name='search_autocomplete'
    ),
    url(
       regex=r'^servicios-administraciones$',
       view=NotificarServiciosUsuarios.as_view(),
       name='servicios-administraciones'
    ),
    url(
       regex=r'^productos-edificios$',
       view=NotificarProductosEdificios.as_view(),
       name='productos-edificios'
    ),
    url(
       regex=r'^servicios-edificios$',
       view=NotificarServiciosEdificios.as_view(),
       name='servicios-edificios'
    ),
    url(
       regex=r'^search-autocomplete-edificios$',
       view=get_autocomplete_edificios_result,
       name='search-autocomplete-edificios'
    ),
    url(
       regex=r'^edificios/list$',
       view=NotificacionesEdificiosView.as_view(),
       name='edificios-list'
    )
)


