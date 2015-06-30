from django import template

register = template.Library()

@register.filter
def icon_by_boolean(value):
    if value:
        return '<i class="fa fa-check"></i>'
    else:
        return '<i class="fa fa-times"></i>'
