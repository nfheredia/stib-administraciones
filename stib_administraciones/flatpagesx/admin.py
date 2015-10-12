# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from imperavi.admin import ImperaviAdmin
from .models import FlatPagesX


class CustomFlatPageAdmin(ImperaviAdmin):
    # -- formulario con WYSIWYG editor
    # -- simplifico los campos a mostrar
    exclude = ['enable_comments', 'template_name', 'registration_required']

# -- quito el modelo de las flatpages original
admin.site.unregister(FlatPage)
# -- registro el flatpagex extendido y form con editor WYSIWYG
admin.site.register(FlatPagesX, CustomFlatPageAdmin)