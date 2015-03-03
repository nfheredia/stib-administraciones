# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import TipoRelaciones
from .models import RelacionesEdificiosProductos
from .models import RelacionesEdificiosServicios
from .models import RelacionesUsuariosProductos
from .models import RelacionesUsuariosServicios

admin.site.register(TipoRelaciones)
admin.site.register(RelacionesEdificiosProductos)
admin.site.register(RelacionesEdificiosServicios)
admin.site.register(RelacionesUsuariosProductos)
admin.site.register(RelacionesUsuariosServicios)