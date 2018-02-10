# Importando modulo del ARCGIS
import arcpy

# sobre escribir la salida
arcpy.env.overwriteOutput=True

arcpy.env.workspace=r"D:\Publicidad cursos\Taller GDB\Python Dia 2\GDB\Dia2.gdb"

reddomiciliaria="reddomiciliaria"
areaafectada="areaafectada"
distancia="20 Meters"
predios="predios"
prediosafectados="prediosafectados"

arcpy.Buffer_analysis(reddomiciliaria,areaafectada,distancia,"FULL","FLAT","NONE","#")

arcpy.Clip_analysis(predios,areaafectada,prediosafectados,"#")

print "Visualizar resultados en el arcmap"