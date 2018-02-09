# Generated by Django 2.0 on 2017-12-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personaje', models.CharField(max_length=40)),
                ('nombre_comercial', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
        ),
    ]
