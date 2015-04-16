from django.conf.urls import patterns, url
from .views import (NovedadesListView,
                    NovedadesDetailView,
                    NovedadesTagsListView
)

urlpatterns = patterns('stib-administraciones.novedades.views',

        url(r'^$', NovedadesListView.as_view(), name='list'),
        url(r'^(?P<pk>\d+)/$', NovedadesDetailView.as_view(), name='detail'),
        url(r'^tag/(?P<tag>[\w-]+)/$', NovedadesTagsListView.as_view(), name='tags'),

)
