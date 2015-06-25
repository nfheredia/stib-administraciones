# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import FormView, CreateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import FormDefinirTipoComunicacion, FormNotificacionUsuariosProductos
from .models import RelacionesUsuariosProductos
from ..productos.models import Productos


class EstableverTipoComunicacion(LoginRequiredMixin, StaffuserRequiredMixin, FormView):
    """
    Vista que presentara un formulario
    para definir el tipo de comunicacion
    """
    template_name = 'relaciones/establecer_tipo_comunicacion.html'
    form_class = FormDefinirTipoComunicacion

    def form_valid(self, form):
        """
        Armamos la Url encargada de redirigir a la pantalla
        adecuada para enviar la notificacion
        """
        entidad = form.cleaned_data["entidad"]
        destinatario = form.cleaned_data["destinatario"]
        self.success_url = entidad + "-" + destinatario
        return super(EstableverTipoComunicacion, self).form_valid(form)


class NotificarUsuariosProductos(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    """
    Notificar a usuarios(administraciones) sobre determinados
    productos
    """
    template_name = 'relaciones/notificar_usuarios_productos.html'
    model = RelacionesUsuariosProductos
    form_class = FormNotificacionUsuariosProductos

    def get_success_url(self):
        messages.success(self.request, 'La notificación se envió con éxito.')
        return reverse('notificaciones:definir')


def search_productos_autocomplete(request):
    """
    Busqueda de productos, se utiliza en una llamada
    ajax en el formulario para auto-sugerir el
    nombre de un producto
    """
    q = request.GET['term']
    productos = Productos.objects.filter(nombre__icontains=q).all()
    productos_list = []

    for producto in productos:
        dic_result = {}
        dic_result['id'] = producto.id
        dic_result['label'] = producto.nombre
        productos_list.append(dic_result)

    return HttpResponse(json.dumps(productos_list), mimetype="application/json")
