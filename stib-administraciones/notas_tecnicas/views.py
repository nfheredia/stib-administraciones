# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from ..settings_local import STIB_TO_EMAIL
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
                body = render_to_string("emails/email_notas_tecnicas.html", ctx)

                return _send_email(email, subject, body)
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


def _send_email(email_to, subject, body, *args):
    """
    Envío de email
    """
    try:
        if isinstance(email_to, tuple) is False:
            email_to = (email_to, )

        msg = EmailMessage(subject=subject,
                           body=body,
                           from_email='no-reply@stibadministraciones.com',
                           to=email_to)
        msg.content_subtype = 'html'
        msg.send()
        return True
    except:
        return False


@staff_member_required
def reenviar_email(request, pk):
    try:
        # -- obtener informacion de la nota técnica
        nt = NotasTecnicas.objects.get(pk=pk)
        # -- obtener el usuario(administracion) dueño del edificio
        user = Edificios.usuario_por_edificio(nt.edificio.id)
        # -- obtengo direccion de mail
        email = Perfiles.obtener_mail_por_usuario(user)

        if len(email) > 0:
            subject = "[STIB] Nota Técnica - " + str(nt.edificio)
            ctx = {'link_vista': 'http://google.com'}
            body = render_to_string("emails/email_notas_tecnicas.html", ctx)
            if _send_email(email, subject, body):
                nt.mail_recibido = True
                nt.enviado = True
                nt.save()

            messages.success(request, "Se ha reenviado el email correctamente.")

        else:
            messages.error(request, 'Error al reenviar el email, verifique el email de la administración'
                                    ' encargada del edificio.')

        return HttpResponseRedirect(reverse("notas-tecnicas:list"))
    except:
        messages.error(request, 'Error inesperado al reenviar el email.')
        return HttpResponseRedirect(reverse("notas-tecnicas:list"))


class NotasTecnicasDetailView(LoginRequiredMixin, DetailView):
    """
    Ver el detalle de una Nota Tecnica
    """
    model = NotasTecnicas

    def get_queryset(self):
        qs = NotasTecnicas.objects.filter(pk=self.kwargs['pk'])
        # -- debemos ademas estar seguros que la nota tecnica
        # -- sea de la administracion logueada
        qs.filter(edificio__user=self.request.user.id)

        # -- si no esta leido, se marca como Nota tecnica leida
        if qs[0].leido is False:
            NotasTecnicas.marcar_leido(qs[0].id)

        return qs


@login_required(redirect_field_name='accounts/login/')
def enviar_cambio_estado(request):
    """
    Cambio de estado de una nota técnica y avisar
    por email al personal de stib
    """
    if request.method == "POST" or request.POST.get("nota_tecnica"):
        try:
            nota_tecnica = get_object_or_404(NotasTecnicas, pk=request.POST.get("nota_tecnica"))
            nota_tecnica.estado = request.POST.get("estado")
            nota_tecnica.save()

            # -- envio de email notificando el cambio de estado
            subject = "Nota Técnica - Cambio de estado"
            ctx = {
                'administracion': nota_tecnica.edificio.user.perfil.nombre_comercial,
                'edificio': nota_tecnica.edificio,
                'estado': NotasTecnicas.ESTADOS[ int(request.POST.get("estado"))-1 ][1],
                'descripcion': nota_tecnica.descripcion,
                'fecha': nota_tecnica.creado,
                'comentario': request.POST.get("comentario")
            }

            body = render_to_string('emails/email_cambio_estado_nota_tecnica.html', ctx)
            _send_email(STIB_TO_EMAIL, subject, body)
            # -- / envio de email notificando el cambio de estado

            messages.success(request, "Se ha cambiado el estado de la Nota Técnica.")
        except:
            messages.error(request, "Error al cambiar el estado de la Nota Técnica.")

        return HttpResponseRedirect(reverse('notas-tecnicas:detail', args=[request.POST.get("nota_tecnica")]))
    else:
        messages.success(request, "Error.")
        return HttpResponseRedirect("/")