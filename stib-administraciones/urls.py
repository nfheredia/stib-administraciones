# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # -- sitio adminitracion
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include("stib-administraciones.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # -- perfiles
    url(r'^perfiles/', include('stib-administraciones.perfiles.urls', namespace='perfiles')),
    url(r'^imperavi/', include('imperavi.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ---------------
# -- flatpages --
# ---------------
urlpatterns += patterns('django.contrib.flatpages.views',
    # -- todas las flatpages
    url(r'^(?P<url>.*/)$', 'flatpage'),
    # -- pagina / , root de la pagina
    url(r'^', 'flatpage', {'url': '/inicio/'}, name='inicio'),
)
