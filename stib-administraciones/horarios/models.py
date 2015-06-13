# -*- coding: utf-8 -*-
from django.db import models

from ..core.models import TimeStampedModel

from ..edificios.models import Edificios
from ..personales.models import Personales


class Horarios(TimeStampedModel):
    """
    Modelo para registrar el horario de entrada
    a los diferentes edificios y vincularlos con
    el personal
    """
    edificio = models.ForeignKey(Edificios, verbose_name='Edificio')
    personales = models.ForeignKey(Personales, verbose_name='Personal')
    lunes = models.BooleanField(default=False, verbose_name='Lunes')
    martes = models.BooleanField(default=False, verbose_name='Martes')
    miercoles = models.BooleanField(default=False, verbose_name='Miércoles')
    jueves = models.BooleanField(default=False, verbose_name='Jueves')
    viernes = models.BooleanField(default=False, verbose_name='Viernes')
    sabado = models.BooleanField(default=False, verbose_name='Sábado')
    domingo = models.BooleanField(default=False, verbose_name='Domingo')
    hora_desde = models.TimeField(blank=False, null=False)
    hora_hasta = models.TimeField(blank=False, null=False)

    _status = 'edited'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            self._status = 'new'
        super(Horarios, self).save(force_insert=False, force_update=False, using=None,
                                   update_fields=None)

    def delete(self, using=None):
        self._status = 'deleted'
        super(Horarios, self).delete(using=None)

    @property
    def get_status(self):
        return self._status

    def __unicode__(self):
        return self.edificio.nombre

    class Meta:
        verbose_name = 'Horarios'
        verbose_name_plural = 'Horarios'



