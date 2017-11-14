# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.utils.encoding import python_2_unicode_compatible

from logging import getLogger
log = getLogger('django')

from django.contrib.auth.models import User
from .managers import CustomAuthCliente, CustomSuperCliente


class Cliente(User):

    objects = CustomAuthCliente()

    def __str__(self):
        return u'{0}:{1}'.format(self.username, self.email)

    def nombres(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_superuser = False
        super(Cliente, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'


class SuperCliente(User):

    objects = CustomSuperCliente()

    def __str__(self):
        return u'{0}:{1}'.format(self.username, self.email)

    def nombres(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_superuser = True
        super(SuperCliente, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = u'Super Cliente'
        verbose_name_plural = u'Super Clientes'