# -*- coding: utf-8 -*-
from django.shortcuts import Http404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from ..edificios.models import Edificios
from .models import Fotos


class FotosAdministracionMixin(object):

    def success_msg(self):
        return NotImplemented

    def __check_perms(self):
        # -- si el edifcio que viene por ID no le pertence
        # -- al usuario logueado, devolvemos un 404
        pertenece = Edificios.edificios_usuarios_object\
            .por_edificio(self.request.user.id, self.kwargs['edificio'])

        if len(pertenece) is 0:
            raise Http404

    def get(self, request, *args, **kwargs):
        self.__check_perms()
        return super(FotosAdministracionMixin, self).get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return '/fotos/administracion/%s' % (self.kwargs['edificio'])

    def get_context_data(self, **kwargs):
        ctx = super(FotosAdministracionMixin, self).get_context_data(**kwargs)
        ctx['edificio'] = Edificios.objects.filter(id=self.kwargs['edificio']).get()
        return ctx


class FotosAdministracionListView(LoginRequiredMixin, FotosAdministracionMixin, ListView):
    """Mostraremos las fotos de un edificio en particular"""
    model = Fotos
    template_name = 'fotos/fotos_administraciones_list.html'

    def get_queryset(self):
        # -- solo las fotos del edificio que llega como parametro de Url
        super(FotosAdministracionListView, self).get_queryset()
        return Fotos.objects.filter(edificio=self.kwargs['edificio']).all()


class FotosAdministracionCreateView(LoginRequiredMixin, FotosAdministracionMixin, CreateView):
    """Creacion de una nueva foto por parte de una administracion"""
    model = Fotos
    template_name = 'fotos/fotos_administraciones_form.html'
    fields = ('path', 'nombre', 'comentario', 'categoria')
    object = None
    success_msg = 'La foto se agregó con éxito.'

    def post(self, request, *args, **kwargs):
        # -- necesito antes indicarle a que edificio pertenece la foto
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.object = None

        if form.is_valid():
            form.instance.edificio_id = self.kwargs['edificio']
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})


class FotosAdministracionUpdateView(LoginRequiredMixin, FotosAdministracionMixin, UpdateView):
    """Edicion de una foto por parte de una administracion"""
    model = Fotos
    template_name = 'fotos/fotos_administraciones_form.html'
    fields = ('path', 'nombre', 'comentario', 'categoria')
    success_msg = 'La foto se modificó con éxito.'


class FotosAdministracionDeleteView(LoginRequiredMixin, FotosAdministracionMixin, DeleteView):
    model = Fotos
    template_name = 'fotos/fotos_administraciones_confirm_delete.html'
    success_msg = 'La foto se eliminó con éxito.'




