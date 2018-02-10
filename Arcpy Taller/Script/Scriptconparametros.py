# Script que permite el uso de parametros para el buffer
'''
Programa realizado por: CAEG
Periodo: 2015
'''

# Importamos la libreria del Arcgis
import arcpy

#Declarar los parametros de entrada
CapaEntrada=arcpy.GetParameterAsText(0)
CapaSalida=arcpy.GetParameterAsText(1)
Distancia=arcpy.GetParameterAsText(2)

#Herramienta de geoproceso
arcpy.Buffer_analysis(CapaEntrada,CapaSalida,Distancia)

#Impresion de finalizado
arcpy.AddMessage("Proceso finalizado")