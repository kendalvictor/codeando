import arcpy
#sobrescribir la salida
arcpy.env.overwriteOutput = True
#Variable de entorno
arcpy.env.workspace = r"C:\compartir\Curso Python\Shapefiles"
#Nueva variable de entorno
rutadesalida=r"C:\\compartir\\Curso Python\GDB\\Dia3.mdb\\"
#Lista de Feature Class
listadeshapefiles = arcpy.ListFeatureClasses()
#Recorrer la lista
for shp in listadeshapefiles:
	#funcion Describe
	desc = arcpy.Describe(shp)
	#Herramienta de geoproceso
	arcpy.CopyFeatures_management(shp, rutadesalida + desc.basename)
	print "Exportado --->> " + desc.basename