from django import forms
from .models import TipoLlaves


class TipoLlavesForm(forms.Form):
    """
    Formulario que descpliega con checkboxes
    todos los tipos de llaves que existen
    """
    def __init__(self,  *args, **kwargs):
        super(TipoLlavesForm, self).__init__(*args, **kwargs)
        tipo_llaves = TipoLlaves.objects.values_list('id', 'nombre').all()
        self.fields['tipo_llaves'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                               choices=tipo_llaves,
                                                               initial=kwargs['initial'] if 'initial' in kwargs else {},
                                                               label="")

