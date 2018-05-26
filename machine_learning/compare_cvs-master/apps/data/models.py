# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Curriculum(models.Model):
    #Datos del csv
    empresa = models.CharField('Empresa', max_length=100, blank=True, null=True)
    nombres = models.CharField('Nombre', max_length=100, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    formacion_inicial_anio = models.CharField('Formación desde anio', max_length=10, blank=True, null=True)
    formacion_ultima_anio = models.CharField('Formación hasta anio', max_length=10, blank=True, null=True)
    institucion = models.CharField('Institucion', max_length=100, blank=True, null=True)
    cargo = models.CharField('Cargo', max_length=100, blank=True, null=True)
    puesto = models.CharField('Puesto', max_length=100, blank=True, null=True)
    sexo = models.CharField('Sexo', max_length=10, blank=True, null=True)
    ruta_cv = models.CharField('Ruta del CV', max_length=200, blank=True, null=True)
    nivel_estudio = models.CharField('Nivel de estudio', max_length=100, blank=True, null=True)
    area_estudio = models.CharField('Area de estudio', max_length=100, blank=True, null=True)
    #Datos del algoritmo
    algoritmo_nombre_doc = models.CharField('Nombre del archivo', max_length=100)
    algoritmo_texto = models.TextField('Texto')
    algoritmo_numero_paginas = models.IntegerField('Numero de páginas', blank=True, null=True)
    algoritmo_formato_documento = models.CharField('Formato del documento', max_length=100)
    algoritmo_numero_saltos_linea = models.IntegerField('Numero de saltos de linea', blank=True, null=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.apellidos, self.nombres)

    class Meta:
        verbose_name = 'Curriculum'
        verbose_name_plural = 'Curriculums'


class DataCurriculum(models.Model):
    formato_documento = models.CharField('Formato del documento', max_length=100, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=100, blank=True, null=True)
    fecha_revision = models.DateTimeField('Fecha de revisión')
    nombre_documento = models.CharField('Nombre del archivo', max_length=100, blank=True, null=True)
    puntaje_nombre_documento = models.IntegerField('Puntaje nombre documento')
    email = models.EmailField('Email', blank=True, null=True)
    seccion_laboral = models.TextField('Sección laboral', blank=True, null=True)
    tiene_experiencia = models.BooleanField('TIene experiencia', default=False)
    seccion_estudios = models.TextField('Sección estudios', blank=True, null=True)
    tiene_estudios = models.BooleanField('Tiene estudios', default=False)
    puntaje_orden_estructura = models.IntegerField('Puntaje Orden Estructura', blank=True, null=True)
    frases_innecesarias = models.TextField('Frases innecesarias', blank=True, null=True)
    puntaje_frases_innecesarias = models.IntegerField('Puntaje Frases Innecesarias', blank=True, null=True)
    numero_lineas = models.IntegerField('Numero de lineas', blank=True, null=True)
    numero_paginas = models.IntegerField('Numero de paginas', blank=True, null=True)
    puntaje_longitud = models.IntegerField('Puntaje longitud', blank=True, null=True)
    antiguedad_laboral = models.CharField('Antiguedad laboral', max_length=100, blank=True, null=True)
    puntaje_antiguedad_laboral = models.IntegerField('Puntaje antiguedad laboral', blank=True, null=True)
    fechas_trabajo = models.TextField('Fechas trbajo', blank=True, null=True)
    permanencia_anios = models.TextField('Lista permanencia años', blank=True, null=True)
    puntaje_permanencia_promedio = models.IntegerField('Puntaje permanencia promedio', blank=True, null=True)
    puntaje_orden_cronologico = models.IntegerField('Puntaje orden cronologico', blank=True, null=True)
    verbos_accion = models.TextField('Verbos accion', blank=True, null=True)
    puntaje_verbos_accion = models.IntegerField('Puntaje verbos accion', blank=True, null=True)
    numeros = models.TextField('Numeros', blank=True, null=True)
    puntaje_numeros = models.IntegerField('Puntaje Numeros', blank=True, null=True)
    texto = models.TextField('Texto', blank=True, null=True)
    tokenized_job_section = models.TextField('Tokenized job section', blank=True, null=True)
    new_job_text = models.TextField('New job text', blank=True, null=True)

    class Meta:
        verbose_name = "Data Curriculum"
        verbose_name_plural = "Data Curriculums"

    def __str__(self):
        return self.nombre_documento
