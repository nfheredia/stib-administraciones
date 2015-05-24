# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied
from ..edificios.models import Edificios


class PermisosAEdificiosMixin(object):
    """
    Clase que chequea si el edificio al que se quiere
    ingresar o ver algunos de sus datos (ejemplo: fotos
    contactos, llaves, etc) pertenece al usuario
    con el cuál se está logueado
    """
    def dispatch(self, request, *args, **kwargs):
        usuario = request.user.id
        edificio = self.kwargs['edificio']

        check = Edificios.edificios_usuarios_object\
            .por_edificio(usuario, edificio)

        if check.count() != 1:
            raise PermissionDenied

        return super(PermisosAEdificiosMixin, self).dispatch(request, *args, **kwargs)


def permisos_a_edificios(view_func):
    """
    Funcion que comprueba si el edificio que
    se quiere ver corresponde a la administracion
    logueada.
    Similar a la clase 'PermisosAEdificiosMixin', pero
    esta se utiliza para vistas basadas en funciones
    """
    def _wrapped_view_func(request, *args, **kwargs):
        usuario = request.user.id
        edificio = kwargs['edificio']

        check = Edificios.edificios_usuarios_object\
            .por_edificio(usuario, edificio)

        if check.count() != 1:
            raise PermissionDenied
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view_func
