from django.shortcuts import render
from django.views.generic import ListView, DetailView
from braces.views import LoginRequiredMixin

from .models import Novedades


class NovedadesListView(LoginRequiredMixin, ListView):
    """
    Lista todas las novedades
    """
    model = Novedades


class NovedadesDetailView(LoginRequiredMixin, DetailView):
    """
    Muestra una novedad en particular
    """
    model = Novedades


class NovedadesTagsListiView(LoginRequiredMixin, ListView):
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


