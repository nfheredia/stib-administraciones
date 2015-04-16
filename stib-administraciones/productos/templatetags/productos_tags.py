from django import template
from ..models import ProductosFotos

register = template.Library()

@register.assignment_tag
def fotos_productos(producto_id):
    return ProductosFotos.objects.filter(producto=producto_id).all()