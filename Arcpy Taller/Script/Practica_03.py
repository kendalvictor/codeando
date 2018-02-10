# Importar la libreria del Arcgis
import arcpy

#Sobrescribir resultados
arcpy.env.overwriteOutput=True

#Declaramos variables locales
CapaEntrada=arcpy.GetParameterAsText(0)
CapaSalida=arcpy.GetParameterAsText(1)
Distancia=arcpy.GetParameterAsText(2)

#Herramienta de geoproceso
arcpy.Buffer_analysis(CapaEntrada,CapaSalida,Distancia)

#Impresion en pantalla de finalizado
arcpy.AddMessage("script finalizado"€œ)