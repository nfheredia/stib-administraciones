# -*- coding: utf-8 -*-

from braces.views import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib import messages
from .models import Feedbacks


class FeedbacksCreate(LoginRequiredMixin, CreateView):
    """
    Creacion de un nuevo feedback
    """
    model = Feedbacks
    fields = ['tipo_feedback', 'asunto', 'mensaje']
    success_url = '/inicio/'

    def form_valid(self, form):
        # -- necesito indicarle el usuario que crea el feedback
        form.instance.user = self.request.user
        form.save()
        # -- msg de Gracias
        messages.success(self.request, u'Muchas gracias por dejarnos tu feedback.')
        return super(FeedbacksCreate, self).form_valid(form)
