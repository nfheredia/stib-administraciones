from django.conf.urls import patterns, url
from .view import post_comment

urlpatterns = patterns('stib-administraciones.custom_comments.views',

    url(
        r'^envio/$',
        post_comment,
        name='envio'
    ),
)

