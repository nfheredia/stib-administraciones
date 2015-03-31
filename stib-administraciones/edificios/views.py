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


class EdificiosAdministracionesMixin(object):
    """
    Mixin con query que filtra por usuario logueado
    y edificio
    """
    def get_qr(self):
        return Edificios.edificios_usuarios_object\
            .por_edificio(self.request.user.id, self.kwargs['pk'])


class EdificiosAdministracionesUpdateMixin(EdificiosAdministracionesMixin):
    """
    Mixin para los update de los edificios pertenecientes
    a las administraciones
    """
    template_name = 'edificios/edificios_administraciones_update_form.html'

    def success_msg(self):
        """ Mensage de informacion """
        return NotImplemented

    def get_object(self, queryset=None):
        """ Devolvemos un objeto correspondiente a un edificio y al usuario logueado """
        return self.get_qr().get()

    def get_success_url(self):
        """ Url de success """
        return '/edificios/administracion/'+self.kwargs['pk']

    def form_valid(self, form):
        """ Definimos el msg y devolvemos un form valido """
        messages.success(self.request, self.success_msg)
        return super(EdificiosAdministracionesUpdateMixin, self).form_valid(form)


class EdificiosAdministracionesView(LoginRequiredMixin, EdificiosAdministracionesMixin, DetailView):
    """
    Muestra el detalle/todos los datos de un edificio, siempre y cuando
    el mismo pertenezca a la administracion logueada..
    """
    template_name = 'edificios/edificios_administraciones_detail.html'

    def get_queryset(self):
        return self.get_qr()


class EdificiosAdministracionesDetallesUpdateView(LoginRequiredMixin, EdificiosAdministracionesUpdateMixin, UpdateView):
    """
    Editar los campos nomre, codigo, cantidad_pisos y cantidad_unidades
    Solo para las administraciones loguedas y que el edificio le pertenezca
    """
    fields = ['nombre', 'codigo', 'cantidad_pisos', 'cantidad_unidades']
    success_msg = 'Los datos del edificio se han editado correctamente.'


class EdificiosAdministracionesComentarioUpdateView(LoginRequiredMixin, EdificiosAdministracionesUpdateMixin, UpdateView):
    """
    Editar el comentario
    Solo para las administraciones loguedas y que el edificio le pertenezca
    """
    fields = ['comentario']
    success_msg = 'Se ha modificado el comentario del edificios.'