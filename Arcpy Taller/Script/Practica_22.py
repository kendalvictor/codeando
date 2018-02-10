import arcpy

arcpy.env.overwriteOutput=True

arcpy.env.workspace = r"C:\compartir\Curso Python\GDB\Dia4.gdb"

consulta="CodigoTipoReferencia = '10'"

capatemporal=arcpy.MakeFeatureLayer_management("PuntoReferencia", "PuntoReferencia_lyr")

arcpy.SelectLayerByLocation_management(capatemporal, "INTERSECT", "Manzana", "", "NEW_SELECTION")

arcpy.SelectLayerByAttribute_management(capatemporal, "SUBSET_SELECTION", consulta)

contarcomedor = int(arcpy.GetCount_management(capatemporal).getOutput(0))

if contarcomedor == 0:
    print('No existe intersecciones')
else:
    arcpy.CopyFeatures_management(capatemporal, 'Comedores')
    arcpy.Delete_management(capatemporal)
    print "La cantidad de comedores intersectados es: " + str(contarcomedor)
