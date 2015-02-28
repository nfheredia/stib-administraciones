# -*- coding: utf-8 -*-
from django.db import models
from model_utils import Choices
from easy_thumbnails.fields import ThumbnailerImageField
from ..core.models import TimeStampedModel


class Productos(TimeStampedModel):
        """
        Productos que comercializa stib
        """
        VALIDEZ_OFERTA = Choices(
            (10, '10', '10'),
            (20, '20', '20'),
            (30, '30', '30'),
            (60, '60', '60'),
        )

        CONDICION_IVA = Choices(
            (1, 'INCLUIDO', 'Incluido'),
            (2, 'NO_INCLUIDO', 'No Incluido'),
        )

        nombre = models.CharField(blank=False, max_length=150, null=False,
                                  verbose_name='Nombre',  unique=True)

        descripcion = models.TextField(blank=True, verbose_name='Descripción')

        forma_pago = models.CharField(blank=False, max_length=150, null=False,
                                      verbose_name='Forma de pago')

        validez_oferta = models.IntegerField(choices=VALIDEZ_OFERTA, blank=False, null=False,
                                             verbose_name="Validez Oferta")

        condicion_iva = models.IntegerField(choices=CONDICION_IVA, blank=False, null=False,
                                            verbose_name="Iva")

        precio = models.FloatField(blank=False, null=False, verbose_name="Precio")

        def __str__(self):
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

    def __str__(self):
        return self.nombre + " (" + self.producto.nombre + ")"

    class Meta:
        verbose_name = "Fotos de productos"
        verbose_name_plural = "Fotos de productos"


