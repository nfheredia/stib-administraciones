from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from django.contrib import messages

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin
)

from .models import Edificios


class EdificiosMixin(object):
    model = Edificios

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(EdificiosMixin, self).form_valid(form)


class EdificiosListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    """
    Listamos todos los edificios
    Solo para usuarios de 'staff'
    """
    model = Edificios
    # -- si alguien no autorizado quiere ingresar,
    # -- lanzamos un 403
    raise_exception = True


class EdificiosCreateView(LoginRequiredMixin, StaffuserRequiredMixin, EdificiosMixin, CreateView):
    """
    Crear un nuevo edificio
    """
    raise_exception = True
    success_msg = 'Se ha creado un Nuevo edificio'


class EdificiosUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, EdificiosMixin, UpdateView):
    """
    Editar un edificio
    """
    raise_exception = True
    success_msg = 'Se han editado los datos del edificio'


class EdificiosDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    """
    Eliminar un edificio
    """
    model = Edificios
    success_url = '/edificios'


class EdificiosAdministracionesView(LoginRequiredMixin, DetailView):
    """
    Muestra el detalle de un edificio, siempre y cuando
    el mismo pertenezca a la administracion logueada..
    """
    template_name = 'edificios/edificios_administraciones_detail.html'

    def get_queryset(self):
        return Edificios.edificios_usuarios_object\
            .por_usuarios(self.request.user.id)\
            .filter(id=self.kwargs['pk'])