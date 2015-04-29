from django.conf.urls import patterns, url

from .views import ServiciosListView, ServiciosDetailView, ServiciosTagsListView, pedido_cotizacion

urlpatterns = patterns('stib-administraciones.productos.views',
    url(
        regex=r'^$',
        view=ServiciosListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=ServiciosDetailView.as_view(),
        name='detail'
    ),
    url(r'^tag/(?P<tag>[\w-]+)/$', ServiciosTagsListView.as_view(), name='tags'),
    url(r'^pedido/cotizacion/(?P<pk>\d+)$', pedido_cotizacion, name='pedido_cotizacion'),
)


