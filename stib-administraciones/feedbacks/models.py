# -*- coding: utf-8 -*-
from django.db import models

from ..settings import AUTH_USER_MODEL

from ..core.models import TimeStampedModel

class TipoFeedbacks(TimeStampedModel):
    """
    Tipo / Clasificación de feedbacks, ejemplo: sugerencia, comentario, error
    """
    nombre = models.CharField(blank=False, null=False, max_length=150)
    descripcion = models.TextField(blank=True, null=True, verbose_name=u"Descripción")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de feedbacks'
        verbose_name_plural = 'Tipo de feedbacks'


class Feedbacks(TimeStampedModel):
    """
    Feedbacks que dejan las administraciones
    """
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=u"Usuario")
    tipo_feedback = models.ForeignKey(TipoFeedbacks, blank=False, null=False,
                                      verbose_name=u"Categoría")
    asunto = models.CharField(blank=False, null=False, max_length=300, verbose_name=u"Asunto")
    mensaje = models.TextField(blank=False, null=False, verbose_name=u"Mensaje")

    def __unicode__(self):
        return self.asunto

    class Meta:
        verbose_name = 'Feedbacks'
        verbose_name_plural = 'Feedbacks'


