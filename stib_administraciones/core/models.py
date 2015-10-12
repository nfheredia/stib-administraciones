# -*- coding: utf-8 -*-
from django.db import models
from model_utils import Choices
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager


class TimeStampedModel(models.Model):
    modificado = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ModelStatus(models.Model):
    _status = 'edited'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            self._status = 'new'
        super(ModelStatus, self).save(force_insert=False, force_update=False, using=None,
                                      update_fields=None)

    def delete(self, using=None):
        self._status = 'deleted'
        super(ModelStatus, self).delete(using=None)

    @property
    def get_status(self):
        return self._status

    class Meta:
        abstract = True


class ProductosSerivicios(TimeStampedModel):
    """
    Clase abstracta para productos y servicios
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

    tags = TaggableManager(blank=True, verbose_name="Etiquetas")

    image = ThumbnailerImageField(blank=True, null=True,
                                  verbose_name="Imágen principal",
                                  upload_to=u"productos_servicios_fotos_principal")

    class Meta:
        abstract = True

