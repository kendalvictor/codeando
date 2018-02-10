#Autor: Richard Flores
#Script: PrediosAfectados.py
#Descripcion: Script que identifica los predios afectados por una fuga de gas
#Fecha: 11 de marzo 2017

#importamos el modulo de ArcGIS
import arcpy

#Sobreescribir los resultados
arcpy.env.overwriteOutput=True

#Declara variable de entorno
arcpy.env.workspace=r"C:\Curso Python\Dia 2\GDB\Dia2.gdb"

#Declarar variables locales
redDomiciliaria="reddomiciliaria"
areaAfectada="areaafectada"
distancia="20 Meters"
predios="predios"
prediosAfectados="prediosafectados"

#Corremos primer analisis espacial
arcpy.Buffer_analysis(redDomiciliaria,areaAfectada,distancia,"FULL","FLAT","NONE","#")

#Corremos el segundo analisis espacial
arcpy.Clip_analysis(predios,areaAfectada,prediosAfectados,"#")

print "visualice el resultado en el ArcMAP"