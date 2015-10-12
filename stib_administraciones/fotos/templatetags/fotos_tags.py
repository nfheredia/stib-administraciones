from django import template
from ..models import Fotos

register = template.Library()

@register.assignment_tag
def obtener_fotos_por_edificio(edificio_id):
    return Fotos.objects.filter(edificio=edificio_id).all()
