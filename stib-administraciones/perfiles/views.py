# -*- coding: utf-8 -*-

import json
from django.views.generic import UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

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


@staff_member_required
def get_autocomplete_nombre_comercial(request):
    """
    Busqueda de perfiles a través de su 'Nombre Comercial',
    se utiliza en una llamada ajax en el formulario
    para auto-sugerir el resultado.
    NOTA: Solo debe mostrar las sugerencias para perfiles
    que no son de usuarios staff
    """
    # -- término a buscar --
    q = request.GET['term']

    perfiles = Perfiles.objects.filter(nombre_comercial__icontains=q, user__is_staff=False)

    result_list = []

    for perfil in perfiles:
        result_temp = {}
        result_temp['id'] = perfil.id
        result_temp['user_id'] = perfil.user_id
        result_temp['label'] = perfil.nombre_comercial
        result_list.append(result_temp)

    return HttpResponse(json.dumps(result_list), mimetype='application/json')