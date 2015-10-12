# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib import messages
from django.core.mail import EmailMessage
from braces.views import LoginRequiredMixin
from ..settings_local import STIB_TO_EMAIL
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

        mail = EmailMessage(subject='Nuevo Feedback - '+form.instance.tipo_feedback.nombre,
                            from_email=self.request.user.perfil.email_1,
                            to=STIB_TO_EMAIL)
        mail.body = form.instance.mensaje
        mail.send()

        return super(FeedbacksCreate, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        # -- antes que nada, validamos si el usuario
        # -- tiene configurado su perfil
        if self.request.user.perfil.alerta_bienvenida == 1:
            msg = "Para poder enviarnos tu feedback, antes debe\
                <a href='/perfiles/update'>completar sus datos de perfil</a>."
            messages.error(self.request, msg)
            return HttpResponseRedirect('/feedbacks/create/')

        return super(FeedbacksCreate, self).post(request, *args, **kwargs)

