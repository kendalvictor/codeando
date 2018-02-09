from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from productos.models import Producto


class Pedido(models.Model):
    usuario = models.ForeignKey(
        User,
        models.CASCADE,
        blank=False,
        null=False
    )

    producto = models.ForeignKey(
        Producto,
        models.CASCADE,
        blank=False,
        null=False
    )

    cantidad = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1)]
    )

    estado = models.CharField(
        max_length=10,
        choices=(
            ('proceso', 'En proceso'),
            ('confirmado', 'Confirmado'),
            ('enviado', 'Enviado'),
            ('recibido', 'Recibido'),
            ('cancelado', 'Cancelado'),
        ),
        default='proceso',
        null=False
    )

    fecha_emision = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    @property
    def codigo(self):
        return 'PRO{:04d}'.format(self.id)

    def __str__(self):
        return self.codigo
