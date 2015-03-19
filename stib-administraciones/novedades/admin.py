from django.contrib import admin
from imperavi.admin import ImperaviAdmin
from .models import Novedades


class NovedadesAdmin(ImperaviAdmin):
    """
    Es necesario agregarle el editor imperavi
    """
    pass


admin.site.register(Novedades, NovedadesAdmin)
