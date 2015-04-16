# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ..core.models import TimeStampedModel, ProductosSerivicios


class Productos(ProductosSerivicios):
    """
    Productos que comercializa stib
    """
    def __unicode__(self):
        """ Muestro el nombre del producto"""
        return self.nombre

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'


class ProductosFotos(TimeStampedModel):
    """
    Fotos de Productos
    """
    producto = models.ForeignKey(Productos, null=False, blank=False)

    path = ThumbnailerImageField(null=False, blank=False, upload_to="productos_fotos", verbose_name=u"Foto")

    nombre = models.CharField(blank=False, max_length=150, null=False,
                              verbose_name='Nombre',  unique=True)

    comentario = models.TextField(blank=True, verbose_name='Comentario')

    def __unicode__(self):
        return self.nombre + " (" + self.producto.nombre + ")"

    class Meta:
        verbose_name = "Fotos de productos"
        verbose_name_plural = "Fotos de productos"


