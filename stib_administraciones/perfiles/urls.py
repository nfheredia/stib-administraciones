from django.conf.urls import patterns, url

from .views import PerfilesUpdateView, get_autocomplete_nombre_comercial

urlpatterns = patterns('stib_administraciones.perfiles.views',
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
    # -- Url para auto-sugerir perfiles de usuarios no staff
    url(
        r'^autocomplete/nombre/comercial$',
        get_autocomplete_nombre_comercial,
        name='autocomplete-nombre-comercial'
    ),
)
