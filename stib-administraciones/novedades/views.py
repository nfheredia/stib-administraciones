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

