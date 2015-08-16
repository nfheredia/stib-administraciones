# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, DeleteView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import NotasTecnicas
from .forms import NotasTecnicasCreateForm, NotasTecnicasSearchForm
from ..edificios.models import Edificios
from ..perfiles.models import Perfiles


class NotasTecnicasCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    """
    Vista para la Creación de una Nota Técnica
    """
    model = NotasTecnicas
    form_class = NotasTecnicasCreateForm
    raise_exception = True

    def get_success_url(self):
        messages.success(self.request, "Se ha creado una nueva Nota Técnica.")
        return reverse('notas-tecnicas:create')

    def form_valid(self, form):
        # -- enviar por mail, solo si desde
        # -- el form se indicar True
        if form.cleaned_data['enviado']:
            if self._enviar_aviso_por_email(form):
                form.instance.mail_recibido = True

        return super(NotasTecnicasCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(NotasTecnicasCreateView, self).form_invalid(form)

    def _enviar_aviso_por_email(self, form):
        try:
            # -- obtengo Id de usuario
            if self.request.POST.get('edificio') is not None:
                user = Edificios.usuario_por_edificio(self.request.POST.get('edificio'))

            # -- obtengo direccion de mail
            email = Perfiles.obtener_mail_por_usuario(user)

            # -- tiene email cargado?
            if len(email) > 0:
                subject = "[STIB] Nota Técnica - "
                if self.request.POST.get('edificio') is not None:
                    subject += str(form.cleaned_data['edificio'])

                ctx = {'link_vista': 'http://google.com'}

                return _send_email(email, subject, ctx)
            else:
                return False
        except:
            messages.error(self.request, "Se produjo un error en el envío del email.")
            return False


class NotasTecnicasListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    """ Listado de notas técnicas """
    model = NotasTecnicas
    context_object_name = 'notas_tecnicas'
    raise_exception = True

    def get_context_data(self, **kwargs):
        ctx = super(NotasTecnicasListView, self).get_context_data(**kwargs)
        ctx['search_form'] = NotasTecnicasSearchForm
        return ctx

    def get_queryset(self):
        qs = super(NotasTecnicasListView, self).get_queryset()

        # -- busqueda x titulo? --
        titulo = self.request.GET.get('titulo', None)
        if titulo:
            qs = qs.filter(titulo__icontains=titulo)
        # -- busqueda x descripcion? --
        descripcion = self.request.GET.get('descripcion', None)
        if descripcion:
            qs = qs.filter(descripcion__icontains=descripcion)
        # -- leido? --
        leido = self.request.GET.get('leido', None)
        if leido:
            qs = qs.filter(leido=True if leido == "1" else False)
        # -- Mail enviado? --
        mail_enviado = self.request.GET.get('mail', None)
        if mail_enviado:
            qs = qs.filter(enviado=True if mail_enviado == "1" else False)
        # -- Mail recibido? --
        mail_recibido = self.request.GET.get('mail_recibido', None)
        if mail_recibido:
            qs = qs.filter(mail_recibido=True if mail_recibido == "1" else False)
        # -- estado? --
        estado = self.request.GET.get('estado')
        if estado:
            qs = qs.filter(estado=estado)
        # -- fechas desde/hasta --
        fecha_desde = self.request.GET.get('fecha_desde')
        fecha_hasta = self.request.GET.get('fecha_hasta')
        if fecha_desde and fecha_hasta:
            fecha_desde = fecha_desde.split('/')
            fecha_hasta = fecha_hasta.split('/')
            fecha_desde = fecha_desde[2] + "-" + fecha_desde[1] + "-" + fecha_desde[0]
            fecha_hasta = fecha_hasta[2] + "-" + fecha_hasta[1] + "-" + fecha_hasta[0]
            qs = qs.filter(creado__gte=fecha_desde, creado__lte=fecha_hasta)
        # -- edificio? --
        edificio = self.request.GET.get('edificio', None)
        if edificio:
            qs = qs.filter(edificio=edificio)

        return qs


class NotasTecnicasDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    """ Borrado de Nota Técnica """
    model = NotasTecnicas
    raise_exception = True

    def get_success_url(self):
        messages.success(self.request, 'La nota técnica fue eliminada.')
        return reverse('notas-tecnicas:list')


def _send_email(email_to, subject, context, *args):
    """
    Envío de email
    """
    try:
        body = render_to_string("emails/email_notificaciones.html", context)
        msg = EmailMessage(subject=subject,
                           body=body,
                           from_email='no-reply@stibadministraciones.com',
                           to=(email_to, ))
        msg.content_subtype = 'html'
        msg.send()
        return True
    except:
        return False