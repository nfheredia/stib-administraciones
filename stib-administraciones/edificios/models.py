# -*- coding: utf-8 -*-
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from ..settings import AUTH_USER_MODEL

from ..core.models import TimeStampedModel


class Edificios(TimeStampedModel):
    """
    Edificios, los mismos pertenecen a las diferentes
    administraciones/usuarios
    """
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=u"Usuario",
                             help_text="Administración a la cual pertenece el edificio")
    nombre = models.CharField(blank=False, max_length=150, verbose_name=u"Nombre del edificio")
    codigo = models.CharField(blank=False, max_length=150, verbose_name=u"Código")
    direccion = models.CharField(blank=False, max_length=150, verbose_name=u"Dirección")
    foto_fachada = ThumbnailerImageField(null=True, blank=True, upload_to='edificios_fachadas', verbose_name=u"Imágen de fachada")
    cantidad_pisos = models.IntegerField(blank=True, null=True, max_length=2, verbose_name=u"Cantidad de pisos")
    cantidad_unidades = models.IntegerField(blank=True, null=True, max_length=2,  verbose_name=u"Cantidad de unidades")
    comentario = models.TextField(blank=True, null=True, verbose_name=u"Comentarios")

    def __str__(self):
        return self.nombre + ' - ' + self.direccion

    class Meta:
        verbose_name = 'Edificios'
        verbose_name_plural = 'Edificios'
