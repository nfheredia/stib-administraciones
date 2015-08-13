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


class NotasTecnicasSearchForm(forms.Form):
    """ Formulario para la búsqueda de Notas tecnicas """
    SI_NO = (
        ('', "-------"),
        (1, "Si"),
        (2, "No"),
    )
    ESTADOS = (
        ('', '-------'),
        (1, 'Nuevo'),
        (2, 'Aceptado'),
        (3, 'Pendiente'),
        (4, 'Cancelado'),
    )

    titulo = forms.CharField(required=False, max_length=150, label="Título")
    descripcion = forms.CharField(required=False, max_length=150, label="Descripción")
    leido = forms.ChoiceField(choices=SI_NO, required=False, label="Leído")
    mail = forms.ChoiceField(choices=SI_NO, required=False, label="Mail enviado")
    fecha_desde = forms.DateField(required=False, label="Fecha Desde",
                                  input_formats=['%d/%m/%Y'],
                                  help_text='Formato: dd/mm/yyyy')
    fecha_hasta = forms.DateField(required=False, label="Fecha Hasta",
                                  input_formats=['%d/%m/%Y'],
                                  help_text='Formato: dd/mm/yyyy')
    mail_recibido = forms.ChoiceField(choices=SI_NO, required=False, label="Mail recibido")
    estado = forms.ChoiceField(choices=ESTADOS, required=False, label="Estado")
    edificio_nombre = forms.CharField(max_length=150, required=False,
                                      label="Edificio", help_text='Escriba el nombre del edificio')
    edificio = forms.CharField(widget=forms.HiddenInput, required=False)