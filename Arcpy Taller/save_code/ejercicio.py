# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy

arcpy.env.overwriteOutput = True
work_space = r"D:\Python para ArcGIS\GDB\curso_python.gdb"
arcpy.env.workspace = work_space
list_filed = arcpy.ListFields("CentralesHidroelectricas")

with open("reporte.xls", "w") as doc_file:
    doc_file.write(
        "Reporte de Centrales Hidroelectricas \n " + "==="*10 + "\n"
    )
    for field in list_filed:
        linea = 'Campo  \t {0} \t Tipo de dato \t {1} \t Longitud \t {2}'.format(
            field.name, field.type, field.length
        )
        doc_file.write(linea + "\n")

print "REPORTE CONCLUIDO"


