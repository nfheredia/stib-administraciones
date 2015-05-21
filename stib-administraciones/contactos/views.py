from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from ..core.views import PermisosAEdificiosMixin
from .models import Contactos
from ..edificios.models import Edificios


class ContactosEdificiosListView(LoginRequiredMixin, PermisosAEdificiosMixin, ListView):
    """
    - Lista todos los contactos de un edificio.
    - El edificio del cual se listaran los contactos es
    el edificio que se pasa como parametro en la url.
    """
    model = Contactos

    def get_context_data(self, **kwargs):
        ctx = super(ContactosEdificiosListView, self).get_context_data(**kwargs)
        ctx['edificio'] = Edificios.objects.get(pk=self.kwargs['pk'])
        return ctx

    def get_queryset(self):
        return Contactos.objects.filter(edificio=self.kwargs['pk']).all()
