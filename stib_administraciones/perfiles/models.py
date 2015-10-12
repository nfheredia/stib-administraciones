# -*- coding: utf-8 -*-
from django.db import models

from ..core.models import TimeStampedModel

from ..users.models import User


class Perfiles(TimeStampedModel):
    """
    Perfiles de los usuarios.
    Para agregar informacion extra al modelo por defecto.
    """
    user = models.OneToOneField(User, related_name="perfil")
    nombre = models.CharField(blank=False, max_length=150, verbose_name=u"Nombre")
    nombre_comercial = models.CharField(blank=False, max_length=150, verbose_name=u"Nombre Comercial",
                                        help_text=u"Nombre de la administración que solo STIB utilizará.")
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
    def obtener_mail_por_usuario(clas, user_id):
        """
        obtenemos el mail del usuario que
        se pasa como parámetro
        """
        result = clas.objects.values('email_1').get(user=user_id)
        return result['email_1']

    class Meta:
        verbose_name = 'Perfiles'
        verbose_name_plural = 'Perfiles'
