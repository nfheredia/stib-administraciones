# -*- coding: utf-8 -*-
from .forms import FormDefinirTipoComunicacion
from django.views.generic import FormView, CreateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import RelacionesUsuariosProductos


class EstableverTipoComunicacion(LoginRequiredMixin, StaffuserRequiredMixin, FormView):
    """
    Vista que presentara un formulario
    para definir el tipo de comunicacion
    """
    template_name = 'relaciones/establecer_tipo_comunicacion.html'
    form_class = FormDefinirTipoComunicacion

    def form_valid(self, form):
        """
        Armamo la Url encargada de redirigir a la pantalla
        adecuada para enviar la notificacion
        """
        entidad = form.cleaned_data["entidad"]
        destinatario = form.cleaned_data["destinatario"]
        self.success_url = entidad + "-" + destinatario
        return super(EstableverTipoComunicacion, self).form_valid(form)


class NotificarUsuariosProductos(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	"""
	Notificar a usuarios sobre determinados
	productos
	"""
	template_name = 'relaciones/notificar_usuarios_productos.html'
	model = RelacionesUsuariosProductos
	    
