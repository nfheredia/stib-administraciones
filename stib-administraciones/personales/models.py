from django.db import models
from ..core.models import TimeStampedModel


class Personales(TimeStampedModel):
    """
    Modelo para almacenar los diferentes
    tipos de personales que trabajan en un edificio.
    Ej: Portero, Limpieza, Seguridad
    """
    nombre = models.CharField(blank=False,
                              max_length=150,
                              null=False,
                              verbose_name='Tipo de Personal',
                              help_text='Ej: Portero, Limpieza, Seguridad',
                              unique=True)
    comentario = models.TextField(blank=True, verbose_name='Comentario')

    def __str__(self):
        """ Muestro el nombre """
        return self.nombre

    class Meta:
        verbose_name = 'Personal de edificios'
        verbose_name_plural = 'Personal de edificios'
