from django import forms


class FormConsulta(forms.Form):
    """
    Formulario para realizar consultas sobre servicios
    """
    consulta = forms.CharField(widget=forms.Textarea, label='', required=True)