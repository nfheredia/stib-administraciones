# -*- coding: utf-8 -*-

from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from ..core.models import TimeStampedModel

from ..edificios.models import Edificios


class CategoriasFotos(TimeStampedModel):
    """
    Categorías de las fotos de los edificios
    """
    nombre = models.CharField(blank=False, max_length=150, null=False, verbose_name=u"Nombre")
    comentario = models.TextField(blank=True, null=True, verbose_name=u"Comentarios")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categorías de Fotos"
        verbose_name_plural = "Categorías de Fotos"


class Fotos(TimeStampedModel):
    """
    Fotos de los edificios
    """
    edificio = models.ForeignKey(Edificios, verbose_name=u"Edificio")
    categoria = models.ForeignKey(CategoriasFotos, verbose_name=u"Categoría")
    nombre = models.CharField(blank=False, max_length=150, null=False, verbose_name=u"Nombre")
    comentario = models.TextField(blank=True, null=True, verbose_name=u"Comentarios")
    path = ThumbnailerImageField(null=False, blank=False, upload_to="edificios_fotos", verbose_name=u"Foto")

    def __unicode__(self):
        return self.nombre + " (" + self.edificio.nombre + " - " + self.edificio.direccion + ")"

    class Meta:
        verbose_name = "Fotos"
        verbose_name_plural = "Fotos"

