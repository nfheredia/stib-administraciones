from django.conf.urls import patterns, url

from .views import ServiciosListView, ServiciosDetailView, ServiciosTagsListView

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
    url(r'^tag/(?P<tag>[\w-]+)/$', ServiciosTagsListView.as_view(), name='tags')
)


