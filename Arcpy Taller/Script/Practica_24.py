import arcpy

arcpy.env.overwriteOutput=True

ruta=r"C:\compartir\Curso Python\Shapefiles"
#ruta=sys.argv[1]
prediosrurales=ruta+"\\PrediosRurales.shp"
hoja=ruta+"\\P_Indice_25000.shp"
expresion=""""COD_25000" = '37v3NO'"""
nuevacapa=ruta+"\\PrediosHoja37v3NO.shp"
arcpy.Select_analysis(hoja,"in_memory\hoja_lyr",expresion)
arcpy.MakeFeatureLayer_management(prediosrurales,"prediosrurales_lyr")
arcpy.SelectLayerByLocation_management("prediosrurales_lyr","INTERSECT","in_memory\hoja_lyr","","NEW_SELECTION")
#arcpy.Clip_analysis("prediosrurales_lyr","in_memory\hoja_lyr",nuevacapa)
arcpy.CopyFeatures_management("prediosrurales_lyr",nuevacapa)
arcpy.Delete_management("in_memory\hoja_lyr")
arcpy.Delete_management("prediosrurales_lyr")
print "fin"