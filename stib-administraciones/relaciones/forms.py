# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from .models import RelacionesUsuariosProductos, RelacionesUsuariosServicios, RelacionesEdificiosProductos, \
    RelacionesEdificiosServicios, TipoRelaciones


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
                                   label='A quién va dirigida tu notificación?', )
    entidad = forms.CharField(widget=forms.Select(choices=ENTIDADES),
                              required=True,
                              label='Que deseas comunicar?', )


class FormNotificacionesUsuarios(forms.ModelForm):
    """
    Formulario base para el envio de notificaciones
    a usuarios adminsitraciones(no staff).
    Va a tener un campo (administracion_nombre_comercial) que será
    un auto-suggest
    """
    administracion_nombre_comercial = forms.CharField(max_length=150, required=True)

    def __init__(self, *args, **kwargs):
        super(FormNotificacionesUsuarios, self).__init__(*args, **kwargs)
        self.fields['administracion_nombre_comercial'].label = 'Administración'
        self.fields['administracion_nombre_comercial'].help_text = 'Escriba el nombre de la administración'
        self.fields['usuario'].widget = forms.HiddenInput()
        self.fields['tipo_relacion'].label = 'Motivos de tu notificacion'


class FormularioAutosuggestEdificios(forms.ModelForm):
    """ Form para el autosuggest de edificios """

    edificio_nombre = forms.CharField(max_length=150, required=True)

    def __init__(self, *args, **kwargs):
        super(FormularioAutosuggestEdificios, self).__init__(*args, **kwargs)
        self.fields['edificio_nombre'].label = 'Edificio'
        self.fields['edificio_nombre'].help_text = 'Escriba el nombre o dirección del edificio'
        self.fields['edificio'].widget = forms.HiddenInput()
        self.fields['tipo_relacion'].label = 'Motivos de tu notificación'


class FormularioAutosuggestProductos(forms.ModelForm):
    """ Form para el autosuggest de productos """

    producto_nombre = forms.CharField(max_length=150, required=True)

    def __init__(self, *args, **kwargs):
        super(FormularioAutosuggestProductos, self).__init__(*args, **kwargs)
        self.fields['producto_nombre'].label = 'Nombre del producto'
        self.fields['producto_nombre'].help_text = 'Escriba el nombre del producto'
        self.fields['producto'].widget = forms.HiddenInput()


class FormularioAutosuggestServicios(forms.ModelForm):
    """ Form para el autosuggest de servicios """

    servicio_nombre = forms.CharField(max_length=150, required=True)

    def __init__(self, *args, **kwargs):
        super(FormularioAutosuggestServicios, self).__init__(*args, **kwargs)
        self.fields['servicio_nombre'].label = 'Nombre del servicio'
        self.fields['servicio_nombre'].help_text = 'Escriba el nombre del servicio'
        self.fields['servicio'].widget = forms.HiddenInput()


class FormNotificacionUsuariosProductos(FormNotificacionesUsuarios, FormularioAutosuggestProductos):
    """
    Formulario que presentara los campos necesarios para
    enviar una notificacion a una administracion sobre un producto.
    - Se re-arma el formulario porque se usa un auto-suggest
    para el campo producto y administraciones.
    """

    class Meta:
        model = RelacionesUsuariosProductos
        fields = ('titulo', 'descripcion', 'administracion_nombre_comercial', 'usuario',
                  'producto_nombre', 'producto', 'tipo_relacion', 'estado', 'enviado', )


class FormNotificacionUsuariosServicios(FormNotificacionesUsuarios, FormularioAutosuggestServicios):
    """
    Formulario que presentara los campos necesarios para
    enviar una notificacion a una administracion sobre un servicio.
    - Se re-arma el formulario porque se usa un auto-suggest
    para el campo servicio y administraciones.
    """

    class Meta:
        model = RelacionesUsuariosServicios
        fields = ('titulo', 'descripcion', 'administracion_nombre_comercial', 'usuario',
                  'servicio_nombre', 'servicio', 'tipo_relacion', 'estado', 'enviado', )


