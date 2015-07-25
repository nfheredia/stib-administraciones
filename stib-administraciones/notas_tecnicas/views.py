# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import NotasTecnicas
from .forms import NotasTecnicasCreateForm


class NotasTecnicasCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    """
    Vista para la Creación de una Nota Técnica
    """
    model = NotasTecnicas
    form_class = NotasTecnicasCreateForm
    raise_exception = True
