# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from .models import RelacionesUsuariosProductos


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


class FormNotificacionUsuariosProductos(forms.ModelForm):
    """
    Formulario que presentara los campos necesario para
    enviar una notificacion a una administracion sobre un producto.
    - Se re-arma el formulario porque se usa una auto-suggest
    para el campo producto.
    - Se filtran los usuarios para mostrar solo los que no
    son usuarios de 'staff'
    """
    producto_nombre = forms.CharField(max_length=150, required=True)

    class Meta:
        model = RelacionesUsuariosProductos
        fields = ('titulo', 'descripcion', 'usuario', 'producto_nombre',
                  'producto', 'tipo_relacion', 'enviado', )

    def __init__(self, *args, **kwargs):
        super(FormNotificacionUsuariosProductos, self).__init__(*args, **kwargs)
        self.fields['producto_nombre'].label = 'Nombre del producto'
        self.fields['producto_nombre'].help_text = 'Escriba el nombre del producto'
        self.fields['producto'].widget = forms.HiddenInput()
        self.fields['usuario'].label = 'Administraciones'
        self.fields['usuario'].queryset = get_user_model().objects.filter(is_staff=False)


