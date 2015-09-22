# -*- coding: utf-8 -*-
from django import template
from ..models import RelacionesEdificiosServicios, RelacionesEdificiosProductos

# -- import notas tecnicas module
nt = __import__("stib-administraciones").notas_tecnicas.models



register = template.Library()

@register.filter
def icon_by_boolean(value):
    """
    dependiendo si es True or False mostrar
    un ícono y otro
    """
    if value:
        return '<i class="fa fa-check"></i>'
    else:
        return '<i class="fa fa-times"></i>'


@register.filter
def mostrar_estados(estado):
    """
    dependiendo el estado que tenga la notificacion,
    mostramos el texto del mismo, con diferentes colores
    """
    if estado == 1:
        return '<span class="label label-default">Nuevo</span>'
    elif estado == 2:
        return '<span class="label label-success">Aceptado</span>'
    elif estado == 3:
        return '<span class="label label-warning">Pendiente</span>'
    elif estado == 4:
        return '<span class="label label-danger">Cancelado</span>'
    else:
        return ''


@register.inclusion_tag('relaciones/_popover_entidad.html')
def show_popover_entidad(obj):
    """
    mostrar un pop up con la info
    de una entidad producto o servicio
    """
    return {'nombre': obj.nombre, 'descripcion': obj.descripcion}


@register.inclusion_tag('relaciones/_popover_descripcion.html')
def show_popover_descripcion(descripcion):
    """
    mostrar un pop up con la descripcion
    de las notificaciones
    """
    return {'descripcion': descripcion}


@register.inclusion_tag('relaciones/_show_search_form.html')
def show_search_form(request, form, collapse_filters):
    """
    mostrar el form para realizar busquedas
    """
    return {'search_form': form,
            'current_path': request.get_full_path(),
            'collapse_filters': collapse_filters}


@register.simple_tag
def show_alertas_edificios(edificio):
    bell_icon = '<span class="fa fa-bell pull-right" style="color: #C9302C"></span>'
    # -- tiene nuevas notas tecnicas?
    notas_tecnicas = nt.NotasTecnicas.objects.\
        filter(edificio=edificio, leido=False, estado=1).count()
    if notas_tecnicas > 0:
        return bell_icon

    # -- tiene nuevas notificaciones de productos?
    notificaciones_productos = RelacionesEdificiosProductos.objects.\
        filter(edificio=edificio, leido=False, estado=1).count()
    if notificaciones_productos > 0:
        return bell_icon

    # -- tiene nuevas notificaciones de servicios?
    notificaciones_servicios = RelacionesEdificiosServicios.objects.\
        filter(edificio=edificio, leido=False, estado=1).count()
    if notificaciones_servicios > 0:
        return bell_icon

    return ""
