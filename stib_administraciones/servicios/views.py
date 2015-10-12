# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from braces.views import LoginRequiredMixin

from .models import Servicios
from ..settings_local import STIB_TO_EMAIL
from .forms import FormConsulta


class ServiciosMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(ServiciosMixin, self).get_context_data(**kwargs)
        ctx['tags'] = self.model.tags.all()
        return ctx


class ServiciosListView(LoginRequiredMixin, ServiciosMixin, ListView):
    """ Listado de servicio """
    model = Servicios

    def get_queryset(self):
        queryset = super(ServiciosListView, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(descripcion__icontains=q).all()

        return queryset


class ServiciosDetailView(LoginRequiredMixin, DetailView):
    """ Detalle de un servicio """
    model = Servicios

    def get_context_data(self, **kwargs):
        ctx = super(ServiciosDetailView, self).get_context_data(**kwargs)
        ctx['form_consulta'] = FormConsulta
        ctx['otros_servicios'] = Servicios.objects.exclude(pk=self.kwargs['pk'])[:3]
        return ctx


class ServiciosTagsListView(LoginRequiredMixin, ServiciosMixin, ListView):
    """ Filtrado por tags """
    model = Servicios

    def get_queryset(self):
        return Servicios.objects.\
            filter(tags__slug__in=[self.kwargs['tag']]).\
            distinct()


def pedido_cotizacion(request, pk):
    """
    - Envio de email para el pedido de una cotizacion
    - Hay que tener en cta que la administracion debe
    tener completo su perfil..
    """
    if request.user.perfil.alerta_bienvenida == 1:
        msg = "Para poder solictar una cotización, antes debe\
            <a href='/perfiles/update'>completar sus datos de perfil</a>."
        messages.error(request, msg)
        return HttpResponseRedirect('/servicios/'+pk)

    servicios = Servicios.objects.get(id=pk)
    mail = EmailMessage(subject='Pedido de cotizacion del serivicio "'+servicios.nombre+'"',
                        from_email=request.user.perfil.email_1,
                        to=STIB_TO_EMAIL)
    mail.body = '"'+request.user.perfil.nombre + '" solicita cotizacion del servicio "'+servicios.nombre+'"'
    mail.send()
    messages.success(request, "Hemos recibido tu pedido de cotización, \
                        a la brevedad nos pondremos en contacto.")
    return HttpResponseRedirect('/servicios/'+pk)


def enviar_consulta(request, pk):
    """
    Proceso de formulario para realizar consulta de un servicio
    y envío de email.
    """
    if request.method == 'POST':
        # -- tiene completo el prefil??
        if request.user.perfil.alerta_bienvenida == 1:
            msg = "Para poder realizar una consulta, antes debe\
                <a href='/perfiles/update'>completar sus datos de perfil</a>."
            messages.error(request, msg)
            return HttpResponseRedirect('/servicios/'+pk)

        formulario = FormConsulta(request.POST)
        if formulario.is_valid():
            servicio = Servicios.objects.get(id=pk)
            mail = EmailMessage(subject='Consulta del servicio "'+servicio.nombre+'"',
                                from_email=request.user.perfil.email_1,
                                to=STIB_TO_EMAIL)
            mail.body = formulario.cleaned_data['consulta']
            mail.send()
            messages.success(request, "Hemos recibido tu consulta, \
                        a la brevedad nos pondremos en contacto.")
        else:
            messages.error(request, 'Complete el formulario.')
    return HttpResponseRedirect('/servicios/'+pk)

