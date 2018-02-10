# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Python para ArcGIS\GDB\curso_python.gdb"

list_fc = arcpy.ListFeatureClasses()

dicc_options = {
    "Point": "10 Meters",
    "Polyline": "6 Meters",
    "Polygon": "-2 Meters",
}

for fc in list_fc:
    if '_Buffer' not in fc:
        desc = arcpy.Describe(fc)
        distancia = dicc_options.get(desc.shapeType, "5 Meters")
        salida = fc + '_Buffer'
        print(salida, distancia)
        arcpy.Buffer_analysis(fc, salida, distancia)

print "PROCESO CONCLUIDO"


