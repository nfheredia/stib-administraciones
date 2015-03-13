# -*- coding: utf-8 -*-
from django.db import models

from ..settings import AUTH_USER_MODEL

from ..core.models import TimeStampedModel


class Perfiles(TimeStampedModel):
    """
    Perfiles de los usuarios.
    Para agregar informacion extra al modelo por defecto.
    """
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=u"Usuario", unique=True)
    nombre = models.CharField(blank=False, max_length=150, verbose_name=u"Nombre")
    telefono_fijo = models.CharField(blank=True, max_length=15, null=True, verbose_name=u"Teléfono Fijo")
    telefono_emergencia = models.CharField(blank=True, max_length=15, null=True, verbose_name=u"Teléfono de emergencia")
    email_1 = models.EmailField(blank=False, verbose_name=u"Email")
    email_2 = models.EmailField(blank=True, null=True, verbose_name=u"Otro Email")
    direccion_oficina = models.CharField(blank=False, max_length=150, verbose_name=u"Dirección de la oficina")
    direccion_alternativa = models.CharField(blank=True, max_length=150, null=True, verbose_name=u"Dirección alternativa")
    alerta_bienvenida = models.BooleanField(default=True, verbose_name=u"Mostrar alerta de bienvenida",
                                            help_text=u"Este campo se utiliza para advertile al usuario que edite su perfil cuando ingresa por primera vez")

    def __unicode__(self):
        """ Muestro el nombre, sirve para el sitio de admin """
        return self.nombre

    @classmethod
    def mostrar_mensaje_bienvenida(cls, user_id):
        return cls.objects.filter(user=user_id).get()

    class Meta:
        verbose_name = 'Perfiles'
        verbose_name_plural = 'Perfiles'
