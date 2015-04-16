# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from braces.views import LoginRequiredMixin

from .models import Productos


class ProductosMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(ProductosMixin, self).get_context_data(**kwargs)
        ctx['tags'] = self.model.tags.all()
        return ctx


class ProductosListView(LoginRequiredMixin, ProductosMixin, ListView):
    """ Listado de productos """
    model = Productos

    def get_queryset(self):
        queryset = super(ProductosListView, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(descripcion__icontains=q).all()

        return queryset


class ProductosDetailView(LoginRequiredMixin, DetailView):
    """ Detalle de un productos """
    model = Productos


class ProductosTagsListView(LoginRequiredMixin, ProductosMixin, ListView):
    """ Filtrado por tags """
    model = Productos

    def get_queryset(self):
        return Productos.objects.\
            filter(tags__slug__in=[self.kwargs['tag']]).\
            distinct()