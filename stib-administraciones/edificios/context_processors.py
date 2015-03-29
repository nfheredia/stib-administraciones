from .models import Edificios


def edificios_usuarios(request):
    """
    Devuelve todos los edificios del usuario logueado
    """
    edificios_usuarios = Edificios.edificios_usuarios_object.por_usuarios(request.user.id)
    return {'edificios_usuarios': edificios_usuarios}
