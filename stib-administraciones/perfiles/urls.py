from django.conf.urls import patterns, url

from .views import PerfilesUpdateView

urlpatterns = patterns('',
    url(
        regex=r'^update/$',
        view=PerfilesUpdateView.as_view(),
        name='perfiles_update'
    ),
)