class FormNotificacionEdificiosProductos(FormularioAutosuggestEdificios, FormularioAutosuggestProductos):
    """
    Formulario que permitira enviar notificaciones de productos
    para un determinado edificio.
    Tiene auto-suggest en los campos de productos y edificios.
    """

    class Meta:
        model = RelacionesEdificiosProductos
        fields = (
        'titulo', 'descripcion', 'edificio', 'edificio_nombre', 'producto_nombre', 'producto', 'tipo_relacion',
        'estado', 'enviado', )


class FormNotificacionEdificiosServicios(FormularioAutosuggestEdificios, FormularioAutosuggestServicios):
    """
    Formulario que permitira enviar notificaciones de servicios
    para un determinado edificio.
    Tiene auto-suggest en los campos de servicios y edificios.
    """

    class Meta:
        model = RelacionesEdificiosServicios
        fields = (
        'titulo', 'descripcion', 'edificio', 'edificio_nombre', 'servicio_nombre', 'servicio', 'tipo_relacion',
        'estado', 'enviado', )


class FormNotificacionesSearchMixin(forms.Form):
    """ Form base para busquedas de productos y servicios """
    ENTIDADES = (
        (0, 'Todas'),
        (1, 'Productos'),
        (2, 'Servicios'),
    )
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
    entidades = forms.ChoiceField(required=False, choices=ENTIDADES,
                                  help_text='Sobre que entidades se realizará la búsqueda')
    motivos = forms.ModelChoiceField(queryset=TipoRelaciones.objects.all(), required=False)
    producto_nombre = forms.CharField(max_length=150, required=False,
                                      label="Producto", help_text='Escriba el nombre del producto')
    producto = forms.CharField(widget=forms.HiddenInput, required=False)
    servicio_nombre = forms.CharField(max_length=150, required=False,
                                      label="Servicio", help_text='Escriba el nombre del servicio')
    servicio = forms.CharField(widget=forms.HiddenInput, required=False)
    mail_recibido = forms.ChoiceField(choices=SI_NO, required=False, label="Mail recibido")
    estado = forms.ChoiceField(choices=ESTADOS, required=False, label="Estado")

    def clean(self):
        cleaned_data = super(FormNotificacionesSearchMixin, self).clean()
        # -- fecha desde/hasta correctas??
        fecha_desde = cleaned_data.get("fecha_desde")
        fecha_hasta = cleaned_data.get("fecha_hasta")
        if fecha_desde is not None and fecha_hasta is None:
            msg = "Debes ingresar una fecha"
            self._errors['fecha_hasta'] = [msg]
        if fecha_hasta is not None and fecha_desde is None:
            msg = "Debes ingresar una fecha"
            self._errors['fecha_desde'] = [msg]
        if fecha_desde is not None and fecha_hasta is not None:
            if fecha_desde > fecha_hasta:
                msg = "La 'fecha desde' debe ser menos a la 'fecha hasta'"
                self._errors['fecha_desde'] = [msg]
                self._errors['fecha_hasta'] = [msg]
        # -- / fecha desde/hasta correctas??
        return cleaned_data


class FormNotificacionesEdificiosSearch(FormNotificacionesSearchMixin):
    """
    Formulario para la búsqueda de notificaciones
    de edificios.
    """
    edificio_nombre = forms.CharField(max_length=150, required=False,
                                      label="Edificio", help_text='Escriba el nombre del edificio')
    edificio = forms.CharField(widget=forms.HiddenInput, required=False)


class FormNotificacionesAdministracionesSearch(FormNotificacionesSearchMixin):
    """
    Formulario para la búsqueda de notificaciones
    de administraciones.
    """
    administracion_nombre_comercial = forms.CharField(max_length=150, required=True,
                                                      label='Administración',
                                                      help_text='Escriba el nombre de la administración')
    usuario = forms.CharField(widget=forms.HiddenInput, required=False)



