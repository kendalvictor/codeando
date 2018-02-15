# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    fecha_creada = models.DateField(auto_now_add=True, null=True, blank=True)
    fecha_modificada = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

