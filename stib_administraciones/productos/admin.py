from django.contrib import admin
from imperavi.admin import ImperaviAdmin

from .models import Productos, ProductosFotos


class ProductosAdmin(ImperaviAdmin):
    """
    Se le agregar el editor de texto imperavi
    """
    pass

admin.site.register(Productos, ProductosAdmin)
admin.site.register(ProductosFotos)
