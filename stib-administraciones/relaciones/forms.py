# -*- coding: utf-8 -*-
from django import forms


class FormDefinirTipoComunicacion(forms.Form):
    """
    Formulario que presentará los diferntes
    medios para establecer una comunicacion (envio
    de notificaciones) epara los diferentes 'destinatarios
    y las diferentes entidades
    """
    DESTINATARIOS = (
        ('edificios', 'Edificios'),
        ('administraciones', 'Administraciones')
    )
    ENTIDADES = (
        ('productos', 'Productos'),
        ('servicios', 'Servicios')
    )

    destinatario = forms.CharField(widget=forms.Select(choices=DESTINATARIOS),
                                   required=True,
                                   label='A quién va dirigida tu notificación?',)
    entidad = forms.CharField(widget=forms.Select(choices=ENTIDADES),
                              required=True,
                              label='Que deseas comunicar?',)
