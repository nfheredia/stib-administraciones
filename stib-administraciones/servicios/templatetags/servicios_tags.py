from django import template
from ..models import ServiciosFotos

register = template.Library()

@register.assignment_tag
def fotos_servicios(servicio_id):
    return ServiciosFotos.objects.filter(servicio=servicio_id).all()