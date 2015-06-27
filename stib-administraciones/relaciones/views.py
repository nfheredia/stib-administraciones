# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import FormView, CreateView
from django.db.models import Q
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import (FormDefinirTipoComunicacion,
                    FormNotificacionUsuariosProductos,
                    FormNotificacionUsuariosServicios,
                    FormNotificacionEdificiosProductos,
                    FormNotificacionEdificiosServicios)
from .models import (RelacionesUsuariosProductos,
                     RelacionesUsuariosServicios,
                     RelacionesEdificiosProductos,
                     RelacionesEdificiosServicios)
from ..productos.models import Productos
from ..servicios.models import Servicios
from ..edificios.models import Edificios


class EstableverTipoComunicacion(LoginRequiredMixin, StaffuserRequiredMixin, FormView):
    """
    Vista que presentara un formulario
    para definir el tipo de comunicacion
    """
    template_name = 'relaciones/establecer_tipo_comunicacion.html'
    form_class = FormDefinirTipoComunicacion

    def form_valid(self, form):
        """
        Armamos la Url encargada de redirigir a la pantalla
        adecuada para enviar la notificacion
        """
        entidad = form.cleaned_data["entidad"]
        destinatario = form.cleaned_data["destinatario"]
        self.success_url = entidad + "-" + destinatario
        return super(EstableverTipoComunicacion, self).form_valid(form)


class NotificarCreateViewMixin(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):

    template_name = 'relaciones/notificar_form.html'

    def get_success_url(self):
        messages.success(self.request, 'La notificación se envió con éxito.')
        return reverse('notificaciones:definir')


class NotificarProductosUsuarios(NotificarCreateViewMixin):
    """
    Notificar a usuarios(administraciones) sobre determinados
    productos
    """
    model = RelacionesUsuariosProductos
    form_class = FormNotificacionUsuariosProductos

    def get_context_data(self, **kwargs):
        ctx = super(NotificarProductosUsuarios, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Notificaciones de Productos para Administraciones '
        return ctx


class NotificarServiciosUsuarios(NotificarCreateViewMixin):
    """
    Notificar a usuarios(administraciones) sobre determinados
    servicios.
    """
    model = RelacionesUsuariosServicios
    form_class = FormNotificacionUsuariosServicios

    def get_context_data(self, **kwargs):
        ctx = super(NotificarServiciosUsuarios, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Notificaciones de Servicios para Administraciones '
        return ctx


class NotificarProductosEdificios(NotificarCreateViewMixin):
    """ Notificar a edificio sobre determinados productos. """
    model = RelacionesEdificiosProductos
    form_class = FormNotificacionEdificiosProductos

    def get_context_data(self, **kwargs):
        ctx = super(NotificarProductosEdificios, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Notificaciones de Productos para Edificios'
        return ctx


class NotificarServiciosEdificios(NotificarCreateViewMixin):
    """ Notificar a edificio sobre determinados servicios. """
    model = RelacionesEdificiosServicios
    form_class = FormNotificacionEdificiosServicios

    def get_context_data(self, **kwargs):
        ctx = super(NotificarServiciosEdificios, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Notificaciones de Servicios para Edificios'
        return ctx


def get_autocomplete_result(request):
    """
    Busqueda de productos y servicios, se utiliza en una llamada
    ajax en el formulario para auto-sugerir el resultado.
    """
    # -- término a buscar --
    q = request.GET['term']
    # -- parametro que indica en que modelo bsucar --
    obj = request.GET['obj']
    # -- convierto string a isntancia de clase --
    class_instance = globals()[obj]
    # -- consulta sql para obtener el resultado --
    results = class_instance.objects.filter(nombre__icontains=q)
    results_list = []

    for result in results:
        dic_result = {}
        dic_result['id'] = result.id
        dic_result['label'] = result.nombre
        results_list.append(dic_result)

    return HttpResponse(json.dumps(results_list), mimetype="application/json")


def get_autocomplete_edificios_result(request):
    """
    Busqueda de edificios, se utiliza en una llamada
    ajax en el formulario para auto-sugerir el resultado.
    """
    # -- término a buscar --
    q = request.GET['term']
    # -- busqueda por nombre o direccion de edificio
    edificios = Edificios.objects.filter(Q(nombre__icontains=q) | Q(direccion__icontains=q))

    results_list = []

    for edificio in edificios:
        dic_result = {}
        dic_result['id'] = edificio.id
        dic_result['label'] = edificio.nombre +" - "+edificio.direccion
        results_list.append(dic_result)

    return HttpResponse(json.dumps(results_list), mimetype="application/json")



