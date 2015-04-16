from django.shortcuts import render
from django.views.generic import ListView, DetailView
from braces.views import LoginRequiredMixin

from .models import Novedades


class NovedadesListMixin(object):
    def get_context_data(self, **kwargs):
        """
        Devolvemos todas las tags para todas las vistas del tipo ListView
        """
        context = super(NovedadesListMixin, self, **kwargs).get_context_data(**kwargs)
        context['tags'] = self.model.tags.all()
        return context


class NovedadesListView(LoginRequiredMixin, NovedadesListMixin, ListView):
    """
    Lista todas las novedades
    """
    model = Novedades

    def get_queryset(self):
        queryset = super(NovedadesListView, self).get_queryset()

        # -- ingreso por el formulario de busqueda??
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(contenido__icontains=q).all()

        return queryset


class NovedadesDetailView(LoginRequiredMixin, DetailView):
    """
    Muestra una novedad en particular
    """
    model = Novedades


class NovedadesTagsListView(LoginRequiredMixin, NovedadesListMixin, ListView):
    """
    Filtro de novedades por los 'tags'
    """
    model = Novedades
    template_name = 'novedades/novedades_list.html'

    def get_queryset(self):
        tag = self.kwargs['tag']
        tag_filter = Novedades.objects.filter(
            tags__slug__in=[tag]
        ).distinct()
        return tag_filter




