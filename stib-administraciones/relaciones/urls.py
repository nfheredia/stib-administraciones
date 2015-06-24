from django.conf.urls import patterns, url

from .views import EstableverTipoComunicacion

urlpatterns = patterns('stib-administraciones.productos.views',
    url(
        regex=r'^$',
        view=EstableverTipoComunicacion.as_view(),
        name='definir'
    ),
)



