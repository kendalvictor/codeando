import arcpy

arcpy.env.overwriteOutput=True
arcpy.env.workspace = r"C:\compartir\Curso Python\GDB\Dia4.gdb"

sqlmunicipio="CodigoTipoReferencia = '31'"
sqlventalicores="CodigoTipoReferencia = '91' or CodigoTipoReferencia = '92'"
distancia="500 meters"

capamunicipio=arcpy.MakeFeatureLayer_management("PuntoReferencia", "municipio_lyr", sqlmunicipio)
capaventalicores=arcpy.MakeFeatureLayer_management("PuntoReferencia", "ventalicores_lyr",sqlventalicores)

arcpy.SelectLayerByLocation_management(capaventalicores, "WITHIN_A_DISTANCE", capamunicipio, distancia, "NEW_SELECTION")

arcpy.SelectLayerByAttribute_management(capaventalicores, "SUBSET_SELECTION", sqlventalicores)

contarlocal = arcpy.GetCount_management(capaventalicores)
if contarlocal == 0:
    print('No existe intersecciones')
else:
    arcpy.CopyFeatures_management(capaventalicores, 'locales_500')
    arcpy.Delete_management(capamunicipio)
    arcpy.Delete_management(capaventalicores)
    print "La cantidad de locales a 500 metros es: " + str(contarlocal)
