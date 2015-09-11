from django.contrib import admin
from imperavi.admin import ImperaviAdmin
from .models import Servicios, ServiciosFotos


class ServiciosAdmin(ImperaviAdmin):
    """
    Se le agregar el editor de texto imperavi
    """
    pass


admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(ServiciosFotos)
