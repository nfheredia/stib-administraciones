# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.contrib import messages
from braces.views import LoginRequiredMixin

from ..settings_local import STIB_FROM_EMAIL
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


def pedir_cotizacion(request, pk):
    """
    - Envio de email para el pedido de una cotizacion
    - Hay que tener en cta que la administracion debe
    tener completo su perfil..
    """
    if request.user.perfil.alerta_bienvenida == 1:
        msg = "Para poder solictar una cotización, antes debe\
            <a href='/perfiles/update'>completar sus datos de perfil</a>."
        messages.error(request, msg)
        return HttpResponseRedirect('/productos/'+pk)

    producto = Productos.objects.get(id=pk)
    mail = EmailMessage(subject='Pedido de cotizacion del producto "'+producto.nombre+'"',
                        from_email=request.user.perfil.email_1,
                        to=STIB_FROM_EMAIL)
    mail.body = '"'+request.user.perfil.nombre + '" solicita cotizacion del producto "'+producto.nombre+'"'
    mail.send()
    messages.success(request, "Hemos recibido tu pedido de cotización, \
                        a la brevedad nos pondremos en contacto.")
    return HttpResponseRedirect('/productos/'+pk)
