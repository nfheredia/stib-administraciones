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
    # -- usuarios
    url(r'^users/', include("stib-administraciones.users.urls", namespace="users")),
    # -- accounts apps
    url(r'^accounts/', include('allauth.urls')),
    # -- perfiles
    url(r'^perfiles/', include('stib-administraciones.perfiles.urls', namespace='perfiles')),
    # -- imperavi editor
    url(r'^imperavi/', include('imperavi.urls')),
    # -- feedbacks
    url(r'^feedbacks/', include('stib-administraciones.feedbacks.urls')),
    # -- novedades
    url(r'^novedades/', include('stib-administraciones.novedades.urls', namespace='novedades')),
    # -- edificios
    url(r'^edificios/', include('stib-administraciones.edificios.urls', namespace='edificios')),
    # -- fotos
    url(r'^fotos/', include('stib-administraciones.fotos.urls', namespace='fotos')),
    # -- productos
    url(r'^productos/', include('stib-administraciones.productos.urls', namespace='productos')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ---------------
# -- flatpages --
# ---------------
urlpatterns += patterns('django.contrib.flatpages.views',
    # -- todas las flatpages
    url(r'^(?P<url>.*/)$', 'flatpage'),
    # -- pagina / , root de la pagina
    url(r'^$', 'flatpage', {'url': '/inicio/'}, name='inicio'),
)
