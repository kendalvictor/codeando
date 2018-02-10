# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# prueba.py
# Created on: 2018-02-03 10:53:25.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Python para ArcGIS\SHP"
# Local variables:
SuperMercado_shp = "SuperMercado.shp"
Distance__value_or_field_ = "20 Kilometers"
Output_Feature_Class = r"SuperMercado_20kmm.shp"
#Puede ser .GDB .mdb SDE(Postgresql, Oracle, Sql)

# Process: Buffer
arcpy.Buffer_analysis(
    SuperMercado_shp,
    Output_Feature_Class,
    Distance__value_or_field_
)

print ".....", Output_Feature_Class, " CREADO"