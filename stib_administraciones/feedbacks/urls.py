from django.conf.urls import patterns, url
from .views import FeedbacksCreate

urlpatterns = patterns('stib_administraciones.stib_administraciones.feedbacks.views',
                       url(r'^create/$', FeedbacksCreate.as_view(), name="feedback_create"),
                       )
