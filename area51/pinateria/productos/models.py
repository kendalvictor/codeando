from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=15,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    personaje = models.CharField(
        max_length=40,
        blank=False,
        null=False
    )

    nombre_comercial = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    precio = models.DecimalField(
        max_digits=15,
        decimal_places=5,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.personaje


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto,
        models.CASCADE,
        blank=False,
        null=False,
        # related_name='imagenes'
    )

    imagen = models.ImageField(
        upload_to='productos',
        blank=False,
        null=False
    )

    def __str__(self):
        return self.producto.personaje
