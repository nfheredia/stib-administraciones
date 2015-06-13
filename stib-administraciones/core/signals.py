from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from ..contactos.models import Contactos
from ..horarios.models import Horarios
from ..llaves.models import Llaves
from ..settings_local import STIB_TO_EMAIL


@receiver(post_save, sender=Contactos)
@receiver(post_delete, sender=Contactos)
@receiver(post_save, sender=Llaves)
@receiver(post_delete, sender=Llaves)
@receiver(post_save, sender=Llaves)
@receiver(post_delete, sender=Llaves)
@receiver(post_save, sender=Horarios)
@receiver(post_delete, sender=Horarios)
def enviar_email_sincronizacion(sender, instance, **kwargs):
    """
    Cada vez que se ejecuta una actividad de 'alta', 'edicion' o 'borrado'
    sobre algunas entidades, el personal de Stib van a recibir un email
    con el detalle.
    """
    if kwargs.get('created', False):
        return

    # -- Entidad sobre la que se realiza un evento (Contacto, llaves o horarios)
    entidad = sender.__name__
    # -- Nombre del edificio
    edificio = instance.edificio
    # -- Nombre de la administracion
    administracion = instance.edificio.user.perfil.nombre
    if administracion == "":
        administracion = '<Nombre Desconocido>'

    # -- Evento que se ejecuta (Edicion, alta o eliminacion)
    evento = instance.get_status
    if evento is 'new':
        evento = 'Alta'
    elif evento is 'edited':
        evento = 'Edicion'
    elif evento is 'deleted':
        evento = 'Borrado'

    # -- Detalle
    detalle = _get_detalle(entidad, instance)

    # -- Envio por email
    ctx = {
        'administracion': administracion,
        'edificio': edificio,
        'entidad': entidad,
        'evento': evento,
        'detalle': detalle
    }

    body = render_to_string('emails/email_sincronizacion.html', ctx)
    msg = EmailMessage(from_email='no-reply@stibadministraciones.com',
                       subject='[STIB ADMINISTRACIONES] - Registro de actividad',
                       to=STIB_TO_EMAIL,
                       body=body)
    msg.content_subtype='html'
    msg.send()


def _get_detalle(entidad, instance):
    """
    Armamos el detalle que se enviara por email
    """
    detalle = {}
    if entidad == 'Contactos':
        detalle = {
            'contacto': instance.nombre,
            'piso': instance.piso,
            'departamento': instance.departamento
        }
    elif entidad == 'Llaves':
        detalle = {
            'llave': instance.tipo_llave
        }
    elif entidad == 'Horarios':
        detalle = {
            'personal': instance.personales,
            'hora_desde': instance.hora_desde,
            'hora_hasta': instance.hora_hasta,
            'lunes': 'Si' if instance.lunes else 'No',
            'martes': 'Si' if instance.martes else 'No',
            'miercoles': 'Si' if instance.miercoles else 'No',
            'jueves': 'Si' if instance.jueves else 'No',
            'viernes': 'Si' if instance.viernes else 'No',
            'sabado': 'Si' if instance.sabado else 'No',
            'domingo': 'Si' if instance.domingo else 'No'
        }
    return detalle