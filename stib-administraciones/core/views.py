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
        edificio = self.kwargs['pk']

        check = Edificios.edificios_usuarios_object\
            .por_edificio(usuario, edificio)

        if check.count() != 1:
            raise PermissionDenied

        return super(PermisosAEdificiosMixin, self).dispatch(request, *args, **kwargs)
