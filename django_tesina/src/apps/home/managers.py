# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomAuthCliente(BaseUserManager):

    def get_queryset(self):
        return super(CustomAuthCliente,
                     self).get_queryset().filter(
            is_staff=False,
            is_superuser=False,
        )


class CustomSuperCliente(BaseUserManager):

    def get_queryset(self):
        return super(CustomSuperCliente,
                     self).get_queryset().filter(
            is_staff=False,
            is_superuser=True,
        )
