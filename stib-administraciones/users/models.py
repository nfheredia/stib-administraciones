# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser
from django.db import models




# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
