# Script que realiza el buffer a 6 km de distancia de un shapefile
'''
Programa realizado por: Richard Flores
Periodo: 2016
'''

# Importamos la libreria del Arcgis
import arcpy

#Sobrescribir resultados
arcpy.env.overwriteOutput=True

#Declaramos una variable de entorno
arcpy.env.workspace=r"C:\compartir\Curso Python\Shapefiles"

#Declaramos variables locales
CapaEntrada="SuperMercado.shp"
CapaSalida="SuperMercadoBuffer6km.shp"
Distancia="6 kilometers"

#Herramienta de geoproceso
arcpy.Buffer_analysis(CapaEntrada,CapaSalida,Distancia)

#Impresion en pantalla de finalizado
print "script finalizado"