# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel
from ..edificios.models import Edificios


class NotasTecnicas(TimeStampedModel):
    """
    Notas técnicas para los edificios
    """
    ESTADOS = (
        (1, 'Nuevo'),
        (2, 'Aceptado'),
        (3, 'Pendiente'),
        (4, 'Cancelado'),
    )
    VALIDEZ_OFERTA = (
        (10, '10'),
        (20, '20'),
        (30, '30'),
        (60, '60'),
    )
    CONDICION_IVA = (
        (1, 'Incluido'),
        (2, 'No Incluido'),
    )

    edificio = models.ForeignKey(Edificios, blank=False, null=False)
    titulo = models.CharField(max_length=150, blank=False, null=False,
                              verbose_name='Título')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    enviado = models.BooleanField(default=False)
    mail_recibido = models.BooleanField(default=False)
    leido = models.BooleanField(verbose_name="Leido", default=False)
    estado = models.IntegerField(choices=ESTADOS, default=1, blank=False, null=False,
                                 help_text="Indica el estado que se encuentra la nota técnica.")
    forma_pago = models.CharField(blank=True, max_length=150, null=True,
                                  verbose_name='Forma de pago')
    validez_oferta = models.IntegerField(choices=VALIDEZ_OFERTA, blank=True, null=True,
                                         verbose_name="Validez Oferta")
    condicion_iva = models.IntegerField(choices=CONDICION_IVA, blank=True, null=True,
                                        verbose_name="Iva")
    precio = models.FloatField(blank=False, null=False, verbose_name="Precio", default='0.00')
    trabajo_realizado = models.BooleanField(verbose_name="Trabajo realizado", default=False)

    class Meta:
        ordering = ['-creado']

    @classmethod
    def marcar_leido(cls, pk):
        """ Marcar la nota tecnica como leida """
        obj = cls.objects.get(pk=pk)
        obj.leido = 1
        obj.save()

    @classmethod
    def marcar_email_recibido(cls, pk):
        """ Marcar la nota tecnica con 'email recibido' """
        obj = cls.objects.get(pk=pk)
        obj.mail_recibido = 1
        obj.save()

    @classmethod
    def marcar_trabajo_realizado(cls, pk):
        """ Marcar la nota tecnica como trabajo realizado """
        obj = cls.objects.get(pk=pk)
        obj.trabajo_realizado = 1
        obj.save()


