# -*- coding: utf-8 -*-
from django import template

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
