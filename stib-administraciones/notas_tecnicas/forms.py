# -*- coding: utf-8 -*-
from django import forms
from .models import NotasTecnicas


class NotasTecnicasCreateForm(forms.ModelForm):
    """
    Formulario para el envío de
    nuevas Notas Técnicas
    """
    edificio_nombre = forms.CharField(max_length=150, required=True)
    def __init__(self, *args, **kwargs):
        super(NotasTecnicasCreateForm, self).__init__( *args, **kwargs)
        self.fields['edificio_nombre'].label = 'Edificio'
        self.fields['edificio_nombre'].help_text = 'Escriba el nombre o dirección del edificio'
        self.fields['edificio'].widget = forms.HiddenInput()
        self.fields['enviado'].label = "Enviar notificación por email"
        self.fields['enviado'].help_text = "ATENCIÓN: Se enviará el mail si la administración " \
                                                 "tiene configurado su dirección de correo"

    class Meta:
        model = NotasTecnicas
        fields = ('titulo', 'descripcion', 'edificio_nombre', 'edificio','forma_pago',
                  'validez_oferta', 'condicion_iva', 'precio', 'estado',
                  'enviado')