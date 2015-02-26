# -*- coding: utf-8 -*-

from django.db import models

from ..core.models import TimeStampedModel

from ..edificios.models import Edificios


class CategoriasFotos(TimeStampedModel):
    """
    Categorías de las fotos de los edificios
    """
    nombre = models.CharField(blank=False, max_length=150, null=False, verbose_name=u"Nombre")
    comentario = models.TextField(blank=True, null=True, verbose_name=u"Comentarios")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categorías de Fotos"
        verbose_name_plural = "Categorías de Fotos"
