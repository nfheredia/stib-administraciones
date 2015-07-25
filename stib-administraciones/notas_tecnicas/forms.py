# -*- coding: utf-8 -*-
from django import forms
from .models import NotasTecnicas


class NotasTecnicasCreateForm(forms.ModelForm):
    """
    Formulario para el envío de
    nuevas Notas Técnicas
    """
    def __init__(self, *args, **kwargs):
        super(NotasTecnicasCreateForm, self).__init__( *args, **kwargs)
        self.fields['mail_recibido'].help_text = "ATENCIÓN: Se enviará el mail si la administración " \
                                                 "tiene configurado su dirección de correo"

    class Meta:
        model = NotasTecnicas
        fields = ('titulo', 'descripcion', 'edificio','forma_pago',
                  'validez_oferta', 'condicion_iva', 'precio', 'estado',
                  'mail_recibido')