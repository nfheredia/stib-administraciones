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
