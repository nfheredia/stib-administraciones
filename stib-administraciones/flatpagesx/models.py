from model_utils.models import TimeStampedModel
from django.db import models
from django.contrib.flatpages.models import FlatPage


class FlatPagesX(FlatPage, TimeStampedModel):
    pass
