# -*- coding: utf-8 -*-
import json
from itertools import chain
from operator import attrgetter
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import FormView, CreateView, TemplateView, ListView
from django.db.models import Q
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import (FormDefinirTipoComunicacion,
                    FormNotificacionUsuariosProductos,
                    FormNotificacionUsuariosServicios,
                    FormNotificacionEdificiosProductos,
                    FormNotificacionEdificiosServicios,
                    FormNotificacionesEdificiosSearch)
from .models import (RelacionesUsuariosProductos,
                     RelacionesUsuariosServicios,
                     RelacionesEdificiosProductos,
                     RelacionesEdificiosServicios)
from ..productos.models import Productos
from ..servicios.models import Servicios
from ..edificios.models import Edificios
from ..perfiles.models import Perfiles


class EstableverTipoComunicacion(LoginRequiredMixin, StaffuserRequiredMixin, FormView):
    """
    Vista que presentara un formulario
    para definir el tipo de comunicacion
    """
    template_name = 'relaciones/establecer_tipo_comunicacion.html'
    form_class = FormDefinirTipoComunicacion
    raise_exception = True

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
    raise_exception = True

    def get_success_url(self):
        messages.success(self.request, 'La notificación se envió con éxito.')
        return reverse('notificaciones:definir')

    def form_valid(self, form):
        self._enviar_aviso_por_email(form)
        return super(NotificarCreateViewMixin, self).form_valid(form)

    def _enviar_aviso_por_email(self, form):
        try:
            # -- obtengo Id de usuario
            if self.request.POST.get('edificio') is None:
                user = self.request.POST.get('usuario')
            else:
                user = Edificios.objects.values('user').get(pk=self.request.POST.get('edificio'))
                user = user['user']

            # -- obtengo direccion de mail
            email = Perfiles.objects.values('email_1').get(user=user)

            # -- tiene email cargado?
            if 'email_1' in email and len(email['email_1']) > 0:
                subject = "[STIB] [%s] " % form.cleaned_data['tipo_relacion']
                if self.request.POST.get('edificio') is not None:
                    subject += str(form.cleaned_data['edificio'])
                else:
                    subject += "Aviso importante"

                ctx = {'link_vista': 'http://google.com'}
                body = render_to_string("emails/email_notificaciones.html", ctx)
                msg = EmailMessage(subject=subject,
                                   body=body,
                                   from_email='no-reply@stibadministraciones.com',
                                   to=(email['email_1'], ))
                msg.content_subtype = 'html'
                msg.send()
                return True
            else:
                return False
        except:
            return False


class NotificarProductosUsuarios(NotificarCreateViewMixin):
    """
    Notificar a usuarios(administraciones) sobre determinados
    productos
    """
    model = RelacionesUsuariosProductos
    form_class = FormNotificacionUsuariosProductos

    def get_context_data(self, **kwargs):
        ctx = super(NotificarProductosUsuarios, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Notificaciones de Productos para Administraciones'
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
        ctx['page_title'] = 'Notificaciones de Servicios para Administraciones'
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
        dic_result['label'] = edificio.nombre + " - " + edificio.direccion
        results_list.append(dic_result)

    return HttpResponse(json.dumps(results_list), mimetype="application/json")


class NotificacionesViewMixin(LoginRequiredMixin, StaffuserRequiredMixin):

    queries = []
    raise_exception = True

    def get_queryset(self):
        qs = self._get_queries_results()
        return qs

    def _get_queries_results(self):
        """
        iteramos las queries, usamos el método from_iterable
        del objecto chain porque le pasamos una tupla de queries
        """
        return sorted(
            chain.from_iterable(self.queries),
            key=attrgetter('creado'),
            reverse=True
        )


class NotificacionesEdificiosView(NotificacionesViewMixin, ListView, FormView):
    """
    Ver las notificaciones de los Edificios, combinamos
    los productos y servicios...
    """
    template_name = 'relaciones/notificaciones_edificios_list.html'
    queries = [RelacionesEdificiosProductos.objects.all(), RelacionesEdificiosServicios.objects.all()]
    success_url = '/notificaciones/edificios/list'
    form_class = FormNotificacionesEdificiosSearch
    context_object_name = 'results'

    # def get_context_data(self, **kwargs):
    #     ctx = super(NotificacionesEdificiosView, self).get_context_data(**kwargs)
    #     ctx['search_form'] = FormNotificacionesEdificiosSearch
    #     return ctx
    #
    # def form_valid(self, form):
    #     self.queries = [RelacionesEdificiosProductos.objects.filter(titulo="forro"),
    #                   RelacionesEdificiosServicios.objects.all()]
    #     return self.form_valid(self)


class NotificacionesAdministracionesView(NotificacionesViewMixin, TemplateView):
    """
    Ver las notificaciones de las administraciones, combinamos
    los productos y servicios...
    """
    template_name = 'relaciones/notificaciones_administraciones_list.html'
    queries = [RelacionesUsuariosProductos.objects.all(), RelacionesUsuariosServicios.objects.all()]

