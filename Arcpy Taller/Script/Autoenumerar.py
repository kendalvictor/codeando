# Script que autoenumera
'''
Programa realizado por: CAEG
Periodo: 2015
'''

# Importamos la libreria del Arcgis
import arcpy

#Sobre escribir resultados
#arcpy.env.overwriteOutput=True

#Declaramos una variable de entorno
#arcpy.env.workspace=r"D:\Geotaller\GDB\Practica.gdb"

entidad=arcpy.GetParameterAsText(0)
campo="id"

for fc in entidad.split(';'):
    arcpy.AddField_management(fc, campo, "TEXT", "", "", "6")
 
bloquecodigo="""rec=0
def autoIncrement():
    global rec
    pStart = 1
    pInterval = 1
    if (rec == 0):
        rec = pStart
    else:
        rec += pInterval
    return str(rec).zfill(6)"""
expresion="autoIncrement()"

for fc in entidad.split(';'):
    arcpy.CalculateField_management(fc,campo,expresion,"PYTHON_9.3",bloquecodigo)


print "Script terminado"