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
    # -- comments
    url(r'^comments/', include("django.contrib.comments.urls")),
    # -- custom comments
    url(r'^custom-comments/', include('stib_administraciones.custom_comments.urls', namespace="custom-comments")),
    # -- usuarios
    url(r'^users/', include("stib_administraciones.users.urls", namespace="users")),
    # -- accounts apps
    url(r'^accounts/', include('allauth.urls')),
    # -- perfiles
    url(r'^perfiles/', include('stib_administraciones.perfiles.urls', namespace='perfiles')),
    # -- imperavi editor
    url(r'^imperavi/', include('imperavi.urls')),
    # -- feedbacks
    url(r'^feedbacks/', include('stib_administraciones.feedbacks.urls')),
    # -- novedades
    url(r'^novedades/', include('stib_administraciones.novedades.urls', namespace='novedades')),
    # -- edificios
    url(r'^edificios/', include('stib_administraciones.edificios.urls', namespace='edificios')),
    # -- fotos
    url(r'^fotos/', include('stib_administraciones.fotos.urls', namespace='fotos')),
    # -- productos
    url(r'^productos/', include('stib_administraciones.productos.urls', namespace='productos')),
    # -- servicios
    url(r'^servicios/', include('stib_administraciones.servicios.urls', namespace='servicios')),
    # -- contactos
    url(r'^contactos/', include('stib_administraciones.contactos.urls', namespace='contactos')),
    # -- horarios
    url(r'^horarios/', include('stib_administraciones.horarios.urls', namespace='horarios')),
    # -- llaves
    url(r'^llaves/', include('stib_administraciones.llaves.urls', namespace='llaves')),
    # -- comunicacion/notificaciones
    url(r'^notificaciones/', include('stib_administraciones.relaciones.urls', namespace='notificaciones')),
    # -- notas técnicas
    url(r'^notas/tecnicas/', include('stib_administraciones.notas_tecnicas.urls', namespace='notas-tecnicas')),
    # -- dashboard
    url(r'^dashboard/', include('stib_administraciones.dashboard.urls', namespace='dashboard')),

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
