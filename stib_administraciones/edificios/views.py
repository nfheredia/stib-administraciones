# -*- coding: utf-8 -*-
import json
from itertools import chain
from operator import attrgetter
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View
)
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin
)

from .models import Edificios
from .forms import FormSearch
from ..relaciones.models import RelacionesEdificiosProductos, RelacionesEdificiosServicios
from ..notas_tecnicas.models import NotasTecnicas


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

    def get_context_data(self, **kwargs):
        ctx = super(EdificiosListView, self).get_context_data(**kwargs)
        ctx['form_search'] = FormSearch
        return ctx

    def get_queryset(self):
        """ queryset y filtros si es que los hay """
        qs = super(EdificiosListView, self).get_queryset()

        nombre = self.request.GET.get('nombre', False)
        if nombre:
            qs = qs.filter(nombre__icontains = nombre)

        direccion = self.request.GET.get('direccion', False)
        if direccion:
            qs = qs.filter(direccion__icontains = direccion)

        codigo = self.request.GET.get('codigo', False)
        if codigo:
            qs = qs.filter(codigo = codigo)

        comentario = self.request.GET.get('comentario', None)
        if comentario:
            qs = qs.filter(comentario__icontains = comentario)

        usuario = self.request.GET.get('usuario', None)
        if usuario:
            qs = qs.filter(user = usuario)

        return qs


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

    def get_context_data(self, **kwargs):
        ctx = super(EdificiosAdministracionesView, self).get_context_data(**kwargs)
        ctx['otros_edificios'] = Edificios.edificios_usuarios_object.por_usuarios(self.request.user.id).\
                                    exclude(pk=self.kwargs['pk'])[:4]
        # -- obtengo las notificaciones del edificio que se consulta
        notificaciones_productos_edificios = RelacionesEdificiosProductos.objects.\
            filter(edificio=self.kwargs['pk'],
                   edificio__user=self.request.user.id)[:5]
        notificaciones_servicios_edificios = RelacionesEdificiosServicios.objects.\
            filter(edificio=self.kwargs['pk'],
                   edificio__user=self.request.user.id)[:5]
        ctx['notificaciones'] = sorted(
            chain.from_iterable([notificaciones_productos_edificios, notificaciones_servicios_edificios]),
            key=attrgetter('creado'),
            reverse=True
        )[:3]
        # -- obtengo notas tecnicas del edificio
        ctx['notas_tecnicas'] = NotasTecnicas.objects.\
            filter(edificio=self.kwargs['pk'],
                   edificio__user=self.request.user.id)[:3]

        return ctx


class EdificiosAdministracionesDetallesUpdateView(LoginRequiredMixin, EdificiosAdministracionesUpdateMixin, UpdateView):
    """
    Editar los campos nombre, codigo, cantidad_pisos y cantidad_unidades
    Solo para las administraciones loguedas y que el edificio le pertenezca
    """
    fields = ['nombre', 'cantidad_pisos', 'cantidad_unidades']
    success_msg = 'Los datos del edificio se han editado correctamente.'


class EdificiosAdministracionesComentarioUpdateView(LoginRequiredMixin, EdificiosAdministracionesUpdateMixin, UpdateView):
    """
    Editar el comentario
    Solo para las administraciones loguedas y que el edificio le pertenezca
    """
    fields = ['comentario']
    success_msg = 'Se ha modificado el comentario del edificios.'


class EdificiosAdministracionesFachadaUpdateView(LoginRequiredMixin, EdificiosAdministracionesUpdateMixin, UpdateView):
    fields = ['foto_fachada']
    success_msg = 'La foto de fachada se editó correctamente.'


@login_required
def search_autocomplete_edificios_por_administracion(request):
    """
    Devuelve un ajax de los edificios que pertencen
    a la adminsitracion logueda
    """
    # -- término a buscar --
    q = request.GET['term']
    # -- busqueda por nombre o direccion de edificio y que sea
    # -- del usuario logueado
    edificios = Edificios.edificios_usuarios_object.por_usuarios(request.user.id)\
        .filter(Q(nombre__icontains=q) | Q(direccion__icontains=q))

    results_list = []

    for edificio in edificios:
        dic_result = {}
        dic_result['id'] = edificio.id
        dic_result['label'] = edificio.nombre + " - " + edificio.direccion
        results_list.append(dic_result)

    return HttpResponse(json.dumps(results_list), mimetype="application/json")


class SearchEdificiosForm(LoginRequiredMixin, View):
    """
    busqueda del edificio, y redirigimos a la pagina
    principal con detalles del edificio
    """
    def post(self, request, *args, **kwargs):
        id_edificio = request.POST.get("id_edificio", False)
        if id_edificio:
            url_destino = reverse("edificios:administraciones", kwargs={'pk': id_edificio})
        else:
            messages.error(request, 'No se encontró el edificio que estas buscando.')
            url_destino = "/"
        return HttpResponseRedirect(url_destino)
