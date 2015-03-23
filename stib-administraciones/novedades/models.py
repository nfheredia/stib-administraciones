# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from ..core.models import TimeStampedModel
from ..users.models import User


class Novedades(TimeStampedModel):
    """
    Novedades generales para todas las administraciones
    """
    titulo = models.CharField(max_length=255, verbose_name=u'Título')
    contenido = models.TextField(verbose_name=u'Contenido')
    user = models.ForeignKey(User, verbose_name=u'Creador')
    tags = TaggableManager(verbose_name=u'Etiquetas', blank=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ['creado']