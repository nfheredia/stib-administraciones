# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import http
from django.conf import settings
from django.contrib import comments, messages
from django.contrib.comments import signals
from django.contrib.comments.views.utils import next_redirect, confirmation_view
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import escape
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from ..settings_local import STIB_TO_EMAIL


class CommentPostBadRequest(http.HttpResponseBadRequest):
    """
    Response returned when a comment post is invalid. If ``DEBUG`` is on a
    nice-ish error message will be displayed (for debugging purposes), but in
    production mode a simple opaque 400 page will be displayed.
    """
    def __init__(self, why):
        super(CommentPostBadRequest, self).__init__()
        if settings.DEBUG:
            self.content = render_to_string("comments/400-debug.html", {"why": why})


@csrf_protect
@require_POST
def post_comment(request, next=None, using=None):
    """
    Post a comment.

    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``comments/preview.html``, will be rendered.
    """
    # Fill out some initial data fields from an authenticated user, if present
    data = request.POST.copy()
    if request.user.is_authenticated():
        if not data.get('name', ''):
            data["name"] = request.user.get_full_name() or request.user.get_username()
        if not data.get('email', ''):
            data["email"] = request.user.email

    # Look up the object we're trying to comment about
    ctype = data.get("content_type")
    object_pk = data.get("object_pk")
    if ctype is None or object_pk is None:
        return CommentPostBadRequest("Missing content_type or object_pk field.")
    try:
        model = models.get_model(*ctype.split(".", 1))
        target = model._default_manager.using(using).get(pk=object_pk)
    except TypeError:
        return CommentPostBadRequest(
            "Invalid content_type value: %r" % escape(ctype))
    except AttributeError:
        return CommentPostBadRequest(
            "The given content-type %r does not resolve to a valid model." % \
                escape(ctype))
    except ObjectDoesNotExist:
        return CommentPostBadRequest(
            "No object matching content-type %r and object PK %r exists." % \
                (escape(ctype), escape(object_pk)))
    except (ValueError, ValidationError) as e:
        return CommentPostBadRequest(
            "Attempting go get content-type %r and object PK %r exists raised %s" % \
                (escape(ctype), escape(object_pk), e.__class__.__name__))


    # Construct the comment form
    form = comments.get_form()(target, data=data)

    # Check security information
    if form.security_errors():
        return CommentPostBadRequest(
            "The comment form failed security verification: %s" % \
                escape(str(form.security_errors())))

    # If there are errors
    if form.errors:
        messages.error(request, "Error al enviar su comentario, por favor complete todos los campos "
                                "del formulario.")
        return http.HttpResponseRedirect(request.POST.get('next'))


    # Otherwise create the comment
    comment = form.get_comment_object()
    comment.ip_address = request.META.get("REMOTE_ADDR", None)
    if request.user.is_authenticated():
        comment.user = request.user

    # Signal that the comment is about to be saved
    responses = signals.comment_will_be_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    for (receiver, response) in responses:
        if response == False:
            return CommentPostBadRequest(
                "comment_will_be_posted receiver %r killed the comment" % receiver.__name__)

    # Save the comment and signal that it was saved
    comment.save()
    signals.comment_was_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    _send_email(request)

    messages.success(request, "Gracias por su comentario, pronto responderemos su consulta.")
    return next_redirect(request, fallback=next or 'comments-comment-done',
        c=comment._get_pk_val())

comment_done = confirmation_view(
    template="comments/posted.html",
    doc="""Display a "comment was posted" success page."""
)


def _send_email(request):
    ctx = {}
    # -- si el comentario es enviado por un usuario no staff
    # -- se envia un mail al personal de STIB desde la cta de email
    # -- del usuario
    if request.user.is_staff is False:
        to_mail = STIB_TO_EMAIL
        from_mail = request.user.perfil.email_1
        ctx['nombre_comercial'] = request.user.perfil.nombre_comercial
    else:
        # -- si quien escribe/responde un comentario es un personal de STIB
        # -- se envia mail al usuario dueño del comentario
        to_mail = (request.POST.get('comment_owner_email'), )
        from_mail = "no-reply@stibadministraciones.com"

    subject = "[STIB] "
    if request.POST.get('content_type_id') == 46:
        subject += " Nota técnica - "
        ctx['tipo'] = "nota técnicas"
    else:
        subject += " Notificaciones - "
        ctx['tipo'] = "notificación"

    subject += " Nuevo Comentario"

    ctx['comentario_link'] = request.build_absolute_uri(request.POST.get('next'))

    body = render_to_string("emails/email_nuevo_comentario.html", ctx)
    email = EmailMessage(subject=subject,
                         body=body,
                         from_email=from_mail,
                         to=to_mail)
    email.content_subtype = 'html'
    email.send()
