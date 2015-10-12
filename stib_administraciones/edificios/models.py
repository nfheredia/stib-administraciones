# -*- coding: utf-8 -*-
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from ..users.models import User

from ..core.models import TimeStampedModel


class EdificiosUsuariosManager(models.Manager):

    def por_usuarios(self, user_id):
        return super(EdificiosUsuariosManager, self).get_queryset().filter(user=user_id)

    def por_edificio(self, user_id, edificio_id):
        return self.por_usuarios(user_id).filter(id=edificio_id)


class Edificios(TimeStampedModel):
    """
    Edificios, los mismos pertenecen a las diferentes
    administraciones/usuarios
    """
    user = models.ForeignKey(User, verbose_name=u"Usuario",
                                help_text="Administración a la cual pertenece el edificio")
    nombre = models.CharField(blank=False, max_length=150, verbose_name=u"Nombre del edificio")
    codigo = models.CharField(blank=False, max_length=150, verbose_name=u"Código")
    direccion = models.CharField(blank=False, max_length=150, verbose_name=u"Dirección")
    foto_fachada = ThumbnailerImageField(null=True, blank=True, upload_to='edificios_fachadas', verbose_name=u"Imágen de fachada")
    cantidad_pisos = models.IntegerField(blank=True, null=True, max_length=2, verbose_name=u"Cantidad de pisos")
    cantidad_unidades = models.IntegerField(blank=True, null=True, max_length=2,  verbose_name=u"Cantidad de unidades")
    comentario = models.TextField(blank=True, null=True, verbose_name=u"Comentarios")

    # managers
    objects = models.Manager()
    edificios_usuarios_object = EdificiosUsuariosManager()

    def get_absolute_url(self):
        return '/edificios'

    @classmethod
    def usuario_por_edificio(cls, edificio_id):
        """
        obtenemos el usuaro de un edificio en particular
        """
        result = cls.objects.values('user').get(pk=edificio_id)
        return result['user']

    def __unicode__(self):
        return self.nombre + ' - ' + self.direccion

    class Meta:
        verbose_name = 'Edificios'
        verbose_name_plural = 'Edificios'
