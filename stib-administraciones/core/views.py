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


def enviar_mails_para_sincronizar(self):
    """
    Funcionalidad que determina que eventos( Alta, baja o edicion) que
    está ejecutando y sobre que entidad (contactos, Llaves, Horarios).
    Va a enviar un correo que el personal encargado esté enterado de
    tal evento.
    """
    # -- nombre de la administracion
    administracion = self.request.user.perfil.nombre
    if administracion == "":
        administracion = '<Nombre Desconocido>'
    # -- / nombre de la administracion

    # -- nombre del edificio
    edificio = Edificios.objects.values('nombre', 'direccion')\
        .get(pk=self.kwargs['edificio'])
    # -- / nombre del edificio

    # -- obtengo el nombre del modelo como string
    entidad = self.model.__name__

    # -- de todas las clases que se heredan en la clase base
    # -- obtengo el nombre la ultima, de esta forma se obtiene
    # -- que tipo de evento se trata (Creacion, edicion o Delete)
    class_evento = self.__class__.__bases__[len( self.__class__.__bases__ )-1].__name__
    if class_evento == 'CreateView':
        evento = 'ALTA'
    elif class_evento == 'UpdateView':
        evento = 'EDICION'
    else:
        evento = 'BORRADO'

    email_body = "<b>Administracion:</b> %s " \
                 "<br><b>Edificio:</b> %s (%s) " \
                 "<br><b>Entidad:</b> %s <br>" \
                 "<br><b>Evento:</b> %s <br>" \
                 % (administracion, edificio['nombre'], edificio['direccion'],
                    entidad, evento)

    print email_body

