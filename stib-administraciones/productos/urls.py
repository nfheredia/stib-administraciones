from django.conf.urls import patterns, url

from .views import ProductosListView, ProductosDetailView, ProductosTagsListView, pedir_cotizacion

urlpatterns = patterns('stib-administraciones.productos.views',
    url(
        regex=r'^$',
        view=ProductosListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=ProductosDetailView.as_view(),
        name='detail'
    ),
    url(r'^tag/(?P<tag>[\w-]+)/$', ProductosTagsListView.as_view(), name='tags'),
    url(r'^pedir/cotizacion/(?P<pk>\d+)$', pedir_cotizacion, name='pedir_cotizacion'),
)

