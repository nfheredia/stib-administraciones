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
    a usuarios adminsitraciones(no staff)
    """
    def __init__(self, *args, **kwargs):
        super(FormNotificacionesUsuarios, self).__init__(*args, **kwargs)
        self.fields['usuario'].label = 'Administraciones'
        self.fields['usuario'].queryset = get_user_model().objects.filter(is_staff=False)
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
    para el campo producto.
    - Se filtran los usuarios para mostrar solo los que NO
    son usuarios de 'staff'
    """

    class Meta:
        model = RelacionesUsuariosProductos
        fields = ('titulo', 'descripcion', 'usuario', 'producto_nombre',
                  'producto', 'tipo_relacion', 'enviado', )


class FormNotificacionUsuariosServicios(FormNotificacionesUsuarios, FormularioAutosuggestServicios):
    """
    Formulario que presentara los campos necesarios para
    enviar una notificacion a una administracion sobre un servicio.
    - Se re-arma el formulario porque se usa un auto-suggest
    para el campo servicio.
    - Se filtran los usuarios para mostrar solo los que NO
    son usuarios de 'staff'
    """

    class Meta:
        model = RelacionesUsuariosServicios
        fields = ('titulo', 'descripcion', 'usuario', 'servicio_nombre',
                  'servicio', 'tipo_relacion', 'enviado', )


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
        'enviado', )


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
        'enviado', )


class FormNotificacionesSearchMixin(forms.Form):
    """ Form base para busquedas de productos y servicios """
    ENTIDADES = (
        (0, 'Todas'),
        (1, 'Productos'),
        (2, 'Servicios'),
    )
    SI_NO = (
        (0, ""),
        (1, "Si"),
        (2, "No"),
    )
    titulo = forms.CharField(required=False, max_length=150, label="Título")
    descripcion = forms.CharField(required=False, max_length=150, label="Descripción")
    leido = forms.ChoiceField(choices=SI_NO, required=False, label="Leído")
    mail = forms.ChoiceField(choices=SI_NO, required=False, label="Mail enviado")
    fecha_desde = forms.DateField(required=False, label="Fecha Desde")
    fecha_hasta = forms.DateField(required=False, label="Fecha Hasta")
    entidades = forms.ChoiceField(required=False, choices=ENTIDADES)
    motivos = forms.ModelChoiceField(queryset=TipoRelaciones.objects.all(), required=False)
    producto_nombre = forms.CharField(max_length=150, required=False,
                                      label="Producto", help_text='Escriba el nombre del producto')
    producto = forms.CharField(widget=forms.HiddenInput)
    servicio_nombre = forms.CharField(max_length=150, required=False,
                                      label="Servicio", help_text='Escriba el nombre del servicio')
    servicio = forms.CharField(widget=forms.HiddenInput)    


class FormNotificacionesEdificiosSearch(FormNotificacionesSearchMixin):
    """
    Formulario para la búsqueda de notificaciones
    de edificios.
    """
    edificio_nombre = forms.CharField(max_length=150, required=False,
                                      label="Edificio", help_text='Escriba el nombre del edificio')
    edificio = forms.CharField(widget=forms.HiddenInput)


class FormNotificacionesAdministracionesSearch(FormNotificacionesSearchMixin):
    """
    Formulario para la búsqueda de notificaciones
    de administraciones.
    """
    usuarios = forms.ModelChoiceField(queryset=get_user_model().objects.filter(is_staff=False), required=False, label='Administraciones')


