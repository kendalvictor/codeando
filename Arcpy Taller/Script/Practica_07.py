#Script que realiza un analisis espacial
'''
Programa realizado por: Richard Flores
Periodo: 2016
'''

import arcpy
arcpy.env.overwriteOutput=True
arcpy.env.workspace=r"C:\compartir\Curso Python\GDB\Dia2.gdb"
reddomiciliaria="reddomiciliaria"
areaafectada="areaafectada"
distancia="20 Meters"
predios="predios"
prediosafectados="prediosafectados"

arcpy.Buffer_analysis(reddomiciliaria,areaafectada,distancia,"FULL","FLAT","NONE","#")

arcpy.Clip_analysis(predios,areaafectada,prediosafectados,"#")

print 'Finalizado'