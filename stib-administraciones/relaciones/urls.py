from django.conf.urls import patterns, url

from .views import EstableverTipoComunicacion, NotificarUsuariosProductos

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
)



