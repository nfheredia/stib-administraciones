from django import forms

from .models import Perfiles


class PerfilesForm(forms.ModelForm):
    """
    Formulario para edicion de perfiles
    """
    class Meta:
        model = Perfiles
        exclude = ['user', 'alerta_bienvenida']
