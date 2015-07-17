# -*- coding: utf-8 -*-
from django import forms
from .models import Edificios


class FormSearch(forms.ModelForm):
    """
    Formulario que se utiliza para realizar
    busquedas de edificios
    """
    def __init__(self, *args, **kwargs):
        super(FormSearch, self).__init__(*args, **kwargs)
        self.fields['comentario'].widget = forms.CharField
        self.fields['comentario'].help_text = 'Encuentra una palabra en el comentario'
        self.fields['comentario'].label = "Comentario"
        self.fields['nombre'].required = False
        self.fields['direccion'].required = False
        self.fields['codigo'].required = False

    class Meta:
        model = Edificios
        fields = ['nombre', 'direccion', 'codigo', 'comentario']

