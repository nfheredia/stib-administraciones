from django.contrib import admin

from django.contrib.flatpages.models import FlatPage
from .models import FlatPagesX
from imperavi.admin import ImperaviAdmin


class CustomFlatPageAdmin(ImperaviAdmin):
    pass


admin.site.unregister(FlatPage)
admin.site.register(FlatPagesX, CustomFlatPageAdmin)