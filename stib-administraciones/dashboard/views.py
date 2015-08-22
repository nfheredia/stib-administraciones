# -*- coding: utf-8 -*-
from itertools import chain
from operator import attrgetter
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

from ..notas_tecnicas.models import NotasTecnicas
from ..relaciones.models import (RelacionesEdificiosProductos,
                                 RelacionesEdificiosServicios,
                                 RelacionesUsuariosProductos,
                                 RelacionesUsuariosServicios)


class DashboardIndexView(LoginRequiredMixin, TemplateView):
    """
    Vista que mostrará un resumen de las ultimas notificaciones,
    sean Notificaciones sobre productos o servicios, notas técnicas o
    notificaciones particulares de la adminsitracion que se esta
    logueado...
    """
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardIndexView, self).get_context_data(**kwargs)
        #-- obtengo notas tecnicas de los edificios que pertenecen a la
        #-- administracion logueada
        ctx['notas_tecnicas'] = NotasTecnicas.objects.filter(edificio__user=self.request.user.id)[:3]

        # -- obtengo las notificaciones de los edificios que pertenecen
        # -- a la administracion logueada
        notificaciones_productos_edificios = RelacionesEdificiosProductos.objects.filter(edificio__user=self.request.user.id)[:5]
        notificaciones_servicios_edificios = RelacionesEdificiosServicios.objects.filter(edificio__user=self.request.user.id)[:5]
        ctx['notificaciones_edificios'] = sorted(
            chain.from_iterable([notificaciones_productos_edificios, notificaciones_servicios_edificios]),
            key=attrgetter('creado'),
            reverse=True
        )[:3]

        # -- obtengo las notificaciones de la dminsitracion logueada
        notificaciones_productos_administracion = RelacionesUsuariosProductos.objects.filter(usuario=self.request.user.id)[:5]
        notificaciones_servicios_administracion = RelacionesUsuariosServicios.objects.filter(usuario=self.request.user.id)[:5]
        ctx['notificaciones_usuarios'] = sorted(
            chain.from_iterable([notificaciones_productos_administracion, notificaciones_servicios_administracion]),
            key=attrgetter('creado'),
            reverse=True
        )[:3]

        return ctx
