import arcpy

arcpy.env.overwriteOutput=True

arcpy.env.workspace = r"C:\compartir\Curso Python\GDB\Dia4.gdb"

consulta = '"COD_ESTAC" like \'3%\''

capatemporal = arcpy.MakeFeatureLayer_management("Estaciones","Estaciones_Layer")

arcpy.SelectLayerByAttribute_management(capatemporal, "NEW_SELECTION", consulta)

contarestaciones = arcpy.GetCount_management(capatemporal)

arcpy.CopyFeatures_management(capatemporal, "Estaciones_3x")

arcpy.Delete_management(capatemporal)

print("El numero de estaciones es: " + str(contarestaciones))
