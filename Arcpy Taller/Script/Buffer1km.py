# Script que realizael buffer a 1 km de distancia
'''
Programa realizado por: CAEG
Periodo: 2015
'''

# Importamos la libreria del Arcgis
import arcpy

#Sobre escribir resultados
arcpy.env.overwriteOutput=True

#Declaramos una variable de entorno
arcpy.env.workspace=r"D:\Geotaller\GDB\Practica.gdb"

#Declararmos variables locales
CapaEntrada="Estaciones"
CapaSalida="EstacionesBuffer1km"
Distancia="1 kilometers"

#Herramienta de geoproceso
arcpy.Buffer_analysis(CapaEntrada,CapaSalida,Distancia)

#Impresion de finalizado
print "script finalizado"