# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from braces.views import LoginRequiredMixin

from .models import Servicios


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


class ServiciosTagsListView(LoginRequiredMixin, ServiciosMixin, ListView):
    """ Filtrado por tags """
    model = Servicios

    def get_queryset(self):
        return Servicios.objects.\
            filter(tags__slug__in=[self.kwargs['tag']]).\
            distinct()