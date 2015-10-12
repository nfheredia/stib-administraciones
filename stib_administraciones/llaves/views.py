# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import TipoLlavesForm
from .models import Llaves
from ..edificios.models import Edificios
from ..core.views import permisos_a_edificios
from ..settings_local import STIB_TO_EMAIL


@login_required(redirect_field_name='accounts/login/')
@permisos_a_edificios
def set_llaves(request, edificio):
    """
    Vista para asignar llaves a los edificios
    """
    # -- obtengo las laves del edificio
    llaves_edificios = Llaves.objects.filter(edificio=edificio).all()

    # -- check initial data
    initial_data = {}
    if llaves_edificios:
        for llave in llaves_edificios:
            initial_data[str(llave.tipo_llave_id)]=1

    ctx = {
        'form': TipoLlavesForm(prefix='llaves', initial=initial_data),
        'edificio': Edificios.objects.get(pk=edificio)
    }

    if request.method == "POST":
        # -- obtengo en una lista todos los tipos de llaves selccionados
        tipo_llaves = request.POST.getlist("llaves-tipo_llaves")
        # -- limpio las llaves del edifico
        Llaves.objects.filter(edificio=edificio).delete()
        # -- asigno una x una las llaves seleccionadas
        for tipo in tipo_llaves:
            llaves = Llaves()
            llaves.tipo_llave_id = tipo
            llaves.edificio_id = edificio
            llaves.save()

        # -- han ingresado un comentario??
        if request.POST.get('llave_comentario'):
            return enviar_comentario(request, edificio)
        else:
            messages.success(request, 'Se han asignado las llaves correctamente.')
            return redirect('edificios:administraciones', edificio)

    return render(request, 'llaves/llaves_form.html', ctx)


def enviar_comentario(request, edificio):
    """
    Envío por email de comentario sobre llaves.
    """
    if request.user.perfil.alerta_bienvenida:
        msg = "Para poder dejar un comentario sobre las llaves. primero debes \
            <a href='/perfiles/update'>completar sus datos de perfil</a>."
        messages.error(request, msg)
        return redirect('edificios:administraciones', edificio)

    cliente = Edificios.objects.get(pk=edificio)

    # -- Nombre de la administracion
    administracion = request.user.perfil.nombre
    if administracion == "":
        administracion = '<Nombre Desconocido>'

    ctx = {
        'administracion': administracion,
        'edificio_nombre': cliente.nombre,
        'edificio_direccion': cliente.direccion,
        'consulta': request.POST.get('llave_comentario')
    }
    body = render_to_string('emails/comentario_llaves.html', ctx)
    email = EmailMessage(from_email=request.user.perfil.email_1,
                         subject='Comentario de llaves',
                         to=STIB_TO_EMAIL,
                         body=body)
    email.content_subtype = 'html'
    email.send()

    messages.success(request, 'Se recibió correctamente su comentario y configuración de llaves.')
    return redirect('edificios:administraciones', edificio)
