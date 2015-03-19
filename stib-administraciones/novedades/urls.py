from django.conf.urls import patterns, url
from .views import NovedadesListView

urlpatterns = patterns('stib-administraciones.novedades.views',

        url(r'^$', NovedadesListView.as_view(), name='novedades_list'),

)
