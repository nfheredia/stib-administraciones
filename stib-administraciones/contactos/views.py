# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin

from ..core.views import PermisosAEdificiosMixin, enviar_mails_para_sincronizar
from .models import Contactos
from ..edificios.models import Edificios


class ContactosEdificiosMixin(object):

    model = Contactos

    # campos que se mostraran en los formulario de alta y edicion
    fields = ['nombre', 'piso', 'departamento', 'telefono', 'comentario']

    def success_msg(self):
        return NotImplemented

    def get_context_data(self, **kwargs):
        ctx = super(ContactosEdificiosMixin, self).get_context_data(**kwargs)
        ctx['edificio'] = Edificios.objects.get(pk=self.kwargs['edificio'])
        return ctx

    def get_success_url(self):
        #enviar_mails_para_sincronizar(self)
        messages.success(self.request, self.success_msg)
        return reverse('contactos:edificio_contactos_list',
                       kwargs={'edificio': self.kwargs['edificio']})


class ContactosEdificiosListView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                 ContactosEdificiosMixin, ListView):
    """
    - Lista todos los contactos de un edificio.
    - El edificio del cual se listaran los contactos es
    el edificio que se pasa como parametro en la url.
    """
    def get_queryset(self):
        return Contactos.objects.filter(edificio=self.kwargs['edificio']).all()


class ContactosEdificiosCreateView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                   ContactosEdificiosMixin, CreateView):
    """
    Vista para agregar un nuevo contacto para un edificio determinado
    """
    success_msg = 'El contacto se agregó correctamente'

    def post(self, request, *args, **kwargs):
        # -- necesito antes indicarle a que edificio pertenece el contacto
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            form.instance.edificio_id = self.kwargs['edificio']
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})


class ContactosEdificiosUpdateView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                   ContactosEdificiosMixin, UpdateView):
    """
    Vista para editar un contacto
    """
    success_msg = 'El contacto se modificó correctamente'


class ContactosEdificiosDeleteView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                   ContactosEdificiosMixin, DeleteView):
    """
    Vista para eliminar un contacto
    """
    success_msg = 'El contacto se eliminó correctamente.'
