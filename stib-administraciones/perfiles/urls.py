from django.conf.urls import patterns, url

from .views import PerfilesUpdateView

urlpatterns = patterns('stib-administraciones.perfiles.views',
    url(
        regex=r'^update/$',
        view=PerfilesUpdateView.as_view(),
        name='perfiles_update'
    ),
    url(
        r'^no-msg-bienvenida/$',
        'no_mostrar_msg_bienvenida',
        name='no_mostrar_msg_bienvenida'
    ),
)
