from django.conf.urls import patterns, url
from .views import FeedbacksCreate

urlpatterns = patterns('stib-administraciones.stib-administraciones.feedbacks.views',
                       url(r'^create/$', FeedbacksCreate.as_view(), name="feedback_create"),
                       )
