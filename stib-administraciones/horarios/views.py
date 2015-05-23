# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin

from ..core.views import PermisosAEdificiosMixin
from .models import Horarios
from ..edificios.models import Edificios


class HorariosEdificiosMixin(object):

    model = Horarios

    # campos que se mostraran en los formularios de alta y edicion
    fields = ['personales', 'lunes', 'martes', 'miercoles', 'jueves',
              'viernes', 'sabado', 'domingo', 'hora_desde', 'hora_hasta']

    def success_msg(self):
        return NotImplemented

    def get_context_data(self, **kwargs):
        ctx = super(HorariosEdificiosMixin, self).get_context_data(**kwargs)
        ctx['edificio'] = Edificios.objects.get(pk=self.kwargs['edificio'])
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return reverse('horarios:edificio_horario_list',
                       kwargs={'edificio': self.kwargs['edificio']})


class HorariosEdificiosListView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                HorariosEdificiosMixin, ListView):
    """
    Lista todos los horarios de un edificio.
    """
    def get_queryset(self):
        return Horarios.objects.filter(edificio=self.kwargs['edificio']).all()


class HorariosEdificiosCreateView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                  HorariosEdificiosMixin, CreateView):
    """
    Vista para agregar un nuevo horario para un edificio determinado
    """
    success_msg = 'El horario se agregó correctamente'

    def post(self, request, *args, **kwargs):
        # -- necesito antes indicarle a que edificio pertenece el horario
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            form.instance.edificio_id = self.kwargs['edificio']
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})


class HorariosEdificiosUpdateView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                  HorariosEdificiosMixin, UpdateView):
    """
    Vista para editar un horario
    """
    success_msg = 'El horario se modificó correctamente'


class HorariosEdificiosDeleteView(LoginRequiredMixin, PermisosAEdificiosMixin,
                                  HorariosEdificiosMixin, DeleteView):
    """
    Vista para eliminar un horario
    """
    success_msg = 'El horario se eliminó correctamente.'
