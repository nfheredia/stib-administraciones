from django.shortcuts import render
from django.views.generic import ListView
from braces.views import LoginRequiredMixin

from .models import Novedades


class NovedadesListView(LoginRequiredMixin, ListView):
    model = Novedades
