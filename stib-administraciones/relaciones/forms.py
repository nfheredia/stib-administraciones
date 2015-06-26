# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from .models import RelacionesUsuariosProductos, RelacionesUsuariosServicios


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


class FormNotificacionesUsuarios(forms.ModelForm):
    """
    Formulario base para el envio de notificaciones
    a usuarios adminsitraciones(no staff)
    """
    def __init__(self, *args, **kwargs):
        super(FormNotificacionesUsuarios, self).__init__(*args, **kwargs)
        self.fields['usuario'].label = 'Administraciones'
        self.fields['usuario'].queryset = get_user_model().objects.filter(is_staff=False)
        self.fields['tipo_relacion'].label = 'Motivos de tu notificacion'


class FormNotificacionUsuariosProductos(FormNotificacionesUsuarios):
    """
    Formulario que presentara los campos necesarios para
    enviar una notificacion a una administracion sobre un producto.
    - Se re-arma el formulario porque se usa un auto-suggest
    para el campo producto.
    - Se filtran los usuarios para mostrar solo los que NO
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


class FormNotificacionUsuariosServicios(FormNotificacionesUsuarios):
    """
    Formulario que presentara los campos necesarios para
    enviar una notificacion a una administracion sobre un servicio.
    - Se re-arma el formulario porque se usa un auto-suggest
    para el campo servicio.
    - Se filtran los usuarios para mostrar solo los que NO
    son usuarios de 'staff'
    """
    servicio_nombre = forms.CharField(max_length=150, required=True)

    class Meta:
        model = RelacionesUsuariosServicios
        fields = ('titulo', 'descripcion', 'usuario', 'servicio_nombre',
                  'servicio', 'tipo_relacion', 'enviado', )

    def __init__(self, *args, **kwargs):
        super(FormNotificacionUsuariosServicios, self).__init__(*args, **kwargs)
        self.fields['servicio_nombre'].label = 'Nombre del servicio'
        self.fields['servicio_nombre'].help_text = 'Escriba el nombre del servicio'
        self.fields['servicio'].widget = forms.HiddenInput()


