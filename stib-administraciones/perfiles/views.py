# -*- coding: utf-8 -*-

from django.views.generic import UpdateView
from django.contrib import messages

from braces.views import LoginRequiredMixin

from .models import Perfiles
from .forms import PerfilesForm


class PerfilesUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar perfil del usuario logueado
    """
    form_class = PerfilesForm
    success_url = '/perfiles/update/'

    def get_object(self, queryset=None):
        return Perfiles.objects.get(user_id=self.request.user.id)

    def get_success_url(self):
        messages.success(self.request, u'Tu perfil fué editado correctamente.')
        return '/perfiles/update/'