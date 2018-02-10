import arcpy
#sobrescribir la salida
arcpy.env.overwriteOutput = True
#Variable de entorno
arcpy.env.workspace = r"C:\compartir\Curso Python\GDB\Practica.mdb"
#Nueva variable de entorno
rutadesalida=r"C:\compartir\Curso Python\Shapefiles"
#Lista de Feature Class
listadefeatureclass = arcpy.ListFeatureClasses()
#Recorrer la lista
for fc in listadefeatureclass:
	capanueva=rutadesalida+"\\"+fc+".shp"
	#Herramienta de geoproceso
	arcpy.CopyFeatures_management(fc, capanueva)
	print "Exportado --->> " + fc