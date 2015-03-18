# -*- coding: utf-8 -*-

from django.views.generic import UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect

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
        return self.success_url

    def form_valid(self, form):
        """
        Cuando se actualiza el perfil,
        no se debe mostrar mas el msg
        de bienvenida para editar el perfil
        """
        form.instance.alerta_bienvenida = 0
        return super(PerfilesUpdateView, self).form_valid(form)


def no_mostrar_msg_bienvenida(request):
    """
    Marcar en 0 el campo para no mostrar mas
    el msg de bienvenida en el perfil
    del usuario logueado...
    """
    perfil = Perfiles.objects.get(user=request.user.id)
    perfil.alerta_bienvenida = 0
    perfil.save()
    return HttpResponseRedirect('/')