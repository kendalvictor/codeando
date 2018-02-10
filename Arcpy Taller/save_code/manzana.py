# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Python para ArcGIS\GDB\curso_python.gdb"


capa_temporal = arcpy.MakeFeatureLayer_management(
    "PuntoReferencia", "PuntoReferencia_lyr")

expresion = "CodigoTipoReferencia = 10"

list_fc = arcpy.SelectLayerByAttribute_management(capa_temporal, "NEW_SELECTION", expresion)

arcpy.SelectLayerByLocation_management(capa_temporal, 'INTERSDECT', 'Manzana', "", "NEW_SELECTION")

arcpy.Delete_management(capa_temporal)


print "PROCESO CONCLUIDO"

