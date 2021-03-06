# -*- coding: utf-8 -*-
from django.db import models

from ..core.models import TimeStampedModel, ModelStatus

from ..edificios.models import Edificios


class TipoLlaves(TimeStampedModel):
    """
    Tipo de llaves, clasificación de las llaves
    """
    nombre = models.CharField(blank=False, max_length=150, null=False, verbose_name=u"Nombre")
    comentario = models.TextField(blank=True, null=True, verbose_name=u"Comentarios")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Llaves"
        verbose_name_plural = "Tipo de Llaves"


class Llaves(TimeStampedModel, ModelStatus):
    """
    Llaves de los edificios
    """
    tipo_llave = models.ForeignKey(TipoLlaves, verbose_name=u"Tipo de llave")
    edificio = models.ForeignKey(Edificios, verbose_name=u"Edificio")

    def __unicode__(self):
        return self.edificio.nombre + " - " + self.edificio.direccion

    class Meta:
        verbose_name = "Llaves"
        verbose_name_plural = "Llaves"


