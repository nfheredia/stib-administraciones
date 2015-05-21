from django.conf.urls import patterns, url
from .views import (ContactosEdificiosListView)

urlpatterns = patterns('',
    url(
        r'^edificio/(?P<pk>\d+)$',
        ContactosEdificiosListView.as_view(),
        name='edificio_contactos_list'
    ),
)
