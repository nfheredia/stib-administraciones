from django import template
from ..models import Perfiles

register = template.Library()

@register.inclusion_tag('perfiles/mostrar_mensaje_bienvenida.html')
def mostrar_mensaje_bienvenida(user_id):
    """
    Recibe el usuario logueado.
    Devuelve en una variable si mostrar o no
    el msg de bienvenida...
    """
    mostrar_msg = Perfiles.mostrar_mensaje_bienvenida(user_id)
    return {"mostrar_msg": mostrar_msg.alerta_bienvenida}

