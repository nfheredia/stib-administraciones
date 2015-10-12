# -*- coding: utf-8 -*-
from model_utils.models import TimeStampedModel
from django.contrib.flatpages.models import FlatPage


class FlatPagesX(FlatPage, TimeStampedModel):
    class Meta:
        verbose_name = 'Páginas estáticas'
        verbose_name_plural = 'Páginas estáticas'
