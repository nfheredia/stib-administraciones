# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel
from ..users.models import User
from ..edificios.models import Edificios
from ..productos.models import Productos
from ..servicios.models import Servicios


class Relaciones(TimeStampedModel):
    """
    Modelo abstracto, reusable
    """

    ESTADOS = (
        (1, 'Nuevo'),
        (2, 'Aceptado'),
        (3, 'Pendiente'),
        (4, 'Cancelado'),
    )

    titulo = models.CharField(blank=False, max_length=150, null=False,
                              verbose_name='Título')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    leido = models.BooleanField(verbose_name="Leido", default=False)
    enviado = models.BooleanField(verbose_name="Enviar por email?",
                                  default=False,
                                  help_text='ATENCIÓN: Se enviará el mail si la '
                                            'administración tiene configurado su dirección'
                                            'de correo')
    mail_recibido = models.BooleanField(default=False)
    estado = models.IntegerField(choices=ESTADOS, default=1, blank=False, null=False,
                                 help_text="Indica el estado que se encuentra una notificación.")

    class Meta:
        abstract = True

    @classmethod
    def cambiar_estado(cls, pk, estado):
        """ Marcar la nota tecnica como leida """
        obj = cls.objects.get(pk=pk)
        obj.estado = estado
        obj.save()

    @classmethod
    def marcar_leido(cls, pk):
        """ Marcar como leida """
        obj = cls.objects.get(pk=pk)
        obj.leido = 1
        obj.save()

    @classmethod
    def marcar_email_recibido(cls, pk):
        """ Marcar la notificacion con 'email recibido' """
        obj = cls.objects.get(pk=pk)
        obj.mail_recibido = 1
        obj.save()


class TipoRelaciones(TimeStampedModel):
    """
    Tipo de relaciones que se establecen con las administracions, ej:
    novedades, sugerencias, notas técnicas
    """
    nombre = models.CharField(blank=False, max_length=150, null=False,
                              verbose_name=u"Nombre")
    comentario = models.TextField(blank=True, verbose_name=u"Comentario")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de relaciones"
        verbose_name_plural = "Tipo de relaciones"


class RelacionesUsuariosProductos(Relaciones):
    tipo_relacion = models.ForeignKey(TipoRelaciones, blank=False, null=False,
                                      verbose_name="Tipo de relación")
    usuario = models.ForeignKey(User, blank=False, null=False,
                                verbose_name="Usuario")
    producto = models.ForeignKey(Productos, null=False,
                                 verbose_name="Producto")

    class Meta:
        verbose_name = "Relaciones usuarios productos"
        verbose_name_plural = "Relaciones usuarios productos"


class RelacionesUsuariosServicios(Relaciones):
    tipo_relacion = models.ForeignKey(TipoRelaciones, blank=False, null=False,
                                      verbose_name="Tipo de relación")
    usuario = models.ForeignKey(User, blank=False, null=False,
                                verbose_name="Usuario")
    servicio = models.ForeignKey(Servicios, blank=False, null=False,
                                 verbose_name="Servicio")

    class Meta:
        verbose_name = "Relaciones usuarios servicios"
        verbose_name_plural = "Relaciones usuarios servicios"


class RelacionesEdificiosProductos(Relaciones):
    tipo_relacion = models.ForeignKey(TipoRelaciones, blank=False, null=False,
                                      verbose_name="Tipo de relación")
    edificio = models.ForeignKey(Edificios, blank=False, null=False,
                                 verbose_name="Edificio")
    producto = models.ForeignKey(Productos, null=False,
                                 verbose_name="Producto")

    class Meta:
        verbose_name = "Relaciones edificios productos"
        verbose_name_plural = "Relaciones edificios productos"


class RelacionesEdificiosServicios(Relaciones):
    tipo_relacion = models.ForeignKey(TipoRelaciones, blank=False, null=False,
                                      verbose_name="Tipo de relación")
    edificio = models.ForeignKey(Edificios, blank=False, null=False,
                                 verbose_name="Edificio")
    servicio = models.ForeignKey(Servicios, null=False,
                                 verbose_name="Servicio")

    class Meta:
        verbose_name = "Relaciones edificios servicios"
        verbose_name_plural = "Relaciones edificios servicios"