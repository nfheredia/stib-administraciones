from django.conf.urls import patterns, url
from .views import set_llaves

urlpatterns = patterns('',

    # setear las llaves de un edificio
    url(
        r'^edificio/(?P<edificio>\d+)$',
        set_llaves,
        name='set_llaves'
    ),
)
