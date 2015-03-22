from django.conf.urls import patterns, url
from .views import NovedadesListView, NovedadesDetailView

urlpatterns = patterns('stib-administraciones.novedades.views',

        url(r'^$', NovedadesListView.as_view(), name='novedades_list'),
        url(r'^(?P<pk>\d+)/$', NovedadesDetailView.as_view(), name='novedades_detail'),

)
