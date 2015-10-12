from django import forms


class FormConsulta(forms.Form):
    """
    Formulario para realizar consultas sobre productos
    """
    consulta = forms.CharField(widget=forms.Textarea, label='', required=True)