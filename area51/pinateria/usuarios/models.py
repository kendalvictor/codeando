from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        User,
        models.CASCADE,
        related_name='perfil'
    )

    dni = models.CharField(
        max_length=8,
        blank=False,
        null=False
    )

    ruc = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    direccion = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.usuario.username
