# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ..core.models import TimeStampedModel, ProductosSerivicios


class Servicios(ProductosSerivicios):
    """
    Servicios que comercializa stib
    """
    def __unicode__(self):
        """ Muestro el nombre del servicio"""
        return self.nombre

    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'
        ordering = ['-creado']


class ServiciosFotos(TimeStampedModel):
    """
    Fotos de Servicios
    """
    servicio = models.ForeignKey(Servicios, null=False, blank=False)

    path = ThumbnailerImageField(null=False, blank=False, upload_to=u"servicios_fotos", verbose_name=u"Foto")

    nombre = models.CharField(blank=False, max_length=150, null=False,
                              verbose_name=u'Nombre',  unique=True)

    comentario = models.TextField(blank=True, verbose_name=u'Comentario')

    def __unicode__(self):
        return self.nombre + " (" + self.servicio.nombre + ")"

    class Meta:
        verbose_name = "Fotos de servicios"
        verbose_name_plural = "Fotos de servicios"



