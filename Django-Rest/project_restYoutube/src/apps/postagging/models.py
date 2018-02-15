# -*- coding: utf-8 -*-
from django.db import models
from apps.core.fields import TimeStampedModel


class PalabraDialecto(TimeStampedModel):
    palabra = models.CharField("Palabra", max_length=300, null=True,
                               blank=True)
    significado = models.CharField("Significado", max_length=100, null=True,
                                   blank=True)

    def __unicode__(self):
        return "{0} - {1}".format(self.palabra, self.significado)


class DirectorioAncora(TimeStampedModel):
    nombre = models.CharField("Nombre", max_length=300, null=True, blank=True)
    procesado = models.BooleanField("Proceso", default=False)

    def __unicode__(self):
        return "{0}".format(self.nombre)


class PalabraCorpus(TimeStampedModel):
    nombre = models.CharField("Nombre", max_length=300, null=True, blank=True)
    cant = models.IntegerField(default=0)
    noun = models.IntegerField(default=0)
    adj = models.IntegerField(default=0)
    det = models.IntegerField(default=0)
    verb = models.IntegerField(default=0)
    conj = models.IntegerField(default=0)
    inter = models.IntegerField(default=0)
    pron = models.IntegerField(default=0)
    adv = models.IntegerField(default=0)
    prep = models.IntegerField(default=0)

    def __unicode__(self):
        return "{0}".format(self.nombre)


class TagCorpus(TimeStampedModel):
    nombre = models.CharField("Nombre", max_length=300, null=True, blank=True)
    codigo = models.CharField("Nombre", max_length=10, null=True, blank=True)
    cant = models.IntegerField(default=0)
    noun = models.IntegerField(default=0)
    adj = models.IntegerField(default=0)
    det = models.IntegerField(default=0)
    verb = models.IntegerField(default=0)
    conj = models.IntegerField(default=0)
    inter = models.IntegerField(default=0)
    pron = models.IntegerField(default=0)
    adv = models.IntegerField(default=0)
    prep = models.IntegerField(default=0)

    def __unicode__(self):
        return "{0}".format(self.nombre)
