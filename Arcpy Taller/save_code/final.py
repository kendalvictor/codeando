# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Python para ArcGIS\GDB\curso_python.gdb"


capa_temporal = arcpy.MakeFeatureLayer_management("Estaciones", "Estaciones_lyr")

expresion = "COD_ESTAC like '3%'"

list_fc = arcpy.SelectLayerByAttribute_management(capa_temporal, "NEW_SELECTION", expresion)

arcpy.CopyFeatures_management(capa_temporal, "Estaciones_3")

arcpy.Delete_management(capa_temporal)


print "PROCESO CONCLUIDO"


