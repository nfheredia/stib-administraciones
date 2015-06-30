from django import template

register = template.Library()

@register.filter
def icon_by_boolean(value):
    if value:
        return '<i class="fa fa-check"></i>'
    else:
        return '<i class="fa fa-times"></i>'


@register.inclusion_tag('relaciones/_pop_up_entidad.html')
def show_pop_up_entidad(obj):
	""" mostrar un pop up con la info
	de una entidad producto o servicio """
	return {'nombre': obj.nombre, 'descripcion': obj.descripcion}
